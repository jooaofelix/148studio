#!/usr/bin/env python3
"""Monta a Biblioteca 148 a partir da pasta "01 - ESTUDIO 148" do Google Drive para desktop.

O que faz:
  1. encontra a pasta do Drive sincronizada no Mac (ou usa a passada em ESTUDIO148_ORIGEM);
  2. copia as imagens para biblioteca/ (que fica fora do git: o repositório é público);
  3. ignora arquivos repetidos (mesmo conteúdo);
  4. separa artes (fundo transparente), artes com fundo e mockups;
  5. gera miniaturas e o índice biblioteca/biblioteca.json, que o editor lê.

Uso: python3 ferramentas/biblioteca.py   (ou dois cliques em atualizar-biblioteca.command)
Só usa o que já vem no macOS (python3 e sips).
"""

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, "biblioteca")
MINIATURAS = os.path.join(DESTINO, ".miniaturas")
EXTENSOES = (".png", ".jpg", ".jpeg", ".webp")
PALAVRAS_MOCKUP = ("mockup", "camiseta", "camisa")
MINUSCULAS = {"de", "da", "do", "das", "dos", "e", "em", "com", "na", "no", "para", "of", "the", "is", "your", "where", "in", "a", "o"}


def achar_origem():
    if os.environ.get("ESTUDIO148_ORIGEM"):
        return os.environ["ESTUDIO148_ORIGEM"]
    candidatos = glob.glob(os.path.expanduser("~/Library/CloudStorage/GoogleDrive-*/*/01 - ESTUDIO 148"))
    candidatos = [c for c in candidatos if "/.Encrypted/" not in c]
    if not candidatos:
        sys.exit("Não achei a pasta '01 - ESTUDIO 148' do Google Drive. Defina ESTUDIO148_ORIGEM com o caminho dela.")
    return candidatos[0]


def nfc(texto):
    return unicodedata.normalize("NFC", texto)


def bonito(texto):
    texto = nfc(texto).replace("_", " ").strip()
    texto = re.sub(r"\s+", " ", texto)
    palavras = texto.split(" ")
    saida = []
    for i, p in enumerate(palavras):
        baixa = p.lower()
        saida.append(baixa if i and baixa in MINUSCULAS else (p[:1].upper() + p[1:].lower() if p.isupper() or p.islower() else p))
    return " ".join(saida)


def colecao_de(relativo):
    """Nome da coleção a partir das pastas: ART/X → X; .../IDEIAS AINDA NAO PRONTAS/Y → Y · ideia."""
    partes = [p for p in nfc(relativo).split("/")[:-1]]
    partes = [p for p in partes if p.strip().upper() not in ("ART", "PNG", "FINAL")]
    ideia = any("IDEIAS AINDA NAO PRONTAS" in p.upper() for p in partes)
    partes = [p for p in partes if "IDEIAS AINDA NAO PRONTAS" not in p.upper()]
    if not partes:
        return "Geral"
    if partes[0] == "PERMANENTES":
        resto = partes[1:] or ["Permanentes"]
        nome = "Logos" if resto[0].strip().upper() == "LOGOS" else f"{bonito(resto[0].strip())} permanentes"
    elif len(partes) > 1 and re.fullmatch(r"\d+", partes[0]):
        sub = re.sub(r"\s+\d+$", "", partes[1].strip())
        sub = re.sub(rf"^{partes[0]}\s*-\s*", "", sub)
        nome = f"{partes[0]} · {bonito(sub)}"
    else:
        nome = bonito(partes[-1])
    return f"{nome} · ideia" if ideia else nome


def info_imagem(caminho):
    saida = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", "-g", "hasAlpha", caminho], capture_output=True, text=True).stdout
    valores = dict(re.findall(r"^\s+(\w+): (.+)$", saida, re.M))
    return int(valores.get("pixelWidth", 0)), int(valores.get("pixelHeight", 0)), valores.get("hasAlpha") == "yes"


def transparencia(miniatura):
    """Fração da imagem que é transparente de verdade (PNG com canal alfa pode ser todo opaco).
    Precisa do Pillow; sem ele devolve None e vale o que o sips diz."""
    try:
        from PIL import Image
    except ImportError:
        return None
    with Image.open(miniatura) as im:
        alfa = im.convert("RGBA").getchannel("A").histogram()
        return sum(alfa[:20]) / max(1, sum(alfa))


def tipo_de(nome, largura, altura, alfa, transparente=None):
    if any(p in nome.lower() for p in PALAVRAS_MOCKUP):
        return "mockup"
    if transparente is not None:
        alfa = transparente > 0.05
    if alfa:
        return "arte"
    # sem transparência: foto horizontal costuma ser mockup (duas camisetas lado a lado); o resto é arte com fundo
    return "mockup" if largura > altura * 1.15 else "arteFundo"


def md5(caminho):
    h = hashlib.md5()
    with open(caminho, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def main():
    origem = achar_origem()
    print(f"Origem: {origem}")
    os.makedirs(MINIATURAS, exist_ok=True)

    vistos = {}
    itens = []
    arquivos = []
    for pasta, _, nomes in os.walk(origem):
        for nome in nomes:
            if nome.lower().endswith(EXTENSOES) and not nome.startswith("."):
                arquivos.append(os.path.join(pasta, nome))
    arquivos.sort(key=nfc)

    for caminho in arquivos:
        relativo = os.path.relpath(caminho, origem)
        destino = os.path.join(DESTINO, relativo)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        if not os.path.exists(destino) or os.path.getsize(destino) != os.path.getsize(caminho):
            shutil.copy2(caminho, destino)
        assinatura = md5(destino)
        if assinatura in vistos:
            continue
        vistos[assinatura] = relativo
        largura, altura, alfa = info_imagem(destino)
        nome = os.path.splitext(os.path.basename(relativo))[0]
        miniatura = os.path.join(MINIATURAS, assinatura + ".png")
        if not os.path.exists(miniatura):
            subprocess.run(["sips", "-Z", "320", "-s", "format", "png", destino, "--out", miniatura], capture_output=True)
        itens.append({
            "arquivo": "biblioteca/" + nfc(relativo).replace(os.sep, "/"),
            "miniatura": "biblioteca/.miniaturas/" + assinatura + ".png",
            "nome": bonito(nome),
            "colecao": colecao_de(relativo.replace(os.sep, "/")),
            "tipo": tipo_de(nome, largura, altura, alfa, transparencia(miniatura)),
            "l": largura,
            "a": altura,
        })
        print(f"  {itens[-1]['tipo']:9} {itens[-1]['colecao']}: {itens[-1]['nome']}")

    colecoes = {}
    for item in itens:
        colecoes.setdefault(item["colecao"], []).append(item)
    indice = {
        "geradoEm": time.strftime("%Y-%m-%d %H:%M"),
        "colecoes": [{"nome": nome, "itens": lista} for nome, lista in sorted(colecoes.items(), key=lambda x: (x[0].startswith("0") is False, "ideia" in x[0], x[0]))],
    }
    with open(os.path.join(DESTINO, "biblioteca.json"), "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    contagem = {t: sum(1 for i in itens if i["tipo"] == t) for t in ("arte", "arteFundo", "mockup")}
    print(f"\nPronto: {len(itens)} imagens em {len(colecoes)} coleções "
          f"({contagem['arte']} artes, {contagem['arteFundo']} artes com fundo, {contagem['mockup']} mockups); "
          f"{len(arquivos) - len(itens)} repetidas ignoradas.")


if __name__ == "__main__":
    main()

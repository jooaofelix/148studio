# 148 Estúdio

Editor de estampas para as camisas da 148, direto no navegador. Monte a arte sobre um mockup de camiseta,
aplique efeitos de texto e baixe o arquivo pronto para impressão.

## Como usar

Abra o `index.html` no navegador (dois cliques basta). Não há nada para instalar. As fontes vêm do
Google Fonts, então a primeira abertura precisa de internet.

## O que tem

- **Mockup realista**: camiseta com caimento, dobras, trama da malha, gola canelada, costuras e sombra, em
  frente e costas e 8 cores. A estampa "assenta" no tecido (pega as dobras e a luz), como num mockup de foto;
  o arquivo de impressão continua limpo. Dá para desligar em "Estampa assentada no tecido".
- **Mockup com foto real**: envie a foto de uma camiseta lisa sua (ou gere uma com a IA), ajuste a área de
  impressão e a estampa entra com as dobras daquela foto.
- **Gerar com IA**: arte para estampa (fundo transparente), foto de mockup ou imagem livre, a partir de uma
  descrição ou de até 4 fotos de referência, usando a API de imagens da OpenAI (veja abaixo).
- **Camadas**: texto, imagem e formas (círculo, retângulo, estrela, linha, anel), com ordem, ocultar e travar.
- **Texto**: 13 fontes; forma reta, em arco, em círculo ou em onda; contorno, contorno externo, sombra chapada,
  sombra 3D, brilho neon, degradê, espaçamento e itálico.
- **Efeitos em um clique**: contorno duplo, sombra 3D, neon, retrô, vazado, vintage, degradê.
- **Desgaste vintage** e **mesclagem** (multiplicar, tela, sobrepor, diferença) em qualquer camada.
- **Alinhar** à área de impressão e guias que encaixam no centro ao arrastar.
- **Serigrafia**: tirar fundo branco, cor única, alto contraste e inverter imagens; o contador no topo mostra
  quantas cores (telas) a estampa tem ou avisa quando é melhor imprimir em DTF.
- **Modelos 148**: número gigante, arco clássico, gótico, peito esquerdo, selo circular, empilhado, onda retrô, neon.
- **Kit da marca**: nome, slogan, ano, paleta e logo, usados pelos modelos.
- **Desfazer/refazer**, salvamento automático no navegador e projetos em `.json`.

## Gerar com IA

1. Crie uma chave em [platform.openai.com/api-keys](https://platform.openai.com/api-keys) e coloque créditos na conta.
2. Clique em **✨ Gerar com IA**, cole a chave e salve. Ela fica **só no seu navegador** (localStorage): não vai
   para o projeto, para os arquivos salvos nem para o GitHub. Nunca coloque a chave no código.
3. Escolha o tipo (arte para estampa, foto de mockup ou livre), descreva e, se quiser, envie fotos de referência.
4. Use o resultado na estampa, como foto do mockup, ou baixe.

Cada imagem é cobrada na sua conta da OpenAI ("Rascunho" é o mais barato). Alguns modelos exigem verificar a
organização na OpenAI; se der erro 403, escolha outro modelo na lista.

## Exportar

- **Baixar arte para impressão**: PNG transparente de 3600×4800 px (30×40 cm a 300 dpi).
- **Baixar mockup**: PNG da camiseta com a estampa, para postar ou mostrar ao cliente.

## Atalhos

| Ação | Atalho |
|---|---|
| Desfazer / refazer | `Ctrl+Z` / `Ctrl+Shift+Z` (ou `⌘` no Mac) |
| Apagar camada | `Delete` |
| Duplicar | `Ctrl+D` |
| Mover devagar / rápido | setas / `Shift` + setas |
| Girar de 15 em 15° | `Shift` enquanto gira |

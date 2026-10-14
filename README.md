# 148 Estúdio

Editor de estampas para as camisas da 148, direto no navegador. Monte a arte sobre um mockup de camiseta,
aplique efeitos de texto e baixe o arquivo pronto para impressão.

## Como usar

Dê dois cliques em **`abrir-estudio.command`**: ele abre o estúdio no navegador (em `http://127.0.0.1:8148`)
já com a Biblioteca 148. Deixe a janela do Terminal aberta enquanto usa. Não há nada para instalar; as fontes
vêm do Google Fonts, então a primeira abertura precisa de internet.

Abrir o `index.html` direto também funciona; aí a biblioteca pede para você escolher a pasta `biblioteca`.

> Se o macOS bloquear o `.command` na primeira vez, clique com o botão direito nele → **Abrir**.

## Biblioteca 148 (artes e mockups do Drive)

As artes e mockups da pasta **01 - ESTUDIO 148** do Google Drive ficam no botão **📚 Biblioteca 148**, separadas
em *Artes* (fundo transparente), *Artes com fundo* e *Mockups*, por coleção, com busca. Clique numa arte para
pôr na estampa, ou use **Como mockup** / **Logo**.

- Para trazer artes novas do Drive: dois cliques em **`atualizar-biblioteca.command`**. Ele lê a pasta do Google
  Drive para desktop, copia as imagens para `biblioteca/`, ignora repetidas e gera as miniaturas.
- A pasta `biblioteca/` **não vai para o GitHub** (está no `.gitignore`): o repositório é público e as artes são
  da marca. Ela fica só no seu computador.
- No site publicado (o repositório faz deploy no Cloudflare a cada push), a biblioteca não aparece sozinha pelo
  mesmo motivo: lá, o botão pede para escolher a pasta `biblioteca` do computador, e as imagens só são abertas no
  navegador, sem ir para a internet.
- Se o Drive estiver em outro lugar: `ESTUDIO148_ORIGEM="/caminho/da/pasta" python3 ferramentas/biblioteca.py`.
- **Usar a paleta das artes 148** (no kit da marca) troca a paleta pelas cores tiradas das artes da biblioteca.

## O que tem

- **Sem área fixa**: a estampa vai para qualquer lugar da camiseta, de qualquer tamanho: peito, manga, barra,
  nuca, costas inteiras. Os botões de **Posição na camiseta** encaixam a camada num lugar comum já no tamanho
  certo, e o painel mostra a medida real em centímetros. A área de 30×40 cm virou só uma guia opcional.
- **Mockup realista**: camiseta com caimento, dobras, trama da malha, gola canelada, costuras e sombra, em
  frente e costas e 8 cores. A estampa "assenta" no tecido (pega as dobras e a luz), como num mockup de foto;
  o arquivo de impressão continua limpo. Dá para desligar em "Estampa assentada no tecido".
- **Mockup com foto real**: envie a foto de uma camiseta lisa sua (ou gere uma com a IA), ajuste a área de
  escala e a estampa entra com as dobras daquela foto. Os mockups da Biblioteca 148 também servem.
- **Gerar com IA**: arte para estampa (fundo transparente), foto de mockup ou imagem livre, a partir de uma
  descrição ou de até 4 fotos de referência, usando a API de imagens da OpenAI (veja abaixo).
- **Camadas**: texto, imagem e formas (círculo, retângulo, estrela, linha, anel), com ordem, ocultar e travar.
- **Texto**: 13 fontes; forma reta, em arco, em círculo ou em onda; contorno, contorno externo, sombra chapada,
  sombra 3D, brilho neon, degradê, espaçamento e itálico.
- **Efeitos em um clique**: contorno duplo, sombra 3D, neon, retrô, vazado, vintage, degradê.
- **Desgaste vintage** e **mesclagem** (multiplicar, tela, sobrepor, diferença) em qualquer camada.
- **Centralizar** na camiseta e guias que encaixam no centro ao arrastar.
- **Serigrafia**: tirar fundo branco, cor única, alto contraste e inverter imagens; o contador no topo mostra
  quantas cores (telas) a estampa tem ou avisa quando é melhor imprimir em DTF.
- **Modelos 148**: número gigante, arco clássico, gótico, peito esquerdo, selo circular, empilhado, onda retrô, neon.
- **Kit da marca**: nome, slogan, ano, paleta e logo, usados pelos modelos.
- **Desfazer/refazer**, salvamento automático no navegador e projetos em `.json`.

## Gerar com IA

### Com a sua conta do ChatGPT (sem custo de API)

1. Clique em **✨ Gerar com IA**, escolha o tipo e descreva o que quer.
2. **💬 Copiar pedido e abrir o ChatGPT**: o editor monta o pedido otimizado para estampa (com o kit da marca,
   se marcado), copia e abre o ChatGPT. Se o texto não aparecer sozinho, cole com `Ctrl+V`.
3. Quando a imagem sair, copie-a no ChatGPT e aperte `Ctrl+V` (`⌘V` no Mac) no editor. Ela vira camada da
   estampa; com a janela no modo **Foto de mockup**, vira a foto do mockup.
4. Se vier com fundo, use **Tirar fundo branco** ou **Cor única** no painel da direita.

Também dá para arrastar qualquer imagem do computador para cima da camiseta.

### Pela API da OpenAI (gera sem sair do editor)

1. Crie uma chave em [platform.openai.com/api-keys](https://platform.openai.com/api-keys) e coloque créditos na conta.
2. Clique em **✨ Gerar com IA**, cole a chave e salve. Ela fica **só no seu navegador** (localStorage): não vai
   para o projeto, para os arquivos salvos nem para o GitHub. Nunca coloque a chave no código.
3. Escolha o tipo (arte para estampa, foto de mockup ou livre), descreva e, se quiser, envie fotos de referência.
4. Use o resultado na estampa, como foto do mockup, ou baixe.

Cada imagem é cobrada na sua conta da OpenAI ("Rascunho" é o mais barato). Alguns modelos exigem verificar a
organização na OpenAI; se der erro 403, escolha outro modelo na lista.

## Exportar

- **Baixar arte para impressão**: PNG transparente a 300 dpi, cortado exatamente na arte, com a medida em cm
  no nome do arquivo. Se a vista tem estampas em lugares diferentes (peito e manga, por exemplo), sai **um arquivo
  por lugar**, como a gráfica precisa.
- **Baixar mockup**: PNG da camiseta com a estampa, para postar ou mostrar ao cliente.

## Atalhos

| Ação | Atalho |
|---|---|
| Desfazer / refazer | `Ctrl+Z` / `Ctrl+Shift+Z` (ou `⌘` no Mac) |
| Apagar camada | `Delete` |
| Duplicar | `Ctrl+D` |
| Mover devagar / rápido | setas / `Shift` + setas |
| Girar de 15 em 15° | `Shift` enquanto gira |

#!/bin/bash
# Abre o 148 Estúdio no navegador, servido por http (assim a Biblioteca 148 aparece sozinha
# e a exportação funciona com as imagens dela). Deixe esta janela aberta enquanto usa o estúdio.
cd "$(dirname "$0")" || exit 1
PORTA=8148
if ! curl -s -o /dev/null "http://127.0.0.1:$PORTA/index.html"; then
  python3 -m http.server "$PORTA" --bind 127.0.0.1 >/dev/null 2>&1 &
  SERVIDOR=$!
  trap 'kill $SERVIDOR 2>/dev/null' EXIT
  sleep 1
fi
open "http://127.0.0.1:$PORTA/"
echo "148 Estúdio aberto em http://127.0.0.1:$PORTA/"
echo "Feche esta janela (ou aperte Ctrl+C) quando terminar."
[ -n "$SERVIDOR" ] && wait "$SERVIDOR"

#!/bin/bash
# Генерує content.json зі ВСІХ .js файлів в scenes/ та dialogues/
# Запуск: bash generate_manifest.sh (з папки app/js/)

cd "$(dirname "$0")"

find scenes dialogues -name "*.js" 2>/dev/null | sort | awk '
BEGIN { print "[" }
{ gsub(/\r/,""); if(NR>1) printf ",\n"; printf "  \"%s\"", $0 }
END { print "\n]" }
' > content.json

echo "content.json: $(grep -c '\.js' content.json) files"

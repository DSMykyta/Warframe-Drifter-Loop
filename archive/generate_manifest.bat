@echo off
REM Генерує dialogues.json — список всіх .js файлів в app/js/dialogues/
REM Запускай після додавання нових діалогів

cd /d "%~dp0\app\js\dialogues"

echo [ > dialogues.json.tmp
setlocal enabledelayedexpansion
set "first=1"
for /r %%f in (*.js) do (
  set "rel=%%f"
  set "rel=!rel:%cd%\=!"
  set "rel=!rel:\=/!"
  if "!rel!" neq "dialogues.json" (
    if !first!==1 (
      echo   "!rel!" >> dialogues.json.tmp
      set "first=0"
    ) else (
      echo  ,"!rel!" >> dialogues.json.tmp
    )
  )
)
echo ] >> dialogues.json.tmp
move /y dialogues.json.tmp dialogues.json >nul
echo Manifest generated: dialogues.json

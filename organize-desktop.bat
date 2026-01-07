@echo off
REM デスクトップファイル整理アプリ - Windowsバッチファイル
REM このファイルのパスを編集して、desktop_organizer.pyの場所を指定してください

setlocal

REM スクリプトのディレクトリを取得
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%desktop_organizer.py

REM Python 3が利用可能か確認
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo エラー: Pythonが見つかりません
    echo Python 3をインストールしてPATHに追加してください
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Pythonスクリプトを実行
python "%PYTHON_SCRIPT%" %*

endlocal

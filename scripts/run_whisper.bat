@echo off
title Whisper Large-v3 - NVIDIA (Managed by Python)

echo ================================================
echo Activating virtual environment...

call %VENV_PATH%\Scripts\activate.bat

echo Using NVIDIA API Key from environment...

echo.
if "%INPUT_FILE%"=="" (
    echo No file provided!
    exit /b 1
)

echo Starting transcription (%LANGUAGE_CODE%)...

python %SCRIPT_PATH% ^
    --server %WHISPER_SERVER% --use-ssl ^
    --metadata function-id "%FUNCTION_ID%" ^
    --metadata "authorization" "Bearer %NVIDIA_API_KEY%" ^
    --language-code %LANGUAGE_CODE% ^
    --input-file %INPUT_FILE%

echo.
echo ================================================
echo Transcription finished!

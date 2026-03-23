import os
import re
import subprocess
from pathlib import Path


class WhisperTranscriber:

    TRANSCRIPT_PATTERN = r"Final transcript:\s*(.+)"

    def __init__(self, settings):
        self.settings = settings
        self.bat_file = Path("scripts/run_whisper.bat")

    # -------------------------
    # INTERNAL
    # -------------------------
    def _extract_transcript(self, output: str):

        # normalize windows line endings
        output = output.replace("\r", "")

        match = re.search(self.TRANSCRIPT_PATTERN, output)

        if not match:
            raise RuntimeError(
                "Transcript not found.\n---- RAW OUTPUT ----\n"
                + output
            )

        return match.group(1).strip()

    # -------------------------
    # PUBLIC
    # -------------------------
    def transcribe(self, audio_path: str):

        env = os.environ.copy()

        env.update({
            "NVIDIA_API_KEY": self.settings.api_key,
            "LANGUAGE_CODE": self.settings.language,
            "FUNCTION_ID": self.settings.function_id,
            "WHISPER_SERVER": self.settings.server,
            "INPUT_FILE": audio_path,
            "VENV_PATH": self.settings.venv_path,
            "SCRIPT_PATH": self.settings.script_path,
        })

        process = subprocess.run(
            [str(self.bat_file)],
            shell=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            env=env
        )

        # ? CRITICAL FIX
        combined_output = (process.stdout or "") + "\n" + (process.stderr or "")

        if process.returncode != 0:
            raise RuntimeError(combined_output)

        return self._extract_transcript(combined_output)
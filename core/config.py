import os
from dotenv import load_dotenv


class Settings:

    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("NVIDIA_API_KEY")
        self.language = os.getenv("WHISPER_LANGUAGE")
        self.function_id = os.getenv("WHISPER_FUNCTION_ID")
        self.server = os.getenv("WHISPER_SERVER")

        self.venv_path = os.getenv("VENV_PATH")
        self.script_path = os.getenv("SCRIPT_PATH")

        self.max_workers = int(os.getenv("MAX_WORKERS"))
        self.queue_size = int(os.getenv("QUEUE_SIZE"))

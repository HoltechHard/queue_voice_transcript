from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class TranscriptionJob:
    audio_path: str
    job_id: str = field(default_factory=lambda: str(uuid4()))
    
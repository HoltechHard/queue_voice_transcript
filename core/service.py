from core.config import Settings
from core.transcriber import WhisperTranscriber
from queue_manager.speech_manager import TranscriptionQueue
from workers.worker import TranscriptionWorker
from queue_manager.job import TranscriptionJob


class TranscriptionService:

    def __init__(self):

        self.settings = Settings()

        self.queue = TranscriptionQueue(
            self.settings.queue_size
        )

        self.transcriber = WhisperTranscriber(self.settings)

        self.workers = [
            TranscriptionWorker(self.queue, self.transcriber)
            for _ in range(self.settings.max_workers)
        ]

        for worker in self.workers:
            worker.start()

        print(f"? Service started with {len(self.workers)} workers")

    def submit_job(self, audio_path: str):

        job = TranscriptionJob(audio_path)
        self.queue.add(job)

        print(f"?? Job queued: {job.job_id}")

        return job.job_id
    
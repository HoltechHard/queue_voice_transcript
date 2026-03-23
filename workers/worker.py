import threading

# concurrency controller for transcription jobs
class TranscriptionWorker(threading.Thread):

    def __init__(self, queue, transcriber):
        super().__init__(daemon=True)
        self.queue = queue
        self.transcriber = transcriber

    def run(self):

        while True:
            job = self.queue.get()

            try:
                print(f"[Worker] Processing {job.job_id}")

                result = self.transcriber.transcribe(job.audio_path)

                print(f"[DONE] {job.job_id}")
                print("Transcript:", result)

            except Exception as e:
                print("Error:", e)

            finally:
                self.queue.task_done()

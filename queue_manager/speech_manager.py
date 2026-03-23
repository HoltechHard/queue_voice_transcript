import queue


class TranscriptionQueue:

    def __init__(self, max_size: int):
        self._queue = queue.Queue(maxsize=max_size)

    def add(self, job):
        self._queue.put(job)

    def get(self):
        return self._queue.get()

    def task_done(self):
        self._queue.task_done()
        
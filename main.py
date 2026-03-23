from core.service import TranscriptionService
import time

def main():

    service = TranscriptionService()

    # simulate 10 concurrency of users
    for i in range(10):
        service.submit_job("voice/test.ogg")

    print("All jobs submitted.")

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()

import time
import winsound

def alarm(total_seconds):
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        print(f"\rAlarm in {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        total_seconds -= 1

    print("\nTime's up! Alarm ringing!")

    # Repeating beep until stopped with Ctrl + C
    try:
        while True:
            winsound.Beep(1000, 500)  # Frequency: 1000 Hz, Duration: 0.5 seconds
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Alarm stopped.")

# Get user input
minutes = int(input("How many minutes to wait? "))
seconds = int(input("How many seconds to wait? "))
alarm(minutes * 60 + seconds)
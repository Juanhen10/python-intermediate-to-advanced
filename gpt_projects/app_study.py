import time


def study_timer():
    print("Starting your study session!")
    # Get the user input for how long they want to study for in minutes
    study_time = int(input("How many minutes do you want to study for? "))

    # Convert the minutes to seconds
    study_time_seconds = study_time * 60

    # Start the timer and count down to 0
    while study_time_seconds > 0:
        minutes, seconds = divmod(study_time_seconds, 60)
        time_left = f"{minutes:02d}:{seconds:02d}"
        print(f"Time remaining: {time_left}", end="\r")
        time.sleep(1)
        study_time_seconds -= 1

    print("\nTime's up! Take a short break.")


def main():
    print("Welcome to the concentration app!")
    while True:
        # Get user input to start the study timer or quit the app
        choice = input(
            "Enter 'start' to begin a study session or 'quit' to exit the app: ")
        if choice.lower() == 'start':
            study_timer()
        elif choice.lower() == 'quit':
            print("Thank you for using the concentration app!")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    main()

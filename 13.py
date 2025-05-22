from datetime import datetime

def write_log():
    # Define the log message with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"Script run at {timestamp}\n"

    # Write log message to file
    with open("log.txt", "a") as log_file:
        log_file.write(log_message)

    print("Log written successfully.")

# Run the function
write_log()

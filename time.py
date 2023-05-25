from datetime import datetime

current_time = datetime.now()

# Format the current time and date
formatted_time = current_time.strftime("%H:%M:%S")  # Hours:Minutes:Seconds
formatted_date = current_time.strftime("%Y-%m-%d")  # Year-Month-Day

# Log the current time and date
print(f"Current Time: {formatted_time}")
print(f"Current Date: {formatted_date}")

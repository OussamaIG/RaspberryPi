from datetime import datetime
import pytz

def get_current_time(city, time_zone):
    # Get the current time in UTC
    current_time = datetime.now(pytz.utc)
    
    # Convert the UTC time to the specified time zone
    target_time_zone = pytz.timezone(time_zone)
    converted_time = current_time.astimezone(target_time_zone)
    
    # Format the converted time
    formatted_time = converted_time.strftime("%H:%M:%S")  # Hours:Minutes:Seconds
    
    # Log the current time in the specified city
    print(f"Current Time in {city}: {formatted_time}")

# Test the function
city = input("Enter a city name: ")
time_zone = input("Enter the time zone of the city (e.g., 'Europe/London'): ")
get_current_time(city, time_zone)

import requests

def get_weather(city):
    api_key = 'a250cee351bb47a0bb9170931232505'  # Replace with your WeatherAPI key
    base_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}'
    
    try:
        response = requests.get(base_url, params={'q': city})
        data = response.json()
        
        if 'error' in data:
            print(f"Error: {data['error']['message']}")
        else:
            location = data['location']['name']
            condition = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']
            
            print(f"Weather in {location}:")
            print(f"Condition: {condition}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Test the function
city_name = input("Enter a city name: ")
get_weather(city_name)

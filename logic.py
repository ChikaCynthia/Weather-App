import requests

API_KEY = "0821d7b675df8643580c2a80f295c29b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def fetch_weather(city):
	try:
		params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
		response = requests.get(BASE_URL, params=params)
		response.raise_for_status()
		data = response.json()

		if data.get("cod") == 401:
			raise ValueError("Invalid API Key")

		return{
			'temp': data['main']['temp'],
			'descriotion': data['weather'][0]['description']
		}

	except requests.RequestException as e:
		print(f"Error fetching weather data: {e}")
		return None
	except ValueError as ve:
		print(f"Error: {ve}")
		return None
		






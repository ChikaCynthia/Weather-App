import tkinter as tk
from tkinter import messagebox
#messagebox is used to show an error dialog if the application fails to fetch weather data example; if the city name is invalid etc.

class WeatherAppGUI:
	def __init__(self, root, fetch_weather_callback):
		self.root = root
		self.root.title("Weather App")

		self.label = tk.Label(root, text="Enter City Name")
		self.label.pack()

		self.city_entry = tk.Entry(root)
		self.city_entry.pack()

		self.search_button = tk.Button(root, text="Get Weather", command=self.get_weather)
		self.search_button.pack()

		self.result_label = tk.Label(root, text="")
		self.result_label.pack()

		self.fetch_weather_callback = fetch_weather_callback


	def get_weather(self):
		city = self.city_entry.get()
		if city:
			weather_data = self.fetch_weather_callback(city)
			if weather_data:
				self.result_label.config(texts=f"{weather_data['temp']}°C), {weather_data['description']}")
			else:
				messagebox.showerror("Error", "could not retrieve weather data.")
		else:
			messagebox.showwarning("Input Error", "Please enter a city name")
	#This script sets up a simple Tkinter GUI with an entry box for the city name, a button to fetch weather data, and a label to display the results.





     
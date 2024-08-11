import json
import os 

PREF_FILE = 'data/preferences.json'

def load_preferences():
	if os.path.exists(PREF_FILE):
		with open(PREF_FILE, 'r') as file:
			return json.load(file)
	return None

def save_preferences(city):
	with open(PREF_FILE, 'w') as file:
		json.dump({'last_city': city}, file)

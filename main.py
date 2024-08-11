
import tkinter as tk
from gui import WeatherAppGUI  # Ensure this import is correct
from logic import fetch_weather
from utils import load_preferences, save_preferences

def main():
    # Create the main window
    root = tk.Tk()  # Initialize the Tkinter root window
    root.title("Weather Application")
    
    # Load user preferences (e.g., last searched city)
    last_city = load_preferences()
    
    # Initialize the GUI with the root window and fetch_weather function
    gui = WeatherAppGUI(root, fetch_weather)

    
    # If a last searched city exists, set it in the entry field
    if last_city:
        gui.city_entry.insert(0, last_city)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()  # This ensures the main function is called when the script is run

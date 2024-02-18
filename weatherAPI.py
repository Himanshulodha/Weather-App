import requests
import json  #json is builtin module 
import win32com.client as wincom
import time
import re  # Import regular expression module


city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=d14e54cd15d34e659f2175351241402&q={city}"


r = requests.get(url)
# print(r.text)
Weather_dic = json.loads(r.text)  # It is function and its loads strings
w = Weather_dic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice") #You can then create the voice dispatcher object,

# text = f"The current weather in {city} is {w} degrees" # and send it the text you want to read,
# speak.Speak(text)



while True:
    # Assuming 'speak.Speak(text)' is a text-to-speech function, and 'city' and 'w' are defined elsewhere in your code
    text = f"The current weather in {city} is {w} degrees"
    speak.Speak(text)
    print(text)

    # Ask the user if they want to repeat, change the city, change the temperature, or exit
    user_input = input("Press 'Enter' to repeat, type 'exit' to stop, "
                       "type 'city' to enter a new city: ")

    # Check user input
    if user_input.lower() == 'e':
        break
    elif user_input.lower() == 'c':
        # Update 'city' with the new input for the next iteration
        city = input("Enter a new city: ")
        # Validate that the new temperature is a number
        if w.match(r'^-?\d+(?:\.\d+)?$', city):
           w = float(city)
           text = f"The new city {city} is not found"
           speak.Speak(text)
    elif user_input:
        print("Invalid input. Please enter 'exit', 'city' or press 'Enter' to repeat.")``



import requests
import json  #json is builtin module 
import win32com.client as wincom

def get_weather(city):  #we using multiple function for different purpose 
    url = f"https://api.weatherapi.com/v1/current.json?key=d14e54cd15d34e659f2175351241402&q={city}"
    r = requests.get(url)
    return json.loads(r.text)

def speak_weather(city, temperature):
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = f"The current weather in {city} is {temperature} degrees"
    speak.Speak(text)
    print(text)

def speak_message(message):
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(message)
    print(message)

city = input("Enter the name of the city\n")

while True:
    weather_data = get_weather(city)

    # Check if the city is found in the response
    if 'error' in weather_data:
        speak_message(f"The city is not found. Please enter a valid city.")
        city = input("Enter a new city: ")
        continue

    w = weather_data["current"]["temp_c"]
    speak_weather(city, w)

    # Ask the user if they want to repeat, change the city, or exit
    user_input = input("Press 'Enter' to repeat, type 'e' to stop, "
                       "or type 'c' to enter a new city: ")

    # Check user input
    if user_input.lower() == 'e':
        break
    elif user_input.lower() == 'c':
        # Update 'city' with the new input for the next iteration
        city = input("Enter a new city: ")

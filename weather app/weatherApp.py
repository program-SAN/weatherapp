import requests
import json
import pyttsx3

text_to_speech =pyttsx3.init()
while(True):
    city = input ("enter the name of the city \nand if u want to exit enter ""NO"" \n")
    url = f"https://api.weatherapi.com/v1/current.json?key=7b17f326daa64e1497e200424231706&q={city}"
    if (city=="NO"):
                break
    r = requests.get(url)
    wdic = json.loads(r.text)

    #print("tempreture in celsius",wdic["current"]["temp_c"])
    #print("percentage of clouds",wdic["current"]["cloud"])

    temp =f"tempreture in celsius in {city} ",wdic["current"]["temp_c"] 
    print("tempreture in celsius",wdic["current"]["temp_c"])
    cloud = "percentage of clouds",wdic["current"]["cloud"]
    print("percentage of clouds",wdic["current"]["cloud"])
    text_to_speech.say(temp)
    text_to_speech.runAndWait()
    

    text_to_speech.say(cloud)
    text_to_speech.runAndWait()
    

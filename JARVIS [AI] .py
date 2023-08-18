# #                                 START                                            # #
 

# # link of video 1 from which I have taken reference  == https://youtu.be/XWQXMncxg4k [SINGLE VIDEO]

#                               SAME CHANNEL VIDEOS              
# # link of video 2 from which I have taken reference  == https://youtu.be/EztlAyuOg6o [JARVIS - 1]
# # link of video 3 from which I have taken reference  == https://youtu.be/eMlOAbUGcwM [JARVIS - 2]
# # link of video 4 from which I have taken reference  == https://youtu.be/w_Q_KBbl2Zs [JARVIS - 3]
# # link of video 5 from which I have taken reference  == https://youtu.be/nP3BCw-r5g8 [JARVIS - 5]
# # link of video 6 from which I have taken reference  == https://youtu.be/CRTszE_1PCQ [jarvis - 6]
# # link of video 7 from which I have taken reference  == https://youtu.be/eHPx91wmWWg [JARVIS - 7]



             ## FOLLOW THE CODE STEP BY STEP TO MAKE AN ARTIFICIAL ITELLIGENCE ##


##   MODULES THAT NEEDDS TO BE IMPORTED ##


# Module for performing speech recognition, with support for several engines and APIs, online and offline. = pip install SpeechRecognition
# sr == short form
import speech_recognition as sr

# Text to Speech (TTS) module for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak. = pip install pyttsx3
import pyttsx3

# Module for date ,time ;used in repot_time function = pip install datetime
import datetime

# Module to access your microphone with speech recognizer or to record audio = pip install PyAudio [no need of importing]

# Module for the access of web browser [no need of installing]
import webbrowser

# Module for the access of wikipedia = pip install wikipedia
import wikipedia

# Module to crack random jokes for the user = pip install pyjokes
import pyjokes

# Module to take a screenshot for the user  or PyAutoGUI lets Python control the mouse and keyboard, and other GUI automation tasks. For Windows, macOS, and Linux, on Python 3 and 2.= pip install pyautogui
import pyautogui

# Module for opening different applications of my laptop = os 
import os

# Module to exit system =  sys [ no need of installing]
import sys

# Requests is an elegant and simple HTTP module for Python, built for human beings.Requests allows you to send HTTP
import requests

# Module for shortning url
import pyshorteners

# A cross-platform clipboard module for Python. (Only handles plain text for now.)
import pyperclip

# Module for designing or making GUI
from tkinter import *

# A pure-python PDF module capable of splitting, merging, cropping, and transforming PDF files
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader, PdfFileWriter

# To poweroff only in the windows
import ctypes

# to get current location
from geopy.geocoders import Nominatim 

# pure india ka data longitude and latitude etc location through ip address leta hai
import geocoder 


import time

# -------------------------------------------------------------------------------------------------------

# code to load speech engine driver
engine=pyttsx3.init()

# code to return voice descriptor objects 
voices=engine.getProperty('voices')

# code to get a female voice = engine.setProperty('voice',voices[1].id)
# code to get a male voice
engine.setProperty('voice',voices[0].id)
# code of a function to accept the command from the user
# this function is created to take input from the user from microphone
def input_query():
    # code to recognise speech
    recognizer=sr.Recognizer()
    # code to setup source of recognition (my microphone)
    with sr.Microphone() as source :
        print("\n\nlistening sir...\n")
        speak_va('\nlistening sir\n')
        # maan lo ki bolte hue agar app rukh jaao to aisa na ho ki jarvis appki baat na sune toh threshold use kiya hai
        recognizer.pause_threshold=2
        # code to capture input from microphone
        voice=recognizer.listen(source)
        # code for recognizer google method
        try:
            query=recognizer.recognize_google(voice).lower()
            print('This is the query that was made....',query)
            return query
        except Exception as ex:
            speak_va("Sorry not understood")
            return "not understood"
        return query
# -------------------------------------------------------------------------------------------------------



# code to make a time report function
def report_time():
    #  code to tell the time in ==[00:00 am/pm]
    # using datetime.datetime.now() function from datetime documentation for telling the current time
     current_time=datetime.datetime.now().strftime('%I:%M %p') 
     return current_time

# -------------------------------------------------------------------------------------------------------



# code to make the virtual assistant speak
def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

# -------------------------------------------------------------------------------------------------------

def open_pdf(pdf_path):
    with open(pdf_path,"rb") as a: 
        pdf=PdfReader(a)
        pages=len(pdf.pages)
        page_no=int(input("enter page number: "))
        page=pdf.pages[page_no]
        text=page.extract_text()
    print(text)


# ----------------------------------------------------------------

def sleep_mode():
    # Define constants
    HWND_BROADCAST = 0xFFFF
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    MONITOR_OFF = 2

    # Put the system into sleep mode
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_OFF)

#------------------------------------------------------------------------------------------------------------ 

def location1():
            g = geocoder.ip('me') # mera ip address liya
            latitude = g.lat 
            longitude = g.lng
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            address = g.address
            city = g.city
            country = g.country
            postal_code = g.postal
            print(f"Address: {address}")
            print(f"City: {city}")
            print(f"Country: {country}")
            print(f"Postal Code: {postal_code}")

# ----------------------------------------------------------------

# function to wish
def wish ():
    hour=datetime.datetime.now().hour
    # using if condition
    if hour>=0 and hour<=12:
        speak_va("good morning Aarush sir  ")
    elif hour>=12 and hour<=16:
        speak_va("good afternoon Aarush sir ")
    else :
        speak_va("good evening Aarush sir ")
if __name__=="__main__":
    wish()
    speak_va("  I am JARVIS please tell me how may I help you.  ")
    speak_va("JARVIS is activated ")
    print('\n                                             JARVIS is activated !\nI can do things like telling the current time ,open website ,open wikipedia ,crack jokes ,google search , take a sreenshot ,play a quiz , opening and closing --notepad ,MS word, MS excel , opening command prompt and switching the window  .\n                                     Please speak to get your work done\n')

# -------------------------------------------------------------------------------------------------------



# creating a new function to see the action of the input_query,report_time,speak_va function
# va is the short form for virtual assistant
# this function is created for the AI work or feed information to AI
def activate_va():
    user_query = input_query()
    print('user query....',user_query) 


# Assigning Taks To JARVIS

    # TASK 1:
    # using if condition to check the term time in the user query
    # if the word time comes in the sentence speaked by the user then this if condition will reprt the current time
    if "time" in user_query:
        current_time=report_time()
        print(f"Sir the current time is {current_time}")
        speak_va(f"Sir the current time is {current_time}")
# -------------------------------------------------------


    # TASK 2:
    # using elif condition to check the term open website in the user query 
    # if the word website comes in the sentence speaked by the user then this elif will open a website specified by the user
    elif "website" in user_query:
        speak_va("Please type the name of the website that you want to open              [specify the full URL\n]")
        website_name=input("Enter here : ")
        print(website_name)
        # using webbrowser .get()function from webbrowser documentation to open chrome to search for information provided by the user
        webbrowser.get("C:/Users/Aarush Jain/AppData/Local/Google/Chrome/Application/chrome.exe %s" ).open(website_name)
        speak_va(f"{website_name}\topened.")
# -------------------------------------------------------


    # TASK 3:
    # using elif condition to check the term wikipedia in the user query 
    # if the word wikipedia comes in the sentence speaked by the user then this elif will open wikipedia specified by the user
    elif "wikipedia" in user_query:
        speak_va("Searching on wikipedia ")
        user_query=user_query.replace('wikipedia','')
        # ab jis wikipedia ko user search karne ke liye bolega uski summary aa jaae gi
        # iss mei hum number of sentences on the particular topic bhi decide kar sakte hai
        result=wikipedia.summary(user_query,sentences=3)
        speak_va("according to wikipedia")
        print(result)
        speak_va(result)
# -------------------------------------------------------


    # TASK 4:
    # using elif condition to check the term joke in the user query
    # if the word joke comes in the sentence speaked by the user then this elif will display random joke
    elif "joke" in user_query:
        # using pyjokes.get_joke()function from pyjokes documentation to get a random joke
        random_joke=pyjokes.get_joke()
        print("The joke is : "+random_joke)
        speak_va("the joke is              "+random_joke)
        speak_va("I hope you liked it sir")
# -------------------------------------------------------


    # TASK 5:
    # using elif condition to check the term screenshot in the user query
    # if the word screenshot comes in the sentence speaked by the user then this elif will take a screenshot
    elif "screenshot" in user_query:
        speak_va("sir please tell me the name you want to choose for you screenshot")
        # iss mei mai user se type karva ke data le sakta hua
        # image_name=input("Enter here : ")
        # iss mei mai user se bulva ke data le sakta hua
        image_name=input_query().lower()
        # using pyautogui.sreenshot()function from pyautogui documentation to capture a screenshot
        image=pyautogui.screenshot()
        image.save(f"{image_name}.png")
        speak_va("screenshot taken sir. it is saved in our main folder")
# -------------------------------------------------------


    # TASK 6:
    # using elif condition to check the term search in the user query
    # if the word search comes in the sentence speaked by the user then this elif will open google search
    elif "open google" in user_query:
        speak_va("What do you want me to search sir please type")
        search_term=input("Enter here : ")
        search_url=f"http://www.google.com/search?q={search_term}"
        webbrowser.get("C:/Users/Aarush Jain/AppData/Local/Google/Chrome/Application/chrome.exe %s" ).open(search_url)
        speak_va("here are the results of the searched term")
# -------------------------------------------------------


    # TASK 7:
    #using elif condition to check the term quiz in the user query 
    # if the word quiz comes in the sentence speaked by the user then this elif will display a quiz
    elif "quiz" in user_query:
        speak_va("well hello welcome to our personality quiz\n I am jarvis your quiz master for today      \n I hope you will like the quiz                  \n    lets start")

        print("\n Q1)Who do you love the most in you house ??")
        speak_va("Question1)Who do you love the most in you house ??")
        print("----------------------------------------------")
        print(" Please select your option \n")
        speak_va("Please select your option")
        op1="1. Mother"
        print(op1)
        op2="2. Father"
        print(op2)
        op3="3. Siblings"
        print(op3)
        print("-----------------------------------------\n")
        a=int(input("Enter 1 ,2 or 3 : "))
        if (a==1):
            print("That's very sweet")
        elif(a==2):
            print("That's very sweet")
        elif(a==3):
            print("That's very sweet")
        print("_________________________________________________________________________________________________\n\n")

        print("Q2) Which field do you want to purcive your career in ??")
        speak_va("Question2) Which field do you want to purcive your career in ??")
        print("-----------------------------------------------------------")
        print("Please select your option\n")
        speak_va("Please select your option")
        op4="1.Science"
        print(op4)
        op5="2.Commerce"
        print(op5)
        op6="3.Arts"
        print(op6)
        print("------------------------------------------------------------\n")
        b=int(input("Enter 1 ,2 or 3 : "))
        if (b==1):
            print("It seems that you are very ambitious\nAmazing! its good to see ambitious people like you")
        elif(b==2):
            print("Good choice!! Commerce is a nice subject")
        elif(b==3):
            print("Good choice!! Arts has a good future")
        print("_____________________________________________________________________________________________________\n\n")

        print("Q3) Which is your favourite bird ??")
        speak_va("Question3) Which is your favourite bird ??")
        print("-----------------------------------------------------------")
        print("Please select your option\n")
        speak_va("Please select your option")
        op7="1.Peacock"
        print(op7)
        op8="2.Ostrich"
        print(op8)
        op9="3.Woodpecker"
        print(op9)
        print("------------------------------------------------------------\n")
        c=int(input("Enter 1 ,2 or 3 : "))
        if (c==1):
            print("Oh nice pick!! I feel you might be fond of colours")
        elif(c==2):
            print("Oh nice pick!! I feel you might be fond of colours")
        elif(c==3):
            print("Oh nice pick!! I feel you might be fond of birds having sharp and strong beak")
        print("_____________________________________________________________________________________________________\n\n")

        print("Q4) What kind of movie do you love to watch??")
        speak_va("Question4) What kind of movie do you love to watch??")
        print("-----------------------------------------------------------")
        print("Please select your option\n")
        speak_va("Please select your option")
        op10="1.Horror"
        print(op10)
        op11="2.Dramatic"
        print(op11)
        op12="3.Adventerous"
        print(op12)
        print("------------------------------------------------------------\n")
        d=int(input("Enter 1 ,2 or 3 : "))
        if (d==1):
            print("Who dosen't love horror")
        elif(d==2):
            print("Who dosen't love drama")
        elif(d==3):
            print("Who dosen't love adventure")
        print("_____________________________________________________________________________________________________\n\n")

        print("THANK YOU FOR ATTENDING THE QUIZ\nIT WAS FUN TO PLAY WITH YOU !!!")
        speak_va("That's all\nTHANK YOU FOR ATTENDING THE QUIZ\nIT WAS FUN TO PLAY WITH YOU !!!")
        print("_____________________________________________________________________________________________________")
# -------------------------------------------------------


    # TASK 8:
    #using elif condition to check the term open notepad in the user query 
    elif "open notepad" in user_query:
        # location of notepad in my laptop
        note_path="C:\\Windows\\notepad.exe"
        # using os.startfile()function to open notepad
        os.startfile(note_path)
        speak_va("notepad opened")
    # to close notepad [or to close any other application]
    elif "close notepad" in user_query:
        speak_va("okay sir closing notepad")
        os.system("taskkill /f /im notepad.exe")
# -------------------------------------------------------


    # TASK 9:
    #using elif condition to check the term open word  in the user query 
    elif  "open word" in user_query:
        # location of  MS word in my laptop
        word_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe"
        # using os.startfile()function to open MS word
        os.startfile(word_path)
        speak_va(" MS word opened")
        # to close MS word [or to close any other application]
    elif "close word" in user_query:
        speak_va("okay sir closing MS word")
        os.system("taskkill /f /im winword.exe")
# -------------------------------------------------------


    # TASK 10:
    #uC
    elif  "open excel" in user_query:
        # location of  MS excel in my laptop
        excel_path="C:\\Program Files\\Microsoft Office\\root\\Office16\\excel.exe"
        # using os.startfile()function to open MS excel
        os.startfile(excel_path)
        speak_va(" MS excel opened")
        # to close MS excel [or to close any other application]
    elif  "close excel"in user_query:
        speak_va("okay sir closing MS excel")
        os.system("taskkill /f /im excel.exe")
# -------------------------------------------------------


    # TASK 11:
    # using os module to shutdowm the laptop
    # elif "shutdown" in user_query:
    #     speak_va("shutting down the laptop")
    #     os.system("shutdown /s /t 5")
# ------------------------------------------------------


 # TASK 12:
    # using os module to restart the laptop
    # elif "restart" in user_query:
    #     speak_va("reatarting the laptop")
    #     os.system("restart /r /t 5")
# -------------------------------------------------------


 # TASK 13:
    # using os module to sleep the laptop
    elif "sleep" in user_query:
        speak_va("laptop going on sleep mode")
        sleep_mode()
        
# -------------------------------------------------------

    # TASK 14:
    # using elif condition to check the term open cmd  in the user query 
    elif "open command prompt" in user_query:
        speak_va("Opening command prompt")
        os.system("start cmd")
    elif "close command prompt" in user_query:
        speak_va("closing command prompt")
        os.system("taskkill /f /im cmd.exe")
# -------------------------------------------------------

    # TASK 15:
    # using elif condition to find my location using ip address
    elif "where i am" in user_query or "location" in user_query:
        location1()

# ---------------------------------------------------------

    # TASK 16:
    # using elif to check the term switch the window in user query
    elif "switch the window"  in user_query:
        # using pyautogui module to switch the window
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("tab")
# ----------------------------------------------------------


    # TASK 17: 
    # using elif to check the term read pdf in user query
    elif "read pdf" in user_query:
        b=input("enter your pdf location :")
        open_pdf(b)
        
# ----------------------------------------------------------


    # TASK 18:
    # using elif condition to hide or unhide the files 
    # elif "hide all files" in user_query or "hide files" in user_query:
        
    
# ---------------------------------------------------------
    # TASK 19:
    elif "thanks" in user_query or "thank you"in user_query:
        print("It's my pleasure sir")
        speak_va("It's my pleasure sir")

# ---------------------------------------------------------


   # TASK 20:
    elif "things you can do" in user_query or "things that you can do" in user_query:
        print("\nI can do things like telling the current time ,open website ,open wikipedia ,crack jokes ,google search , take a sreenshot ,play a quiz , opening and closing --notepad ,MS word, MS excel , command prompt and switching the window etc .\n                                   ")
        speak_va("well sir \nI can do things like telling the current time ,open website ,open wikipedia ,crack jokes ,google search , take a sreenshot ,play a quiz , opening and closing --notepad ,MS word, MS excel , command prompt and switching the window etc .\n")

# ---------------------------------------------------------


    # LAST TASK:
    # using elif condition to check the term no in the user query
    # if the word no comes in the sentence speaked by the user then this elif will quit JARVIS
    elif "quit" in user_query or "leave" in user_query or "by" in user_query:
        speak_va("thanks for using me sir , have a good day")
        print("Thanks for using me sir , have a good day!!")
        sys.exit()
    print ("\nSir now you can proceed on for the next task....")
    speak_va("\nSir now you can proceed on for the next task ")
    print("------------------------------------------------------")

    
    

# -------------------------------------------------------------------------------------------------------

while True:
    activate_va()


# #                                    END                                          # #        

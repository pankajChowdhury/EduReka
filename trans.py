#Importing all required  dependencies
import streamlit as st
import speech_recognition as sr
from google_trans_new import google_translator
from googletrans import Translator
import pyttsx3 

#Function to translate audio 
def translate_audio(filepath, src_lang, dest_lang): 
    
        recognizer=sr.Recognizer()
        engine=pyttsx3.init()

        with sr.AudioFile(filepath) as source:
            print("Clearing the background noises")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=1) 
            
        
        try:
            result = recognizer.recognize_google(audio, language=str(src_lang))
            print("Recognized!")
            translator = Translator()
            print("Translating...")
            #Output after translation
            out = translator.translate(str(result), dest=str(dest_lang))
            return str(out.text)
        except Exception as ex:
            print("ERROR FOUND:", ex)

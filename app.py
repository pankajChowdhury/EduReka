#Importing required dependencies
import streamlit as st
from explore_page import show_explore_page
from aisuggest_page import show_aisuggest_page
from chatbot_page import show_chatbot_page
from speech_recog import show_speech_recog_page
from supply_side import show_supply_side_page

# Sidebar to switch between pages
page = st.sidebar.selectbox("Pages", ("Auto-Suggest Page", "Search by Audio Page", "Conversational-UI Page","Multi-Linguistic Notes Rendering Page", "About Us"))

#Pages of the Web-Application
if page=="Auto-Suggest Page":
    show_aisuggest_page()  #This page uses AI models to recommend courses to users based on their previously bought courses
elif page=="Search by Audio Page":
    show_speech_recog_page() #This page takes user's voice command (in multiple languages) and based on that provides the courses asked for.
elif page=="Conversational-UI Page":
    show_chatbot_page() # This is an AI based Chatting Interface for users to try.
elif page=="Multi-Linguistic Notes Rendering Page":
    show_supply_side_page() #This is a Supply side or Creator side interface
else:
    show_explore_page() #This page gives details about the applications,  AI/ML models used, datasets used to train these models, graphical representation of constraints of datasets etc.

#importing all required dependencies
import streamlit as st
import openai
import os

def show_chatbot_page(): 
    st.title("\n")
    st.title("EduReka")
    st.subheader("Welcome to AI Based Chatting Interface")
    st.title("")
   
   
    #Creating Environment
    os.environ['OPENAI_Key']=st.secrets["API_KEY"]
    openai.api_key=os.environ['OPENAI_Key']

    txt = st.text_area('How can I help you?', '''
    ''')
    #Extracting a response
    response=openai.Completion.create(engine='text-davinci-003',prompt=txt,max_tokens=200)
    #Getting Response
    if st.button("Ask now"):
        st.markdown("**Response :**")
        st.write(response['choices'][0]['text'])

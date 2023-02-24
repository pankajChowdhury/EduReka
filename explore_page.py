# Importing All Dependencies
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pickle

@st.cache_resource
def load_items():
   df = pickle.load(open('df2.pkl', 'rb'))
   df['rating'] = df['avg_rating'].astype(int)
   return df

def show_explore_page(): 
    df=load_items()

    st.title("\n")
    st.title("EduReka")
   
    st.write("EduReka is an **AI Integrated Educational and Skill Development platform**. Various innovative features are added to make user accessibility easier and prove a good experience.These features include:")
    st.subheader("1. Auto-Suggest:")
    st.markdown('''This feature runs over an Artificial Intelligence Model which predicts five most-likely-to-buy courses based
    on user's earlier bought courses.Various algorithms were implemented to design the model but the one that gave the best results was **Cosine 
    Similarity Algorithm** We first researched and found the most appropriate dataset. It was pre-processed to remove unnecessary
    and error-causing values. After this, two models were generated: one trained with about 20k data-entries, very accurate and only compatible for high-end PCs 
    saved as **model-large** (about 3.5 GB file size) and the other model trained with sufficient data and suitable for low-end PCs as well, saved as
    **model-small** . Some Details about the Dataset used to train are given below: ''')

    
    data = df["rating"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=False, startangle=0)
    ax1.axis("equal")
    st.write("""#### Percentage of Courses with user ratings in range 1 to 4""")
    st.pyplot(fig1)

    st.subheader("2. Audio Search Feature:")
    st.markdown('''This feature allows the users,especially those who are **disabled** or find difficulty 
     in typing over keyboards, to **search courses with speech**. The feature is designed to support 
     multiple languages and gives impressive results in less time. The accuracy obtained in the process is also
     very promising. We have provided two .wav files for the users to try their hands with.''')
    st.subheader("3. Multi Language Support:")
    st.markdown('''This feature allows the users to search courses in **different non-English languages**.
    Both **translation and speech-to-text feature is implemented** in the process. This feature can surely prove to be the basis 
    of future technologies making AI able to translate entire course videos or notes with impressive accuracy.''')

    st.subheader("4. AI Integrated Chat Service:")
    st.markdown('''Unlike other basic chatbot service, this feature helps user to get variety of answers over
    a question rather than just the pre-defines ones. This was made possible by integrating the **very famous Chat-GPT service**
    with the app using API endpoints. ''')

    st.subheader("5. Notes Rendering Interface:")
    st.markdown(''' This feature allows educators or creators to upload notes of lectures for their students. 
    This feature automatically converts the English-written notes of the educator into various languages. By doing so, we
    assist the **non-English** students to **get access of notes in any language they are comfortable with.**''')

    st.markdown('''**Please Note:** Since the product runs over various AI/ML algorithms, it can be definitely 
    said that the service of the product highly depends on data. The mode the product scales, more data
    it receives to train its models with, resulting in greater accuracy.''')

   
    


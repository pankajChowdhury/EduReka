#Importing Required Dependencies
import streamlit as st
import whisper
import nltk
nltk.download('punkt')
import pickle
from nltk.corpus import stopwords
nltk.download('stopwords') #Getting all stopwords defined in NLTK

from nltk.tokenize import word_tokenize
from trans import translate_audio

#Function to show page on WebApp
def show_speech_recog_page(): 

    st.title("EduReka")
    st.subheader(" Introducing Multi-linguistic Audio Search Feature")
    st.title("")
    option = st.selectbox('Select Language of audio:',('English', 'Hindi', 'Arabic', 'Bengali', 'Greek', 'Japanese', 'Tamil', 'Telugu'))
    uploaded_file = st.file_uploader("Upload a recorded audio file(in .wav):")


    #Taking Audio input and saving locally
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue() #binary output of audio
        st.audio(bytes_data, format='audio/ogg')
        with open(uploaded_file.name, 'wb') as f: #Saving the file locally for translation purpose
            f.write(uploaded_file.getbuffer())

        
        #Dictionary Created to store language codes of few languages 
        lang_codes = {'English' : 'en', 'Hindi' : 'hi', 'Arabic':'ar', 'Bengali':'bn', 'Greek':'el', 'Japanese': 'ja', 'Tamil': 'ta','Telugu': 'te'}

        speech=""
        if option=='English':
            #No translation required
            model = whisper.load_model("base")
            result = model.transcribe(uploaded_file.name,fp16=False)
            speech = result["text"]
        else: 
            speech = translate_audio(str(uploaded_file.name), str(lang_codes[option]), 'en')

        st.write("**Do you mean:**")
        st.write(speech)
        text_tokens = word_tokenize(speech)

        #Removing all Stop-words
        tokens = [word for word in text_tokens if not word in stopwords.words()]
        #Sorting in decreasing length of words as longer words should be given more preference
        tokens.sort(key=len, reverse=True)
        #Removing two-lettered words and punctuations from the list
        tokens = [word for word in tokens if len(word) > 2] 
        #Finding Courses
        df = pickle.load(open('df2.pkl', 'rb'))
        df['details'] = df[['url', 'published_time', 'price', 'avg_rating']].values.tolist()
        detail_map = dict(zip(df.title, df.details))
        courses = list(df['title'].values)

        # SEarching

        # Generate a list of courses that contain the token
        found = [course for course in courses if any(token in course for token in tokens)]

        # Take the first five items from the found list
        found = found[:5]
        
        st.subheader("Courses Found : ")
        for x in found:
           
            details  =  detail_map[x]
            st.text(str(found.index(x)+1) +". " + x)
            with st.expander("See More Details"): 
               st.markdown("Course Available on : **:green[UDEMY]**")
               st.markdown("URL : https://udemy.com"  + details[0])
               st.markdown("Published time : **" + details[1] + "**")
               st.markdown("Price : " + ":red[$" + details[2] + "$]")
               st.markdown("Average Rating  : **" + str(details[3]) + "**")
        



<h1 align="center">Welcome to EduReka -A Smart AI-Integrated Educational Platform 👋</h1>
<p>
  <a href="." target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> EduReka is an AI Integrated Smart Educational and Skill Development platform that helps students to access courses and other educational resources easily with its smart features.

### 🏠 [Homepage](https://github.com/pankajChowdhury/EduReka/)
---
### 🎥 Check out our [demo video](https://vimeo.com/802227141)
---
### 🖥️ Also Check out our [presentation](https://drive.google.com/file/d/1LvUeCPEpvFY3n_3TB3fNRsLBoyCm4KTE/view?usp=sharing)
---
## Abstract

- The objective of this project is to create a AI Integrated Educational Platform named [Edureka](https://ai-based-educational-platform-teamagastya.streamlit.app/) , which is intended to assist students in getting access to various educational resources like courses, notes etc. very easily though **smart features like auto-recommendation, audio-search(in non-english languages), chat-gpt service and multi-linguistic document conversion**. The application employs ML algorithms like **Cosine Similarity Algorithm** for accurate recommendation,**audio-processing** for speech-to-text conversion and **NLP techniques** like text extraction, preprocessing,etc for accurate text-translation. The targeted audience for this project are **students worldwide who face difficulties in searching courses by typing manually(may be disabled students or those who are uncomfortable with English keyboards) and those non-English students who find difficulties in understanding their english written notes or other documents.**


- EduReka implements **technologies such as OpenAI, Speech-to-Text, Text-Transformation,etc.** to offer students the resources that they want. The system is built to **boost productivity and save time for students** as it efficiently filters the resource that he/she needs and also in the language they want and also suggest some other courses that are most likely to be liked by them.

- EduReka very efficently removes the **language barriers** between students and education. 

---

## Features


Our Application offers several smart features. for students. More details on each of these features are mentioned below:

1.**Auto-Suggest:**

- This feature runs over an Artificial Intelligence Model which predicts five most-likely-to-buy courses based on user's earlier bought courses.

- Auto-suggesting courses not only helps students to save time looking for a course in a bush of millions but also helps the platform to sell more courses and hence scale.

2. **Audio Search Feature:**

- This feature allows the users,especially those who are disabled or find difficulty in typing over keyboards, to search courses with speech.

- The feature is designed to support multiple languages and gives impressive results in less time.

- The accuracy obtained in the process is also very promising. We have provided two .wav files in the codebase for testing.

3. **Multi Language Support:**

 - This feature allows the users to search courses in different non-English languages.
 
 - Both translation and speech-to-text feature is implemented in the process.
 
 - This feature can surely prove to be the basis of future technologies making AI able to translate entire course videos or class notes with impressive accuracy.
4.  **AI Integrated Chat Service:**

 - Unlike other basic chatbot service, this feature helps user to get variety of answers over a question rather than just the pre-defines ones.
 
 - This was made possible by integrating the very famous Chat-GPT service with the app using API endpoints.
 
5. **Notes Rendering Interface:**

 - This feature allows educators or creators to upload notes of lectures for their students. 
 
 - This feature automatically converts the English-written notes of the educator into various languages.
 
 - By doing so, we assist the non-English students to get access of notes in any language they are comfortable with.
![Screenshot from 2023-02-25 17-05-17](https://user-images.githubusercontent.com/104211567/221439826-2fcf0b4b-e30d-4800-9bd9-da0acca4150b.png)

---
## Workflow
- The workflow for **Course Recommendationation Engine** is: 

  1. User selects multiple courses and clicks Buy button to purchase them.
  
  2. The trained **AI Model (using NLP techniques like porter-stemming tokenization,etc.)** takes these bought courses as input.
  
  3. Then it creates a two-dimensional table called **Similarity table** between all the courses using *Vectorization.
  
  4. Referring to it, it quickly suggest five most similar courses.
  
  5. These similar courses are the most-likely to be bought.
  
- The workflow for **Multi-Linguistuc Audio Search** includes : 

  1. User gives an audio input to the Application
  
  2. Some **audio-processing like clearing background noises, trimming,etc** is done.
  
  3. If the Audio is in English, then it gets coverted to text. Otherwise it is translated to English and then converted to text.
  
  4. Then **NLP techniques** are applied on it for **removing stop-words and punctuations.**
  
  5. The application then takes the words of these text as tokens and sort them in descending order.
  
  6. As a result of which, most important words come in the front.
  
  7. It then starts searching for courses that contain these tokens. Once it receives five courses, it stops,avoiding unnecessary tokens to take part.
  
- The workflow for **AI Integrated Chat Service** is : 

  1. User types a question for the Chat App and clicks on ASK NOW Button.
  
  2. It then sends the question to **Chat-GPT3 API Service** and waits for response.
  
  3. Once response is received. The answer part is shown to the user.
  
- The workflow for **Notes Rendering Service** is :

  1. User uploads a document written in English.
  
  2. The Application *extracts the **text from the document** and then **translates** it to the specifies language.
  
  3. The translated text is then written in a new file and is provided for the user to download.
  
  
 

*Text extraction refers to the process of extracting relevant text data from a given source, such as a PDF document, web page, or image.

*Vectorization is the process of converting text data into a numerical vector representation, allowing it to be processed and analyzed using mathematical algorithms. 
 
 ![Screenshot from 2023-02-25 16-59-24](https://user-images.githubusercontent.com/104211567/221439721-050f2748-bc0c-40b9-9ca4-bbbc3c72c2ed.png)


----
## Tech Stack

### Programming Language

- [**Python**](https://www.python.org/doc/): A popular, high-level programming language known for its simplicity, readability, and versatility.

### Data Processing and Analysis

- [**Numpy**](https://numpy.org): A library for scientific computing and numerical analysis in Python. It provides support for large, multi-dimensional arrays and matrices, as well as a collection of mathematical functions.

### Natural Language Processing

- [**NLTK**](https://www.nltk.org): A suite of libraries and programs for natural language processing tasks such as tokenization, stemming, and part-of-speech tagging.

### DOCX Text Extraction

- [**Python-docx**](https://pypi.org/project/python-docx/): A pure-python library for extracting text from DOCX documents. It can also be used to extract metadata and other information from these files.

### Web App Framework

- [**Streamlit**](https://pypi.org/project/PyPDF2/): An open-source web app framework for building interactive, customizable, and data-driven apps using Python. It provides an intuitive UI and fast feedback, making it easy to create and iterate on apps.

### AI and Machine Learning Frameworks:

- [**OpenAI**](https://openai.com): OpenAI is known for its advanced language models such as GPT-3, which provide developers with powerful natural language processing capabilities for a wide range of applications. Their language models can perform tasks such as text completion, translation, and question-answering with impressive accuracy.

### AI Models:

- [**model-large**](https://colab.research.google.com/drive/1QtPpMV5bMebarhQesjozg7BmEZPVNHry?usp=sharing): This AI model was developed by us for the course recommendation engine. It can be easily extracted by running dump method of pickle library in the link.It was **trained with 20,000 data entries** and hence gives a remarkable accuracy.However, it takes some time to load in low-end PCs due to its **large file size of 3.5 GB.**

- [**model-small**](https://colab.research.google.com/drive/1S1z-cXiS4eS_itC9yRJ8nQg2Ukdo7pLw?usp=sharing): The same AI model when trained with **sufficient data (around 1200 data entries)** gives a satisfying result and **file size also reduces exponentially making it compatible for low-end PCs.**
Both the Models were developed for future purposes.
----

## Open-source Goods used:

1.	Python
2.	Numpy
3.	NLTK
4.	Streamlit
5.	Google-trans
6.  Whisper

---
## User's Guide 👥
Here's a quick guide to help you get started:

1. Visit [EduReka](https://ai-based-educational-platform-teamagastya.streamlit.app/)

2. Once you're on our website, you can access and switch between several features using the sidebar.

3. On Course Recommendation Page, simply select some courses and then click BUY button.On the basis of bought courses, our model will recommend you other good ones.

4. On Audio Search, select a language and just upload an audio asking for a course (sample audios already given in codebase in .wav format) and wait. You will be provided with some courses found.

5. On Chatting Interface, just type your question ad click ASK NOW button. You will get the answer.

6. On Notes Rendering Page, just upload your english-written documents in .docx format(notes.docx provided in codebase for reference).Then, select the language you want your notes to be in and wait. The system quickly shows you the download button to download.




---
## Developer's Guide 💻

### **Prerequisites: Obtain required OpenAPI Keys 🔑**

1. Go to the [OpenAI](https://openai.com) website and click on the "Sign Up"/ "Login" button

2. Once you have successfully registered/ logged in, go to the API dashboard and click on "Create API Key".

3. Select the API plan that best suits your needs and click "Continue".

4. Review the API agreement and accept the terms and conditions.

5. Your API key will now be displayed on the dashboard. Copy the key and use it in place of "st.secrets[API_KEY]" in file chatbot.py.

*Note: Keep your API key confidential and do not share it with anyone. Also, make sure to follow the OpenAI API usage guidelines to avoid any misuse of the API.*

### **Run on local server**
1. Download the zip file from [here](https://drive.google.com/file/d/1Fst3FGglAHzbof49KWVCybtm-YeUN16e/view?usp=sharing) and Extract them in your PC. Then, Open all the files in it in an IDE like VS Code. OR you may also Clone our github [repo](https://github.com/pankajChowdhury/EduReka.git)

```bash
git clone https://github.com/pankajChowdhury/EduReka.git
```
2. Install dependencies

```sh
pip freeze > requirements.txt && pip install -r requirements.txt
```

3. Run app.py
```
streamlit run app.py
```
**Note:** In LINUX, you may need to install espeak and ffmpeg packages. You can do so using commands:
```
sudo apt-get install espaek
```
```
sudo apt-get install ffmpeg
```

---
## Authors

👤 **Agastya Team**

* Pankaj Chowdhury, Department of Computer Science and Engineering, Jadavpur Univeristy, Kolkata
* Ajay Chowdhury, Department of Computer Science and Engineering, MAKAUT(W.B)
* Bikram Ghosh, Department of Mechanical Engineering, Jadavpur University, Kolkata


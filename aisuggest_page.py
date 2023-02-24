#Importing rewuired Dependencies
import streamlit as st
import pickle
import time

#Function to load models and also cache for better user-experience
@st.cache_resource
def load_items():
   df = pickle.load(open('df2.pkl', 'rb')) #pandas dataframe 
   similarity = pickle.load(open('similarity2.pkl', 'rb')) # AI-model designed using Cosine Similarity algorithm
   return [df, similarity]

def show_aisuggest_page(): 

    #loading DataFrame and models
    items = load_items()
    df=items[0]
    similarity=items[1]

    #Creating a new column in Dataframre for storing all details at one place and a hashmap for easy access
    df['details'] = df[['url', 'published_time', 'price', 'avg_rating']].values.tolist()
    detail_map = dict(zip(df.title, df.details))
    
    #List of all courses
    courses = list(df['title'].values)
    
    #Function that recommend five courses most likely to buy based on a course already bought
    def recommend_course (course) :
         course_index  = df[df['title']==course].index[0]
         distances = similarity[course_index]
         courses_list = sorted(list(enumerate(distances)), reverse=True, key = lambda x : x[1])[1 : 6]
         recommendedlist=[]
         for i in courses_list :
            recommendedlist.append(df.iloc[i[0]].title)
         return recommendedlist
    
    st.title("\n")
    st.title("EduReka")
    st.subheader(" Welcome to AI Based Course Recommendation Engine of the platform")
    st.title("")
    options = st.multiselect(
    'Select courses you wish to buy?', courses, [])
   
    st.subheader("Selected Courses: ")
    for x in options : 
        details  =  detail_map[x]
        with st.expander(x) : 
            st.markdown("Course Available on : **:green[UDEMY]**")
            st.markdown("URL : https://udemy.com"  + details[0])
            st.markdown("Published time : **" + details[1] + "**")
            st.markdown("Price : " + ":red[$" + details[2] + "$]")
            st.markdown("Average Rating  : **" + str(details[3]) + "**")
    

   
    if st.button('Buy'):
         # Progress bar of Streamlit
         progress = st.progress(0, "")
         for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1, "")
         
         st.markdown("**:green[Thanks for Buying. Happy Learning!]**")
         st.subheader("Bought Courses: ")
         recommended = []
         
         for x in options:
            st.text(str(options.index(x)+1) +". " + x)
            recommended.extend(recommend_course(x))
         st.subheader("Suggested Courses: ")
         st.write("**Note:** Some Courses are recommended by our AI model based on your previous experiences. You can can learn more about the model in the explore page")
         for x in recommended:
            
            exp  =  detail_map[x]
            st.text(str(recommended.index(x)+1) +". " + x)
            with st.expander("See More Details"): 
               st.markdown("Course Available on : **:green[UDEMY]**")
               st.markdown("URL : https://udemy.com"  + exp[0])
               st.markdown("Published time : **" + exp[1] + "**")
               st.markdown("Price : " + ":red[$" + exp[2] + "$]")
               st.markdown("Average Rating  : **" + str(exp[3]) + "**")
         
        

         
            
         
    

           

         
         
         

    
        
    
     

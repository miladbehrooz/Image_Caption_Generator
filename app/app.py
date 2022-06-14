import os
import subprocess
import requests
import streamlit as st
from gtts import gTTS 
from caption_generator import generate_caption



def file_selector(folder_path='../data/Flicker8k_Dataset/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select an image', filenames)
    return os.path.join(folder_path, selected_filename)

def text_to_speech(text):
    speech = gTTS(text = 'generated caption is   '+text, lang = 'en', slow = False)
    speech.save("./tmp/temp.mp3")
    subprocess.call(["afplay", "./tmp/temp.mp3"])
    os.remove('./tmp/temp.mp3')



submit = False


st.set_page_config(layout="centered", page_icon="📷", page_title="Saffron - An image caption generator app based on artificial intelligent")
st.sidebar.image('./images/logo.png',width=230)


with st.sidebar.expander("About the App"):
     st.write("""
        Saffron is an image caption generator that works based on artificial intelligence.
        \n  \nThis app was created by Milad Behrooz. Hope you enjoy!
     """)
with st.sidebar.container():
    source =st.radio("Please Select an Image From",
     ('Flicker8k DataSet','Your PC','Link on the Web','Your Camera'))
    
    if source =='Flicker8k DataSet':
        folder_path = '../data/Flicker8k_Dataset/'
        filename = file_selector(folder_path=folder_path)
        col1, col2, col3 = st.columns(3)
        if col2.button('Submit'):
            submit = True
    if source =='Your PC':
        uploaded_file = st.file_uploader('', type=['jpg','png','jpeg'])
        col1, col2, col3 = st.columns(3)
        if col2.button('Submit'):
            submit = True
    if source =='Link on the Web':
       url = st.text_input('Insert Image URL Here', '')
       col1, col2, col3 = st.columns(3)
       if col2.button('Submit'):
           response = requests.get(url)
           open("./tmp/temp.jpg", "wb").write(response.content)
           submit = True
    if source =='Your Camera':
        cam_img = st.camera_input("Take a picture")
        col1, col2, col3 = st.columns(3)
        if col2.button('Submit'):
            submit = True
           

if source=='Flicker8k DataSet' and  filename is not None and submit:
            col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
            with col1:
                st.write(' ')
            with col2:
                with st.spinner('Generating Caption ...'): 
                    actuals,predicted, bleu = generate_caption(filename)
                    st.image(filename)
                    st.markdown('<h3 style="text-align: left;color: red;">Generated Caption</h3>',unsafe_allow_html=True)
                    st.markdown(f'<h5 style="text-align: left">{predicted}</h5>',unsafe_allow_html=True)            
                    st.write("---")
                    with st.expander("Actual Captions"):
                        for actual in actuals:
                            st.markdown(f"- {actual}")
            with col3:
                st.write(' ')
            text_to_speech(predicted)
            
            
if source=='Your PC' and uploaded_file is not None and submit:
            col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
            with col1:
                st.write(' ')
            with col2:
                with st.spinner('Generating Caption ...'): 
                    with open('./tmp/' + uploaded_file.name,'wb') as f:
                        f.write(uploaded_file.getbuffer())
                    img = './tmp/' + uploaded_file.name
                    predicted = generate_caption(img,actual_caption=False) 
                    st.image(uploaded_file)
                    os.remove(img)   
                    st.markdown('<h3 style="text-align: left;color: red;">Generated Caption</h3>',unsafe_allow_html=True)
                    st.markdown(f'<h5 style="text-align: left">{predicted}</h5>',unsafe_allow_html=True) 
            with col3:
                st.write(' ')
            text_to_speech(predicted)   


if source=='Link on the Web' and url is not None and submit:
            col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
            with col1:
                st.write(' ')
            with col2:   
                with st.spinner('Generating Caption ...'):              
                    img = './tmp/temp.jpg'
                    predicted = generate_caption(img,actual_caption=False) 
                    st.image(img)
                    os.remove(img)   
                    st.markdown('<h3 style="text-align: left;color: red;">Generated Caption</h3>',unsafe_allow_html=True)
                    st.markdown(f'<h5 style="text-align: left">{predicted}</h5>',unsafe_allow_html=True) 
            with col3:
                st.write(' ')
            text_to_speech(predicted)   


if source=='Your Camera' and cam_img is not None and submit:
            col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
            with col1:
                st.write(' ')
            with col2:
                with st.spinner('Generating Caption ...'): 
                    with open('./tmp/' + cam_img.name,'wb') as f:
                        f.write(cam_img.getbuffer())
                    img = './tmp/' + cam_img.name
                    predicted = generate_caption(img,actual_caption=False)
                    st.image(cam_img) 
                    os.remove(img)   
                    st.markdown('<h3 style="text-align: left;color: red;">Generated Caption</h3>',unsafe_allow_html=True)
                    st.markdown(f'<h5 style="text-align: left">{predicted}</h5>',unsafe_allow_html=True)     
            with col3:
                st.write(' ')
            text_to_speech(predicted) 

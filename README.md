# Image Caption Generator App 
![demo](demo.gif)
- Built model based on CNN and LSTM to generate captions for images automatically
 - Trained deep learning model on Flickr8K dataset. 
- Built an image caption generator  web application with Streamlit based on the deep learning model  

## Usage 
- Clone the git repository: ```git clone https://github.com/miladbehrooz/Image_Caption_Generator.git```
- Download [Flicker8K](https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip) Dataset
- Unzip and copy Flicker8k_Dataset to ```data``` folder
- Install the requirements: ```pip install requirements.txt```
- Run web app locally: ``` streamlit app/app.py```

### To do
- Use Inception pre-trained image model instead of VGG16
- Use the pre-trained Embedding layer in the LSTM model
- Tune the configuration of the model to achieve better performance

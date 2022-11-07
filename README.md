# Image Caption Generator App 
![demo](demo.gif)

In this project, the image caption generator using CNN-LSTM encoder-decoder model was implemented. The image features were extracted from the CNN model and then those were fed into the LSTM model which is responsible for generating the image captions.
Project workflow consists of following steps:

- Created features for each image using VGG16 pre-trained CNN.
-  Prepared text data which involves text cleaning and text tokenization.
- Transformed image features and text data into input-output pairs of data for training CNN-LSTM model.
- Built, trained and evaluated an encoder-decoder neural network.
- Built an image caption generator web application with Streamlit based on the CNN-LSTM model.


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

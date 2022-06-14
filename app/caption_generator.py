import pickle
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.translate.bleu_score import sentence_bleu



def features_extraction(image_path):
    """
    extract features from given image
    """
    # load the model
    model = VGG16(weights='imagenet')
    # remove the last layer (dense layer) of model
    layer_output = model.layers[-2].output
    model = Model(inputs=model.inputs, outputs=layer_output)
    # extract features of photos
    # load an image from file
    #image_path = '../data/Flicker8k_Dataset/' + image_id + '.jpg'
    image = load_img(image_path, target_size=(224, 224))
    # convert image to a numpy array
    numpy_image = np.array(image)
    # add an extra dimension to the image in numpy array fromat to define number of samples
    image_batch = np.expand_dims(numpy_image, axis=0)
    # do preprocessing on the image for the VGG model
    processed_image = preprocess_input(image_batch)
    # get features
    feature = model.predict(processed_image, verbose=0)
    return feature
def get_captions(text):
    """
    extract the image id and related image captions from text file and 
    retuern them in a dict.
    """
    
    captions = text.split('\n')
    descriptions = {}
    for caption in captions[:-1]:
        image_id , image_des = caption.split('\t')
        image_id = image_id.split('.')[0]

        if image_id not in descriptions:
            descriptions[image_id] = [image_des] 
        else:
            descriptions[image_id].append(image_des)
    return descriptions

def load_text_file(filepath):
    """
    load text file from given filepath
    """
    with open(filepath,'r') as file:
        text = file.read()
    file.close()
    return text
def predict_caption(model, feature,tokenizer,max_len): 
    in_text = 'startseq'
    for i in range(max_len):
        seq = tokenizer.texts_to_sequences([in_text])[0]
        seq = pad_sequences([seq],max_len)
        y_pred = model.predict([feature,seq],verbose = 0)
        y_pred = np.argmax(y_pred)
        new_word = index_to_word[y_pred]
        if new_word is None:
            break
        in_text += " " + new_word
        if new_word == "endseq":
            break
    return in_text

def generate_caption(image_path, actual_caption = True):
    
    feature = features_extraction(image_path)
    y_pred = predict_caption(model, feature,tokenizer,max_len)
    y_pred = y_pred.split()[1:-1]
    y_pred =  " ".join(y_pred)
    
    if actual_caption:
        actuals = []
        bleu = 0
        image_id = image_path.split('/')[-1].split('.')[0]
        captions = cleaned_captions[image_id]
        for caption in captions:
            caption= caption.split()[1:-1]
            caption =  " ".join(caption)
            actuals.append(caption)
            bleu += sentence_bleu([caption],y_pred)
            
    
        bleu = bleu / len(captions)
    
        return actuals,y_pred,bleu
    else:
        return y_pred


model = load_model('../models/model-ep003-loss3.366-val_loss3.974.h5')
 
with open('../models/tokenizer.pkl','rb') as tok:
    tokenizer = pickle.load(tok)


cleaned_captions = load_text_file('../data/cleaned_captions.txt')
cleaned_captions = get_captions(cleaned_captions)
     
max_len = 34

index_to_word = dict([(index,word) for word, index in tokenizer.word_index.items()])



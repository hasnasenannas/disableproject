import streamlit as st
import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
import joblib
#nltk.download('stopwords')
st.title('DISABILITY CLASSIFICATION')
st.balloons()


spam_model = joblib.load('proj.joblib')
vectorizer = joblib.load('CountVect.joblib')
inp_text = st.text_area('Paste the Disability type to know the name of disability ',height=200)

vectorised_text = vectorizer.transform([inp_text])
pred = ''
# add a placeholder

def spam_predict(inp_text):
    prediction = spam_model.predict(inp_text)
    if prediction == 0:
        pred = 'Amyotrophic lateral sclerosis'
    elif prediction == 1:
        pred = 'Aphasia'        
    elif prediction == 2:
        pred = 'Autism'             
    elif prediction == 3:
        pred = 'Blindness '         
    elif prediction == 4:
        pred = 'Cerebral Palsy'   
    elif prediction == 5:
        pred = 'Deaf'         
    elif prediction == 6:
        pred = 'DeafBlind'         
    elif prediction == 7:
        pred = 'Dementia'         
    elif prediction == 8:
        pred = 'Diabetes'         
    elif prediction == 9:
        pred = 'Down syndrome'         
    elif prediction == 10:
        pred = 'Dump'         
    elif prediction == 11:
        pred = 'Dwarfism'         
    elif prediction == 12:
        pred = 'Dyslexia'         
    elif prediction == 13:
        pred = 'Dyspraxia'         
    elif prediction == 14:
        pred = 'Dystonia '         
    elif prediction == 15:
        pred = 'Epilepsy' 
    elif prediction == 16:
        pred = 'Hemophilia'         
    elif prediction == 17:
        pred = 'Huntingtons disease'         
    elif prediction == 18:
        pred = 'Intellectual disability'         
    elif prediction == 19:
        pred = 'Leprosy'         
    elif prediction == 20:
        pred = 'Locomotor Disability'         
    elif prediction == 21:
        pred = 'Mental Illness'         
    elif prediction == 22:
        pred = 'Mental Retardation'         
    elif prediction == 23:
        pred = 'Mental Retardation'         
    elif prediction == 24:
        pred = 'Multiple Sclerosis'         
    elif prediction == 25:
        pred = 'Muscular Dystrophy'         
    elif prediction == 26:
        pred = 'Muscular Dystrophy'         
    elif prediction == 27:
        pred = 'Paralytic Illness'         
    elif prediction == 28:
        pred = 'Parkinson’s disease'
    elif prediction == 29:
        pred = 'Schizophrenia'        
    elif prediction == 30:
        pred = 'Sickle Cell Disease'        
    elif prediction == 31:
        pred = 'Stammering'        
    elif prediction == 32:
        pred = 'Thalassemia'        
    elif prediction == 33:
        pred = 'Tourette syndrome'                                
    else :
        pred = 'INVALID TEXT'
    return pred
if st.button('Classify'):
    st.write('The name of disability is:  ',spam_predict(vectorised_text))
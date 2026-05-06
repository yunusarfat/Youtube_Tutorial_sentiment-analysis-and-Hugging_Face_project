import pickle
import gradio as gr
import re

# load model
model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def predict(text):
    clean = preprocess(text)
    vec = tfidf.transform([clean])
    pred = model.predict(vec)[0]
    return f"Cleaned: {clean}\nSentiment: {pred}"

gr.Interface(fn=predict, inputs="text", outputs="text").launch()

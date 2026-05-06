# YouTube Tutorial Segment Reviews Sentiment Analysis (NLP Project)
###  Project Overview

This project performs sentiment analysis on YouTube tutorial segment reviews/comments using Natural Language Processing (NLP) and Machine Learning. The goal is to classify user feedback on tutorial segments into Positive or Negative sentiment based on the review text. The dataset contains user feedback extracted from tutorial-related review/comments data.
### Objective
* Clean and preprocess real-world text data (YouTube-style comments)
* Perform exploratory data analysis (EDA)
* Extract meaningful features from text
* Build a sentiment classification model
* Deploy an interactive web app using Hugging Face Spaces
Live Demo

## 👉 Try the live application here:
🔗 [https://huggingface.co/spaces/arfat16/Youtube-Tutorial-Sentiment-Analysis]

### Dataset Information
#### Dataset: YouTube Tutorial Segment Reviews (from Kaggle / tutorial dataset)
Columns used:
Text → User review/comment
Score → Rating or sentiment indicator
Sentiment Mapping:
* Score 1–2 → Negative 
* Score 3 → Neutral 
* Score 4–5 → Positive 

### Tech Stack
* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib / Seaborn
* TF-IDF Vectorizer (unigram + bigram)
* LinearSVC (or Logistic Regression)
* Gradio (UI)
* Hugging Face Spaces (deployment)

### Feature Engineering
* Word Count
* Character Count
* Vocabulary Size
* Most Frequent Words
* TF-IDF Features (1-gram + 2-gram)

### Machine Learning Model
Model Used: Linear Support Vector Classifier (LinearSVC)
### Performance:
Accuracy Achieved: ~0.82

### Input:
This tutorial explanation is terrible 
### Output:
Cleaned: tutorial explanation terrible  <br/>
Sentiment: Negative 😞<br/>

### 👨‍💻 Author

Arfat<br/>
Full-Stack Developer | ML Enthusiast
  

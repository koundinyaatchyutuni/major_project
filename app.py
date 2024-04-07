from flask import Flask, render_template, request
import pandas as pd
import pickle
import en_SkillExtraction
import pymongo
import pandas as pd
import maj
import pke
import string
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nlp = en_SkillExtraction.load()
import traceback
from flashtext import KeywordProcessor
from keybert import KeyBERT
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'
client = pymongo.MongoClient("mongodb+srv://mulesaikrishnareddy2003:saikris2003@cluster0.bnz2azr.mongodb.net/subject_DB?retryWrites=true&w=majority")
def extract_keywords(text):
    
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    
    keywords = model.extract_keywords(text)
    
    return [keyword[0] for keyword in keywords][:5]



db = client["subject_DB"]

collection = db["subjects"]

x = pickle.load(open('test.pkl', 'rb'))

que = x.m()
qt = x.l()
x.set_seed(42)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')

def about():
      return render_template('about.html')

@app.route('/contact')

def contact():
      return render_template('contact.html')

@app.route('/main')

def main():
      return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    w=request.form['jobDescription']
   
    st = str(w)
    doc = nlp(st)
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    
    skills = list(set(skills))
    skills=[skill.lower() for skill in skills]
   

    matching_documents = collection.find({"topic": {"$in": skills}})
    matching_documents_content=[]
    for document in matching_documents:
   
        for content_item in document["content"]:
            matching_documents_content.append(content_item['value'])
   
    questions = []
    
    i=0
    for text in matching_documents_content:
        i+=1
        qs = []
      
        summarized_text = x.summarizer(text, x.summary_model, x.summary_tokenizer)
             
        keywords = extract_keywords(text)
        print ("keywords unsummarized: ",keywords)
        keyword_processor = KeywordProcessor()
        for keyword in keywords:
            keyword_processor.add_keyword(keyword)
            keywords_found = keyword_processor.extract_keywords(summarized_text)
            keywords_found = list(set(keywords_found))
        print ("keywords_found in summarized: ",keywords_found)

        important_keywords =[]
        for keyword in keywords:
            if keyword in keywords_found:
                important_keywords.append(keyword)
               
        for answer in important_keywords:
            ques = x.get_question(summarized_text, answer, que, qt) 
            qs.append(ques)
        qsz = set(qs)
        for z in qsz:
            questions.append(z)
            questions=list(set(questions))
        if(i==5):
            break    
    return render_template("main.html", prediction_text=questions)


if __name__ == "__main__":
    app.run(debug=True)

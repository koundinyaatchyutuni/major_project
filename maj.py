import pandas as pd
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer
import random
import numpy as np
import nltk
# import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
# import nltk   
nltk.download('averaged_perceptron_tagger')
import string
nltk.download('punkt')
nltk.download('brown')
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import pke
import traceback
from flashtext import KeywordProcessor


class maj:


  def set_seed(self,seed: int):
      random.seed(seed)
      np.random.seed(seed)
      torch.manual_seed(seed)
      torch.cuda.manual_seed_all(seed)

  def postprocesstext(self,content):
    final=""
    for sent in sent_tokenize(content):
      sent = sent.capitalize()
      final = final +" "+sent
    return final
  
  summary_model = T5ForConditionalGeneration.from_pretrained('t5-base')
  summary_tokenizer = T5Tokenizer.from_pretrained('t5-base')

  
  def summarizer(self,text,model,tokenizer):
    text = text.strip().replace("\n"," ")
    text = "summarize: "+text
   
    max_len = 512
    encoding = tokenizer.encode_plus(text,max_length=max_len, pad_to_max_length=False,truncation=True, return_tensors="pt")

    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    outs = model.generate(input_ids=input_ids,
                                    attention_mask=attention_mask,
                                    early_stopping=True,
                                    num_beams=3,
                                    num_return_sequences=1,
                                    no_repeat_ngram_size=2,
                                    min_length = 75,
                                    max_length=300)


    dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
    summary = dec[0]
    summary = self.postprocesstext(summary)
    summary= summary.strip()
    return summary
  
  
  

  def m(self):
    question_model = T5ForConditionalGeneration.from_pretrained('Koundinya-Atchyutuni/t5-end2end-questions-generation')
    
    return question_model
  
  def l(self):
    question_tokenizer = T5Tokenizer.from_pretrained('Koundinya-Atchyutuni/t5-end2end-questions-generation')
    return question_tokenizer

  def get_question(self,context,answer,model,tokenizer):
    text = "context: {} answer: {}".format(context,answer)
    encoding = tokenizer.encode_plus(text,max_length=384, pad_to_max_length=False,truncation=True, return_tensors="pt")
    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]
    outs = model.generate(input_ids=input_ids,
                                    attention_mask=attention_mask,
                                    early_stopping=True,
                                    num_beams=5,
                                    num_return_sequences=1,
                                    no_repeat_ngram_size=2,
                                    max_length=72)
    dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]
    Question = dec[0].replace("question:","")
    Question= Question.strip()
    return Question
  
import pickle
obj=maj()
pickle.dump(obj,open('test.pkl','wb'))
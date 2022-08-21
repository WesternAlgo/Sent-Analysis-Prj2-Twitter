import spacy
import csv 
 
nlp = spacy.load("en_core_web_sm")
with open('tweetsList.txt','rt+') as f:
    for line in f.readlines():
        #lines = f.readline()
        doc=nlp(line)
        for ent in doc.ents:
            print(ent.text, ent.label_)

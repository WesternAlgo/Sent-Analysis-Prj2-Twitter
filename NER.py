import spacy
import csv 
from itertools import *
 
nlp = spacy.load("en_core_web_sm")

with open('tweetsList.txt','rt+') as f:
    for line in f.readlines():
        #lines = f.readline()
        doc=nlp(line)
 #entities = {key: list(g) for key, g in groupby(sorted(doc.ents, key=lambda x: x.label_), lambda x: x.label_)}
        for ent in doc.ents:
           print(ent.text, ent.label_)
            #textF.write(ent.text, ent.label_)   
    entities = {key: list(set(map(lambda x: str(x), g))) for key, g in groupby(sorted(doc.ents, key=lambda x: x.label_), lambda x: x.label_)}
    print(entities['DATE'])
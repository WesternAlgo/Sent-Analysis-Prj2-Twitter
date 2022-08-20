import spacy
 
nlp = spacy.load("en_core_web_sm")
 
text = "Sundar Pichai, the CEO of Google Inc. is walking in the streets of California."
 
doc = nlp(text)
 
for ent in doc.ents:
    print(ent.text, ent.label_)

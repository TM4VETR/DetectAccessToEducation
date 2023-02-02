import pickle
import spacy

nlp = spacy.load("de_core_news_sm")

file = open("data/m1.map",'rb')
matcher = pickle.load(file)
file.close()
file = open("data/m2.map",'rb')
matcher2 = pickle.load(file)
file.close()
file = open("data/m3.map",'rb')
matcher4 = pickle.load(file)
file.close()
file = open("data/mv.map",'rb')
voc = pickle.load(file)
file.close()

def accessdetection(text):
    doc = nlp(text.replace("Schulabschluss","Hauptschulabschluss"))
    retrieved = []
    matches = matcher4(doc)
    for match_id, start, end in matches:
        rule_id = voc[match_id]  # get the unicode ID, i.e. 'COLOR'
        retrieved.append(rule_id)
    matches = matcher(doc)
    for match_id, start, end in matches:
        rule_id = voc[match_id]  
        retrieved.append(rule_id)
    matches = matcher2(doc)
    for match_id, start, end in matches:
        rule_id = voc[match_id]
        retrieved.append(rule_id)
    retrieved = list(set(retrieved))
    if "X" in retrieved:
        retrieved.remove("X")
    if "B-" in retrieved:
        if "B+" in retrieved:
            retrieved.remove("B+")
        retrieved.remove("B-")
    if "BE-" in retrieved:
        if "BE" in retrieved:
            retrieved.remove("BE")
        retrieved.remove("BE-")
    return (retrieved)

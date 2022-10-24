from pyexpat import model
from utlis import freeling_analyze
from tqdm import tqdm
from time import time
import os, spacy
import stanza

filein = open('Alicia_utf8.txt', 'r')

print('\033[96m\033[1m***Analyzing with Freeling***\033[0m')
sentences = [line for line in filein]

start = time()
with open('freeling.txt', 'w') as file:
  for i in tqdm(range(len(sentences)), bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):
    file.write(' '.join(freeling_analyze(sentences[i])) + '\n')

print(f'\033[96m\033[1mTime: {time() - start}\033[0m')


print('\033[96m\033[1m***Analyzing with Spacy***\033[0m')
os.system('python -m spacy download es_core_news_sm')

model = spacy.load("es_core_news_sm")

start = time()
with open('Spacy.txt', 'w') as file:
  for i in tqdm(range(len(sentences)), bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):

    proc = model(sentences[i].strip())
    file.write(' '.join([f'{word.text}/{word.tag_}' for word in proc]) + '\n')

print(f'\033[96m\033[1mTime: {time() - start}\033[0m')


print('\033[96m\033[1m***Analyzing with Stanza***\033[0m')

stanza.download('es')
model = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos')

start = time()
with open('Stanza.txt', 'w') as file:

  for i in tqdm(range(len(sentences)), bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}'):

    proc = model(sentences[i].strip())
    file.write(' '.join([f'{word.text}/{word.upos}' for sent in proc.sentences for word in sent.words]) + '\n')

print(f'\033[96m\033[1mTime: {time() - start}\033[0m')

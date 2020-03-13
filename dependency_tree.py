import numpy as np
import spacy
import pickle
from Utils.entityopinionparser import parseXML

nlp = spacy.load('en_core_web_sm')

def dependency_adj_matrix(text):
    document = nlp(text)
    seq_len = len(text.split())
    matrix = np.zeros((seq_len, seq_len)).astype('float32')
    
    for token in document:
        if token.i < seq_len:
            matrix[token.i][token.i] = 1

            for child in token.children:
                if child.i < seq_len:
                    matrix[token.i][child.i] = 1
    
    return matrix

def process(filename):
    idx2graph = {}

    reviews = parseXML(filename)
    review_list = []
    EA_Pair_list = []

    for review in reviews:
        if review['EA_Pair'] == []:
            pass
        else:
            review_list.append(review['sentence'])
            EA_Pair_list.append(review['EA_Pair'])

    for i, sentence in enumerate(review_list):
        adj_matrix = dependency_adj_matrix(sentence)
        idx2graph[i] = adj_matrix

    print(idx2graph)

if __name__ == "__main__":
    process(r'C:/Users/ujzr76l/Desktop/ABSA/ABSA-15_Laptops_Train_Data.xml')
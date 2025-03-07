from __future__ import unicode_literals
from hazm import sent_tokenize, word_tokenize, Normalizer
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def preprocess_text(text):
    normalizer = Normalizer()
    text = normalizer.normalize(text)
    sentences = sent_tokenize(text)
    return sentences

def build_similarity_matrix(sentences):
    tfidf_vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

def summarize_text(text, num_sentences=3):
    sentences = preprocess_text(text)
    similarity_matrix = build_similarity_matrix(sentences)
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = ' '.join([s for _, s in ranked_sentences[:num_sentences]])
    return summary

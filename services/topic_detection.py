import numpy as np
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from hazm import stopwords_list

def topic_modeling_persian(documents, n_topics=3, n_top_words=5):
    persian_stop_words = stopwords_list()
    
    tfidf_vectorizer = TfidfVectorizer(stop_words=persian_stop_words)
    tfidf = tfidf_vectorizer.fit_transform(documents)
    
    nmf_model = NMF(n_components=n_topics, random_state=42)
    nmf_model.fit(tfidf)
    
    feature_names = tfidf_vectorizer.get_feature_names_out()
    topics = {}
    for topic_idx, topic in enumerate(nmf_model.components_):
        top_indices = topic.argsort()[:-n_top_words - 1:-1]
        topics[f"موضوع {topic_idx+1}"] = [feature_names[i] for i in top_indices]
    
    return topics

def detect_topic(text: str) -> str:
    if not text:
        return "متنی دریافت نشد."
    
    # تقسیم متن به اسناد جداگانه بر اساس خط‌های جدید
    documents = [line.strip() for line in text.split("\n") if line.strip()]
    if len(documents) < 2:
        documents = [text]
    
    n_topics = min(3, len(documents))  
    topics = topic_modeling_persian(documents, n_topics=n_topics)
    
    result_str = "موضوعات استخراج شده:\n"
    for topic, words in topics.items():
        result_str += f"{topic}: {', '.join(words)}\n"
    
    return result_str

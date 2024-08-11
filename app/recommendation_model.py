import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

class JobRecommendationModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.job_features = None
        self.jobs = None

    def fit(self, jobs):
        self.jobs = jobs
        job_descriptions = [f"{job['title']} {' '.join(job['skills'])}" for job in jobs]
        self.job_features = self.vectorizer.fit_transform(job_descriptions)

    def get_recommendations(self, user_skills, top_n=5):
        user_description = " ".join(user_skills)
        user_features = self.vectorizer.transform([user_description])
        similarities = cosine_similarity(user_features, self.job_features)[0]
        top_indices = similarities.argsort()[-top_n:][::-1]
        return [(self.jobs[i], float(similarities[i])) for i in top_indices]

    def update(self, new_jobs):
        updated_jobs = self.jobs + new_jobs
        self.fit(updated_jobs)

    def save_model(self, filename):
        joblib.dump({
            'vectorizer': self.vectorizer,
            'job_features': self.job_features,
            'jobs': self.jobs
        }, filename)

    @classmethod
    def load_model(cls, filename):
        data = joblib.load(filename)
        model = cls()
        model.vectorizer = data['vectorizer']
        model.job_features = data['job_features']
        model.jobs = data['jobs']
        return model
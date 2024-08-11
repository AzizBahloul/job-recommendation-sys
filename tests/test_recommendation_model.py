import pytest
from app.recommendation_model import JobRecommendationModel

@pytest.fixture
def sample_jobs():
    return [
        {"id": 1, "title": "Python Developer", "skills": ["python", "django", "flask"]},
        {"id": 2, "title": "Data Scientist", "skills": ["python", "machine learning", "statistics"]},
        {"id": 3, "title": "Frontend Developer", "skills": ["javascript", "react", "css"]}
    ]

def test_model_fit(sample_jobs):
    model = JobRecommendationModel()
    model.fit(sample_jobs)
    assert model.jobs == sample_jobs
    assert model.job_features is not None

def test_get_recommendations(sample_jobs):
    model = JobRecommendationModel()
    model.fit(sample_jobs)
    recommendations = model.get_recommendations(["python", "machine learning"])
    assert len(recommendations) == 3
    assert recommendations[0][0]['title'] == "Data Scientist"

def test_update_model(sample_jobs):
    model = JobRecommendationModel()
    model.fit(sample_jobs)
    new_job = {"id": 4, "title": "DevOps Engineer", "skills": ["docker", "kubernetes", "jenkins"]}
    model.update([new_job])
    assert len(model.jobs) == 4
    assert model.jobs[-1] == new_job
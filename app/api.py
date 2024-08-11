from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .recommendation_model import JobRecommendationModel

app = FastAPI()
model = JobRecommendationModel()

class UserSkills(BaseModel):
    skills: List[str]

class Job(BaseModel):
    id: int
    title: str
    skills: List[str]

class JobRecommendation(BaseModel):
    job_id: int
    title: str
    score: float

@app.post("/recommendations", response_model=List[JobRecommendation])
async def get_recommendations(user_skills: UserSkills):
    recommendations = model.get_recommendations(user_skills.skills)
    return [JobRecommendation(job_id=job['id'], title=job['title'], score=score) 
            for job, score in recommendations]

@app.post("/update_model")
async def update_model(new_jobs: List[Job]):
    model.update([job.dict() for job in new_jobs])
    return {"message": "Model updated successfully"}
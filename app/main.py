from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database, recommendations
from pydantic import BaseModel
from typing import List

app = FastAPI()

class InteractionCreate(BaseModel):
    user_id: int
    job_id: int
    interaction_type: str
    interaction_value: float

class JobMetadataCreate(BaseModel):
    job_id: int
    title: str
    description: str
    skills: List[str]

@app.get("/api/recommendations/{user_id}")
def get_recommendations(user_id: int, db: Session = Depends(database.get_db)):
    recommended_jobs = recommendations.get_job_recommendations(user_id, db)
    return {"user_id": user_id, "recommended_jobs": recommended_jobs}

@app.post("/api/recommendations/interactions")
def log_interaction(interaction: InteractionCreate, db: Session = Depends(database.get_db)):
    new_interaction = recommendations.log_interaction(
        interaction.user_id, 
        interaction.job_id, 
        interaction.interaction_type, 
        interaction.interaction_value,
        db
    )
    return {"message": "Interaction logged successfully"}

@app.post("/api/recommendations/job-metadata")
def update_job_metadata(job_metadata: JobMetadataCreate, db: Session = Depends(database.get_db)):
    updated_metadata = recommendations.update_job_metadata(
        job_metadata.job_id,
        job_metadata.title,
        job_metadata.description,
        job_metadata.skills,
        db
    )
    return {"message": "Job metadata updated successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
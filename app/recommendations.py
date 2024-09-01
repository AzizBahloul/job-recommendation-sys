import numpy as np
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Optional
from . import models, utils
import logging
from fastapi import HTTPException
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

class RecommendationEngine:
    def __init__(self):
        self.postings_df = None
        self.tfidf_matrix = None
        self.cosine_sim = None

    def load_data(self):
        try:
            self.postings_df, self.tfidf_matrix, _ = utils.load_data()
            self.cosine_sim = cosine_similarity(self.tfidf_matrix)
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            raise HTTPException(status_code=500, detail="Error loading recommendation data")

    def get_recommendations(self, job_index: int, num_recommendations: int) -> List[Dict[str, Any]]:
        sim_scores = list(enumerate(self.cosine_sim[job_index]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations + 1]
        job_indices = [i[0] for i in sim_scores]
        scores = [i[1] for i in sim_scores]
        return [
            {"job_id": int(self.postings_df.iloc[i]['job_id']), "score": float(score)}
            for i, score in zip(job_indices, scores)
        ]

recommendation_engine = RecommendationEngine()

async def get_job_recommendations(user_id: int, db: Session, num_recommendations: int = 5) -> List[Dict[str, Any]]:
    if recommendation_engine.postings_df is None:
        recommendation_engine.load_data()

    try:
        recent_interactions = db.query(models.UserInteraction).filter(
            models.UserInteraction.user_id == user_id
        ).order_by(models.UserInteraction.interaction_timestamp.desc()).limit(5).all()
    except Exception as e:
        logger.error(f"Error fetching user interactions: {e}")
        raise HTTPException(status_code=500, detail="Error fetching user interactions")

    if not recent_interactions:
        logger.info(f"No recent interactions for user {user_id}. Returning random recommendations.")
        random_jobs = recommendation_engine.postings_df.sample(num_recommendations)
        return [
            {"job_id": int(job.job_id), "score": 1.0} 
            for _, job in random_jobs.iterrows()
        ]

    job_id = recent_interactions[0].job_id
    logger.info(f"Generating recommendations based on job_id: {job_id}")

    job_index = recommendation_engine.postings_df[recommendation_engine.postings_df['job_id'] == job_id].index
    if len(job_index) == 0:
        logger.warning(f"Job ID {job_id} not found in postings DataFrame.")
        raise HTTPException(status_code=404, detail="Job ID not found in postings data")

    return recommendation_engine.get_recommendations(job_index[0], num_recommendations)

def log_interaction(user_id: int, job_id: int, interaction_type: str, interaction_value: float, db: Session) -> models.UserInteraction:
    try:
        new_interaction = models.UserInteraction(
            user_id=user_id,
            job_id=job_id,
            interaction_type=interaction_type,
            interaction_value=interaction_value
        )
        db.add(new_interaction)
        db.commit()
        db.refresh(new_interaction)
        return new_interaction
    except Exception as e:
        logger.error(f"Error logging interaction: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Error logging interaction")

def update_job_metadata(job_id: int, title: str, description: str, skills: List[str], db: Session) -> models.JobMetadata:
    try:
        job_metadata = db.query(models.JobMetadata).filter(models.JobMetadata.job_id == job_id).first()
        if job_metadata:
            job_metadata.title = title
            job_metadata.description = description
            job_metadata.skills = skills
        else:
            job_metadata = models.JobMetadata(job_id=job_id, title=title, description=description, skills=skills)
            db.add(job_metadata)
        db.commit()
        db.refresh(job_metadata)
        return job_metadata
    except Exception as e:
        logger.error(f"Error updating job metadata: {e}")
        db.rollback()
        raise HTTPException(status_code=500, detail="Error updating job metadata")

def refresh_recommendations():
    recommendation_engine.load_data()
    logger.info("Recommendation data refreshed")
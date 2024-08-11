import uvicorn
from app.utils import load_job_data
from app.recommendation_model import JobRecommendationModel
from app.api import app, model

if __name__ == '__main__':
    # Load initial job data
    jobs = load_job_data('data/job_data.json')
    
    # Initialize and train the model
    model.fit(jobs)
    
    # Run the FastAPI app
    uvicorn.run(app, host="0.0.0.0", port=8000)
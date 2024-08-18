
# Job Recommendation System

This project provides a job recommendation system using FastAPI, SQLAlchemy, and a content-based recommendation model. The system allows users to get job recommendations based on their interactions and update job metadata.

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Pandas**: Data manipulation and analysis library.
- **Scikit-learn**: Machine learning library used for TF-IDF vectorization and computing cosine similarity.
- **Joblib**: Used for saving and loading model artifacts.
- **PostgreSQL**: Database used for storing user interactions and job metadata.

## Endpoints

### 1. **Get Recommendations**

**Endpoint:** `GET /api/recommendations/{user_id}`  
**Description:** Retrieves job recommendations for a specific user. Recommendations are based on the user's recent interactions with jobs.

**Parameters:**
- `user_id` (path parameter): The ID of the user for whom to get recommendations.

**Response:**
- Returns a list of recommended jobs with their IDs and scores.

### 2. **Log Interaction**

**Endpoint:** `POST /api/recommendations/interactions`  
**Description:** Logs a new interaction between a user and a job.

**Request Body:**
```json
{
  "user_id": 1,
  "job_id": 123,
  "interaction_type": "click",
  "interaction_value": 5.0
}
```

**Response:**
- Returns a message indicating that the interaction was logged successfully.

### 3. **Update Job Metadata**

**Endpoint:** `POST /api/recommendations/job-metadata`  
**Description:** Updates or creates metadata for a job, including its title, description, and skills.

**Request Body:**
```json
{
  "job_id": 123,
  "title": "Software Engineer",
  "description": "Develop and maintain software applications.",
  "skills": ["Python", "Django", "SQL"]
}
```

**Response:**
- Returns a message indicating that the job metadata was updated successfully.

## How to Run

1. **Install Dependencies:**  
   Ensure you have Python 3.7+ installed and then install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Database:**  
   Make sure PostgreSQL is running and configured with the credentials provided in `app/database.py`.

3. **Run the Application:**  
   Start the FastAPI application using:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

4. **Access the API:**  
   The API will be available at `http://localhost:8000`. You can use tools like [Swagger UI](http://localhost:8000/docs) or [Postman](https://www.postman.com/) to interact with the endpoints.

## Data Preparation

1. **Preprocess Data:**  
   Run `scripts/preprocess.ipynb` to preprocess the job postings data and save the necessary files.

2. **Train Model:**  
   Execute `scripts/train_model.py` to compute and save the cosine similarity matrix used for recommendations.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. For any questions or issues, please contact [Your Name].

---

You can adjust the details according to your specific setup and preferences.

# 🎯 Job Recommendation System

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
</div>

<div align="center">
  <h3>🚀 Intelligent Job Matching Powered by Machine Learning</h3>
  <p>A sophisticated content-based recommendation system that connects job seekers with their perfect opportunities using advanced ML algorithms and real-time user interaction tracking.</p>
</div>

---

## ✨ Features

- 🤖 **Smart Recommendations** - Content-based filtering using TF-IDF and cosine similarity
- 📊 **Real-time Analytics** - Track user interactions and behavior patterns
- 🔄 **Dynamic Updates** - Live job metadata management
- 🎯 **Personalized Results** - Tailored job suggestions based on user history
- ⚡ **High Performance** - Fast API responses with optimized database queries
- 📚 **Interactive Documentation** - Built-in Swagger UI for easy testing

## 🛠️ Tech Stack

<table>
<tr>
<td align="center"><strong>Backend</strong></td>
<td align="center"><strong>Database</strong></td>
<td align="center"><strong>ML/Data</strong></td>
<td align="center"><strong>Tools</strong></td>
</tr>
<tr>
<td align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" width="100" alt="FastAPI"><br>
  <strong>FastAPI</strong>
</td>
<td align="center">
  <img src="https://wiki.postgresql.org/images/a/a4/PostgreSQL_logo.3colors.svg" width="100" alt="PostgreSQL"><br>
  <strong>PostgreSQL</strong>
</td>
<td align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="100" alt="Scikit-learn"><br>
  <strong>Scikit-learn</strong>
</td>
<td align="center">
  <img src="https://pandas.pydata.org/static/img/pandas_white.svg" width="100" alt="Pandas"><br>
  <strong>Pandas</strong>
</td>
</tr>
</table>

### Core Technologies

| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | Modern, fast web framework for building APIs | Latest |
| **SQLAlchemy** | Python SQL toolkit and ORM | Latest |
| **Pandas** | Data manipulation and analysis | Latest |
| **Scikit-learn** | Machine learning library for TF-IDF and similarity | Latest |
| **Joblib** | Model persistence and caching | Latest |
| **PostgreSQL** | Primary database for storing interactions and metadata | 12+ |

## 🚀 Quick Start

### Prerequisites

```bash
# Ensure you have Python 3.7+ installed
python --version

# PostgreSQL should be running
psql --version
```

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd job-recommendation-system
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   ```bash
   # Update database credentials in app/database.py
   # Ensure PostgreSQL is running with correct permissions
   ```

5. **Launch the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Access the API**
   - 🌐 **API Base URL**: `http://localhost:8000`
   - 📖 **Interactive Docs**: `http://localhost:8000/docs`
   - 📋 **ReDoc**: `http://localhost:8000/redoc`

## 📡 API Endpoints

### 🎯 Get Job Recommendations

<details>
<summary><strong>GET</strong> <code>/api/recommendations/{user_id}</code></summary>

**Description**: Retrieves personalized job recommendations for a specific user based on their interaction history.

**Parameters**:
- `user_id` (path): User identifier

**Response Example**:
```json
{
  "user_id": 123,
  "recommendations": [
    {
      "job_id": 456,
      "title": "Senior Python Developer",
      "score": 0.95,
      "match_reasons": ["Python", "Django", "API Development"]
    }
  ],
  "total_count": 10
}
```

**Status Codes**:
- `200`: Success
- `404`: User not found
- `500`: Internal server error

</details>

### 📝 Log User Interaction

<details>
<summary><strong>POST</strong> <code>/api/recommendations/interactions</code></summary>

**Description**: Records user interactions with job postings for improving future recommendations.

**Request Body**:
```json
{
  "user_id": 123,
  "job_id": 456,
  "interaction_type": "click",
  "interaction_value": 5.0,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Interaction Types**:
- `click` - User clicked on job
- `view` - User viewed job details
- `apply` - User applied to job
- `save` - User bookmarked job
- `share` - User shared job

**Response**:
```json
{
  "message": "Interaction logged successfully",
  "interaction_id": 789
}
```

</details>

### 🔄 Update Job Metadata

<details>
<summary><strong>POST</strong> <code>/api/recommendations/job-metadata</code></summary>

**Description**: Updates or creates job metadata including title, description, and required skills.

**Request Body**:
```json
{
  "job_id": 456,
  "title": "Senior Full-Stack Developer",
  "description": "Join our team to build scalable web applications using modern technologies...",
  "skills": ["Python", "React", "PostgreSQL", "Docker"],
  "location": "San Francisco, CA",
  "salary_range": "$120k-$180k",
  "company": "TechCorp Inc."
}
```

**Response**:
```json
{
  "message": "Job metadata updated successfully",
  "job_id": 456,
  "updated_fields": ["title", "description", "skills"]
}
```

</details>

## 🧠 Machine Learning Pipeline

### Data Preprocessing

```bash
# Navigate to scripts directory
cd scripts

# Run preprocessing notebook
jupyter notebook preprocess.ipynb
```

**What it does**:
- Cleans and normalizes job descriptions
- Extracts and standardizes skill requirements
- Handles missing data and outliers
- Prepares data for model training

### Model Training

```bash
# Train the recommendation model
python train_model.py
```

**Model Components**:
- **TF-IDF Vectorizer**: Converts job descriptions to numerical features
- **Cosine Similarity**: Measures similarity between jobs
- **Content-based Filtering**: Recommends jobs similar to user preferences

### Model Artifacts

The system generates and uses these files:
- `models/tfidf_vectorizer.pkl` - Trained TF-IDF model
- `models/cosine_similarity_matrix.pkl` - Precomputed similarity scores
- `data/processed_jobs.csv` - Clean job data for recommendations

## 🏗️ Project Structure

```
job-recommendation-system/
├── 📁 app/
│   ├── 🔧 __init__.py          # Package initialization
│   ├── 🗄️ database.py          # Database configuration and connection
│   ├── 🐍 main.py              # FastAPI application entry point
│   ├── 📊 models.py            # SQLAlchemy database models
│   ├── 🎯 recommendations.py   # Recommendation logic and algorithms
│   └── 🛠️ utils.py             # Utility functions and helpers
├── 📁 data/
│   └── 📦 postings.rar         # Compressed job postings dataset
├── 📁 scripts/
│   ├── 📊 preprocess.ipynb     # Data preprocessing notebook
│   └── 🤖 train_model.py       # Model training script
├── 🚫 .gitignore              # Git ignore rules
├── 📄 LICENSE                  # Project license
├── 📖 README.md               # Project documentation (this file)
└── 📋 requirements.txt         # Python dependencies
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/job_recommendations

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Model Configuration
MODEL_UPDATE_INTERVAL=3600  # seconds
SIMILARITY_THRESHOLD=0.1
```

### Database Schema

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    preferences JSONB
);

-- Jobs table
CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    skills TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Interactions table
CREATE TABLE interactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    job_id INTEGER REFERENCES jobs(id),
    interaction_type VARCHAR(50),
    interaction_value FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 📊 Performance Metrics

The system tracks several key metrics:

- **Response Time**: Average API response time < 200ms
- **Recommendation Accuracy**: Measured using precision@k and recall@k
- **User Engagement**: Click-through rate and conversion metrics
- **System Throughput**: Requests per second capacity

## 🐛 Troubleshooting

### Common Issues

<details>
<summary>Database Connection Issues</summary>

```bash
# Check PostgreSQL status
pg_ctl status

# Verify connection
psql -h localhost -U your_username -d your_database

# Check database configuration in app/database.py
```

</details>

<details>
<summary>Missing Model Files</summary>

```bash
# Retrain models
cd scripts
python train_model.py

# Verify model files exist
ls -la models/
```

</details>

<details>
<summary>Slow API Responses</summary>

- Check database indexes
- Monitor memory usage
- Consider caching frequent queries
- Profile API endpoints for bottlenecks

</details>

## 🚀 Deployment

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/jobdb
  
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: jobdb
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## 📈 Future Enhancements

- [ ] **Collaborative Filtering**: Add user-based recommendations
- [ ] **Deep Learning**: Implement neural collaborative filtering
- [ ] **Real-time Updates**: Add WebSocket support for live recommendations
- [ ] **A/B Testing**: Framework for testing recommendation algorithms
- [ ] **Analytics Dashboard**: Admin panel for monitoring system performance
- [ ] **Multi-language Support**: Internationalization capabilities

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Khalil Zahmoul**

- 📧 Email: [khalil.zahmoul@example.com](mailto:khalil.zahmoul@example.com)
- 💼 LinkedIn: [Khalil Zahmoul](https://linkedin.com/in/khalil-zahmoul)
- 🐱 GitHub: [@khalilzahmoul](https://github.com/khalilzahmoul)

---

<div align="center">
  
**⭐ Star this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/username/job-recommendation-system?style=social)](https://github.com/username/job-recommendation-system)
[![GitHub forks](https://img.shields.io/github/forks/username/job-recommendation-system?style=social)](https://github.com/username/job-recommendation-system)

</div>

---

 

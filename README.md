
 ↓
FastAPI API
 ↓
Docker Container
 ↓
AWS EC2 Server
 ↓
Document Processing Pipeline
```

---

## Features

- Extract text from PDF documents
- Clean and preprocess document data
- Split documents into searchable chunks
- Question-answer retrieval from documents
- REST API using FastAPI
- Docker containerization
- Cloud deployment on AWS
- Automated CI/CD deployment using GitHub Actions
- Document storage using Amazon S3

---

## Project Structure

```
├── Architecture Diagram
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn api.api:app --reload
```

Open Swagger UI:

```
http://localhost:8000/docs
```

---

## Running with Docker

Build and run the container:

```bash
docker-compose up --build
```

API will be available at:

```
http://localhost:8000/docs
```

---

## AWS Deployment

The application was deployed on an **AWS EC2 instance** using Docker.

Deployment steps included:

- Launch EC2 instance
- Install Docker and Docker Compose
- Clone GitHub repository
- Run container using docker-compose
- Expose FastAPI service on port 8000

API endpoint:

```
http://54.163.209.172:8000/docs
```

---

## EC2 Cost Management

To **avoid unnecessary AWS charges**, the EC2 instance has been **stopped after testing**.

The instance can be **started again whenever needed** to demonstrate the live API.

This approach ensures the project shows real cloud deployment while managing infrastructure costs responsibly.

---

## CI/CD Pipeline

Continuous deployment is implemented using **GitHub Actions**.

Workflow:

1. Push code to GitHub
2. GitHub Actions triggers deployment
3. SSH connection to EC2 server
4. Pull latest code
5. Rebuild Docker container
6. Restart API automatically

---

## Amazon S3 Storage

The regulatory document is stored in **Amazon S3**.

The API downloads the document from S3 before processing.

Benefits:

- Scalable cloud storage
- Decoupled data layer
- Suitable for large document storage

---

## Screenshots

The repository includes screenshots demonstrating:

- Project setup
- FastAPI API functionality
- Docker containerization
- EC2 cloud deployment
- GitHub Actions CI/CD
- S3 document storage integration

---

## Author

**Sudharsan B**

B.E. Computer Science Engineering  
Cloud & DevOps Enthusiast

# Automated CI/CD Pipeline using Jenkins, GitHub and Docker

## Project objective
Build, test, containerize and deploy a Flask web application automatically using a Jenkins CI/CD pipeline.

## Architecture
Developer → GitHub → Jenkins → Test → Docker Build → Docker Container → Web App

## Requirements
- Git
- Python 3
- Docker
- Jenkins
- GitHub repository

## Run locally
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
pytest -q
python app.py
```
Open http://localhost:5000

## Run with Docker
```bash
docker build -t devops-demo .
docker run -d --name devops-demo-container -p 5000:5000 devops-demo
```

## Jenkins
Create a Jenkins Pipeline job connected to this GitHub repository and use the included Jenkinsfile.

The pipeline performs:
1. Checkout source code
2. Install dependencies
3. Run automated tests
4. Build Docker image
5. Deploy the latest container

## Demo
1. Run a successful Jenkins build.
2. Open the application.
3. Change `APP_VERSION` display text or application content.
4. Commit and push to GitHub.
5. Trigger Jenkins again.
6. Show the new build number and refreshed application.

## Important Jenkins host note
The Jenkins agent must have Docker installed and permission to execute Docker commands.

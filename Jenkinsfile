pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-demo"
        CONTAINER_NAME = "devops-demo-container"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Install Dependencies") {
            steps {
                sh "python3 -m pip install -r requirements.txt"
            }
        }

        stage("Run Tests") {
            steps {
                sh "python3 -m pytest -q"
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }

        stage("Deploy") {
            steps {
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d --name ${CONTAINER_NAME} -p 5000:5000 -e APP_VERSION=${BUILD_NUMBER} ${IMAGE_NAME}:latest"
            }
        }
    }

    post {
        success {
            echo "CI/CD pipeline completed successfully."
        }
        failure {
            echo "Pipeline failed. Check the stage logs."
        }
    }
}

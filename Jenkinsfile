pipeline {
    agent any

    environment {
        // Set WORKSPACE as an absolute path
        WORKSPACE = pwd()
    }

    stages {
        stage('e2e-tests') {
            agent {
                docker {
                    // Specify the Docker image
                    image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
                    // Additional Docker configurations if needed
                }
            }

            steps {
                script {
                    // Run pip install and pytest within the Docker container
                    echo "Running in workspace: ${WORKSPACE}"
                    bat "docker run -v ${WORKSPACE}:/app -w /app mcr.microsoft.com/playwright/python:v1.40.0-jammy sh -c 'pip install -r requirements.txt && pytest'"
                }
            }
        }
    }
}

pipeline {
    agent any

    environment {
        // Set WORKSPACE as an absolute path
        WORKSPACE = pwd()
    }

    stages {
        stage('e2e-tests') {
            steps {
                script {
                    // Run your Docker command or other steps here
                    echo "Running in workspace: ${WORKSPACE}"
                    docker.image('mcr.microsoft.com/playwright/python:v1.40.0-jammy').inside("-v ${WORKSPACE}:/app -w /app") {
                        sh 'pip install -r requirements.txt'
                        sh 'pytest'
                    }
                }
            }
        }
    }
}

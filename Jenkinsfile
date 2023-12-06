pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
            reuseNode true
        }
    }

    stages {
        stage('e2e-tests') {
            steps {
                script {
                    sh 'cd /app && pip install -r requirements.txt && pytest -v --headed'
                }
            }
        }
    }
}
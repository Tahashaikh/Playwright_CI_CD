pipeline {
    agent any

    environment {
        WORKSPACE = pwd()
    }

    stages {
        stage('e2e-tests') {
            agent {
                docker {
                    image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy'
                    reuseNode true
                }
            }

            steps {
                script {
                    echo "Running in workspace: ${WORKSPACE}"
                    sh 'cd /app && pip install -r requirements.txt && pytest'
                }
            }
        }
    }
}

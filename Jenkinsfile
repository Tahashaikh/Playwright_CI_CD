pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Clone the Git repository
                    checkout scm

                    // Build the Docker image
                    sh 'docker build -t my-playwright-test .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh 'docker run my-playwright-test'
                }
            }
        }
    }
}

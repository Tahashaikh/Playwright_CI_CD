pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        // Clone the Git repository
                        checkout scm

                        // Build the Docker image
                        bat 'docker build -t my-playwright-test .'
                    } catch (Exception buildError) {
                        echo "Error building Docker image: ${buildError.message}"
                        error "Failed to build Docker image"
                    }
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    try {
                        // Run the Docker container in detached mode
                        bat 'docker run -t my-playwright-test .'
                    } catch (Exception runError) {
                        echo "Error running Docker container: ${runError.message}"
                        error "Failed to run Docker container"
                    }
                }
            }
        }
    }

    post {
        failure {
            echo 'One or more stages failed. Sending notification...'
            // Add code to send notifications or take other actions on failure
        }
        success {
            echo 'Pipeline completed successfully.'
            // Add code for successful pipeline completion
        }
    }
}

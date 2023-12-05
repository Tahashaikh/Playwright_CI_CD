#!groovy
pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.40.0-jammy' } }
   environment {
       WORKSPACE = pwd()
   }
   stages {
      stage('e2e-tests') {
         steps {
            dir("${WORKSPACE}") {
               sh 'pip install -r requirements.txt'
               sh 'pytest'
            }
         }
      }
   }
}
pipeline {
    agent any  // This means Jenkins will use any available agent to run the pipeline
    environment {
        PYTHON_ENV = 'python3'  // Define a Python environment variable
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from GitHub
                git branch: 'main', url: 'https://github.com/thouxzzh/pytest_demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Install Python dependencies from requirements.txt
                    sh '''#!/bin/bash
                        ${PYTHON_ENV} -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Run the tests using the batch command on Windows
                bat '''#!/bin/bash
                    . venv/Scripts/activate
                    pytest
                '''
            }
        }
    }
    post {
        always {
            // Clean up workspace after the build is done
            cleanWs()
        }
        success {
            echo 'Build and tests were successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

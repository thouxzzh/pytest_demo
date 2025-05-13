pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                deleteDir() 
                git branch: 'main', url: 'https://github.com/thouxzzh/pytest_demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                echo Installing required packages...
                python -m pip install --upgrade pip
                python -m pip install selenium pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                echo Running tests...
                python -m pytest --maxfail=5 --disable-warnings --junitxml=results.xml
                '''
            }
        }

       stage('Publish Results') {
            steps {
                junit 'results.xml'
                            }
        }
    }
}

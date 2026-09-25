pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                sh 'mkdir -p build'
                sh 'cp app.py build/'
                sh 'cp requirements.txt build/'
            }
        }

    }
}
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                sh '.venv/bin/python -m py_compile app.py test_app.py'
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
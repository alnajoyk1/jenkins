pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo 'Installing Flask dependencies'

                sh 'python3 --version'

                sh 'python3 -m venv .venv'

                sh '.venv/bin/python -m pip install --upgrade pip'

                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Flask application tests'

                sh '.venv/bin/python -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python files'

                sh '.venv/bin/python -m py_compile app.py test_app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                echo 'Installing Flask dependencies'

                sh 'python3 --version'

                sh 'python3 -m pip install --user -r requirements.txt'

                sh 'python3 -m pip install --user pytest'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Flask application tests'

                sh 'python3 -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Python files'

                sh 'python3 -m py_compile app.py test_app.py'
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
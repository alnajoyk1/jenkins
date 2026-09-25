pipeline {
    agent any

    stages {
     stage('Install Dependencies') {
       steps {
          sh 'pip install -r requirments.txt'
        }
     }

      stage('Test') {
        steps {
          sh 'pytest'
        }
      }

      stage('Build') {
        steps {
          sh 'mkdir build'
          sh 'copy app.py build\\'
          sh 'copy requirements.txt build\\'
        }
      }

    }
}
pipeline {
    agent any

    stages {
     stages('Install Dependencies') {
       steps {
          bat 'pip install -r requirments.txt'
        }
     }

      stages('Test') {
        steps {
          bat 'pytest'
        }
      }

      stage('Build') {
        steps {
          bat 'mkdir build'
          bat 'copy app.py build\\'
          bat 'copy requirments.txt build\\'
        }
      }

    }
}
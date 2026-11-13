pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
              echo 'Checking Python application'
              bat 'python -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Unit Tests'
                bat 'python -m unittest app.py'
            }
        }
        stage('Run Application') {
            steps {
                echo 'Running Student Calculator Application'
                bat 'python app.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the errors.'
        }

        always {
            echo 'Jenkins Pipeline execution completed.'
        }
    }
}

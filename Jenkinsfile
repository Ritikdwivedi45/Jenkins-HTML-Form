pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ritikdwivedi45/Jenkins-HTML-Form.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}
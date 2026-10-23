pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'YOUR_GITHUB_REPOSITORY_URL'
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}
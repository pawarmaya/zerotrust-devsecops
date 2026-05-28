pipeline {

    agent any

    environment {
        IMAGE_NAME = "secure-app"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/pawarmaya/zerotrust-devsecops.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    sh 'echo Running SonarQube Analysis'
                }
            }
        }

        stage('Dependency Verification') {
            steps {
                sh 'echo Verifying Dependencies..!!'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t secure-app ./app'
            }
        }

        stage('Trivy Container Scan') {
            steps {
                sh 'trivy image secure-app'
            }
        }

        stage('Deploy Container') {
            steps {
		sh 'docker stop secure-container || true'
		sh 'docker rm secure-conatiner || true'
                sh 'docker run -d --name secure-container -p 5000:5000 secure-app'
            }
        }

    }
}

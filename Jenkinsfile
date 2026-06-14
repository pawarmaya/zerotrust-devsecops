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
        echo 'Running SonarQube Analysis...'
        sh 'sonar-scanner'

        // Demo: Force pipeline failure after Sonar scan
        error('Quality Gate Failed - Blocking Deployment')
    }
}
        stage('Build Docker Image.!!') {
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

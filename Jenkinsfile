pipeline {
    agent any

    environment {
        IMAGE_NAME = 'leducnguyen21/nick-jenkins-project'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/nickldn2211/nick-jenkins-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                    withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-token', 
                    usernameVariable: 'DOCKER_USER', 
                    passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME'
                }
            }
        }
    }
}

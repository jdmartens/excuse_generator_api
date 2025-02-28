pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "excuse_generator_api"
        VERSION = readFile('VERSION').trim()
    }

    stages {
        stage('Verify Docker Access') {
            steps {
                script {
                    sh 'docker ps'
                }
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${VERSION} ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'pytest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh "sed -i.bak 's|${DOCKER_IMAGE}:.*|${DOCKER_IMAGE}:${VERSION}|' k8s-deployment.yaml"
                    sh 'kubectl apply -f k8s-deployment.yaml'
                }
            }
        }

        stage('Port Forward') {
            steps {
                script {
                    sh 'kubectl port-forward service/excuse-generator-service 8000:8000 &'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

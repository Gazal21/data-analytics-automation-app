pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Pull the code from the repository
                git 'https://github.com/your-username/data-analytics-app.git'
                
                // Build the Docker image
                script {
                    dockerImage = docker.build("data-analytics-app")
                }
            }
        }
        stage('Test') {
            steps {
                // Run tests inside the Docker container
                script {
                    docker.image('data-analytics-app').inside {
                        sh 'pytest tests/'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                // Deploy the Docker container (this could be to a local Minikube cluster or a remote Kubernetes cluster)
                script {
                    sh 'kubectl apply -f deployment.yaml'
                }
            }
        }
    }
}


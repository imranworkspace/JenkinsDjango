pipeline {
    agent any

    environment {
        CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
        CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
        VENV = "myenv"
        PYTHON = "C:\\Users\\imran\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"   // <-- adjust if Python path is different
        DOCKER_IMAGE = "imrandocker24/jenkins_django:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/imranworkspace/JenkinsDjango'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                bat "%PYTHON% -m venv %VENV%"
                bat "%VENV%\\Scripts\\python -m pip install --upgrade pip"
                bat "%VENV%\\Scripts\\pip install -r requirements.txt"
            }
        }

        stage('Run Migrations') {
            steps {
                bat "%VENV%\\Scripts\\python manage.py makemigrations"
                bat "%VENV%\\Scripts\\python manage.py migrate"
            }
        }

        stage('Run Tests') {
            steps {
                bat "%VENV%\\Scripts\\python manage.py test myapp.tests.test_views"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                        docker push %DOCKER_IMAGE%
                    """
                }
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker-compose -f docker-compose.yml up -d --force-recreate'
            }
        }

        
    }
}
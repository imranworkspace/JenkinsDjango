pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/imranworkspace/DjRedCleDockerJenkins.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Migrate DB') {
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                python manage.py migrate
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                python manage.py test
                """
            }
        }

        stage('Run Server') {
            steps {
                bat """
                call %VENV%\\Scripts\\activate
                start /B python manage.py runserver 0.0.0.0:8000
                """
            }
        }
    }
}

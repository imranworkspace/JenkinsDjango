pipeline {
    agent any

    environment {
        VENV = "myenv"
        PYTHON = "C:\\Users\\imran\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"   // <-- adjust if Python path is different
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
        // optional 
        post {
            always {
                junit '**/tests/results/*.xml'
            }
        }
        // optional 2
        post {
            failure {
                mail to: 'imranlatur24studymaterial@gmail.com',
                    subject: "Jenkins Build Failed",
                    body: "Check Jenkins for details."
            }
        }
        // optional 3
        post {
            success {
                mail to: 'imranlatur24studymaterial@gmail.com',
                    subject: "Jenkins Build Success: ",
                    body: "Good news! The build succeeded.\nCheck details here "
            }
        }
    }

}
pipeline {
    agent { label 'windows-python-agent' }

    environment {
        // Chemin complet vers Python 3.14.2
        PYTHON = 'C:\\Users\\soumaya\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        // Dossier pour le venv
        PYTHON_ENV = 'venv'
        // Dossier pour les rapports
        REPORTS_DIR = 'reports'
    }

    stages {
        stage('Check Python') {
            steps {
                bat """
                "%PYTHON%" --version
                where python
                """
            }
        }

        stage('Setup Python & Dependencies') {
            steps {
                bat """
                "%PYTHON%" -m venv %PYTHON_ENV%
                call %PYTHON_ENV%\\Scripts\\activate.bat
                pip install --upgrade pip
                pip install selenium pytest pytest-html webdriver-manager
                """
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat """
                call %PYTHON_ENV%\\Scripts\\activate.bat
                mkdir %REPORTS_DIR%
                "%PYTHON%" main_test.py
                """
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports\\**', fingerprint: true
            }
        }
    }

    post {
        always {
            bat """
            if exist %PYTHON_ENV% rmdir /s /q %PYTHON_ENV%
            """
        }
    }
}

pipeline {
agent any 
     environment {
        PYTHON_ENV = 'venv'  // virtual environment folder
    }

  

    stages {
        stage('Setup Python & Dependencies') {
            steps {
                script {
                    // Check if Python is installed
                    bat '''
                    python --version >nul 2>&1
                    if errorlevel 1 (
                        echo Python not found, please install Python3 on this agent!
                        exit /b 1
                    ) else (
                        echo Python already installed
                    )
                    '''

                    // Create virtual environment and install dependencies
                    bat """
                    python -m venv %PYTHON_ENV%
                    call %PYTHON_ENV%\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install selenium pytest pytest-html
                    """
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                script {
                    // Activate venv and run tests
                    bat """
                    call %PYTHON_ENV%\\Scripts\\activate.bat
                    pytest tests/ --html=reports\\report.html --self-contained-html
                    """
                }
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports\\report.html', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Cleaning up virtual environment"
            bat 'rmdir /s /q %PYTHON_ENV%'
        }
    }
}



pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                echo 'Installation des dépendances Python...'
                bat '''
                chcp 65001
                C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install --upgrade pip
                C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Tests + Rapport HTML') {
            steps {
                echo 'Exécution des tests et génération du rapport...'
                bat '''
                chcp 65001
                mkdir reports
                C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pytest ^
                --html=reports/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminée'
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Rapport Tests Selenium'
            ])
        }

        success {
            echo 'Tous les tests ont réussi'
        }

        failure {
            echo 'Certains tests ont échoué'
        }
    }
}

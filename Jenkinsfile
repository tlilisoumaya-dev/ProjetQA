pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo '🔹 Installation des dépendances Python...'
                bat 'C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test Login Echoué') {
            steps {
                echo '🔹 Exécution du test de connexion échouée...'
                bat 'python testConnexion.py'
            }
        }

        stage('Test Produits') {
            steps {
                echo '🔹 Exécution du test des produits...'
                bat 'python SecondTestSelenium.py'
            }
        }
    }

    post {
        always {
            echo '🎉 Pipeline terminée'
        }
        success {
            echo '✅ Tous les tests ont réussi'
        }
        failure {
            echo '❌ Certains tests ont échoué'
        }
    }
}

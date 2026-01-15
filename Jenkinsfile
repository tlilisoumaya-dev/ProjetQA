pipeline {
    agent any

    environment {
        GIT_URL = 'https://github.com/tlilisoumaya-dev/ProjetQA' // Ton repo GitHub
        GIT_BRANCH = 'main' // Branche cible
        GIT_CREDENTIALS_ID = 'github-token' // Credentials Jenkins avec ton PAT GitHub
    }

    stages {

        // 🔹 Étape 1 : Installation des dépendances Python
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

        // 🔹 Étape 2 : Lancement des tests et génération du rapport HTML
        stage('Tests + Rapport HTML') {
            steps {
                echo 'Exécution des tests et génération du rapport...'
                bat '''
                chcp 65001
                C:\\Users\\tlili\\AppData\\Local\\Programs\\Python\\Python314\\python.exe -m pytest tests --html=report/report.html --self-contained-html
                '''
            }
        }

        // 🔹 Étape 3 : Ajouter uniquement le fichier report.html dans Git et push
        stage('Push Report to GitHub') {
            steps {
                echo 'Mise à jour du fichier report/report.html sur GitHub...'
                withCredentials([usernamePassword(credentialsId: "${env.GIT_CREDENTIALS_ID}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    bat """
                    git config user.email "tlilisoumaya255@gmail.com"
                    git config user.name "tlilisoumaya-dev"

                    git add report/report.html
                    git commit -m "Mise à jour du rapport de tests Selenium" || echo "Pas de changements à commit"
                    git push https://${GIT_USER}:${GIT_PASS}@${env.GIT_URL.replace('https://','')} ${GIT_BRANCH}
                    """
                }
            }
        }
    }

    // 🔹 Post-actions : publication du rapport HTML dans Jenkins
    post {
        always {
            echo 'Publication du rapport HTML dans Jenkins...'
            publishHTML([
                reportDir: 'report',          // le dossier existant
                reportFiles: 'report.html',   // fichier à publier
                reportName: 'Rapport Tests Selenium',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
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
pipeline {
    agent any

    environment {
        GIT_URL = 'https://github.com/tlilisoumaya-dev/ProjetQA' // ton repo GitHub
        GIT_BRANCH = 'main' // branche cible
        GIT_CREDENTIALS_ID = 'github-token' // tes identifiants Jenkins pour GitHub (PAT)
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

        // 🔹 Étape 3 : Ajouter le rapport dans Git et push
        stage('Push Report to GitHub') {
            steps {
                echo 'Mise à jour du fichier report/report.html sur GitHub...'
                withCredentials([usernamePassword(credentialsId: "${env.GIT_CREDENTIALS_ID}", usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    bat """
                    git config user.email "tlilisoumaya255@gmail.com"
                    git config user.name "tlilisoumaya-dev"

                    git checkout -B ${env.GIT_BRANCH}   // crée ou force la branche main locale
                    git add report/report.html
                    git commit -m "Mise à jour du rapport de tests Selenium" || echo "Pas de changements à commit"
                    git push https://${GIT_USER}:${GIT_PASS}@${env.GIT_URL.replace('https://','')} ${env.GIT_BRANCH}
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
                reportDir: 'report',
                reportFiles: 'report.html',
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
pipeline{
    agent any

    environment{
        PYTHON = 'C:\\Users\\adity\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        APP_TOKEN = credentials("APP_TOKEN")
    }

    stages{
        stage('Checkout Code'){
            steps{
                checkout scm
            }
        }
        stage('Install dependencies'){
            steps{
                bat "${env.PYTHON} -m pip install -r requirements.txt"

            }

        }
 
    stage('extract data'){
        steps{
            bat "SET TOEKN-${env.APP_TOKEN}"
            bat "${env.PYTHON} extract_data.py" // use "" 

            }

    }
       }

}
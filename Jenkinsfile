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
            bat """
            SET TOEKN=%APP_TOKEN%
            %PYTHON extract_data.py
            """
// if you want to write 2 or more command got for multiline string

            }

    }
       }

}
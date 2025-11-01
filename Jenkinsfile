pipeline{
    agent any

    environment{
        PYTHON = 'C:\\Users\\adity\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages{
        stage('Checkout Code'){
            steps{
                checkout scm
            }
        }
        stage('Install dependencies'){
            steps{
                bat 'pip install -r requirements.txt'

            }

        }
 
    stage('extract data'){
        steps{
            bat "${env.PYTHON} extract_data.py" // use "" 

            }

    }
       }

}
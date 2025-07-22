pipeline{
    agent { docker {image 'python:3.11'}}
    parameters{
        password(name:'AWS_ACCESS_KEY', defaultValue:'',description:'Enter AWS Access Key')
        password(name:'AWS_SECRET_KEY', defaultValue:'',description:'Enter AWS Secret Key')
    }
    stages{
        stage('Activating virtual env'){
            steps{
                sh 'python -m venv .venv'
                sh '. venv/bin/activate'
            }
        }
        stage('Installing Requirements'){
            steps{
                sh 'pip install boto3'
            }
        }
        stage('Running Python File'){
            steps{
                python script.py
            }
        }
    }
}
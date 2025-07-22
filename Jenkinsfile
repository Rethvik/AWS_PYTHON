pipeline{
    agent { docker {image 'python:3.11'}}
    parameters{
        password(name:'AWS_ACCESS_KEY', defaultValue:'',description:'Enter AWS Access Key')
        password(name:'AWS_SECRET_KEY', defaultValue:'',description:'Enter AWS Secret Key')
    }
    stages{
        stage('Activation of Virtual Env'){
            steps{
                sh './venv/Scripts/activate'
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
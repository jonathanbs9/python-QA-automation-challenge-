pipeline{
    agent any
    
    stages{
        stage("First Stage - Check Version"){
            steps{
                echo "========executing First Stage ========"
                sh 'python3.9 --version'
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Second Stage - Get Libraries && Env"){
            steps{
                echo "========executing Second Stage ========"
                //sh 'source challengeEnv\Script\activate'
                sh "source './challengeEnv/Script/activate'"
                sh "pip install -r requirements.txt"
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========Second Stage executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Third Stage - Execute Challenge 2 Stock Exchange Market"){
            steps{
                echo "========executing Third Stage ========"
                sh 'python3.9 challenge2.py'
            }
            post{
                always{
                    echo "======== Always ========"
                }
                success{
                    echo "======== Third Stage executed successfully ========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}

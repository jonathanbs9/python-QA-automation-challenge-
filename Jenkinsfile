pipeline{
    agent any
    
    stages{
        stage("First Stage - Check Version"){
            steps{
                echo "========executing First Stage ========"
                sh 'python --version'
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
        stage("Second Stage - Execute Challenge 2 Stock Exchange Market"){
            steps{
                echo "========executing Second Stage ========"
                sh 'python challenge2.py'
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

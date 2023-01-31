pipeline {
    agent any
    
    parameters {
        string(name: 'EnviromentInfra', defaultValue: 'coe', description: 'Name of LifeTime user that triggered the pipeline remotely.')
    }

    stages {
        stage('Prepare') {
            steps {

                def pipeline = readYaml file: 'pipeline.yaml'                


                def lifetime-baseUrl = pipeline.lifetime."baseUrl-"+$EnviromentInfra
                 

               echo "Pipeline lifetime baseUrl: ${lifetime-baseUrl}" 
            }
        }
        
        stage('Portão HTTP Não Seguro') {
            steps{
                echo('Fim Portão HTTP Não Seguro')
            }
        }
        
        stage('DSV') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        stage('Portão Architecture Dashboard Checkpoint') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        stage('TST') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        
        stage('Deploy HMG') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        stage('Deploy PPRD') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        
        stage('Deploy PRD') {
            steps{
                echo('Fim DSV')
            }    
        }
    }
}

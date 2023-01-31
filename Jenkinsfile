
def loadValuesYaml(){
  def valuesYaml = readYaml (file: 'pipeline.yaml')
  return valuesYaml;
}

pipeline {
    agent any
    
    parameters {
        string(name: 'EnviromentInfra', defaultValue: 'infra', description: 'Name of LifeTime user that triggered the pipeline remotely.')
    }

    stages {
        stage('Prepare') {
            steps {
               script{
                    valuesYaml = loadValuesYaml()
                    println valuesYaml.getClass()
                }
                
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

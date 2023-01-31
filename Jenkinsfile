def valueConfigOutSystems(nodeParent, nodeChild){
  def valuesYaml = readYaml (file: 'pipeline.yml')
  return valuesYaml['outsystems'][nodeParent][nodeChild];
}


pipeline {
    agent any
    
    parameters {
        string(name: 'EnviromentInfra', defaultValue: 'infra', description: 'Name of LifeTime user that triggered the pipeline remotely.')
    }

    stages {
        stage('Prepare') {
            steps {
              def lifetimeBaseUrl = valueConfigOutSystems('lifetime',"baseUrl-${params.EnviromentInfra}")
              echo "Pipeline lifetime baseUrl-${params.EnviromentInfra}: ${lifetimeBaseUrl}" 
            }
        }
        
        stage('Portão HTTP Não Seguro') {
            steps{
               def activationCode = valueConfigOutSystems('activationCode',"${params.EnviromentInfra}")
               echo "Pipeline activationCode baseUrl: ${params.EnviromentInfra}" 
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

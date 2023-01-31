def valueConfigOutSystems(nodeParent, nodeChild){
  def valuesYaml = readYaml (file: 'pipeline.yml')
  return valuesYaml['outsystems'][nodeParent][nodeChild];
}


pipeline {
    agent any
    
    parameters {
        string(name: 'TriggeredBy', defaultValue: 'infra', description: 'Name of LifeTime user that triggered the pipeline remotely.')
    }

    stages {
        stage('Prepare') {
            steps {
                script {

                    def lifetimeBaseUrl = valueConfigOutSystems('lifetime',"baseUrl-${params.TriggeredBy}")
                    echo "Pipeline lifetime baseUrl-${params.TriggeredBy}: ${lifetimeBaseUrl}" 
                }
              
            }
        }
        
        stage('Portão HTTP Não Seguro') {
            steps{
                script {
                    def activationCode = valueConfigOutSystems('activationCode',"${params.TriggeredBy}")
                    echo "Pipeline activationCode: ${activationCode}" 
                }
            }
        }
        
        stage('DSV') {
            steps{
                echo('Fim DSV')
            }    
        }
        
        stage('Portão Architecture Dashboard Checkpoint') {
            steps{
                echo('Fim Portão Architecture Dashboard Checkpoint')
            }    
        }
        
        stage('TST') {
            steps{
                echo('Fim TST')
            }    
        }
        
        
        stage('Deploy HMG') {
            when {
                expression { params.TriggeredBy == 'infra' }
            }
            steps{
                echo('Fim HMG')
            }    
        }
        
        stage('Deploy PPRD') {
            steps{
                echo('Fim PPRD')
            }    
        }
        
        
        stage('Deploy PRD') {
            steps{
                echo('Fim PRD')
            }    
        }
    }

    post {
        always {
            script {
                addInfoBadge(text: "OutSystems Infra: ${params.TriggeredBy}")
            }
        }
    }
}

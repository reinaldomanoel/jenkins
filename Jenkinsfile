def valueConfigOutSystems(nodeParent, nodeChild){
  def valuesYaml = readYaml (file: 'pipeline.yml')
  return valuesYaml['outsystems'][nodeParent][nodeChild];
}


pipeline {
    agent any
    
    // parameters {
    //     string(name: 'TriggeredBy', defaultValue: 'infra', description: 'Name of LifeTime user that triggered the pipeline remotely.')
    // }

    environment {
        FLUXO_OUTSYSTEM = params.TriggeredBy.trim().toLowerCase()
    }

    stages {
        stage('Prepare') {
            steps {
                script {

                    def lifetimeBaseUrl = valueConfigOutSystems('lifetime',"baseUrl-${FLUXO_OUTSYSTEM}")
                    echo "Pipeline lifetime baseUrl-${FLUXO_OUTSYSTEM}: ${lifetimeBaseUrl}" 
                }
              
            }
        }
        
        stage('Portão HTTP Não Seguro') {
            steps{
                script {
                    def activationCode = valueConfigOutSystems('activationCode',"${FLUXO_OUTSYSTEM}")
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
                expression { 
                    return FLUXO_OUTSYSTEM == 'infra' 
                }
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
                def log = "Fluxo OutSystems: ${params.TriggeredBy}"
                manager.addShortText(log, "grey", "white", "0px", "white")
            }

            deleteDir()
        }
    }
}

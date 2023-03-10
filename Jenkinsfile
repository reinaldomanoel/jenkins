def globalConfig
def activationCode
def lifetime


def setEnviromentConfigOutSystems(ambienteDeploy, fluxoOutsystems, globalConfig){
   globalConfig.outsystems.envs."${ambienteDeploy}".baseUrl  = globalConfig.outsystems.envs."${ambienteDeploy}".baseUrl.replaceAll('INFRA',fluxoOutsystems)
}


pipeline {
    agent any
    
    parameters {
        choice(name: 'TriggeredBy', choices: ['Infra', 'CoE', 'Corp'], description: 'Fluxo OutSystems')
    }

    environment {
        FLUXO_OUTSYSTEMS = params.TriggeredBy.trim().toLowerCase()
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    globalConfig = readYaml (file: './pipeline.yml')
                    
                    activationCode = globalConfig.outsystems.activationCode."${FLUXO_OUTSYSTEMS}"
                    lifetime = globalConfig.outsystems.lifetime.baseUrl."${FLUXO_OUTSYSTEMS}"
                    
                    echo "Pipeline lifetime baseUrl-${FLUXO_OUTSYSTEMS}: ${lifetime}" 
                }
              
            }
        }
        
        stage('Portão HTTP Não Seguro') {
            steps{
                script {
                    echo "Pipeline activationCode: ${activationCode}" 
                }
            }
        }
        
        stage('DSV') {
            steps{
                setEnviromentConfigOutSystems('DSV', FLUXO_OUTSYSTEMS, globalConfig)
                echo(globalConfig.outsystems.envs.DSV.baseUrl)
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
                setEnviromentConfigOutSystems('TST', FLUXO_OUTSYSTEMS, globalConfig)
                echo(globalConfig.outsystems.envs.TST.baseUrl)
                echo('Fim TST')
            }    
        }
        
        
        stage('Deploy HMG') {
            when {
                expression { 
                    return FLUXO_OUTSYSTEMS == 'infra' 
                }
            }
            steps{
                setEnviromentConfigOutSystems('HMG', FLUXO_OUTSYSTEMS, globalConfig)
               // echo(globalConfig.outsystems.envs.HMG.baseUrl)
                echo('Fim HMG')
            }    
        }
        
        stage('Deploy PPRD') {
            steps{
                setEnviromentConfigOutSystems('PPRD', FLUXO_OUTSYSTEMS, globalConfig)
                echo(globalConfig.outsystems.envs.PPRD.baseUrl)
                echo('Fim PPRD')
            }    
        }
        
        
        stage('Deploy PRD') {
            steps{
                setEnviromentConfigOutSystems('PRD', FLUXO_OUTSYSTEMS, globalConfig)
                echo(globalConfig.outsystems.envs.PRD.baseUrl)
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

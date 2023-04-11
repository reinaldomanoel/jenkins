// Importa a classe HttpBuilder
import groovyx.net.http.HttpBuilder


pipeline {
    agent any
    
    stages {
        stage('Access API') {
            steps {
                script {
                   


                    // Cria um objeto HttpBuilder
                    def http = new HttpBuilder('https://mockbin.com/bin')

                    // Define os parâmetros de solicitação
                    def response = http.get(
                        path: '/0b3c3a67-df1d-4448-8159-0210a84b7640',
                        contentType: 'application/json'
                    )

                    // Imprime a resposta
                    echo response.toString()
                }
            }
        }
    }
}



// pipeline {
//     agent any
    
//     parameters {
//         choice(name: 'TriggeredBy', choices: ['Infra', 'CoE', 'Corp'], description: 'Fluxo OutSystems')
//     }

//     environment {
//         FLUXO_OUTSYSTEMS = params.TriggeredBy.trim().toLowerCase()
//     }

//     stages {
//         stage('Prepare') {
//             steps {
//                 script {
//                     globalConfig = readYaml (file: './pipeline.yml')
                    
//                     activationCode = globalConfig.outsystems.activationCode."${FLUXO_OUTSYSTEMS}"
//                     lifetime = globalConfig.outsystems.lifetime.baseUrl."${FLUXO_OUTSYSTEMS}"
                    
//                     echo "Pipeline lifetime baseUrl-${FLUXO_OUTSYSTEMS}: ${lifetime}" 
//                 }
              
//             }
//         }
        
//         stage('Portão HTTP Não Seguro') {
//             steps{
//                 script {
//                     echo "Pipeline activationCode: ${activationCode}" 
//                 }
//             }
//         }
        
//         stage('DSV') {
//             steps{
//                 setEnviromentConfigOutSystems('DSV', FLUXO_OUTSYSTEMS, globalConfig)
//                 echo(globalConfig.outsystems.envs.DSV.baseUrl)
//                 echo('Fim DSV')
//             }    
//         }
        
//         stage('Portão Architecture Dashboard Checkpoint') {
//             steps{
//                 echo('Fim Portão Architecture Dashboard Checkpoint')
//             }    
//         }
        
//         stage('TST') {
//             steps{
//                 setEnviromentConfigOutSystems('TST', FLUXO_OUTSYSTEMS, globalConfig)
//                 echo(globalConfig.outsystems.envs.TST.baseUrl)
//                 echo('Fim TST')
//             }    
//         }
        
        
//         stage('Deploy HMG') {
//             when {
//                 expression { 
//                     return FLUXO_OUTSYSTEMS == 'infra' 
//                 }
//             }
//             steps{
//                 setEnviromentConfigOutSystems('HMG', FLUXO_OUTSYSTEMS, globalConfig)
//                // echo(globalConfig.outsystems.envs.HMG.baseUrl)
//                 echo('Fim HMG')
//             }    
//         }
        
//         stage('Deploy PPRD') {
//             steps{
//                 setEnviromentConfigOutSystems('PPRD', FLUXO_OUTSYSTEMS, globalConfig)
//                 echo(globalConfig.outsystems.envs.PPRD.baseUrl)
//                 echo('Fim PPRD')
//             }    
//         }
        
        
//         stage('Deploy PRD') {
//             steps{
//                 setEnviromentConfigOutSystems('PRD', FLUXO_OUTSYSTEMS, globalConfig)
//                 echo(globalConfig.outsystems.envs.PRD.baseUrl)
//                 echo('Fim PRD')
//             }    
//         }
//     }

//     post {
//         always {
//             script {
//                 def log = "Fluxo OutSystems: ${params.TriggeredBy}"
//                 manager.addShortText(log, "grey", "white", "0px", "white")
//             }

//             deleteDir()
//         }
//     }
// }

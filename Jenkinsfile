def getPasswordFromConan(senha){

    def req = new URL("https://mockbin.com/bin/0b3c3a67-df1d-4448-8159-0210a84b7640").openConnection();
    def content = req.getInputStream().getText()

    // Imprime a resposta da API
    return content
}

pipeline {
  agent any

  stages {
    stage('Access API') {
      steps {
        script {
           def pwsAirGap = getPasswordFromConan("SENHA_OSPTOOL_API_COE_1Y7R")

           print pwsAirGap

            try {
                withEnv(['VAR_NAME=${pwsAirGap}']) {
                    sh """

                    python3 ./common/deploy_apps_to_target_env_with_airgap.py --airgap_pass "${pwsAirGap}"

                    """
                }
                
            } catch (Exception e) {
                throw e
            }

        }
      }
    }
  }
}
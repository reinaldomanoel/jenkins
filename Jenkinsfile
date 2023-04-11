pipeline {
  agent any

  stages {
    stage('Access API') {
      steps {
        script {
          
          // Cria um objeto HTTPBuilder
          def response  = httpRequest 'https://mockbin.com/bin/0b3c3a67-df1d-4448-8159-0210a84b7640'

          // Imprime a resposta da API
          println response.statusLine
          println response.headers
          println response.data
        }
      }
    }
  }
}
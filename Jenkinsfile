pipeline {
  agent any
  stages {
    stage('List pods') {
      withKubeConfig([credentialsId: '7ac4b35d-364f-434e-83f2-9ff976e23047',
                    caCertificate: '',
                    serverUrl: 'https://kubernetes.default:443',
                    contextName: 'dev'
                    ]) {
      sh 'kubectl get pods'
      }
    }  
  }
}
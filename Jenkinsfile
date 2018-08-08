pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh 'echo "Hello"'
        withKubeConfig(contextName: 'dev', credentialsId: '7ac4b35d-364f-434e-83f2-9ff976e23047', serverUrl: 'https://kubernetes.default:443') {
          sh 'kubectl get pods'
        }

      }
    }
  }
}
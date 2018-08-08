pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh 'echo "Hello"'
        withKubeConfig(contextName: 'dev', credentialsId: 'kubeconfig.txt', serverUrl: 'https://kubernetes.default:443') {
          sh 'kubectl get pods'
        }

      }
    }
  }
}
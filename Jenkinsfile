pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh 'echo "Hello"'
        withKubeConfig(contextName: 'c2.fra.k8scluster.de', credentialsId: '24d2e3c8-8b53-4333-99d4-62181446e589', serverUrl: 'https://kubernetes.default:443') {
          sh '''kubectl version
kubectl run nginx --image=nginx
kubectl get pods'''
        }

      }
    }
  }
}
pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh '''curl -O https://storage.googleapis.com/kubernetes-release/release/v1.9.10/bin/linux/amd64/kubectl
chmod +x kubectl

env
cp kubectl /usr/local/bin/
./kubectl version'''
        sh 'ls -al'
        withKubeConfig(contextName: 'dev', credentialsId: '7ac4b35d-364f-434e-83f2-9ff976e23047', serverUrl: 'https://kubernetes.default:443') {
          sh './kubectl get pods'
        }

      }
    }
  }
}
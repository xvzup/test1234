pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh '''curl -O https://storage.googleapis.com/kubernetes-release/release/v1.9.10/bin/linux/amd64/kubectl
chmod +x kubectl
./kubectl version'''
      }
    }
  }
}
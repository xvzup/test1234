pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."

ls -al
echo "---------------------"
find / -name kubectl
echo "---------------------"
kubectl get nodes'''
      }
    }
  }
}
pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."

kubectl version
kubectl run nginx --image=nginx
'''
      }
    }
  }
}
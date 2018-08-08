pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."

ls -al
echo "---------------------"
cat /etc/os-release
echo "---------------------"
env
echo "---------------------"
set
'''
      }
    }
  }
}
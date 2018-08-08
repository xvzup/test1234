pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."'''
      }
    }
    stage('deploy') {
      steps {
        kubernetesDeploy(configs: 'test_deploy.yaml', kubeconfigId: '2a296293-c563-4b0d-92a0-786d79258de5')
      }
    }
  }
}
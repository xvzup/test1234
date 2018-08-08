pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."

kubectl create cm appcode --from-file=hello_world.py -o yaml --dry-run > test1234_cm.yaml'''
      }
    }
    stage('deploy') {
      steps {
        kubernetesDeploy(configs: 'test_deploy.yaml,test1234_cm.yaml', enableConfigSubstitution: true, kubeconfigId: '2a296293-c563-4b0d-92a0-786d79258de5')
      }
    }
  }
}
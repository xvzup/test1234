pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Creating configmap ..."

#kubectl create cm appcode --from-file=hello_world.py -o yaml --dry-run > test1234_cm.yaml

ls -al'''
      }
    }
    stage('deploy') {
      steps {
        kubernetesDeploy(configs: 'test_deploy.yaml', enableConfigSubstitution: true, kubeconfigId: '7ac4b35d-364f-434e-83f2-9ff976e23047')
      }
    }
  }
}
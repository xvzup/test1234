pipeline {
  agent any
  stages {
    stage('deploy') {
      parallel {
        stage('deploy') {
          steps {
            kubernetesDeploy(kubeconfigId: '2a296293-c563-4b0d-92a0-786d79258de5', configs: 'test_deploy.yaml')
            sh '''#!/bin/bash

echo "Creating configmap ..."'''
          }
        }
        stage('Create_configmap') {
          steps {
            sh '''#!/bin/bash

echo "Creating configmap"'''
          }
        }
      }
    }
  }
}
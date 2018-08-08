pipeline {
  agent any
  stages {
    stage('stage1') {
      withKubeConfig([credentialsId: '7ac4b35d-364f-434e-83f2-9ff976e23047',
                    caCertificate: '',
                    serverUrl: 'https://kubernetes.default:443',
                    contextName: 'dev'
                    ]) {
      steps {
        sh '''#!/bin/bash

echo "Step 1"'''
        sh '''#!/bin/bash

echo "Step 2"'''
      }
    }
    }
  }
}

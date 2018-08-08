pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Downloading kubectl ..."
curl -O https://storage.googleapis.com/kubernetes-release/release/v1.9.10/bin/linux/amd64/kubectl 
chmod +x kubectl

echo "Creating configmap ..."
./kubectl version
./kubectl create cm test1234 --from-file=hello_world.py -o yaml --dry-run > test1234_cm.yaml
'''
      }
    }
    stage('List pods') {
      withKubeConfig([credentialsId: '7ac4b35d-364f-434e-83f2-9ff976e23047',
                    caCertificate: '',
                    serverUrl: 'https://kubernetes.default:443',
                    contextName: 'dev'
                    ]) {
      sh 'kubectl get pods'
      }
    }  
  }
}
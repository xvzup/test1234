pipeline {
  agent any
  stages {
    stage('create_configmap') {
      steps {
        sh '''#/bin/bash

echo "Download kubectl ..."
curl -O https://storage.googleapis.com/kubernetes-release/release/v1.9.10/bin/linux/amd64/kubectl 
chmod +x kubectl
id

echo "Creating configmap ..."
./kubectl version
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
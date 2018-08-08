pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        kubernetesDeploy(configs: 'test_deploy.yaml', enableConfigSubstitution: true, kubeconfigId: '7ac4b35d-364f-434e-83f2-9ff976e23047')
      }
    }
  }
}
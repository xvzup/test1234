pipeline {
  agent any
  stages {
    stage('deploy') {
      steps {
        kubernetesDeploy(secretName: 'admin-user-token-r27kv', secretNamespace: 'kube-system', kubeconfigId: '2a296293-c563-4b0d-92a0-786d79258de5')
      }
    }
  }
}
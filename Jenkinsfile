pipeline {
  agent any
  stages {
    stage('deploy') {
      steps {
        kubernetesDeploy(secretName: 'admin-user-token-r27kv', secretNamespace: 'kube-system', kubeconfigId: 'k8s-2')
      }
    }
  }
}
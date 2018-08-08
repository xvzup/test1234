pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
        sh 'echo "Hello"'
        withKubeConfig(contextName: 'c2.fra.k8scluster.de', credentialsId: '24d2e3c8-8b53-4333-99d4-62181446e589', serverUrl: 'https://kubernetes.default:443') {
          sh '''kubectl create cm test1234 --dry-run --from-file=hello_world.py -o yaml > test1234_cm.yaml
ls -al
kubectl apply -f test_deploy.yaml
kubectl apply -f test1234_cm.yaml
echo "----------------"
kubectl get pods 
kubectl get cm'''
        }

      }
    }
  }
}
pipeline {
  agent any
  stages {
    stage('deploy_k8s') {
      steps {
        withKubeConfig(contextName: 'c2.fra.k8scluster.de', credentialsId: '24d2e3c8-8b53-4333-99d4-62181446e589') {
          sh '''kubectl create cm test1234 --dry-run --from-file=hello_world.py -o yaml > test1234_cm.yaml
kubectl apply -f test1234_cm.yaml

if [ `kubectl get job | grep helloworld | wc -l ` -gt 0 ]; then
  kubectl delete job helloworld
  sleep 10
fi 
kubectl apply -f test1234_job.yaml'''
        }

      }
    }
  }
}
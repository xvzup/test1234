apiVersion: batch/v1
kind: Job
metadata:
  name: helloworld
spec:
  template:
    metadata:
      name: helloworld
    spec:
      containers:
      - name: app
        image: python
        volumeMounts:
          - name: pythoncode
            mountpath: /application
        command: [ "sh", "-c", "/application/hello_world.py" ]
      restartPolicy: Never
      volumes:
      - name: pythoncode
        configMap:
          name: test1234
          items:
            - key: hello_world.py
     
docker build -f Dockerfile -t hello-python:latest docker

docker run -p 6050:6050 hello-python

docker run --rm -p 5001:6050 hello-python

kubectl apply -f deployment.yaml


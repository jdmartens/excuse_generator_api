# Variables
IMAGE_NAME=excuse_generator_api
DEPLOYMENT_FILE=k8s-deployment.yaml

# Default target
all: build deploy fwd

# Set Minikube Docker environment
minikube-env:
	eval $$(minikube docker-env)

# Build Docker image
build: minikube-env
	docker build -t $(IMAGE_NAME):latest .

# Apply Kubernetes deployment
deploy:
	kubectl apply -f $(DEPLOYMENT_FILE)
fwd:
	kubectl port-forward service/excuse-generator-service 8000:8000

# Get status of pods
status:
	kubectl get pods

# Get logs of the first pod
logs:
	kubectl logs $$(kubectl get pods -o jsonpath='{.items[0].metadata.name}')

.PHONY: all minikube-env build deploy status logs

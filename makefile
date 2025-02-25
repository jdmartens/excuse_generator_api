# Variables
IMAGE_NAME=excuse_generator_api
DEPLOYMENT_FILE=k8s-deployment.yaml
VERSION_FILE=VERSION

# Default target
all: build deploy fwd

# Set Minikube Docker environment
minikube-env:
	eval $$(minikube docker-env)

# Build Docker image with specified version
build: minikube-env
	@$(MAKE) build-version VERSION=$(VERSION)

build-version: minikube-env
	@echo $(VERSION) > $(VERSION_FILE)
	@sed -i.bak 's|$(IMAGE_NAME):.*|$(IMAGE_NAME):$(VERSION)|' $(DEPLOYMENT_FILE)
	docker build -t $(IMAGE_NAME):$(VERSION) .

# Apply Kubernetes deployment
deploy:
	kubectl apply -f $(DEPLOYMENT_FILE)

undeploy:
	kubectl delete -f $(DEPLOYMENT_FILE)

# Port-forward the backend service
fwd:
	kubectl port-forward service/excuse-generator-service 8000:8000 &

# Get status of pods
status:
	kubectl get pods

# Get logs of the first pod
logs:
	kubectl logs $$(kubectl get pods -o jsonpath='{.items[0].metadata.name}')

.PHONY: all minikube-env build build-version deploy fwd status logs

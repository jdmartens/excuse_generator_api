# excuse_generator_api

A FastAPI-based application that generates creative excuses for various scenarios using OpenAI's GPT-4 model.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setting Up Secrets](#setting-up-secrets)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [License](#license)

## Introduction

`excuse_generator_api` is a FastAPI application that generates creative excuses for various scenarios using OpenAI's GPT-4 model. It provides several endpoints to generate excuses for work, being late, not helping someone, missing events, and more.

## Features

- Generate excuses for various scenarios
- Customizable prompts for generating excuses
- Easy deployment to Kubernetes
- Comprehensive test suite

## Prerequisites

- Python 3.11
- Docker
- Kubernetes (Minikube recommended for local development)
- OpenAI API key

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/excuse_generator_api.git
   cd excuse_generator_api
   ```

2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```


## Setting Up Secrets

1. Copy `secrets.example.yaml` to `secrets.yaml`.
2. Replace `<base64-encoded-openai-api-key>` with the actual base64-encoded value.
example
```sh
echo -n 'your-openai-api-key' | base64
```
3. Apply the secrets to your Kubernetes cluster:
```sh
kubectl apply -f secrets.yaml
```

## Running the Application

1. Ensure Minikube is running and configured to use the local Docker daemon:
```sh
kubectl apply -f secrets.yaml
```

2. Build the Docker Image:
```sh
minikube start
eval $(minikube docker-env)
```

3. Deploy the application to Kubernetes:
```sh
docker build -t excuse_generator_api:1.0.0 .
```

4. Port-forward the service to Kubernetes:
```sh
kubectl port-forward service/excuse-generator-service 8000:8000
```

5. Access the application at http://localhost:8000.


## Running Tests

1. Ensure the virtual environment is activated:
```sh
source venv/bin/activate
```

2. Run the tests using pytest:
```sh
pytest
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
# excuse_generator_api



## Setting Up Secrets

1. Copy `secrets.example.yaml` to `secrets.yaml`.
2. Replace `<base64-encoded-openai-api-key>` and `<base64-encoded-debug-mode>` with the actual base64-encoded values.
example
```sh
echo -n 'your-openai-api-key' | base64
```
3. Apply the secrets to your Kubernetes cluster:
```sh
kubectl apply -f secrets.yaml
```
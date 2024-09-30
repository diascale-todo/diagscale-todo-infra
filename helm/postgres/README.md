# Installation
```bash
helm install postgres -n diagscale-todo oci://registry-1.docker.io/bitnamicharts/postgresql -f values.yaml
```

# Usage
Getting the password:

```bash
export POSTGRES_PASSWORD=$(kubectl get secret --namespace diagscale-todo postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)
```

Getting the service IP:

```bash
export SERVICE_IP=$(kubectl get svc --namespace diagscale-todo postgresql --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
```

## Internal cluster testing
To connect to your database run the following command:

```bash
kubectl run postgresql-client --rm --tty -i --restart='Never' --namespace diagscale-todo --image docker.io/bitnami/postgresql:16.4.0-debian-12-r13 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
  --command -- psql --host postgresql -U postgres -d postgres -p 5432
```

## External connection
```bash
# Install postgres client
sudo apt-get install postgresql-client # Or equivalent or the appropriate client in given programming language
PGPASSWORD=$POSTGRES_PASSWORD psql --host $SERVICE_IP --port 5432 -U postgres -d postgres
```
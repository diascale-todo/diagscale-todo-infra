# Diagscale TODO API Helm chart
## Prerequisites
- Kubernetes cluster
- Helm installed
- PostgreSQL database (with a `Secret` for the password created in Kubernetes or specify secret at installation time)

## Installation
```bash
helm install diagscale-todo-api ./diagscale-todo-api
```

This will deploy the API backend with the default values specified in the `values.yaml` file.

### Configuration

You can override default configurations when installing the chart by passing custom values via the `--set` flag or a custom `values.yaml` file.

For example, to set a custom image tag:

```bash
helm install my-api-backend ./my-api-backend-chart \
  --set image.tag=v1.2.3
```

Alternatively, you can modify the `values.yaml` file directly to customize the settings for the deployment, such as the replica count, service type, and resource limits.


## Uninstalling the Chart

To uninstall the chart and remove all related resources:

```bash
helm uninstall my-api-backend
```

This command will delete all Kubernetes resources associated with this release, including the Deployment and Service.


## Customizing

The following parameters can be customized in the `values.yaml` file:

| Parameter                  | Description                                                       | Default                                 |
|----------------------------|-------------------------------------------------------------------|-----------------------------------------|
| `replicaCount`              | Number of API backend pod replicas                                 | `2`                                     |
| `image.repository`          | API backend image repository                                       | `<to-be-decided>`                       |
| `image.tag`                 | Image tag                                                         | `latest`                                |
| `image.pullPolicy`          | Image pull policy                                                  | `IfNotPresent`                          |
| `service.type`              | Kubernetes service type                                            | `ClusterIP`                             |
| `service.port`              | API backend port                                                   | `8080`                                  |
| `postgres.secretName`       | Name of the existing secret for PostgreSQL credentials (optional)   | `""` (empty, meaning a new secret is created) |
| `postgres.host`             | PostgreSQL service host                                            | `postgresql.default.svc.cluster.local`  |
| `postgres.port`             | PostgreSQL service port                                            | `5432`                                  |
| `postgres.database`         | PostgreSQL database name                                           | `postgres`                              |
| `postgres.user`             | PostgreSQL user                                                    | `postgres`                              |
| `postgres.password`         | PostgreSQL password (only used if no existing secret is specified)  | `""` (set during Helm installation)     |
| `ingress.enabled`           | Enable/disable Ingress                                             | `false`                                 |
| `ingress.hosts`             | Hostnames for Ingress                                              | `[]`                                    |
| `resources`                 | Resource requests and limits for the API backend pods              | `{}`                                    |
| `nodeSelector`              | Node selector for pod scheduling                                   | `{}`                                    |
| `tolerations`               | Tolerations for pod scheduling                                     | `[]`                                    |
| `affinity`                  | Pod affinity rules for scheduling                                  | `{}`                                    |

---

### Notes:
- If `postgres.secretName` is empty (`""`), a new secret is created for the PostgreSQL password during the chart installation.
- The `postgres.password` value will only be used if a `secretName` is not provided. You can set the password during installation using Helm's `--set` flag.
- The `resources` section allows for setting CPU and memory limits for your pods, which can be customized based on your deployment needs.

---

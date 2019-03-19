# Nucleus Config

## Kubernetes YAML

- Cluster: [frankfurt](frankfurt/)
  - Namespace: [nucleus-dev](frankfurt/nucleus-dev/)
    - [Deployment](frankfurt/nucleus-dev/deploy.yaml)
      - derived from Deis Workflow managed Deployment
    - [Service](frankfurt/nucleus-dev/svc.yaml)
      - derived from Deis Workflow managed Service
- Cluster: [iowa-b](iowa-b/)
  - [Namespace](iowa-b/nucleus-dev/nucleus-dev-ns.yaml): [nucleus-dev](iowa-b/nucleus-dev/)
    - [Argo Tunnel](iowa-b/nucleus-dev/argo-tunnel.yaml)
      - may want to move this to its own namespace in a future revision
    - [Deployment](iowa-b/nucleus-dev/deploy.yaml)
      - depends on secrets that are stored encrypted via [sops](https://github.com/mozilla/sops) in a private repo
    - [Ingress](iowa-b/nucleus-dev/ingress.yaml)
      - depends on Argo Tunnel created above and Service below
    - [Service](iowa-b/nucleus-dev/svc.yaml)
      - internal service, no public load balancer needed

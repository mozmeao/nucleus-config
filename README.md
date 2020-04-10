# Nucleus Config

## Kubernetes YAML

- Cluster: [frankfurt](frankfurt/) in [AWS eu-central-1a](https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1)
  - [nucleus-dev](frankfurt/nucleus-dev/)
    - [Namespace](frankfurt/nucleus-dev/ns.yaml)
    - [Deployment](frankfurt/nucleus-dev/web-deploy.yaml)
    - [Worker Deployment](frankfurt/nucleus-dev/worker-deploy.yaml)
  - [nucleus-stage](frankfurt/nucleus-stage/)
    - [Namespace](frankfurt/nucleus-stage/ns.yaml)
    - [Deployment](frankfurt/nucleus-stage/deploy.yaml)
  - [nucleus-prod](frankfurt/nucleus-prod/)
    - [Namespace](frankfurt/nucleus-prod/ns.yaml)
    - [Deployment](frankfurt/nucleus-prod/deploy.yaml)

- CI/CD: [.gitlab-ci.yml](.gitlab-ci.yml)
  - Git branch to [job](https://gitlab.com/mozmeao/nucleus-config/-/jobs) mapping:
    - [master](https://github.com/mozmeao/nucleus-config/tree/master)
      - frankfurt dev
      - frankfurt stage
      - frankfurt prod
    - [frankfurt](https://github.com/mozmeao/nucleus-config/tree/frankfurt)
      - frankfurt dev
      - frankfurt stage
      - frankfurt prod
    - [stage](https://github.com/mozmeao/nucleus-config/tree/stage)
      - frankfurt stage
    - [prod](https://github.com/mozmeao/nucleus-config/tree/prod)
      - frankfurt prod
    - [frankfurt-prod](https://github.com/mozmeao/nucleus-config/tree/frankfurt-prod)
      - frankfurt prod

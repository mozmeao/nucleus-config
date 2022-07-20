#!/bin/bash

helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

HELMOPTIONS=$(cat << EOM
  --namespace $NS \
  --version 3.37.0 \
  -f $DEPLOYMENT/helm_configs/ingress.yml \
  nucleus-prod-ingress ingress-nginx/ingress-nginx
EOM
)

echo "Options are:"
echo "$HELMOPTIONS"

# shellcheck disable=SC2086
helm upgrade --install $HELMOPTIONS

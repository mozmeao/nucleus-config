#!/bin/bash


helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update

envsubst < helm_configs/ingress_template.yml > helm_configs/ingress.yml


HELMOPTIONS=$(cat << EOM
  --namespace $NS \
  -f helm_configs/ingress.yml \
  mozmeao-ingress ingress-nginx/ingress-nginx
EOM
)

echo "Options are:"
echo "$HELMOPTIONS"

# shellcheck disable=SC2086
helm upgrade --install $HELMOPTIONS

rm helm_configs/ingress.yml

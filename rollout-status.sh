#!/bin/bash -ex

for DEPLOY in $1/*-deploy.yaml; do
    kubectl rollout status -f ${DEPLOY} -w --timeout=10m
done

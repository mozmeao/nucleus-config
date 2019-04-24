#!/usr/bin/env python3
import os
import yaml
from subprocess import check_output, CalledProcessError, STDOUT
from time import sleep


def kubectl(*args):
    cmd = [os.environ.get('KUBECTL', 'kubectl')]
    cmd.extend(args)
    print(' '.join(cmd))
    print(check_output(cmd, stderr=STDOUT).decode('utf-8'))


def load_yaml(directory):
    loaded = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            try:
                with open(os.path.join(root, filename)) as f:
                    loaded.append(yaml.safe_load(f))
            except Exception as e:
                'TODO: log exceptions we might care about'
    return loaded


def check_unfinished_deployments(deployments):
    unfinished = []
    for d in deployments:
        if d['kind'] == 'Deployment':
            try:
                kubectl('rollout', 'status', '-n', d['metadata']['namespace'],
                        'deploy',  d['metadata']['name'])
                # exit code 1 if status is not complete
            except CalledProcessError as e:
                print(e)
                unfinished.append(d)
    return unfinished


def main():
    cluster = os.environ.get('CLUSTER', 'iowa-b')
    kubectl('apply', '-f', cluster)
    unfinished = check_unfinished_deployments(load_yaml(cluster))
    while unfinished:
        sleep(5)
        unfinished = check_unfinished_deployments(unfinished)
        #TODO: add timeout
        # can use -w --timeout=10m in kubectl version 1.12+



if __name__ == '__main__':
    main()

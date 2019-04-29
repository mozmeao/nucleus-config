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
            if filename.endswith('.yaml') or filename.endswith('.yml'):
                with open(os.path.join(root, filename)) as f:
                    loaded.append(yaml.safe_load(f))
    return loaded


def watch_rollout_status(deployment):
    # timeout requires kubectl v1.12+
    # values need to include unit abbrev, e.g. '10m', '600s'
    timeout = os.environ.get('ROLLOUT_TIMEOUT')
    if timeout:
        kubectl('rollout', 'status', '-n', d['metadata']['namespace'],
                'deploy',  d['metadata']['name'], '-w', '--timeout', timeout)
    else:
        kubectl('rollout', 'status', '-n', d['metadata']['namespace'],
                'deploy',  d['metadata']['name'], '-w')


def main():
    cluster = os.environ.get('CLUSTER', 'iowa-b')
    kubectl('apply', '-f', cluster)
    for o in load_yaml(cluster):
        if o['kind'] == 'Deployment':
            watch_rollout_status(o)


if __name__ == '__main__':
    main()

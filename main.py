#!/usr/bin/python3

import core
import yaml
import importlib
import argparse

from plugin import RandomInputFaker, FibonacciInputFaker, VoidInput

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('cfgFile', metavar='N', type=str, nargs='?',
        help='config file name')
    args = parser.parse_args()

    # read config from "console" (file | RPC)
    with open("config/%s.yaml" % args.cfgFile, 'r') as stream:
        CONFIG = yaml.safe_load(stream)

    if CONFIG['input'] == 'fibonacci':
        input_process = FibonacciInputFaker()
    elif CONFIG['input'] == 'random':
        input_process = RandomInputFaker()
    else:
        input_process = VoidInput()

    pluggable_processes = CONFIG['pipeline']

    external_modules = []
    for j in pluggable_processes:
         external_modules.append(importlib.import_module(j))

    # Run with plugins, internal and dynamically loaded ones
    app = core.RadicosApplication(plugins=
        [
            input_process
        ] + [m.ExternalProcess() for m in external_modules]
    )

    app.run()

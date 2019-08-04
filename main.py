#!/usr/bin/python3

import src.core as core
from src.yaml.parser import PipelineConfig
import importlib
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('cfgFile', metavar='N', type=str, nargs='?',
        help='config file name')
    args = parser.parse_args()

    PipelineConfig.read_config(args.cfgFile)
    input_process = PipelineConfig.get_input_process()
    pluggable_processes = PipelineConfig.get_pluggable_processes()

    external_modules = []
    for j in pluggable_processes:
         external_modules.append(importlib.import_module('src.' + j))

    # Run with plugins, internal and dynamically loaded ones
    app = core.RadicosApplication(plugins=
        [
            input_process
        ] + [m.ExternalProcess() for m in external_modules]
    )

    app.run()

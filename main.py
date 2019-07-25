#!/usr/bin/python3

import core
import importlib
from plugin import SimpleProcess, AlternativeProcess

if __name__ == "__main__":

    # read config from "console" (file | RPC)
    external_processes = ['input.csv', 'output.http']
    
    external_modules = []
    for j in external_processes:
         external_modules.append(importlib.import_module(j))

    # Run with plugins, internal and dynamically loaded ones
    app = core.RadicosApplication(plugins=[
            SimpleProcess(),
            AlternativeProcess(),
        ] + [m.ExternalProcess() for m in external_modules]
    )

    app.run()

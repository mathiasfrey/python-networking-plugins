class InitialProcess(object):
    """Internal business logic"""
    def process(self, data):
        print("Initial processing")
        return 1 + 34

class RadicosApplication(object):
    """First attempt at a plugin system"""
    def __init__(self, *, plugins: list=list()):
        self.internal_modules = [InitialProcess()]
        self._plugins = plugins

    def run(self):
        print("Starting program")
        print("-" * 79)

        modules_to_execute = self.internal_modules + self._plugins
        data = None
        for module in modules_to_execute:
            data = module.process(data)

        print("-" * 79)
        print("Program done")
        print(data)
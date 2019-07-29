class InitialProcess(object):
    """Internal business logic"""
    def process(self, data):
        print("Initial Setup, e.g. connecting serial inputs")
        
        return None

class RadicosApplication(object):
    """First attempt at a plugin system"""
    def __init__(self, *, plugins: list=list()):
        self.internal_modules = [InitialProcess()]
        self._plugins = plugins

    def run(self):
        print("Starting program")
        print("-" * 79)

        modules_to_execute = self.internal_modules + self._plugins
        
        # The main loop of the program
        # Some people just want to see CPUs burn!
        data = None

        for module in modules_to_execute:
            data = module.process(data)

        print("-" * 79)
        print("Program done")
        print('Result:',)

        for x in data:
            print(x)
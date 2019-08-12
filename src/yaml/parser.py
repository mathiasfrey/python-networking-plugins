#!/usr/bin/env python

import yaml

class InputNotProvided(Exception):
    def __init__(self):
        Exception.__init__(self, 'Provide an input channel - at least "input: void"')

class PipelineConfig(object):

    #extra_config = {}

    @classmethod
    def read_config(cls, file_name):

        # TODO: read config from "console" (file | RPC)
        with open("config/%s.yaml" % file_name, 'r') as stream:
            CONFIG = yaml.safe_load(stream)

            if CONFIG['input'] == 'fibonacci':
                from src.input.simulators import FibonacciInputFaker
                cls.input_process = FibonacciInputFaker()
            elif CONFIG['input']['module'] == 'random':
                from src.input.simulators import RandomInputFaker
                cls.input_process = RandomInputFaker(**CONFIG['input'])
            elif CONFIG['input']['module'] == 'void':
                from src.input.simulators import VoidInput
                cls.input_process = VoidInput()
            elif CONFIG['input']['module'] == 'range':
                from src.input.simulators import RangeInputFaker
                cls.input_process = RangeInputFaker(**CONFIG['input'])

            else:
                raise InputNotProvided

            cls.pluggable_processes = CONFIG['pipeline']
    
    @classmethod
    def get_input_process(cls):
        return cls.input_process
    
    @classmethod
    def get_pluggable_processes(cls):
        return cls.pluggable_processes
    
    #def get_extra_config(cls):
    #    return cls.get_extra_config
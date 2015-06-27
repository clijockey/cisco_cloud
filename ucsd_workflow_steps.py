#! /usr/bin/env python

'''
    Command Line Utility to return the steps in a workflow in UCS Director
'''


import requests
import json
from ucsd_library import workflow_steps

if __name__ == '__main__':

    import sys
    from pprint import pprint
    from argparse import ArgumentParser, FileType

    p = ArgumentParser()
    p.add_argument('-n', '--number',                          # Name stored in namespace
                   metavar = 'The Service request number',            # Arguement name displayed to user
                   help = 'What Service Request number do you what to get the steps for',
                   default=""
                    )

    ns = p.parse_args()

    sr = workflow_steps(ns.number)

    print (sr)

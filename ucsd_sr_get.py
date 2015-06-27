#! /usr/bin/env python

'''
    Command Line Utility to return the steps in a workflow in UCS Director
'''


import requests
import json
from ucsd_library import sr_get

if __name__ == '__main__':

    import sys
    from pprint import pprint
    #from argparse import ArgumentParser, FileType

    #p = ArgumentParser()
    #ns = p.parse_args()

    sr = sr_get()
    pprint (sr)

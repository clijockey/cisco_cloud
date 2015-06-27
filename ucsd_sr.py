#!/usr/bin/env python

#==============================================================================
# Title:				ucsd_sr
# Description:			The pupose is to provide CLI functionality around
#                       service requests
# Author:          		Rob Edwards (clijockey)
# Date:		            27/05/15
# Version:				0.1
# Dependencies:			prettytable module ('sudo easy_install prettytable')
#                       cisco_cloud module
# Limitations/issues:
#==============================================================================

import json
import argparse
import ucsd_library
from prettytable import PrettyTable

def tabular(type):
    # Obtain the data from UCSD
    sr_list = ucsd_library.sr_table(type)

    # Convert JSON string to Dictionary
    srTable = json.loads(sr_list)

    srTableResult = srTable["serviceResult"]
    rows = srTableResult["rows"]

    # Create the table
    table = PrettyTable(["ID", "Catalog", "Status", "Comment", "User"])

    for item in rows:
    	a = item["Service_Request_Id"]
    	b = item["Catalog_Workflow_Name"]
    	c = item["Request_Status"]
    	d = item["Initiator_Comments"]
    	e = item["Initiating_User"]
    	table.add_row([a, b, c, d, e])

    return table


#
parser = argparse.ArgumentParser(
    description='The pupose is to provide CLI functionality around UCSD service requests')
parser.add_argument('--list', '-l',
    action='store_true',
    help='produces a table of all the active service requests' )
parser.add_argument('--archive', '-a',
    action='store_true',
    help='produces a table of all the archived service requests' )

args = parser.parse_args()

if args.list:
    srTable = tabular('active')
    print(srTable)
elif  args.archive:
    srTable = tabular('archive')
    print(srTable)
else:
    print('Need to specify a flag, use -h or --help for more info')

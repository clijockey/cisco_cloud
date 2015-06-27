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

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('--verbose',
    action='store_true',
    help='verbose flag' )
parser.add_argument('--list', '-l',
    action='store_true',
    help='list flag' )

args = parser.parse_args()

if args.list:
    sr_list = ucsd_library.sr_table()

    # Convert JSON string to Dictionary
    srTable = json.loads(sr_list)


    TabularReportValues = srTable["serviceResult"]
    rows = TabularReportValues["rows"]


    table = PrettyTable(["ID", "Catalog", "Status", "Comment", "User"])

    for item in rows:
    	a = item["Service_Request_Id"]
    	b = item["Catalog_Workflow_Name"]
    	c = item["Request_Status"]
    	d = item["Initiator_Comments"]
    	e = item["Initiating_User"]
    	table.add_row([a, b, c, d, e])

    print table
else:
    print("~ No flag selected")

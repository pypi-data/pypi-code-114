#!/usr/bin/env python3.8

# You might want to change the line above to generic python, however, it does require python 3.8 or above to run correctly.
# You MIGHT get away with older versions... but... no warranty here.

import os, sys, io, re
import argparse
import json, csv
import requests

from datetime import datetime,timedelta
import time

import py_helper as ph
from py_helper import CmdLineMode, DebugMode, DbgMsg, Msg, ErrMsg, DbgAuto
from py_helper import DownloadContent

#
# Purpose : Given a string (MAC Address, OUI Code or "other") search through the IEEE MA-L, MA-M, MA-L and CID OUI Code listings.
#
# This code does not dynamically search the online database, it downloads the CSV's and caches them. (See Usage Notes)
#
# Usage Notes:
#
# This module can be used as a command line tool, a plugin using the "run(**kwargs)/arguments/args Pattern" or just as a module
# for some other python program.
#
# There are "output" calls in this code, Msg/DbgMsg, these are controlled by the DebugMode and CmdLineMode functions of the
# py_helper module. Accordingly, when using as a Module or plugin, you want CmdLineMode(False) somewhere in your code prior to
# calling anything in here to avoid output. DebugMode(True) [or False] controls the debug output. The default is CmdLineMode(False).
#
# There are two dependencies in this module...
#
# 1. My py_helper library needs to be installed for this thing to work.
# 2. The variable "StorageLocation" has to be set to someplace writable by the caller. It can be "/tmp" if need be.
#    The caches do not have to be stored permanantly, as they will be dynamically pulled down everytime there is a
#    query when they are not present, however, it's not a good idea to keep pulling these down from IEEE when a
#    cache will do. These files don't change much.
#
# So, please consider this dependency when implementing or customizing this code. Don't abuse the download.
#

#
# Global Variables and Constants
#

#
# Originally, this was designed as plugin for another cmdline tool. But I felt it meritted it's own module
# accordingly, there are some plugin artifacts (like the output Msg calls and other plugin infrastructure)
# still in the code. Also, IT CAN still be used as a plugin.
#

VERSION=(0,0,4)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# Plugins Name
Name = "oui"

# Short Description
ShortDescription = "Get OUI Info from IEEE"

# Description of what this does
Description = "Given a MAC Address or OUI Code, retrieve the registration from IEEE"

# Help, Usage Description
Help = f"{Name} [mac-address|oui-code|search-str]"

# Last Result
LastResult = None

# Internal Functions list
InternalFunctions = list(['run'])

# Tags
Tags = [ "plugins", "command" ]

#
# Non-Plugin Functional Bits
#

# Find Temp Space
__tempspace__ = os.environ["TEMP"] if sys.platform == "win32" else os.environ.get("tmp","/tmp")

# Storage Location (User may want to change this location)
StorageLocation=f"{__tempspace__}/ieee_oui_cache"

# RefreshInterval (in days)
RefreshInterval = 30
# Refresh Cmdline Flag
__Refresh__ = False

# URL To IEEE File
Caches = {
		"oui-ma-l" : [ "oui.csv","http://standards-oui.ieee.org/oui/oui.csv",None,None ],
		"oui-ma-m" : [ "mam.csv","http://standards-oui.ieee.org/oui28/mam.csv",None,None ],
		"oui-ma-s" : [ "oui36.csv","http://standards-oui.ieee.org/oui36/oui36.csv",None,None ],
		"cid" : [ "cid.csv","http://standards-oui.ieee.org/cid/cid.csv",None,None ]
	}

# Parser
__Parser__ = None
# Parsed Args
__Args__ = None
__Unknowns__ = None

# Expressions and RegEx Objects
MACExpr = "^([a-fA-F\d]{2}[\:\-\s]{0,1}){6}$"
OUIExpr = "^([a-fA-F\d]{2}[\:\-\s]{0,1}){3}$"

MACAddress_re = re.compile(MACExpr)
OUICode_re = re.compile(OUIExpr)

#
# Internal functions
#

# Local Cache Loader
def LoadCache(datafile):
	"""Load Local Cache"""

	items = list()

	if os.path.exists(datafile):
		with open(datafile,"r",newline="") as csvfile:
			dialect = csv.Sniffer().sniff(csvfile.read(1024))
			csvfile.seek(0)

			reader = csv.DictReader(csvfile,dialect=dialect)

			for row in reader:
				items.append(row)
	else:
		Msg(f"Can't find local cache, {datafile}")

	return items

# Clean strings
def Strip(mac_oui):
	"""Strip extraneous characters out of MAC/OUI"""

	data = mac_oui.replace(":","").replace("-","").replace(" ","")

	return data

# Get All IEEE Files
def GetCaches(storage_location=None,caches=None):
	"""Get IEEE Data Files"""

	global StorageLocation, Caches, RefreshInterval, __Refresh__

	caches = caches if caches != None else Caches
	storage_location = storage_location if storage_location != None else StorageLocation

	if not os.path.exists(storage_location):
		os.makedirs(storage_location,mode=0o777,exist_ok=True)

	dl_files = list()

	for key,value in caches.items():
		fname,url,cache_location,cache = value

		if cache_location == None:
			cache_location = os.path.join(storage_location,f"{fname}")
			value[2] = cache_location

		# Prep td in case cache does not exist yet
		td = timedelta(days=RefreshInterval + 1)

		if os.path.exists(cache_location):
			# If file in fs is > RefreshInternval old, redownload
			modtime = datetime.fromtimestamp(os.path.getmtime(cache_location))
			localtm = datetime.fromtimestamp(time.mktime(time.localtime()))

			td = localtm - modtime

		if not os.path.exists(cache_location) or td.days > RefreshInterval or __Refresh__:
			Msg(f"{key} does not exist or is out of date, downloading...")
			if DownloadContent(url,cache_location):
				dl_files.append((key,cache_location))
				value[3] = LoadCache(cache_location)

		if value[3] == None:
			value[3] = LoadCache(value[2])

	return dl_files

# Search (The bidness end of this thing)
def Search(search_str):
	"""Search The Caches for Matching OUI or string"""

	global MACAddress_re, OUICode_re, Name

	found = list()

	code = None

	if MACAddress_re.search(search_str):
		# MACAddress
		DbgMsg("MAC Address detected")
		m = Strip(search_str)
		code = m[0:6]
	elif OUICode_re.search(search_str):
		# OUI
		DbgMsg("OUI Code detected")
		code = Strip(search_str)

	code = code.upper()

	DbgMsg(f"{Name} : Beginning Search {search_str} / {code}")

	for cache_name,cache_list in Caches.items():
		fname,url,cache_file,cache = cache_list

		DbgMsg(f"Checking {cache_name}")

		if cache == None:
			cache_list[3] = cache = LoadCache(cache_file)

		for row in cache:
			if code and code == row["Assignment"]:
				DbgMsg(f"Found row by {code}")
				found.append(row)
			elif code == None:
				for value in row.values():
					if search_str in value:
						DbgMsg(f"Found row by {search_str}")
						found.append(row)

	return found

# Build Parser
def BuildParser():
	"""Build Parser"""

	global __Parser__

	if __Parser__ == None:
		parser = __Parser__ = argparse.ArgumentParser(prog="oui",description="IEEE OUI Code Lookup")

		parser.add_argument("-s",help="Storage Location for Cache files")
		parser.add_argument("-r",action="store_true",help="Force refresh")
		parser.add_argument("-d","--debug",action="store_true",help="Enter debug mode")
		parser.add_argument("-t","--test",action="store_true",help="Execute Test Stub")
		parser.add_argument("searchfor",nargs="*",help="OUI Codes to look up")

# Parse Args
def ParseArgs(arguments=None):
	"""Parse Arguments"""

	global __Parser__, __Args__, __Unknowns__
	global StorageLocation, __Refresh__

	if arguments:
		args,unknowns = __Parser__.parse_known_args()
	else:
		args,unknowns = __Parser__.parse_known_args()

	__Args__ = args
	__Unknowns__ = unknowns

	# Check Debug Mode Flag
	if args.debug:
		DebugMode(True)
		DbgMsg("Debug Mode Enabled")

	# Set Cache Location if supplied
	if args.s: StorageLocation = args.s

	__Refresh__ = args.r

	return args,unknowns

# Init Pattern
def Initialize():
	"""Initialize Module"""

	BuildParser()

#
# Run Pattern entry point (for plugin model)
#

# Plugin Starting Point
def run(**kwargs):
	"""Required Plugin Entry Point"""

	global Name, StorageLocation, Caches

	DbgMsg(f"Entering {Name}")

	# If arguments, a list of cmdline args was supplied
	arguments = kwargs.get("arguments",None)
	# If args, a argparse namespace was supplied (i.e. pre-processed cmdline args)
	args = kwargs.get("args",None)

	data = list()		# Any returned data, for machine processing (i.e. csv rows)

	if arguments:
		args,unknowns = ParseArgs(arguments)
	if not args:
		args,unknowns = ParseArgs()

	# Make sure the caches are available (or get them)
	downloaded = GetCaches(StorageLocation,Caches)

	if args.test:
		Test()

		return data

	# Alrighty then, let's git down to bidness
	for arg in args.searchfor:
		found = Search(arg)

		if len(found) > 0:
			data.extend(found)

	if len(data) == 0:
		Msg("Nothing found")
	elif CmdLineMode():
		keys = data[0].keys()
		Msg(",".join(keys))

		for row in data:
			values = row.values()
			line = ",".join(values)
			Msg(line)

	return data

#
# Test Stub
#

# Test Stub
def Test():
	"""Test Stub"""

	pass

#
# Pre Execute Inits
#

Initialize()

#
# Main Loop
#

if __name__ == "__main__":
	CmdLineMode(True)

	run()



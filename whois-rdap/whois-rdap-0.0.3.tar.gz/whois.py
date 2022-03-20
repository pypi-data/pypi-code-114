#!/usr/bin/env python3.8

#
# Imports
#

import os
import sys
import re
import argparse
import requests
import random
import json
import ipaddress
import time

import py_helper as ph
from py_helper import DebugMode, CmdLineMode, ModuleMode, Msg, DbgMsg

# Init Random
random.seed()

#
# Variables
#

# Version
VERSION=(0,0,3)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# Parser
__Parser__ = None

# Email Addess Expression
loose_emailaddr_exp = "(?P<username>[\w_-]+)@(?P<domain>([\w\-]+\.)+([\w\-]*))"

# Email Addess Expression
emailaddr_exp = r"^(?P<username>[\w_-]+)@(?P<domain>([\w\-]+\.)+([\w\-]*))$"
# Generic Abuse Email Expressions
abuse_exp = r"(?P<username>[\w_-]*abuse[^@]*)@(?P<domain>.+)"

# Cmd Line Header Strings
header = [ "http code", "name","handle","start","end","cidr","parent","abuse" ]

# Whois ReSTful Web Service

# Whois RDAP
RDAP_URL="https://rdap-bootstrap.arin.net/bootstrap"

# Resources
ip = "/ip"
poc = "/poc"
org = "/org"
net = "/net"
asn = "/asn"
customer = "/customer"
rdns = "/rdns"

# Handles
orgs = "/orgs"
asns = "/asns"
nets = "/nets"
pocs = "/pocs"
parent = "/parent"
children = "/children"

#
# Lambdas
#

# Loose Email Check
mailcheck = lambda data: re.search(loose_emailaddr_exp,data)

# Check for occurrence of email address in string
#mailcheck = lambda data: re.search(emailaddr_exp,data)

# Check for user email with "abuse" in it
abusecheck = lambda data: re.search(abuse_exp,data)

#
# Support Functions
#

# Get Network Block Specifics
def BreakdownNetwork(start,end):
	"""
	Take an IP starting address for a subnet and it's ending address and get the specifics
	for the subnet, including the netmask, number of bits and the CIDR string
	"""

	network = None
	bits = 0
	cidr = None
	count = 0

	if type(start) is str:
		start = ipaddress.ip_address(start)

	if type(end) is str:
		end = ipaddress.ip_address(end)

	summary = ipaddress.summarize_address_range(start,end)

	try:
		net = next(summary)

		network = net.network_address
		netmask = net.netmask
		bits = net.prefixlen
		cidr = net.with_prefixlen
		count = net.num_addresses
	except StopIteration:
		pass
	except Exception as err:
		DbgMsg(err)

	return network,netmask,bits,cidr,count

# Extract Mail Groups From String (user@domain)
def ExtractMailGroups(data):
	"""
	Wrapper function to simplify removing username and domain from poorly deliniated string.
	"""
	m = re.search(loose_emailaddr_exp,data)

	return "{}@{}".format(m.group("username"),m.group("domain"))

# Be more selective about Abuse addresses
def SelectAbuse(items):
	"""
	Wrapper function to selected the best effort email address from a list of email addresses for
	the abuse email. The algorithm is simple, first, try to find "abuse@domain", next, and email
	addres with "abuse" in the user id. All others are added to the potentials list.
	"""
	hit = None

	potentials = []

	for item in items:
		user,domain = item.split("@")

		if re.search("^abuse$",user):
			hit = item
		else:
			potentials.append(item)

	return hit, potentials

# Hunt for email addresses in a List (of possible JSON, Lists or values)
def HuntEmailAddressesInList(items,level=0):
	"""
	Hunt through a JSON document (in this case list in the JSON Doc) for anything resembling an email address
	"""

	addresses = []

	for item in items:
		if type(item) is list:
			addresses.extend(HuntEmailAddressesInList(item,level+1))
		elif type(item) is dict:
			addresses.extend(HuntEmailAddressesInJSON(item,level+1))
		else:
			if type(item) is str and mailcheck(item):
				item = ExtractMailGroups(item)
				addresses.append(item)

	return addresses

# Hunt for email addresses
def HuntEmailAddressesInJSON(jdoc,level=0):
	"""
	Hunt through a JSON document for anything resembling an email address.
	"""

	keys = jdoc.keys()
	addresses = []

	for key in keys:
		value = jdoc[key]

		if type(value) is list:
			addresses.extend(HuntEmailAddressesInList(value,level+1))
		elif type(value) is dict:
			addresses.extend(HuntEmailAddressesInJSON(value,level+1))
		else:
			if type(value) is str and mailcheck(value):
				value = ExtractMailGroups(value)
				addresses.append(value)

	return addresses

# Get Abuse Address
def GetAbuseAddress(jdoc):
	"""
	Wrapper function to hunt through the JSON returned by WHOIS for an abuse email address.

	Failing to find a match, attempt to find any email address with "abuse" in the username
	and failing that, random select any email addres found as the abuse email address.
	"""

	addresses = HuntEmailAddressesInJSON(jdoc)
	potentials = []
	nonpotentials = []

	for address in addresses:
		if type(address) is str and abusecheck(address):
			potentials.append(address)
		else:
			nonpotentials.append(address)

	hit,others = SelectAbuse(potentials)

	if hit is None and (others is None or len(others) == 0):
		return (None,nonpotentials)

	abusemail = hit if hit else random.choice(others) if len(others) > 0 else ""

	return (abusemail,None)

# Make URL
def MkUrl(resource,querydata):
	"""Wrapper function to make well formed URLs"""

	return "{}{}/{}".format(RDAP_URL,resource,querydata)

#
# Whois Functions
#

# Whois Query with Direct RDAP URL
def whois_rdap(url):
	"""Whois RDAP function"""

	DbgMsg(">>> Entering whois_rdap")

	payload = None
	response = requests.post(url=url)

	if response and response.status_code == requests.codes.ok:
		payload = response.json()

	return response, payload

# Get IP Info
def GetIPInfo(ipaddr,retry_in=10,pause=0):
	"""Use WHOIS API to get whois info for the supplied IP Address"""
	global ip

	DbgMsg(">>> Entering GetIPInfo")

	retry_count = 0
	retry_limit = 2

	result = [ 404, None, None, None, None, None, None ]

	while retry_count < retry_limit:
		response = payload = None

		try:
			response, payload = whois_rdap(MkUrl(ip,ipaddr))
		except requests.ConnectionError:
			time.sleep(retry_in)			# Most likely a rate limit hit
			retry_count += 1
			continue
		except Exception as err:
			break					# Major bummer

		result[0] = response.status_code

		if response.status_code == 429 and retry_count < retry_limit:
			# Rate Limit
			retry_rate = "Retry-After"

			retry_count += 1

			if retry_rate in response.headers:
				try:
					retry_when = int(response.headers[retry_rate])

					time.sleep(retry_when)
				except:
					time.sleep(retry_in)

		elif response.status_code == 200:
			break					# Gooooood
		else:						# Failsafe
			break

	if payload:
		name = payload.get("name","unknown")
		handle = payload.get("handle","")
		startAddress = payload.get("startAddress",ipaddr)
		endAddress = payload.get("endAddress",ipaddr)
		country = payload.get("country","")

		parentHandle = payload.get("parentHandle","")

		abuse,others = GetAbuseAddress(payload)

		if not abuse:
			abuse = random.choice(others) if len(others) > 0 else ""

		network,netmask,bits,cidr,count = BreakdownNetwork(startAddress,endAddress)

		result = [ response.status_code, name, handle, startAddress, endAddress, cidr, parentHandle, abuse, payload, country ]

	if pause > 0:
		time.sleep(pause)

	return result

#
# Init and Run Pattern Handler
#

# Build Parser
def BuildParser():
	"""Build Parser"""

	global __Parser__

	if __Parser__ == None:
		parser = __Parser__ = argparse.ArgumentParser(description='Whois Python Module and Utility')

		parser.add_argument("-d","--debug",action="store_true",help="Enter debug mode")
		parser.add_argument("-t",action="store_true",help="Run test function")
		parser.add_argument("-j",action="store_true",help="Return JSON Response")
		parser.add_argument("-s",action="store_true",help="Show header for output")
		parser.add_argument("ip",nargs='?',help="Search event list")

# Init Module
def Initialize():
	"""Init Module"""

	BuildParser()

# Init Module
Initialize()

# Run/Plugin/CmdLine Pattern Handler
def run(arguments=None):
	"""Run Pattern Handler"""

	global __Parser__, header

	args = None

	if arguments != None:
		args = __Parser__.parse_args(arguments)
	else:
		args = __Parser__.parse_args()

	info = None

	if args.debug:
		DebugMode(True)
		DbgMsg("Setting to debug mode")

	if args.t:
		DbgMsg("Calling test stub")
		test(args)
	elif args.ip:
		DbgMsg("Getting IP Info")

		info = GetIPInfo(args.ip)

		DbgMsg("Checking response\n{}".format(info))
		if info[0] == 200:
			DbgMsg("Attempting to output")

			if args.j:
				Msg(json.dumps(info[8],indent=2))
			else:
				if args.s:
					Msg(",".join(header[1:-1]))

				Msg(",".join(info[1:-2]))
		else:
			Msg("Bummer, RDAP Failed - {}".format(info[0]))
	else:
		Msg("No ip supplied to look up... fool")

#
# Test Stub
#

# Test Function
def test(args):
	""" Test stub"""

	DebugMode(True)
	ModuleMode(False)

	Msg("I do nothing ATM")
	pass

#
# Main Loop
#

if __name__ == "__main__":
	"""Cmdline Loop"""
	ModuleMode(False)

	run()

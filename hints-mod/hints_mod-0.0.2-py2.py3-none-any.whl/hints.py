#!/usr/bin/env python3.8

#
# Hints: Interface for hints and notations, a kind of free form quick and dirty defacto documentation
#

import os, sys, io, re, getpass
import argparse, cmd
import sqlite3 as sql
from sqlite3 import Error
import csv,json
import copy, uuid

from datetime import date,datetime,timedelta,time
import time as tm

# Hmmm... probably not needed
from contextlib import contextmanager

# Ma stoof
import mysqlite as sql

import py_helper as ph
from py_helper import CmdLineMode, DebugMode, DbgMsg, Msg, ErrMsg

#
# Global Variables and Constants
#

# Version Info
VERSION=(0,0,2)
Version = __version__ = ".".join([ str(x) for x in VERSION ])

# Hint File Location
HintURL = None
# Default/Test Hint File
__HintFile__ = "/tmp/hints.sql3"

# Parser
Parser = None

#
# Classes
#

# HintEntry Class
class HintEntry:
	"""HintEntry Class"""

	RecordID = None
	PrimaryTag = None
	Tags = list()
	Description = None
	Timestamp = None
	User = None

	# Init Instance
	def __init__(self,primary=None,description=None,tags=None,timestamp=None,user=None,recordid=None,record=None):
		"""Init Instance"""

		DbgMsg("Exitting HintEntry::__init__")

		if record != None:
			self.Read(record)
		else:
			if recordid:
				self.RecordID = recordid
			else:
				self.RecordID = uuid.uuid1()

			self.PrimaryTag = primary

			if tags != None:
				if type(tags) == list:
					self.Tags = tags
				else:
					self.Tags = tags.split(",")

			self.Description = description

			timestamp = datetime.now() if timestamp == None else timestamp

			self.Timestamp = timestamp

			self.User = getpass.getuser() if user == None else user

		DbgMsg("Exitting HintEntry::__init__")

	# Print Instance Info
	def Print(self,output=True):
		"""Print Instance"""

		DbgMsg("Exitting HintEntry::Print")

		buffer = ""

		buffer = "{:<24} {}\n\t{}\n\t{}\{}".format(self.PrimaryTag,self.Description,",".join(self.Tags),self.Timestamp,self.User)

		if output:
			Msg(buffer)

		DbgMsg("Exitting HintEntry::Print")

		return buffer

	# Format Instance Into JSON
	def Json(self):
		"""Output Contents as JSON"""

		jdoc = {
			"RecordID" : self.RecordID,
			"PrimaryTag" : self.PrimaryTag,
			"Tags" : self.Tags,
			"Description" : self.Description,
			"Timestamp" : self.Timestamp,
			"User" : self.User
		}

		return jdoc

	# Format Instance Into List
	def List(self):
		"""Output Contents as List (for CSV/TSV)"""

		lst = [
			self.RecordID,
			self.PrimaryTag,
			self.Tags,
			self.Description,
			self.Timestamp,
			self.User
		]

		return lst

	# Write Record to Open Connection
	def Write(self,connection=None):
		"""Write to Open Connection"""

		DbgMsg("Entering HintEntry::Write")

		ins = """
			INSERT INTO hints(recordid,primarytag,tags,description,added,user)
			VALUES(?,?,?,?,?,?)
		"""

		parameters = [ str(self.RecordID), self.PrimaryTag, ",".join(self.Tags), self.Description, self.Timestamp, self.User ]

		result = sql.Insert(ins,parameters,connection)

		DbgMsg("Exitting HintEntry::Write")

		return result

	# Read Data For Instance From Open Connection
	def Read(self,datum):
		"""Read Data for Instance From Open Connection"""

		DbgMsg("Entering HintEntry::Read")

		self.RecordID = uuid.UUID(datum[0])
		self.PrimaryTag = datum[1]
		self.Tags = datum[2].split(",")
		self.Description = datum[3]
		self.Timestamp = datum[4]
		self.User = datum[5]

		DbgMsg("Exitting HintEntry::Read")

	# Update Hint Entry
	def Update(self,connection=None):
		"""Update Entry"""

		DbgMsg("Entering HintEntry::Update")

		ins = "UPDATE hints set primary = ?, tags = ?, decription = ? WHERE recordid = ?"
		params = [ self.PrimaryTag, ",".join(self.Tags), self.Description, str(self.RecordID) ]

		result = sql.Update(ins,params,connection)

		DbgMsg("Exiting HintEntry::Update")

		return result

	# Delte This Instance from Database
	def Delete(self,connection=None):
		"""Delete From Database"""

		DbgMsg("Entering HintEntry::Delete")

		ins = "DELETE FROM hints WHERE recordid = ?"

		parameters = [ str(self.RecordID) ]

		result = sql.Delete(ins,parameters,connection=connection)

		DbgMsg("Exitting HintEntry::Delete")

		return result

# Hint Shell
class HintShell(cmd.Cmd):
	"""Hint Shell"""

	intro = "Welcome to the Hint Shell. Type help or ? to list commands.\n"
	prompt = "hint > "
	file = None

	add_parser = None


	# Init Parsers
	def InitParsers(self):
		"""Init Parsers"""

		if add_parser == None:
			add_parser = argparser.ArgumentParser(description="Add Hint")
			add_parser.add_argument("keyword",nargs="?",help="Keyword/Primry Tag, quoted if a phrase")
			add_parser.add_argument("comment",nargs="?",help="Comment, in quotes")
			add_parser.add_argument("tags",nargs="?",help="Any other tags, comma separated")

	# Set HintDB
	def do_hintdb(self,args):
		"""Get or Set Hint DB URL"""

		global HintURL

		if args in [ None, ""]:
			Msg(HintURL)
		else:
			CloseHintDB()

			HintURL = args

			OpenHintDB()

	# Add Hint Entry
	def do_add(self,args):
		"""Add Hint Entry"""

		self.InitParsers()

		arguments = ph.ParseDelimitedString(args)

		args,unknowns = self.add_parser.parse_args(arguments)

		he = HintEntry(args.keyword,args.comment,args.tags)

		he.Write()

	# Bulk Add
	def do_bulkadd(self,args):
		"""Bulk Add"""

		BulkAdd(args)

	# Remove Hint
	def do_rm(self,args):
		"""Remove Hint"""

		Delete(args)

	# Bulk Remove
	def do_bulkrm(self,args):
		"""Bulk remove"""

		BulkDelete(args)

	# Edit Entry
	def do_edit(self,args):
		"""Edit Single Hint Entry"""

		# args should be uuid
		hes = Search(args)

		if hes and len(hes) > 0:
			he = hes[0]

			buffer = f"{he.PrimaryTag}\n{he.Description}\n{he.Tags}"

			EditBuffer(buffer)

			fields = buffer.split("\n")

			he.PrimaryTag = fields[0]
			he.Description = fields[1]
			he.Tags = fields[2]

			he.Update()

	# Info
	def do_info(self,args):
		"""Info About Hint Database"""

		HintFileInfo()

	# Dump
	def do_dump(self,args):
		"""Dump hint database"""

		results = Dump()

		output = True
		f_out = None

		if not args in [ None, "" ]:
			output = False
			f_out = open(args,"w")

		for result in results:
			buffer = result.Print(output)

			if not output:
				f_out.write(buffer + "\n")

		if f_out: close(f_out)

	# Search
	def do_search(self,args):
		"""Search Hint Database"""

		results = Search(args)

		for result in results:
			result.Print()

	# Quit Shell
	def do_quit(self,args):
		"""Quit Shell"""
		return True

#
# Functions
#

# Edit Buffer (added to py_helper 2/24/2022, can remove this at some point)
def EditBuffer(buffer,prompt=False):
	"""
	Edit a string buffer in an external editor

	If input buffer/string remains unchanged, None is returned
	"""

	tmp = ph.TmpFilename()
	new_buffer = ""

	with open(tmp,"w") as f_out:
		f_out.write(buffer)

	ph.Edit(tmp)

	with open(tmp,"r") as f_in:
		new_buffer = f_in.read()

	os.remove(tmp)

	response = "y"

	if prompt:
		response = input("Keep (y/n)? ")

	if buffer == new_buffer or response.lower() == "n":
		new_buffer = None

	return new_buffer

# Open DB
def OpenHintDB(url=None):
	"""Open Database"""

	DbgMsg("Entering hints::OpenHintDB")

	global HintURL, CurrentConnection

	conn = None

	if url == None: url = HintURL

	hint_table = """CREATE TABLE IF NOT EXISTS hints (
		recordid VARCHAR(36),
		primarytag VARCHAR(64),
		tags VARCHAR(924),
		description VARCHAR(1024),
		added timestamp,
		user VARCHAR(32)
	);"""

	table_specs = [ hint_table ]

	if sql.ActiveConnection != None:
		sql.Close(sql.ActiveConnection)

	try:
		conn = sql.Open(url,table_specs)
		CurrentConnection = conn
	except Error as dberr:
		ErrMsg(dberr,f"An error occurred trying to open {url}")
	except Exception as err:
		ErrMsg(err,f"An error occurred trying to open {url}")

	DbgMsg("Exitting hint::OpenHintDB")

	return conn

# Close Hint DB
def CloseHintDB(connection=None):
	"""Close current Connection"""

	if connection != None:
		connection.close()
	else:
		sql.Close(sql.ActiveConnection)

# Get Stats On Hint File
def HintFileInfo(output=True):
	"""Get Hint File Data"""

	global HintURL

	count = 0
	accessible = True

	buffer = "{:<20} : {}\n".format("Hint File",HintURL)

	try:
		buffer += "{:<20} : {}\n".format("File Size",os.path.getsize(HintURL))

		recs = Dump()
		count = len(recs)
	except Exception as err:
		accessible = False;

	buffer += "{:<20} : {}\n".format("Accessible",accessible)
	buffer += "{:<20} : {}".format("Records",count)

	if output:
		Msg(buffer)

	return buffer

# Add Hint
def Add(keyword,description,tags,timestamp=None,user=None,connection=None):
	"""Add Hint"""

	global CurrentConnection

	DbgMsg("Entering hints::Add")

	he = HintEntry(keyword,description,tags,timestamp=timestamp,user=user)

	he.Write(connection)

	DbgMsg("Exitting hint::Add")

	return he

# Bulk Adds
def BulkAdd(filename,connection=None):
	"""Bulk Adds"""

	DbgMsg("Entering hints::BulkAdd")

	he = None

	hes = list()

	if os.path.exists(filename):
		with open(filename,"r",newline='') as tsvfile:
			reader = csv.reader(tsvfile,delimiter="\t")

			for row in reader:
				he = HintEntry(row[0],row[1],row[2])

				he.write(connection)

				hes.append(he)

	DbgMsg("Exitting hint::BulkAdd")

	return hes

# Delete Hint(s)
def Delete(record_id,connection=None):
	"""Delete Hints from DB"""

	DbgMsg("Entering hints::Delete")

	he = HintEntry(recordid=record_id)

	result = he.Delete(connection)

	DbgMsg("Exitting hint::Delete")

	return result

# Bulk Delete
def BulkDelete(filename,connection=None):
	"""Bulk Delete"""

	success = False

	if os.path.exists(filename):
		with open(filename,"r") as f_in:
			for line in f_in:
				result = Delete(line,connection)

		success = True

	return success

# Dump Hint DB
def Dump(connection=None):
	"""Dump Database"""

	DbgMsg("Entering hints::Dump")

	rows = sql.Select("SELECT * FROM hints",connection=connection)

	records = list()

	for row in rows:
		he = HintEntry(record=row)

		records.append(he)

		Msg(f"{he.PrimaryTag}, {he.Description}, {he.Tags}, {he.RecordID}")

	DbgMsg("Exitting hint::Dump")

	return records

# Search Hint DB
def Search(pattern,all=False,exact=False,connection=None):
	"""Search Hint File"""

	DbgMsg("Entering hints::Search")

	cmd = None
	records = list()

	if not all:
		parameters = [ pattern, pattern, pattern ]

		if exact:
			cmd = "SELECT * FROM hints where primarytag = ? or description = ? or tags = ?"
		else:
			cmd = "SELECT * FROM hints where primarytag like ? or description like ? or tags like ?"

		results = sql.Select(cmd,parameters,connection)

		for result in results:
			records.append(result)
	else:
		cmd = "SELECT * FROM hints"

		results = sql.Select(cmd,connection)

		for arg in args:
			exp = re.compile(pattern)

			for row in results:
				flag = (exp.search(row[1]) or exp.search(row[2]) or exp.search(row[3]))

				if flag:
					records.append(row)

	DbgMsg("Exitting hint::Search")

	return records

# Set Hintfile/Location
def SetHintFile(fname=None):
	"""Set Hint File"""

	global HintURL

	if fname:
		HintURL = fname
	else:
		HintURL = __HintFile__

# Build Parser
def BuildParser():
	"""Build Parser"""

	global Parser

	Parser = parser = argparse.ArgumentParser(prog="Hints App",description="Hints App")

	parser.add_argument("-d","--debug",action="store_true",help="Enter debug mode")
	parser.add_argument("--hint",help="Hint DB Url")

	subparsers = parser.add_subparsers(help="Sub commands",dest="operation")

	# Test Mode
	test_sp = subparsers.add_parser("test",help="Enter Test Mode")

	# Shell Mode
	shell_sp = subparsers.add_parser("shell",help="Enter Shell Mode")

	# Shell Mode
	dump_sp = subparsers.add_parser("dump",help="Dump hint database")

	# Add Cmd
	add_sp = subparsers.add_parser("add",help="Add hint")
	add_sp.add_argument("keyword",nargs=1,help="Keyword/primary tag of hint")
	add_sp.add_argument("description",nargs=1,help="Description of hint")
	add_sp.add_argument("tags",nargs="?",help="Any extra tags")

	# Bulk Add
	bulkadd_sp = subparsers.add_parser("bulkadd",help="Bulk add")
	bulkadd_sp.add_argument("filename",help="Filename with bulk data")

	# Delete One Cmd
	del_ap = subparsers.add_parser("rm",help="Remove hint")
	del_ap.add_argument("recordid",default=None,help="Hint to delete")

	# Bulk Delete Cmd
	bulkdel_ap = subparsers.add_parser("bulkrm",help="Bulk Remove")
	bulkdel_ap.add_argument("filename",help="Filenme with bulk data")

	# Search Cmd
	search_sp = subparsers.add_parser("search",help="Search hint database")
	search_sp.add_argument("-e","--exact",action="store_true",help="Exact tring search")
	search_sp.add_argument("--all",action="store_true",help="Return/Search all entries")
	search_sp.add_argument("pattern",help="Pattern to search for, can be regular expression if --all is enabled")

# Parse Args
def ParseArgs(arguments=None):
	"""Parse Args"""

	DbgMsg("Entering hints::ParseArgs")

	args = unknowns = None

	if arguments != None:
		args,unknowns = Parser.parse_known_args(arguments)
	else:
		args,unknowns = Parser.parse_known_args()

	if args.debug: DebugMode(True)

	if args.hint:
		SetHintFile(args.hint)

	DbgMsg("Exitting hint::ParseArgs")

	return args,unknowns

#
# Initialize Module
#
def Initialize():
	"""Initialize Module"""

	DbgMsg("Entering hints::Initialize")

	SetHintFile()

	BuildParser()

	DbgMsg("Exitting hint::Initialize")

# Run pattern handler
def run(**kwargs):
	"""Run/plugin pattern handler"""

	arguments = kwargs.get("arguments",None)
	args = kwargs.get("args",None)
	results = None

	if arguments:
		args,unknowns = ParseArgs(arguments)
	elif args == None:
		args,unknowns = ParseArgs()

	try:
		OpenHintDB()
	except Exception as err:
		ErrMsg(err,"A problem occurred trying to open the hint database")

		return results

	try:
		op = args.operation

		if op == "test" and CmdLineMode():
			test()
		elif op == "shell":
			HintShell().cmdloop()
		elif op == "add":
			result = Add(args.keyword,args.decription,args.tags)
		elif op == "bulkadd":
			result = BulkAdd(args.filename)
		elif op == "rm":
			result = Delete(args.recordid)
		elif op == "bulkrm":
			result = BulkDelete(args.filenme)
		elif op == "search":
			results = Search(args.pattern,args.all,args.exact)

			if CmdLineMode():
				for result in results:
					result.Print()
		elif op == "dump":
			result = Dump()

	except Exception as err:
		ErrMsg(err,f"An error occurred trying operation on hint database - {cmd}")
	finally:
		CloseHintDB()

	return results

#
# Test Scaffolding
#

# Test Scaffolding
def Test():
	"""Test Scaffolding"""

	Msg("Entering Test Scaffolding")

	Msg("Does nothing ATM")

	Msg("Exitting Test Scaffolding")

#
# Internal Init
#

Initialize()

#
# Main Loop
#

if __name__ == "__main__":
	# Setup CommandLine Mode
	CmdLineMode(True)

	run()

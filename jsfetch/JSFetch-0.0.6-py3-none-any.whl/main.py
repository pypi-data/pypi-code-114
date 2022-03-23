#! /usr/bin/env python

from .errors import NoCallBack
import aiohttp
import json

class Promise:
	def __init__(self, prev_promise, then_callable=None, catch_callable=None, finally_callable=None):
		self.prev_promise = prev_promise
		# Basic Variables
		self.data = None
		self.resolved = False
		self.next_promise = None

		# Add a check here to see if atleast one of the callables are provided
		if not then_callable and not catch_callable and not finally_callable:
			raise NoCallBack("Callback is needed to form a chain")
		self.then_callable = then_callable
		self.catch_callable = catch_callable
		self.finally_callable = finally_callable
		
	# Basic Methods for user
	def then(self, callable):
		self.next_promise = Promise(self, then_callable=callable)
		return self.next_promise
	
	def catch(self, callable):
		self.next_promise = Promise(self, catch_callable=callable)
		return self.next_promise
	
	def finally_(self, callable):
		self.next_promise = Promise(self, finally_callable=callable)
		return self.next_promise
	
	# Util methods for user
	def toJSON(self):
		return self.then(lambda data: json.loads(data))
	
	# Methods not for user
	def resolve(self, value):
		self.resolved = True
		try:
			# Give More Data to the callable
			self.data = self.then_callable(value)
			self.next_promise.resolve(self.data)
		except Exception as err:
			if self.catch_callable:
				self.catch_callable(err)
			elif self.next_promise:
				self.next_promise.rejected(value)
			else:
				raise err
		finally:
			if self.finally_callable:
				self.finally_callable()
	
	# Methods for working with the class
	def __str__(self):
		if self.resolved:
			return "Promise {<fulfilled>: {0}}".format(self.data)
		else:
			return "Promise {<pending>}"
	
	def __bool__(self):
		return self.resolved
	
	# If the user is using any other method which is not from class then return the data
	def __getattr__(self, name):
		return getattr(name, self.data)
	
	def __getitem__(self, key):
		return self.data[key]


async def fetch(url):
	empt_promise = Promise(None)
	yield empt_promise
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			empt_promise.resolve(await response)
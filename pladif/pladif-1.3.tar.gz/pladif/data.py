""""This file is part of PLADIF.

	MIT License

	Copyright (c) 2022 - Thibault Hilaire

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.


PLADIF is a simple tool that plots attrakdiff graphs from CSV files (like those from Usabilla).
It is written by Thibault Hilaire

File: data.py
Date: March 2022

	class for the data
"""
from __future__ import annotations

from io import BytesIO
from os.path import splitext
from pandas import read_csv, read_excel
from math import log10
from pladif.naming import order_long, order_short, pairs


def datasize(size, lang):
	"""
	Calculate the size of a code in B/KB/MB.../
	Return a tuple of (value, unit)
	"""
	# see https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb
	units = {'en': ["B", "kB", "MB", "GB", "TB"], 'fr': ["o", "ko", "Mo", "Go", "To"], 'de': ["B", "kB", "MB", "GB", "TB"]}
	if size:
		scaling = round(log10(size))//3
		scaling = min(len(units)-1, scaling)
		return "%.3f %s" % (size/(10**(3*scaling)), units[lang][scaling])
	else:
		return "unknown"


def removeStar(st: str) -> str:
	"""remove the '*' character in the end of the categories"""
	return st[:-1] if '*' in st else st


class DataAttrakdiff:
	"""encapsulates the data
	- _filename: (str) file name
	- _CSVcolumns: list of initial column names (in the CSV file)
	- _df: (DataFrame) data
	"""

	def __init__(self, file: BytesIO | str):
		"""Load the data from an (already open) csv file
		The data is normalize in [-3,3]
		"""
		# open the file if its just a filename
		if isinstance(file, str):
			file = open(file, "rb")
		self._filename = file.name
		_, ext = splitext(self._filename)
		# read the excel file into a dataframe
		if ext[1:] == 'csv':
			self._df = read_csv(file, index_col=0, encoding="UTF-16", delimiter='\t')  # encoding=None, encoding_errors="replace"
			# drop all the columns after the URL column
			try:
				url_index = self._df.columns.get_loc("URL")
			except KeyError:
				raise ValueError("The csv file is not a valid Usabilla one (does not contain a 'URL' column) !")
			self._CSVcolumns = self._df.columns[:url_index]
			self._df.drop(columns=self._df.columns[url_index:], inplace=True)
			# check the size and rename the columns
			if len(self._df.columns) not in [len(order_short), len(order_long)]:
				raise ValueError("The csv file is not a valid Usabilla one (doesn not have %d or %d useful columns)" % (
				len(order_short), len(order_long)))
			self._df.columns = order_short if len(self._df.columns) == len(order_short) else order_long
		elif ext[1:] in ['xls', 'xlsx', 'xlsm', 'xlsb', 'odf', 'ods', 'odt']:
			self._df = read_excel(file, sheet_name=0, index_col=0)  # encoding=None, encoding_errors="replace"
			self._CSVcolumns = self._df.columns
			# check if the columns are valid
			if set(self._df.columns) != set(order_short) and set(self._df.columns) != set(order_long):
				raise ValueError("The excel file doesn't have proper columns (not in %s)" % str(order_long))

		# normalize data in [-3,3]
		for col, serie in self._df.items():
			if '*' in col:
				self._df[col] = 4 - self._df[col]  # reverse from 3 to -3
			else:
				self._df[col] = self._df[col] - 4  # from -3 to 3
		# remove the '*' and sort the columns (same order as the ordered dictionary `pairs`
		self._df.columns = map(removeStar, self._df.columns)
		d = {k: v for v, k in enumerate(pairs)}
		col, self._CSVcolumns = zip(*sorted(zip(self._df.columns, self._CSVcolumns), key=lambda x: d.get(x[0])))
		self._df = self._df.reindex(columns=col)
		# get filesize
		try:
			self._size = file.getbuffer().nbytes
		except AttributeError:
			self._size = 0


	def summary(self, col, lang):
		"""return a summary of the data
		containing the filename, the number of users and """
		col = list(c if '*' not in c else c[:-1] for c in col)
		d = {col: csv for col, csv in zip(self._df.columns, self._CSVcolumns)}
		return [self._filename, str(self._df.shape[0]), datasize(self._size, lang)] + [d.get(c, '') for c in col]

	@property
	def columns(self):
		"""returns the columns"""
		return self._df.columns

	@property
	def df(self):
		"""return the dataframe"""
		return self._df

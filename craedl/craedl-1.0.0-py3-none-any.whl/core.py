# Copyright 2022 The Johns Hopkins University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from datetime import timezone
import glob
import hashlib
import json
import os
import requests
from requests_toolbelt import MultipartEncoder
import sys
import time

from craedl import cache as sync_cache
from craedl import errors

BUF_SIZE = 10485760
RETRY_MAX = 5
RETRY_SLEEP = 1
DT1970 = datetime(1970, 1, 1, tzinfo=timezone.utc)

##########
import requests.packages.urllib3.util.connection as urllib3_cn
import socket
"""
Forces systems that default to IPv6 to use IPv4.
"""
def allowed_gai_family():
  family = socket.AF_INET  # force IPv4
  return family
urllib3_cn.allowed_gai_family = allowed_gai_family
##########

def hash_directory(path):
  """
  Generate a hash string representing the state of the files in a directory.
  The hash changes if any file is added, removed, or modified on disk.

  :param path: the directory path
  :type path: string
  :returns: a SHA1 hash representation of the files in the directory
  """
  children_hash = hashlib.sha1()
  children = os.scandir(path)
  for child in children:
    basename = os.path.basename(child.path)
    if (basename[0] != '.' and basename[0] != '~'):
      children_hash.update(child.stat().st_mtime.hex().encode('utf-8'))
  return children_hash.hexdigest()

def to_x_bytes(bytes):
  """
  Take a number in bytes and return a human-readable string.

  :param bytes: number in bytes
  :type bytes: int
  :returns: a human-readable string
  """
  x_bytes = bytes
  power = 0
  while x_bytes >= 1000:
    x_bytes = x_bytes * 0.001
    power = power + 3
  if power == 0:
    return '%.0f bytes' % x_bytes
  if power == 3:
    return '%.0f kB' % x_bytes
  if power == 6:
    return '%.0f MB' % x_bytes
  if power == 9:
    return '%.0f GB' % x_bytes
  if power == 12:
    return '%.0f TB' % x_bytes


class Auth():
  """
  This base class handles low-level RESTful API communications. Any class that
  needs to perform RESTful API communications should extend this class.
  """
  token = None
  if sys.platform == 'win32':
    token_path = os.path.abspath(
      os.path.join(
        os.sep,
        os.path.expanduser('~'),
        'AppData',
        'Local',
        'Craedl',
        'craedl'
      )
    )
  elif sys.platform == 'darwin':
    token_path = os.path.abspath(
      os.path.join(
        os.sep,
        'Users',
        os.getlogin(),
        'Library',
        'Preferences',
        'Craedl',
        'craedl'
      )
    )
  else:
    token_path = os.path.expanduser('~/.config/Craedl/craedl')

  def __init__(self, host=None):
    if not os.path.isfile(os.path.expanduser(self.token_path)):
      raise errors.Missing_Token_Error
    if host:
      self.host = host
    else:
      self.host = 'https://api.craedl.org'

  def __repr__(self):
    string = '{'
    for k, v in vars(self).items():
      if k != 'token':
        if type(v) is str:
          string += "'" + k + "': '" + v + "', "
        else:
          string += "'" + k + "': " + str(v) + ", "
    if len(string) > 1:
      string = string[:-2]
    string += '}'
    return string

  def DELETE(self, path):
    """
    Handle a DELETE request.

    :param path: the RESTful API method path
    :type path: string
    :returns: a dict containing the contents of the parsed JSON response or
      an HTML error string if the response does not have status 200
    """
    if not self.token:
      self.token = open(os.path.expanduser(self.token_path)).readline().strip()
    attempt = 0
    while attempt < RETRY_MAX:
      attempt = attempt + 1
      try:
        response = requests.delete(
          self.host + path,
          headers={'Authorization': 'Bearer %s' % self.token},
        )
        return self.process_response(response)
      except requests.exceptions.ConnectionError:
        time.sleep(RETRY_SLEEP)
    raise errors.Retry_Max_Error

  def GET(self, path, data=False):
    """
    Handle a GET request.

    :param path: the RESTful API method path
    :type path: string
    :param data: whether the response is a data stream (default False)
    :type data: boolean
    :returns: a dict containing the contents of the parsed JSON response,
      data stream, or an HTML error string if the response does not have
      status 200
    """
    if not self.token:
      self.token = open(os.path.expanduser(self.token_path)).readline().strip()
    attempt = 0
    while attempt < RETRY_MAX:
      attempt = attempt + 1
      try:
        if not data:
          response = requests.get(
            self.host + path,
            headers={'Authorization': 'Bearer %s' % self.token},
          )
          return self.process_response(response)
        else:
          response = requests.get(
            self.host + path,
            headers={'Authorization': 'Bearer %s' % self.token},
            stream=True,
          )
          return response
      except requests.exceptions.ConnectionError:
        time.sleep(RETRY_SLEEP)
    raise errors.Retry_Max_Error

  def POST(self, path, data, filepath=None):
    """
    Handle a POST request.

    :param path: the RESTful API method path
    :type path: string
    :param data: the data to POST to the RESTful API method as described at
      https://api.craedl.org
    :type data: dict
    :param filepath: the path to the file to be passed
    :type filepath: string
    :returns: a dict containing the contents of the parsed JSON response or
      an HTML error string if the response does not have status 200
    """
    if not self.token:
      self.token = open(os.path.expanduser(self.token_path)).readline().strip()
    attempt = 0
    while attempt < RETRY_MAX:
      attempt = attempt + 1
      try:
        if not filepath:
          response = requests.post(
            self.host + path,
            json=data,
            headers={'Authorization': 'Bearer %s' % self.token},
          )
        else:
          d = data
          for k in d:
            if type(d[k]) != str:
              d[k] = str(d[k])
          with open(filepath, 'rb') as f:
            d['file'] = (filepath.split(os.sep)[-1], f, 'application/octet-stream')
            encoder = MultipartEncoder(d)
            response = requests.post(
              self.host + path,
              data=encoder,
              headers={
                'Authorization': 'Bearer %s' % self.token,
                'Content-Type': encoder.content_type
              },
            )
        return self.process_response(response)
      except requests.exceptions.ConnectionError:
        time.sleep(RETRY_SLEEP)
    raise errors.Retry_Max_Error

  def process_response(self, response):
    """
    Process the response from a RESTful API request.

    :param response: the RESTful API response
    :type response: a response object
    :returns: a dict containing the contents of the parsed JSON response or
      an HTML error string if the response does not have status 200
    """
    if response.status_code == 200:
      out = json.loads(response.content.decode('utf-8'))
      if out:
        return out
    elif response.status_code == 400:
      raise errors.Parse_Error(details=response.content.decode('ascii'))
    elif response.status_code == 401:
      raise errors.Invalid_Token_Error
    elif response.status_code == 403:
      raise errors.Unauthorized_Error
    elif response.status_code == 404:
      raise errors.Not_Found_Error
    elif response.status_code == 500:
      raise errors.Server_Error
    else:
      raise errors.Other_Error


class Craedl(Auth):
  """
  A Craedl. Get a Craedl from the API by passing `id`. Get a Craedl from an
  existing dictionary (for example, a child carried by a parent)without any
  network traffic by passing `data`.
  """

  def __init__(self, host, slug, id=None, data={}):
    super().__init__(host=host)
    self.children = []
    if not data:
      if not id:
        data = self.GET('/db/%s/craedl/' % (slug,))
        self.__unpack_tree__(host, data)
      else:
        data = self.GET('/db/%s/craedl/%d/' % (slug, id,))
    for k, v in data.items():
      if not (type(v) is dict or type(v) is list):
        if not v == None:
          setattr(self, k, v)

  def __repr__(self, depth=0):
    out = '%s [%s:%d]' % (self.name, self.slug, self.id)
    depth += 1
    for child in self.children:
      out += '\n'
      for _ in range(depth-1):
        out += '    '
      out += '  - '
      out += child.__repr__(depth)
    return out

  def __unpack_tree__(self, host, data):
    """
    Unpack a Craedl tree.
    """
    for child in data['children']:
      craedl = Craedl(
        host,
        child['slug'],
        child['id'],
        data=child,
      )
      craedl.__unpack_tree__(host, child)
      self.children.append(craedl)

  def get_data(self):
    """
    Retrieve the root directory associated with this Craedl.

    :returns: the root Inode of this Craedl
    """
    return Inode(self, self.root_inode)

  def get_wiki(self, revision=0):
    """
    Retrieve the wiki for this Craedl.

    :param revision: the historical revision to view, moving backward through
      time (defaults to current revision)
    :type revision: int
    """
    data = self.GET('/db/%s/craedl/%d/wiki/' % (self.slug, self.id))
    return data['results'][-revision]['content']


class Inode(Auth):
  """
  A Craedl inode (directory or file) object. Get an Inode from the API by
  passing `id`. Get an Inode from an eisting dictionary (for example, a child
  carried by a parent) without any network traffic by passing `data`.
  """

  def __init__(self, craedl, id=None, data={}):
    super().__init__(host=craedl.host)
    self.craedl = craedl
    if not data:
      data = self.GET('/mech/%s/craedl/%d/inode/%d/?all=true' % (
        craedl.slug,
        craedl.id,
        id
      ))
    for k, v in data.items():
      setattr(self, k, v)
    if not hasattr(self, 'children'):
      self.children = {'results': []}
    if self.type == 'd':
      h = hashlib.sha1()
      for c in self.children['results']:
        if c['type'] == 'f':
          h.update((
            datetime.fromisoformat(c['date_modify']) - DT1970
          ).total_seconds().hex().encode('utf-8'))
      self.hash = h.hexdigest()

  def __repr__(self):
    out = '%s [%d]' % (self.name, self.id)
    return out

  def abspath(self):
    """
    Get a string representation of the absolute path for an inode.

    :returns: a string containing the absolute path for an inode
    """
    if not hasattr(self, 'path'):
      self = Inode(self.craedl, self.id)
      path = self.path
    else:
      path = self.path
    out = ''
    for p in path:
      out += '/%s [%d]' % (p['name'], p['id'])
    if self.type == 'd':
      out += '/'
    return out

  def create_directory(self, name):
    """
    Create a new directory within the current directory.

    :param name: the name of the new directory
    :type name: string
    :returns: the new Inode
    """
    data = {
      'name': name,
      'parent': self.id,
      'type': 'd',
    }
    response_data = self.POST('/mech/%s/craedl/%d/inode/' % (
      self.craedl.slug,
      self.craedl.id,
    ), data)
    child = Inode(self.craedl, data=response_data)
    self.children['results'].append(child)
    return child

  def delete(self):
    """
    Delete the current directory.
    """
    response_data = self.DELETE('/mech/%s/craedl/%d/inode/%d/?c=%d' % (
      self.craedl.slug,
      self.craedl.id,
      self.parent,
      self.id
    ))

  def download(self, save_path, rescan=True, output=False, accumulated_size=0):
    """
    Download the contents of the current Inode into `save_path`. If the current
    Inode is a directory, download recursively; this generates a cache database
    file in the `save_path` that is used to enhance performance of retries and
    synchronizations.

    :param save_path: the path to the directory on your computer that will
      contain this file's data
    :type save_path: string
    :param rescan: whether to rescan the directories (defaults to True);
      ignores new children in already transferred directories if False
    :type rescan: boolean
    :param output: whether to print to STDOUT (defaults to False)
    :type output: boolean
    :param accumulated_size: the total size of the download so far; primarily
      supports recursive download output messages
    :returns: a tuple containing the updated instance of this directory and the
      size of the download
    """
    save_path = os.path.expanduser(save_path)
    if not os.path.isdir(save_path):
      print('Failure: %s is not a directory.' % save_path)
      exit()

    if self.type == 'd':
      # create this directory
      save_path = save_path + os.sep + self.name
      if output:
        print('CREATE DIR %s...' % (save_path + os.sep), end='', flush=True)
      try:
        os.mkdir(save_path)
        if output:
          print('created', flush=True)
      except FileExistsError:
        if os.path.isfile(save_path):
          print('Failure: %s is a file.' % save_path)
        else:
          if output:
            print('exists', flush=True)
          pass
      cache_path = save_path + os.sep + '.craedl-download-cache-%d.db' % (
        self.id
      )
      cache = sync_cache.Cache()
      cache.open(cache_path)

      # begin the recursive download 
      (self, this_size) = self.download_recurse(
        cache,
        save_path,
        rescan,
        output,
        0
      )

      if cache:
        cache.close()

      return (self, this_size)

    else:
      # download this file
      if output:
        print('DOWNLD FIL %s...' % (save_path + os.sep + self.name),
          end='',
          flush=True
        )

      # check timestamps to determine whether we should stream this data
      stream_data = True
      if os.path.isfile(save_path + os.sep + self.name):
        local_mtime = os.path.getmtime(save_path + os.sep + self.name)
        remote_mtime = (datetime.fromisoformat(
          self.date_modify
        ) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
        if local_mtime > remote_mtime:
          stream_data = False
      if stream_data: # stream the data only if remote is newer than local
        data = self.GET('/mech/%s/craedl/%d/inode/%d/data/' % (
          self.craedl.slug,
          self.craedl.id,
          self.id
        ), data=True)
        try:
          f = open(save_path, 'wb')
        except IsADirectoryError:
          f = open(save_path + os.sep + self.name, 'wb')
        for chunk in data.iter_content():
          # because we are using iter_content and GET_DATA uses stream=True
          # in the request, the data is not read into memory but written
          # directly from the stream here
          f.write(chunk)
        f.close()
        size = self.size
        if output:
          print('downloaded %s (%s)' % (
            to_x_bytes(size),
            to_x_bytes(size + accumulated_size)
          ), flush=True)
        return (self, size)
      else:
        if output:
          print('current (%s)' % to_x_bytes(accumulated_size), flush=True)
        return (self, 0)

  def download_recurse(
    self,
    cache,
    save_path,
    rescan,
    output,
    accumulated_size
  ):
    """
    The recursive function that does the downloading. There is little reason
    to call this directly; use :meth:`Inode.download` to start a recursive
    directory download.

    :param cache: the cache database
    :type cache: :py:class:`~craedl.cache.Cache`
    :param save_path: the path to the directory on your computer that will
      contain this file's data
    :type save_path: string
    :param rescan: whether to rescan the directories (defaults to True);
      ignores new children in already transferred directories if False
    :type rescan: boolean
    :param output: whether to print to STDOUT (defaults to False)
    :type output: boolean
    :param accumulated_size: the amount of data that has been downloaded so
      far
    :type: integer
    :returns: a tuple containing the updated instance of this directory and
      the amount of data that has been downloaded by this recursion level
      and its children
    """
    this_size = 0

    do_download = True
    if cache.check(save_path, self.hash):
      # no need to download
      do_download = False
      if not rescan:
        # skip this recursion branch if user requests not to look for
        # changes to already downloaded children
        return (self, this_size)
    else:
      # record the directory hash
      cache.start(save_path, self.hash)

    ls = self.list()
    if do_download:
      for f in ls['files']:
        # download child files
        (f, new_size) = f.download(
          save_path,
          output=output,
          accumulated_size=accumulated_size + this_size
        )
        this_size = this_size + new_size
    else:
      for f in ls['files']:
        # safe to skip this file
        if output:
          print('SYNCHD FIL %s...skip (%s)' % (
            save_path + os.sep + f.name,
            to_x_bytes(accumulated_size + this_size)
          ))

    for d in ls['dirs']:
      # recurse into child directories
      if output:
        print('CREATE DIR %s...' % (
          save_path + os.sep + d.name + os.sep
        ), end='', flush=True)
      try:
        os.mkdir(save_path + os.sep + d.name)
        if output:
          print('created', flush=True)
      except FileExistsError:
        if os.path.isfile(save_path + os.sep + d.name):
          print('Failure: %s is a file.' % save_path + os.sep + d.name)
        else:
          if output:
            print('exists', flush=True)
          pass

      (d, new_size) = d.download_recurse(
        cache,
        save_path + os.sep + d.name,
        rescan=rescan,
        output=output,
        accumulated_size=accumulated_size + this_size
      )
      this_size = this_size + new_size

    # mark download as completed in cache
    cache.finish(save_path, self.hash)

    return (self, this_size)

  def get(self, path):
    """
    Get a particular directory or file. This may be an absolute or relative
    path.

    :param path: the directory or file path
    :type path: string
    :returns: the requested directory or file
    """
    if not path or path == '.':
      return self
    if path[0] == os.sep:
      p = path.split(os.sep)[1]
      try:
        root_inode = Inode(self.craedl, self.craedl.root_inode)
        if p != root_inode.name:
          raise FileNotFoundError(p + ': No such file or directory')
        return root_inode.get(path.replace('/%s/' % root_inode.name, ''))
      except errors.Not_Found_Error:
        raise FileNotFoundError(p + ': No such file or directory')
    while path.startswith(os.sep) or path.startswith('.' + os.sep):
      if path.startswith(os.sep):
        path = path[1:]  # 1 = len('/')
      else:
        path = path[2:]  # 2 = len('./')
    if not path or path == '.':
      return self
    p = path.split(os.sep)[0]
    if p == '..':
      path = path[2:]  # 2 = len('..')
      while path.startswith(os.sep):
        path = path[1:]  # 1 = len('/')
      try:
        return Inode(self.craedl, self.parent).get(path)
      except errors.Not_Found_Error:
        raise FileNotFoundError(p + ': No such file or directory')
    for c in self.children['results']:
        if type(c) != Inode:
          c = Inode(self.craedl, data=c)
        if p == c.name:
          path = path[len(p):]
          while path.startswith(os.sep):
            path = path[1:]  # 1 = len('/')
          if path:
            return Inode(self.craedl, c.id).get(path)
          else:
            return Inode(self.craedl, c.id)
    raise FileNotFoundError(p + ': No such file or directory')

  def list(self):
    """
    List the contents of this directory.

    :returns: a dictionary containing a list of directories ('dirs') and a list
      of files ('files')
    """
    dirs = []
    files = []
    for c in self.children['results']:
      if type(c) != Inode:
        c = Inode(self.craedl, data=c)
      if c.type == 'd':
        dirs.append(c)
      else:
        files.append(c)
    return {'dirs': dirs, 'files': files}

  def upload(self, path, rescan=True, output=False, follow_symlinks=False):
    """
    Upload to the current directory. If uploading a directory, this generates a
    cache database in the `path` that is used to enhanceperformance of retries
    and synchronizations.

    :param path: the local path to the file/directory to be uploaded
    :type path: string
    :param rescan: whether to rescan the directories (defaults to True);
      ignores new children in already transferred directories if False
    :type rescan: boolean
    :param output: whether to print to STDOUT (defaults to False)
    :type output: boolean
    :param follow_symlinks: whether to follow symlinks (default False)
    :type follow_symlinks: boolean
    :returns: the uploaded Inode
    """
    if self.type != 'd':
      raise errors.Not_A_Directory_Error
    path = os.path.expanduser(path)
    if os.path.isfile(path):
      return self.upload_file(path, output)
    else:
      return self.upload_directory(path, rescan, follow_symlinks, output)

  def upload_file(self, file_path, output=False, accumulated_size=0):
    """
    Upload a new file contained within this directory.

    :param file_path: the path to the file to be uploaded on your computer
    :type file_path: string
    :param output: whether to print to STDOUT (defaults to False)
    :type output: boolean
    :param accumulated_size: the size that has accumulated prior to this
      upload (defaults to 0); this is entirely for output purposes
    :type accumulated_size: int
    :returns: a tuple with the updated instance of the current directory
      and the uploaded size
    """
    file_path = os.path.expanduser(file_path)
    if not os.path.isfile(file_path):
      print('Failure: %s is not a file.' % file_path)
      exit()

    if (os.path.basename(file_path)[0] == '.'
      or os.path.basename(file_path)[0] == '~'
    ):
      if output:
        print('UPLOAD FIL %s...skip' % (file_path), flush=True)
      return (self, 0)

    if output:
      print('UPLOAD FIL %s...' % (file_path), end='', flush=True)
    stream_data = False
    try:
      # check if file exists remotely
      f = None
      for c in self.children['results']:
        if type(c) != Inode:
          c = Inode(self.craedl, data=c)
        if c.type == 'f':
          if os.path.basename(file_path) == c.name:
            f = c
      if not f:
        f = self.get(os.path.basename(file_path))
      # check timestamps to determine whether we should stream this data
      local_mtime = os.path.getmtime(file_path)
      remote_mtime = (
        datetime.fromisoformat(f.date_modify) - DT1970
      ).total_seconds()
      if local_mtime > remote_mtime:
        stream_data = True
    except FileNotFoundError:
      stream_data = True
    if stream_data:
      data = {
        'name': file_path.split(os.sep)[-1],
        'parent': self.id,
        'type': 'f',
      }
      response_data = self.POST('/mech/%s/craedl/%d/inode/' % (
        self.craedl.slug,
        self.craedl.id,
      ), data, file_path)
      size = response_data['size']
      if output:
        print('uploaded %s (%s)' % (
          to_x_bytes(size),
          to_x_bytes(size + accumulated_size),
        ), flush=True)
      new_file = Inode(self.craedl, data=response_data)
      self.children['results'].append(new_file)
      return (new_file, size)
    else:
      if output:
        print('current (%s)' % to_x_bytes(accumulated_size), flush=True)
      return (self, 0)

  def upload_directory(
    self,
    directory_path,
    rescan=True,
    follow_symlinks=False,
    output=False
  ):
    """
    Upload a new directory contained within this directory. It generates a
    cache database in the `directory_path` that is used to enhance
    performance of retries and synchronizations.

    :param directory_path: the path to the directory to be uploaded on your
      computer
    :type directory_path: string
    :param follow_symlinks: whether to follow symlinks (default False)
    :type follow_symlinks: boolean
    :param rescan: whether to rescan the directories (defaults to True);
      ignores new children in already transferred directories if False
    :type rescan: boolean
    :param output: whether to print to STDOUT (defaults to False)
    :type output: boolean
    :returns: the updated instance of the current directory
    """
    accumulated_size = 0
    directory_path = os.path.expanduser(directory_path)
    if not os.path.isdir(directory_path):
      print('Failure: %s is not a directory.' % directory_path)
      exit()

    cache_path = directory_path + os.sep + '.craedl-upload-cache-%d.db' % (
      self.id
    )
    cache = sync_cache.Cache()
    cache.open(cache_path)

    # begin the recursive upload
    (self, this_size) = self.upload_directory_recurse(
      cache,
      directory_path,
      rescan,
      follow_symlinks,
      output,
      0
    )

    if cache:
      cache.close()

    return self

  def upload_directory_recurse(
    self,
    cache,
    directory_path,
    rescan,
    follow_symlinks,
    output,
    accumulated_size
  ):
    """
    The recursive function that does the uploading. There is little reason
    to call this directly; use :meth:`Directory.upload_directory` to start a
    directory upload.

    :param cache: the cache database
    :type cache: :class:`Cache`
    :param directory_path: the path to the directory on your computer that
      will contain this file's data
    :type directory_path: string
    :param rescan: whether to rescan the directories (defaults to True);
      ignores new children in already transferred directories if False
    :type rescan: boolean
    :param follow_symlinks: whether to follow symlinks
    :type follow_symlinks: boolean
    :param output: whether to print to STDOUT
    :type output: boolean
    :param accumulated_size: the amount of data that has been uploaded so
      far
    :type: int
    :returns: a tuple containing the updated instance of this directory and
      the amount of data that has been downloaded by this recursion level
      and its children
    """
    if directory_path[-1] == os.sep:
      directory_path = directory_path[:-1]
    this_size = 0

    children = sorted(os.scandir(directory_path), key=lambda d: d.path)

    directory_hash = hash_directory(directory_path)
    do_upload = True
    if cache.check(directory_path, directory_hash):
      # no need to upload
      do_upload = False
      if not rescan:
        # skip this recursion branch if user requests not to look for
        # changes to already uploaded children
        return (self, this_size)
    else:
      # record the directory hash
      cache.start(directory_path, directory_hash)

    # create new directory
    if output:
      print('CREATE DIR %s...' % (directory_path + os.sep), end='', flush=True)
    if (os.path.basename(directory_path)[0] == '.'
      or os.path.basename(directory_path)[0] == '~'
    ):
      if output:
        print('skip', flush=True)
      return (self, this_size)

    try:
      new_dir = self.get(os.path.basename(directory_path))
      if output:
        print('exists', flush=True)
    except FileNotFoundError:
      new_dir = self.create_directory(os.path.basename(directory_path))
      if output:
        print('created', flush=True)

    for child in children:
      if not follow_symlinks and child.is_symlink():
        # skip this symlink if ignoring symlinks
        if output:
          print('SKIP SMLNK %s...done' % (child.path + os.sep), flush=True)
      elif child.is_file():
        if do_upload:
          # upload file
          (new_file, new_size) = new_dir.upload_file(
            child.path,
            output,
            accumulated_size + this_size
          )
          this_size = this_size + new_size
        else:
          # safe to skip this file
          if output:
            print('SYNCHD FIL %s...skip (%s)' % (
              child.path,
              to_x_bytes(accumulated_size + this_size)
            ), flush=True)
      else:
        # recurse into this directory
        (new_file, new_size) = new_dir.upload_directory_recurse(
          cache,
          child.path,
          rescan=rescan,
          follow_symlinks=follow_symlinks,
          output=output,
          accumulated_size=accumulated_size + this_size
        )
        this_size = this_size + new_size

    # mark upload as completed in cache
    cache.finish(directory_path, directory_hash)

    return (new_dir, this_size)


class Profile(Auth):
  """
  A Craedl profile object. Get a Profile from the API by passing `id`. Get a
  Profile from an existing dictionary without network traffic by passing `data`.
  Get your profile by passing no arguments.
  """

  def __init__(self, id=None, data=None):
    super().__init__()
    if not data and not id:
      data = self.GET('/profile/whoami/')
    elif not data:
      data = self.GET('/profile/' + str(id) + '/')
    for k, v in data.items():
      setattr(self, k, v)
    self.craedls = self.get_craedls()

  def get_craedl(self, slug, id=None):
    """
    Get a particular Craedl.

    :param slug: the Craedl slug
    :type slug: string
    :param id: the Craedl id
    :type id: int
    :returns: A Craedl instance
    """
    host = None
    for root_craedl in self.craedls:
      if root_craedl.slug == slug:
        host = root_craedl.host
        break
    if not host:
      raise errors.Not_Found_Error

    return Craedl(host, slug, id)

  def get_craedls(self):
    """
    Get a list of craedls to which this profile belongs.

    :returns: a list of craedls
    """
    data = self.GET('/craedl/')
    root_craedls = []
    for root_craedl in data:
      craedl = Craedl(
        root_craedl['host']['domain'],
        root_craedl['slug'],
      )
      root_craedls.append(craedl)
    return root_craedls

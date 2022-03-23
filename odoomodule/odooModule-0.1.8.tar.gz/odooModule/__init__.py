import json, xmlrpc.client

__doc__ = "Module for getting/modifying data models in Odoo"

class Odoo():
  def __init__(self, url, database, username, password) -> None:
    self.url = url
    self.db = database
    self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
    self.username = username
    self.password = password
    self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
    self.uid = self.common.authenticate(self.db, self.username, self.password, {})

  def getObject(self, object, id):
    obj = self.models.execute_kw(self.db, self.uid, self.password, object, 'read', [id])
    return obj[0]

  def createObject(self, object, data):
    obj = self.models.execute_kw(self.db, self.uid, self.password, object, 'create', [data])
    print(obj)
    return obj

  def searchObject(self, object, filters=[]):
    res = self.models.execute_kw(self.db, self.uid, self.password, object, 'search', [filters])
    return res

  def getFields(self, object, required=False):
    res = self.models.execute_kw(self.db, self.uid, self.password, object, 'fields_get', [])
    x = {res[x]['string']: res[x] for x in res.keys()}
    if required:
      return {y: x[y] for y in x.keys() if x[y]['required']}
    return x

  def updateObject(self, object, id, fields):
    res = self.models.execute_kw(self.db, self.uid, self.password, object, 'write', [[id], fields])
    return res
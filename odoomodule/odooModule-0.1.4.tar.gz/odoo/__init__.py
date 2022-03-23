import json, xmlrpc.client

class Odoo():
  def __init__(self) -> None:
    self.url = 'https://little-unicorn.odoo.com'
    self.db = 'little-unicorn'
    self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))
    self.username = 'bbrandley@littleunicorn.com'
    self.password = "4Od0024!"
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
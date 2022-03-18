import requests, json
import vytools.utils as utils
import vytools.printer as printer

def _checkupdate(datatype, item, check_only, url, headers):
  item['check_only'] = check_only
  res = requests.post(url+'/update_'+datatype, json=item, headers=headers)
  result = res.json()
  if not result.get('processed',False):
    return json.dumps(result)
  elif check_only:
    if result.get('confirm',False):
      return result
    elif result.get('nochange',False):
      return '{} is the same locally as at {}'.format(datatype,url)    
  return result

def _check(datatype, type_name, url, uname, token, items):
  if not utils.ok_dependency_loading('upload', type_name, items):
    return False
  headers = {'token':token, 'username':uname}
  try:
    item = items[type_name]
    result = _checkupdate(datatype, item, True, url, headers)
    if type(result) == str:
      if 'is the same locally' in result:
        printer.print_success('{d} "{n}" {e}'.format(d=datatype, n=type_name, e=result))
      else:
        printer.print_info('{d} "{n}" not updated: {e}'.format(d=datatype, n=type_name, e=result))
      return False
    return result 
  except Exception as exc:
    printer.print_fail('Failed upload of {d} "{n}": {e}'.format(d=datatype, n=type_name, e=exc))
  return False

def _update(datatype, type_name, url, uname, token, onsuccess, items):
  if not utils.ok_dependency_loading('upload', type_name, items):
    return False

  headers = {'token':token, 'username':uname}
  success = True
  reason = ''
  try:
    item = items[type_name]
    result = _checkupdate(datatype, item, False, url, headers)
    if type(result) == str:
      printer.print_info('{} "{}" not updated: {}'.format(datatype, type_name, result))
      return False
    else:
      success = onsuccess(item, url, headers, result)
  except Exception as exc:
    reason = exc
    success = False

  if not success:
    printer.print_fail('Failed upload of {} "{}"-- {}'.format(datatype, type_name, reason))
  else:
    printer.print_success('Finished uploading {} "{}"'.format(datatype, type_name))
  return success

def upload(datatype, lst, url, uname, token, check_first, update_list, onsuccess, items):
  uploadlst = lst if lst else items
  uploadlst = utils.sort([tn for tn in items if tn.startswith(datatype+':')], items)
  if check_first:
    updatable_list = []
    for type_name in uploadlst:
      if type_name.startswith(datatype):
        results = _check(datatype, type_name, url, uname, token, items)
        if results != False:
          updatable_list.append({'type_name':type_name,'results':results})
    for it in updatable_list:
      printer.print_info('{} "{}" is different locally than at {} and can be uploaded'.format(datatype, it['type_name'],url))
    
    if len(updatable_list)>0 and input('Would you like to upload all these without seeing the diff of each? (y/n) (n means you will be shown individual diffs)').lower() == 'y':
      uploadlst = [it['type_name'] for it in updatable_list]
    else:
      uploadlst = []
      while updatable_list:
        type_name = updatable_list[0]['type_name']
        question = updatable_list[0]['results'].get('confirm',None)
        printer.print_info('{} "{}" is different locally than at {} and can be uploaded'.format(datatype,type_name,url))
        if question and input(question).lower() == 'y' and _update(datatype, type_name, url, uname, token, onsuccess, items):
            update_list.append(type_name)
        updatable_list.pop(0)

  for type_name in uploadlst:
    if _update(datatype, type_name, url, uname, token, onsuccess, items):
      update_list.append(type_name)

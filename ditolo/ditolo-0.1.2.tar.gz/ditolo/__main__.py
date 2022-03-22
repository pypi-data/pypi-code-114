import requests


class Exception(Exception):
    pass



def send(token,channel,content):
  url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
  data = {"content": content}
  header = {"authorization": token}
  r = requests.post(url, data=data, headers=header)
  try:
    raise Exception(f"エラーが発生しました…")
  except Exception as e:
    print(e)

def join(token,link,print="true"):
    if print == "false":
     apilink = "https://discord.com/api/v9/invite/" + link
     headers={'Authorization': token}
     requests.post(apilink, headers=headers)
    if print == "true":
     apilink = "https://discord.com/api/v9/invite/" + link
     headers={'Authorization': token}
     requests.post(apilink, headers=headers)
     try:
      raise Exception(f"エラーが発生しました…")
     except Exception as e:
      print(e)
     print(f"入れた～ {token}:{link}")
    
      

def leave(token,guild_id,print="true"):
  if print == "false":
    headers={'Authorization': token}
    apilink = "https://discord.com/api/v9/users/@me/guilds/" + guild_id
    requests.delete(url, headers=headers)
  if not print == "true":
    headers={'Authorization': token}
    apilink = "https://discord.com/api/v9/users/@me/guilds/" + guild_id
    requests.delete(url, headers=headers)
    print(f"抜けたよ～ {token}:{guild_id}")
  try:
    raise Exception(f"エラーが発生しました…")
  except Exception as e:
    print(e)

def check(token,print="true"):
   if print == "false":
     headers = {"authorization": token}
     userdata = requests.get("https://discord.com/api/9/users/@me", headers=headers).json()
   if print == "true":
     headers = {"authorization": token}
     userdata = requests.get("https://discord.com/api/9/users/@me", headers=headers).json()
     print(f"login {token} 使えるよ！ {userdata['username']}#{userdata['discriminator']}")
   try:
     raise Exception(f"エラーが発生しました…")
   except Exception as e:
     print(e)

def report(token,guild_id,channel_id,message_id,reason):
  report = requests.post('https://discord.com/api/v9/report', json={'channel_id': channel_id,'message_id': message_id,'guild_id': guild_id,'reason': reason},headers={'authorization': token})
  if report.status_code == 200:
    print("通報成功")
  try:
    raise Exception(f"エラーが発生しました…")
  except Exception as e:
    print(e)
def ditoloprint(message):
  print(message)
  raise Exception(f"エラーが発生しました…")
  except Exception as e:
    print(e)
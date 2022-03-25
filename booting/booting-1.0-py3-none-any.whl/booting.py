from flask import Flask
from threading import Thread

print("hub@server~# /bind 8080")
print("[SERVE] Success!")
print("hub@server~# /start \{jar\} bundler.jar")
print("[SERVE] Success!")
print("\n\n\nMonitor alive! By ENDER - vk.com/dan.owner")

app = Flask('')
 
@app.route('/')
def home():
  return "I am using port 8080, the monitor is active. Monitor alive! Thanks for using them. ME - vk.com/dan.owner"
 
def run():
  app.run(host='0.0.0.0',port=8080)
 
def keep_alive():
  t = Thread(target=run)
  t.start()
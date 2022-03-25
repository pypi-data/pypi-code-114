
import urllib.parse
import urllib.request
import urllib.error
import ssl
import json
import base64
import binascii
from .base import ApiException, ApiAuthenticationException

class AuthBase:
	def __init__(self):
		self._oauthTokenUrlPath  = "/oauth2/token" 
		self._oauthRevokeUrlPath = "/oauth2/revoke" 

	def init (self, host, tls, ssl_verify, ssl_ca_options, callback=None):
		self._host = host
		self._tls = tls 
		self._ssl_verify = ssl_verify
		self._ssl_ca_options = ssl_ca_options
		self._callback = callback # called on every login

	def __del__(self):
		pass

class AuthClientCredential(AuthBase):

	def __init__(self, clientId, clientSecret):
		AuthBase.__init__(self)
		self._clientId = clientId
		self._clientSecret = clientSecret
		self._accessToken = "" 
		self._tokenType = ""
		
	def __del__(self):
		try:
			self._logout()
		except:
			#ingore all errors; and do not print them
			pass

			
	def getHeader(self):
		if self._accessToken == "":
			self._login() 
		if self._accessToken != "":
			return {'Authorization': self._tokenType + " " + self._accessToken}
		return {}

	def _sendRequest(self, url, data, headers, method):
		resp = ""	# json http response as dict
		err = None	# exception
		try:
			if self._tls:
				context = ssl.create_default_context(**self._ssl_ca_options)
				if not self._ssl_verify:
					context.check_hostname = False
					context.verify_mode = ssl.CERT_NONE
			else:
				context = None
			conn = urllib.request.Request(url, data=data, headers=headers, method=method)
			res = urllib.request.urlopen(conn, context=context)
			content = res.read().decode("utf-8")
			#print(8*"-")
			#print(content)
			if content:
				resp = json.loads(content)
		except urllib.error.HTTPError as e:
			if e.code == 502:
				raise ApiException ("HTTP Error 502: Management Server is not running")

			content = e.read().decode("utf-8")
			#print(16*"-" + str(e.code))
			#print(content)
			if content:
				resp = json.loads(content)	#when this fails, it might be an ssl error...
				e.msg = resp["error"] + ": " + resp["error_description"]
			err = e

		finally:
			if err:
				if err.code == 400:
					raise ApiAuthenticationException("HTTP Error 400: "+err.msg)
				else:
					raise err
		return resp

	def _login(self, verbose=False, show_requests=False):
		headers = {
			'Accept'		: 'application/json,UTF-8',
			'Content-Type'	: 'application/x-www-form-urlencoded',
		}
		url = self._host + self._oauthTokenUrlPath
		data = f"client_id={urllib.parse.quote(self._clientId)}"
		data += f"&client_secret={urllib.parse.quote(self._clientSecret)}"
		data +=	"&grant_type=client_credentials"
		data = bytes(data, encoding="utf-8")

		if verbose:
			print ("Login ------------")
		if verbose or show_requests:
			print ("POST " + url)
		if verbose:
			print ("\t"+ str(headers))
			print ("\t"+ str(data)) # this prints credentials

		resp = self._sendRequest(url, data, headers, "POST")
		self._accessToken = resp.get("access_token", "")
		self._tokenType = resp.get("token_type", "")

		if verbose:
			print(resp)
		if self._callback:
			self._callback()

	def _logout(self):
		if not self._accessToken:
			return
		#print("Logout -----")
		authorization_b64 = base64.b64encode("{}:{}".format(self._clientId, self._clientSecret).encode()).decode('ascii')
		headers = {
			'Accept'		: 'application/json,UTF-8',
			'Content-Type'	: 'application/x-www-form-urlencoded',
			'Authorization': "Basic " + authorization_b64 
		}
		url = self._host + self._oauthRevokeUrlPath
		data = f"token={urllib.parse.quote(self._accessToken)}"
		data += "&token_type_hint=access_token"
		data = bytes(data, encoding="utf-8")
		#print("POST "+url)
		#print ("\t"+ str(headers))
		#print ("\t"+ str(data)) # this prints credentials
		resp = self._sendRequest(url, data, headers, "POST")
		#if resp:
		#	print(resp)

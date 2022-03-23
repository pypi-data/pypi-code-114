class NoCallBack:
	pass

class ResponseError:
	def __init__(self, status_code:int, response, expected_status_code:int=200):
		self.status_code = status_code
		self.response = response
		self.expected_status_code = expected_status_code
	
	def __str__(self) -> str:
		return f"The server responded with a {self.status_code} status code." + ("" if self.expected_status_code == 200 else f" Expected {self.expected_status_code}")
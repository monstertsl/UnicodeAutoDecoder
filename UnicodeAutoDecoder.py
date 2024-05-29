# coding=utf-8
from burp import IBurpExtender, IHttpListener
import re

class BurpExtender(IBurpExtender, IHttpListener):

	def registerExtenderCallbacks(self, callbacks):
		self._callbacks = callbacks
		self._helpers = callbacks.getHelpers()
		callbacks.setExtensionName("UnicodeAutoDecoder")
		callbacks.registerHttpListener(self)
		callbacks.printOutput("UnicodeAutoDecoder By monstertsl")
		callbacks.printOutput("Auto converts Unicode encodings in Proxy, Repeater, and Intruder into easy-to-read natural language")
		callbacks.printOutput("GitHub: https://github.com/monstertsl/UnicodeAutoDecoder")
		callbacks.printOutput("Refer to the following two authors create project")
		callbacks.printOutput("GitHub: https://github.com/amir-h-fallahi/UnicodeDecoder")
		callbacks.printOutput("GitHub: https://github.com/no001ce/N-DecodeAllUnicode")


	def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
		toolName = self._callbacks.getToolName(toolFlag)
		if toolName == "Repeater" or toolName == "Proxy" or toolName == "Intruder":
			if not messageIsRequest:
				is_response_json = False

				response = messageInfo.getResponse()
				analyzedResponse = self._helpers.analyzeResponse(response)
				response_headers = analyzedResponse.getHeaders()

				for header in response_headers:
					if header.lower().startswith("content-type: application/json"):
						is_response_json = True
				
				if is_response_json:
					body = response[analyzedResponse.getBodyOffset():]
					bodyStr = body.tostring()
					u_escape = re.findall(r'\\u[a-z0-9A-Z]{4}', bodyStr)
					#u_escape = list(set(u_escape))
					if u_escape:
						for i in u_escape:
							decodeUnicodes = i.decode('unicode_escape').encode('utf8')
							bodyStr = bodyStr.replace(i, decodeUnicodes)
						finalModifiedBody = self._helpers.stringToBytes(bodyStr)
						messageInfo.setResponse(self._helpers.buildHttpMessage(response_headers, finalModifiedBody))

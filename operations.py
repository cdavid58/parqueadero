import requests, json

class Operation:

	def Operations_Schedule(self,plate,helmet,note):
		url = "http://127.0.0.1:9090/schedule/Operations_Schedule/"
		payload = json.dumps({
		  "plate": plate,
		  "helmet":helmet,
		  'note':note,
		  "cart": 1,
		  "pk_user": 1,
		  "parking_lot": "Parqueadero"
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		print(json.loads(response.text))
		return json.loads(response.text)['result']

	def Get_List_Schedule(self):
		url = "http://127.0.0.1:9090/schedule/GET_LIST/"
		payload = ""
		headers = {}
		response = requests.request("GET", url, headers=headers, data=payload)
		print(json.loads(response.text))
		return json.loads(response.text)

	def Get_Last_Record(self,plate):
		print("PLACA LAST RECORD",plate)
		url = "http://127.0.0.1:9090/schedule/Get_Last_Record/"
		payload = {"plate":plate}
		headers = {}
		response = requests.request("GET", url, headers=headers, data=payload)
		print(json.loads(response.text))
		return json.loads(response.text)

	def Get_History(self):
		url = "http://127.0.0.1:9090/history/Get_History/"
		response = requests.request("GET", url, headers={}, data={})
		print(json.loads(response.text))
		return json.loads(response.text)


class Operations_User:
	def Login(self,user_name,psswd):
		url = "http://127.0.0.1:9090/user/Login/"
		payload = json.dumps({
		  "user_name": user_name,
		  "psswd": psswd
		})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("POST", url, headers=headers, data=payload)
		print(response.text)
		return json.loads(response.text)['result']
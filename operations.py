import requests, json

class Operation:

	def Operations_Schedule(self,plate,helmet,note,user):
		url = "http://127.0.0.1:9090/schedule/Operations_Schedule/"
		payload = json.dumps({
		  "plate": plate,
		  "helmet":helmet,
		  'note':note,
		  "cart": 1,
		  "pk_user": user,
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
		response = requests.request("GET", url, headers={}, data={})
		return json.loads(response.text)

	def Get_Last_Record(self,plate):
		print("PLACA LAST RECORD",plate)
		url = "http://127.0.0.1:9090/schedule/Get_Last_Record/"
		payload = {"plate":plate}
		response = requests.request("GET", url, headers={}, data=payload)
		return json.loads(response.text)

	def Get_History(self):
		url = "http://127.0.0.1:9090/history/Get_History/"
		response = requests.request("GET", url, headers={}, data={})
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
		return json.loads(response.text)

	def Create_User(self,data,parking):
		url = "http://127.0.0.1:9090/user/Create_User/"
		payload = json.dumps({
		  "user_name": data['user_name'],
		  "psswd": data['psswd'],
		  "type_user": data['type_user'],
		  "parking_lot" : parking
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("POST", url, headers=headers, data=payload)
		return json.loads(response.text)['result']

	def List_User(self):
		url = "http://127.0.0.1:9090/user/List_User/"
		response = requests.request("GET", url, headers={}, data={})
		return json.loads(response.text)

	def Get_User(self,pk):
		url = "http://127.0.0.1:9090/user/Get_User/"
		payload = json.dumps({"pk": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("GET", url, headers=headers, data=payload)
		return json.loads(response.text)

	def Edit_User(self,data,pk):
		url = "http://127.0.0.1:9090/user/Edit_User/"
		payload = json.dumps({
		  "pk_user": pk,
		  "user_name": data['user_name'],
		  "psswd": data['psswd'],
		  "type_user": data['type_user']
		})
		headers = {
		  'Content-Type': 'application/json'
		}
		response = requests.request("PUT", url, headers=headers, data=payload)
		return json.loads(response.text)['result']

	def Delete_User(self,pk):
		url = "http://127.0.0.1:9090/user/Delete_User/"
		payload = json.dumps({"pk_user": pk})
		headers = {'Content-Type': 'application/json'}
		response = requests.request("DELETE", url, headers=headers, data=payload)
		print(json.loads(response.text))
		return json.loads(response.text)['result']



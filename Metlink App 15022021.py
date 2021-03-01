import requests
import json
import tkinter as tk

#Pete's dairy bus stop id = 7235

#Api url and headers
url = "https://api.opendata.metlink.org.nz/v1/gtfs/routes?stop_id=7235"
h = {
    'accept': 'application/json',
    'x-api-key':'1KXjoTHz7P7kipBX0aiax3qQnlX3Saut4Z4EyOZN'
}

urlrt = 'https://api.opendata.metlink.org.nz/v1/gtfs-rt/vehiclepositions'
hh = {
    'accept': 'application/json',
    'x-api-key':'1KXjoTHz7P7kipBX0aiax3qQnlX3Saut4Z4EyOZN',
    'Accept':'accept/x-protobuf'
}

#Api request and json parse
req = requests.get(url, headers=h)
parsed = req.json()

reqrt = requests.get(urlrt, headers=hh)
parsedrt = reqrt.json()
#Returns the name of the bus
def busName(name):
    for i in range(6):
        if parsed[i]["route_short_name"] == str(name):
            return parsed[i]["route_short_name"]
#Returns the route id of the bus 
def routeId(name):
    for i in range(6):
        if parsed[i]["route_short_name"] == str(name):
            return parsed[i]["route_id"]
        
#Returns description of the route provided by Metlink
def routeDesc(name):
    for i in range(6):
        if parsed[i]["route_short_name"] == str(name):
            return parsed[i]["route_desc"]

#Returns the id of the bus used by Metlink
def getBusId(name):
    for i in range(len(parsed)):
        if parsed[i]["route_short_name"] == str(name):
            return parsed[i]['id']
#Prints the API in pretty format
def printPrettyJson(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

#Testing functions
printPrettyJson(parsedrt)
printPrettyJson(parsed)
#Tkinter
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.createField()
        self.createWidget()
    def createWidget(self):
        self.yes = tk.Button(self, text="YES", fg="green", command=item.returnBusData)
        self.yes.pack()
    def createField(self):
        self.entry = tk.Entry()
        self.entry.pack()

        self.contents = tk.StringVar()
        self.contents.set('Enter a bus: (e.g 18e, 2, 31x)')

        self.entry["textvariable"] = self.contents
        global item
        item = self

    def returnBusData(self):    
        self.entry["textvariable"] = self.contents
        bus = self.contents.get()
        print("Bus:", busName(bus), "Route Id:", routeId(bus), "Route Description:", routeDesc(bus), "Bus ID:", getBusId(bus))
        self.contents.set('Enter a bus: (e.g 18e, 2, 31x)')

root = tk.Tk()
myapp = App(root)
myapp.master.title("Metlink Bus Services")
myapp.master.maxsize(400,400)
myapp.mainloop()

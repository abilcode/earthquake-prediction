import requests
import json
import pandas as pd

def earthquake_querry(f, alertlevel):
    paramss = {"format": "csv", "starttime": "2000-01-01", "endtime": "2022-12-31", "alertlevel":alertlevel,'limit':2000}
               #"minlongitude":93.516, "maxlongitude":141.416, "minlatitude":-11.867, "maxlatitude":5.966}
    data = requests.get(f, params = paramss)
    #data = json.loads(data.text)
    return data

if __name__ == "__main__":
   color = ['green','yellow','orange','red']
   for c in color:
    f = r"https://earthquake.usgs.gov/fdsnws/event/1/query?"
    a = earthquake_querry(f,c)
    with open(f'world_data_{c}.txt', 'w') as file:
        file.write(a.text)
        print(f"Querry {c} Selesai")
   
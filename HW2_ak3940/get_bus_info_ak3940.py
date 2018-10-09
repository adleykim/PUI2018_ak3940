import os
import sys
import json
import pandas as pd
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python show_bus_locations_ak3940.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

MTAkey = sys.argv[1]
busLine = sys.argv[2]
fileName = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(MTAkey, busLine)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

lat = []
lon = []
stopName = []
stopStat = []

for i in range(len(buses)):
    lt = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    ln = buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    if len(buses[i]['MonitoredVehicleJourney']['OnwardCalls']) > 0:
        sn = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        ss = buses[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    else:
        sn = "N/A"
        ss = "N/A"
    lat.append(lt)
    lon.append(ln)
    stopName.append(sn)
    stopStat.append(ss)

df = {'Latitude': lat, 'Longitude': lon, 'Stop Name': stopName, 'Stop Status': stopStat}
df = pd.DataFrame(data=df)

df.to_csv(fileName)

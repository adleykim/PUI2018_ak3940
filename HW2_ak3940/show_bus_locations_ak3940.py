import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_locations_ak3940.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

MTAkey = sys.argv[1]
busLine = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(MTAkey, busLine)

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


print("Bus Line: ", busLine)
print("Number of Active Buses: ", len(buses))
for i in range(len(buses)):
    print("Bus {} is at latitude {} and longitude {}".format(i + 1, buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], buses[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))

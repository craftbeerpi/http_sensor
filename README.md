# HTTP Sensor Endpoint for CraftBeerPi

With this sensor other system can push sensor data to CraftBeerPi via HTTP GET request.

## Installation

Download and Install this Plugin via the CraftBeerPi user interface.

## Sensor Confiuration

Add a new sensor to your CraftBeerPi. The key properies defines the sensor name in the HTTP Endpoint.

The other system need to push the data to the following endpoint of your CraftBeerPi server.

* key = sensor key - alpha nummeric name without blanks
* value = the new sensor value. Internaly handled as string

```
http://<RaspberryPi-IP-Addresse>:5000/api/httpsensor/<key>/<value>
```

down vote
accepted
Try putting your HTML snippet inside an ```HTML block like this:

Example URL:

```
http://192.168.0.19:5000/api/httpsensor/sensor1/10
```

## Hints

It's not recommanded to push new data every millsecond. Normaly extenal sensor should push data every 5-10 seconds.


#!/usr/bin/env python

import time

from homie.device_dimmer import Device_Dimmer

mqtt_settings = {
    'MQTT_BROKER' : 'QueenMQTT',
    'MQTT_PORT' : 1883,
}


dimmers = []

class My_Dimmer(Device_Dimmer):

    def set_dimmer(self,percent):
        print('Received MQTT message to set the dimmer to {}. Must replace this method'.format(percent))
        

try:

    for x in range(200):
        dimmer = My_Dimmer(name = 'Test Dimmer {}'.format(x),mqtt_settings=mqtt_settings)
        dimmers.append (dimmer)
    
    while True:
        time.sleep(5)
        for dimmer in dimmers:
            dimmer.update_dimmer(50)
        time.sleep(5)
        for dimmer in dimmers:
            dimmer.update_dimmer(100)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")        

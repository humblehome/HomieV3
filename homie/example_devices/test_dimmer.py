#!/usr/bin/env python

import time

from homie.device_dimmer import Device_Dimmer

mqtt_settings = {
    'MQTT_BROKER' : 'QueenMQTT',
    'MQTT_PORT' : 1883,
}


class My_Dimmer(Device_Dimmer):

    def set_dimmer(self,topic,payload):
        print('Received MQTT message to set the dimmer to {}. Must replace this method'.format(payload))
        

try:

    dimmer = My_Dimmer(name = 'Test Dimmer',mqtt_settings=mqtt_settings)
    
    while True:
        time.sleep(5)
        dimmer.update_dimmer(50)
        time.sleep(5)
        dimmer.update_dimmer(100)

except (KeyboardInterrupt, SystemExit):
    print("Quitting.")        
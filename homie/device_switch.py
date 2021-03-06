#!/usr/bin/env python

from homie.device_base import Device_Base
from homie.node.node_switch import Node_Switch
import logging

logger = logging.getLogger(__name__)

class Device_Switch(Device_Base):

    def __init__(self, device_id=None, name=None, homie_settings=None, mqtt_settings=None):
        super().__init__ (device_id, name, homie_settings, mqtt_settings)

        self.add_node(Node_Switch(self,id='switch',set_switch=lambda onoff: self.set_switch(onoff)))

        self.start()

    def update_switch(self,onoff): #sends updates to clients
        self.get_node('switch').update_switch(onoff)
        logging.info ('Switch Update {}'.format(onoff))

    def set_switch(self,onoff):#received commands from clients
        logging.info ('Switch Set {}'.format(onoff))

        


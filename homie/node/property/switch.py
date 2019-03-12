from .property_enum import Property_Enum

class Switch(Property_Enum):

    def __init__(self, id='switch', name = 'Switch', settable = True, retained = True, qos=1, unit = None, data_type= 'enum', data_format = 'ON,OFF', value = None, set_value=None):
        
        super().__init__(id,name,settable,retained,qos,unit,data_type,data_format,value,set_value)

 


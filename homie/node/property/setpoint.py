from .property_float import Property_Float

class Setpoint(Property_Float):

    def __init__(self, id=None, name=None, settable=True, retained=True, qos=1, unit=None, data_type=None, data_format=None, value=None, set_value=None):
        
        super().__init__(id,name,settable,retained,qos,unit,data_type,data_format,value,set_value)

 

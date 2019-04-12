from .property_base import Property_Base
import logging

logger = logging.getLogger(__name__)

class Property_Integer(Property_Base):

    def __init__(self, node, id, name, settable=True, retained=True, qos=1, unit=None, data_type='integer', data_format=None, value=None, set_value=None):
        super().__init__(node,id,name,settable,retained,qos,unit,'integer',data_format,value,set_value)

        if data_format:
            range = data_format.split(':')
            self.low_value = int(range[0])
            self.high_value = int(range[1])
        else:
            self.low_value = None
            self.high_value = None

    def validate_value(self, value):
        valid = True

        if self.low_value is not None and value < self.low_value:
            valid = False
        if self.high_value is not None and value > self.high_value:
            valid = False

        return valid

    def message_handler(self,topic,payload):
        try: 
            value = int(payload)
            if self.validate_value(value):
                super().message_handler(topic,payload)
            else:
                logger.warning ('Payload integer value out of range for property for message {}, payload is {}, low value {}. high value {}'.format(topic,payload,self.low_value,self.high_value))
        except:
            logger.warning ('Unable to convert payload to integer property for message {}, payload is {}'.format(topic,payload))

 
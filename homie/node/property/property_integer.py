import logging
from .property_base import Property_Base

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Property_Integer(Property_Base):

    def __init__(self, id, name, settable=True, retained=True, qos=1, unit=None, data_type='integer', data_format=None, value=None, set_value=None):
        super().__init__(id,name,settable,retained,qos,unit,'integer',data_format,value,set_value)

        if data_format:
            range = data_format.split(':')
            self.low_value = int(range[0])
            self.high_value = int(range[1])
        else:
            self.low_value = None
            self.high_value = None

    def message_handler(self,topic,payload):
        try: 
            value = int(payload)
            valid = True

            if self.value is not None and value < self.low_value:
                valid = False
            if self.high_value is not None and value > self.high_value:
                valid = False

            if valid:
                super().message_handler(topic,payload)
            else:
                logger.warning ('Payload integer value out of range for property for message {}, payload is {}, low value {}. high value {}'.format(topic,payload,self.low_value,self.high_value))
        except:
            logger.warning ('Unable to convert payload to integer property for message {}, payload is {}'.format(topic,payload))

 
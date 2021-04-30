import blynklib
import time
import io
import picamera

BLYNK_AUTH = 'Y_3drVlwkx1gaWTjb54wCD4ERZSFBf2t'

blynk = blynklib.Blynk(BLYNK_AUTH)

CONNECT_PRINT_MSG = '[CONNECT_EVENT]'
DISCONNECT_PRINT_MSG = '[DISCONNECT_EVENT]'
WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
READ_EVENT_PRINT_MSG = "[READ_EVENT_PRINT_MSG] Pin: V{} Value {}"

@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    #capture()
    
@blynk.handle_event("disconnect")
def disconnect_handler():
    print(DISCONNECT_PRINT_MSG)
    print('Sleeping 4 sec in disconnect handler...')
    time.sleep(4)

@blynk.handle_event('write V1')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin,value))
    if(value != 0):
        blynk.notify("Someone is at the Door!")

    
###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
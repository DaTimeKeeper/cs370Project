import blynklib
from time import sleep
from picamera import PiCamera

BLYNK_AUTH = 'Y_3drVlwkx1gaWTjb54wCD4ERZSFBf2t'
def capture():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')

blynk = blynklib.Blynk(BLYNK_AUTH)

CONNECT_PRINT_MSG = '[CONNECT_EVENT]'
DISCONNECT_PRINT_MSG = '[DISCONNECT_EVENT]'

@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    blynk.notify("I an connected")
    capture()



@blynk.handle_event("disconnect")
def disconnect_handler():
    print(DISCONNECT_PRINT_MSG)
    print('Sleeping 4 sec in disconnect handler...')
    time.sleep(4)


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
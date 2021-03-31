import blynklib
import time

BLYNK_AUTH = 'wcQdKcosK1kE12NUpj9wBesbQh9i-ILY'

blynk = blynklib.Blynk(BLYNK_AUTH)

CONNECT_PRINT_MSG = '[CONNECT_EVENT]'
DISCONNECT_PRINT_MSG = '[DISCONNECT_EVENT]'


@blynk.handle_event("connect")
def connect_handler():
    print(CONNECT_PRINT_MSG)
    print('Sleeping 2 sec in connect handler...')
    time.sleep(2)
    blynk.disconnect()


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
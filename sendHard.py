from pynput.keyboard import Controller
import pynput,time
keyboard = Controller()
def hardSend(msg):
    for i in msg:
        keyboard.type(i)
        time.sleep(0.0001)
    keyboard.press(pynput.keyboard.Key.ctrl_l)
    keyboard.press(pynput.keyboard.Key.enter)
    time.sleep(0.01)
    keyboard.release(pynput.keyboard.Key.enter)
    keyboard.release(pynput.keyboard.Key.ctrl_l)


# hardSend("1234")

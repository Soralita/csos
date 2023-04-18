import threading
import time

from pynput import keyboard


scanstr = ""
auth_code=""

def on_press(key):
    global scanstr,auth_code
    try:
        try:
            if str.isnumeric(key.char):
                scanstr+=key.char
            else:
                scanstr=""
        except TypeError:
            pass
    except AttributeError:
        # print('special key {0} pressed'.format(key))

        if(key==keyboard.Key.enter):
            # print("输入了enter")
            if( len(scanstr)>=18):
                auth_code=scanstr

            scanstr=""


    # print(key,type(key))


def get_auth_code():

    return auth_code

def on_release():
    if get_auth_code()!="":
        return



def listen_keyboard():
    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()

    # 创建新的线程，监测 auth_code 的值
    def check_auth_code():
        global auth_code
        timecount=0
        while True:
            if auth_code != "":
                # print("Auth code:",auth_code)
                print(auth_code)
                listener.stop()
                break

            time.sleep(0.5)  # 休眠 1 秒钟

            timecount+=1
            if(timecount>=60):
                listener.stop()
                break
        listener.stop()

    t = threading.Thread(target=check_auth_code)
    t.start()
    t.join()
    listener.join()

    return auth_code


if __name__=="__main__":
    listen_keyboard()
    # with keyboard.Listener(on_press=on_press) as lsn:
    #     lsn.join()


from pywinauto import mouse
from pywinauto.application import Application
from selenium.webdriver.common.by import By
from pywinauto.keyboard import send_keys
from time import sleep
import pywinauto
# 双击图标
mouse.double_click(button="left",coords=(195,206))
sleep(2)
# 点击ok
mouse.click(button="left",coords=(1570,850))
sleep(2)
def connect_GProgrammer():
    # 点击连接
    mouse.click(button="left",coords=(1547,398))
    sleep(2)
    #点击add
    mouse.click(button="left",coords=(649,850))
    #
    # app = pywinauto.Desktop()
    # dlg = app["打开"]
    sleep(2)
    # 选中文件
    mouse.press(coords=(888,423))
    mouse.release(coords=(888,300))
    #提交文件确认
    mouse.click(button="left",coords=(1424,684))
    #选中文件2
    mouse.click(button="left",coords=(727,657))
    # 点击startup
    mouse.click(button="left",coords=(811,847))
    #点击commit
    mouse.click(button="left",coords=(1541,839))
    sleep(2)
    #点击ok
    send_keys("{VK_ESCAPE}")
    mouse.click(button="left", coords=(930, 500))
    send_keys("{VK_ESCAPE}")


if __name__ == '__main__':
    while True:
        connect_GProgrammer()
        sleep(50)
        mouse.click(button="left", coords=(966, 488))
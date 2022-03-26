import datetime
import time
import requests
import logging

from decimal import Decimal
from appium import webdriver
from selenium.webdriver.common.by import By
from django.core.management import BaseCommand


class WxAuto(object):
    """
    adb connect 127.0.0.1:5555
    """
    args = ""

    def login(self):
        # 使用微信号和QQ登录
        self.driver.find_element(By.ID, "com.tencent.mm:id/d5u").click()
        time.sleep(3)

        # 输入微信号和登录密码
        username_input = self.driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText")
        username_input.send_keys("微信ID")

        password_input = self.driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText")
        password_input.send_keys("微信密码")

        # 点击登录
        self.driver.find_element(By.ID, "com.tencent.mm:id/d5n").click()
        # 等待微信导入通讯录数据 根据实际情况延长时间
        time.sleep(5)

    def add_user(self, wx_id):
        # 输入要搜索的微信号
        print("输入要添加的微信号:", wx_id)
        search_wx_input = self.driver.find_element(By.ID, "com.tencent.mm:id/bhn")
        search_wx_input.clear()
        search_wx_input.send_keys(wx_id)
        time.sleep(1)

        print("点击搜索微信号")
        self.driver.find_element(By.ID, "com.tencent.mm:id/ga1").click()
        time.sleep(3)

        # 检查微信号是否存在
        try:
            if self.driver.find_element(By.ID, "com.tencent.mm:id/aze").text == '该用户不存在':
                print("该用户不存在")
                return False
        except Exception as e:
            pass

        print("点击添加到通讯录")
        self.driver.find_element(By.ID, "com.tencent.mm:id/g6f").click()
        time.sleep(3)

        # 输入添加好友申请理由
        print("输入添加好友申请理由")
        add_friend_reason = self.driver.find_element(By.ID, "com.tencent.mm:id/f5e")
        add_friend_reason.clear()
        add_friend_reason.send_keys("杭州境界软件")

        print("添加添加通讯录按钮")
        self.driver.find_element(By.ID, "com.tencent.mm:id/ch").click()
        time.sleep(3)

        try:
            print("wx:", self.driver.find_element(By.XPATH,
                                                  "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.View[1]").text)
        except Exception as e:
            print("获取微信号出错")
            pass

        # 返回主页
        self.driver.find_element(By.ID, "com.tencent.mm:id/dn").click()
        time.sleep(1)

        return True

    def main(self):
        desired_caps = {
            "platformName": "Android",  # 操作系统
            "deviceName": "emulator-5554",  # 设备 ID
            "platformVersion": "6.0.1",  # 设备版本号
            "appPackage": "com.tencent.mm",  # app 包名
            "appActivity": ".ui.LauncherUI",  # app 启动时主 Activity
            'noReset': True,  # 是否保留 session 信息，可以避免重新登录
            'unicodeKeyboard': True,  # 使用 unicodeKeyboard 的编码方式来发送字符串
            'resetKeyboard': True  # 将键盘给隐藏起来
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(15)

        # 如果账户已经登录，可以注释登录步骤
        # self.login()

        print("点击右上角+按钮")
        self.driver.find_element(By.ID, "com.tencent.mm:id/ef9").click()
        time.sleep(1)

        print("点击添加朋友")
        self.driver.find_element(By.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
        time.sleep(3)

        print("点击微信搜索输入框")
        self.driver.find_element(By.ID, "com.tencent.mm:id/fcn").click()
        time.sleep(3)


if __name__ == "__main":
    WxAuto().main()

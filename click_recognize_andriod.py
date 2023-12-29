# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:platformVersion": "12",
    "appium:deviceName": "rk3588_s",
    "appium:appPackage": "com.shifang.aidish.offline",
    "appnium:appActivity": ".mvp.ui.LoginActivity",
    "appium:autoAcceptAlerts": "true ",
    "appium:noReset": "true",
    "appium:dontStopAppOnReset": "true",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    'automationName': 'uiautomator2',
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

driver.implicitly_wait(3)
print("已连接服务")

# driver.start_activity("com.shifang.aidish.offline",".mvp.ui.LoginActivity")

# driver.find_element(By.ID,"com.shifang.aidish.offline:id/btn_login").click()
# driver.find_element(By.ID,"com.shifang.aidish.offline:id/ahp_iv_order_calc").click()
detect = driver.find_element(By.ID, "com.shifang.aidish.offline:id/btn_re_detect")
for i in range(1000):
    detect.click()
    time.sleep(1)
    print(i)
driver.quit()

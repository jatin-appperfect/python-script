
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import constant


desired_capabilities={
    "platformName": constant.ANDROID_PLATFORM_NAME,    
    "platformVersion": constant.ANDROID_PLATFORM_VERSION,
    "deviceName": constant.ANDROID_DEVICE_NAME,
    "automationName": constant.ANDROID_AUTOMATION_NAME,
    "app": constant.ANDROID_APP,
    "appPackage": constant.ANDROID_APP_PACKAGE,
    "noReset": True
}


class Test():
    driver = ""
    def __init__(self):
        print(">> Setup...")
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)


    def testone(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Sign in to a BBC Account").click()
        print("Clicked...")

        time.sleep(4)
        inp1 = self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@content-desc="BBC – Sign in"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View/android.widget.EditText').send_keys("jimmysharma00000m@gmail.com")

        time.sleep(1)
        self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@content-desc="BBC – Sign in"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View/android.widget.EditText').send_keys("J83027::11S")

        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Sign in"]').click()





obj = Test()
obj.testone()

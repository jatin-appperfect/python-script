
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

import constant


desired_capabilities = {
    "platformName": constant.IOS_PLATFORM_NAME,
    "appium:platformVersion": constant.IOS_PLATFORM_VERSION,
    "appium:deviceName": constant.IOS_DEVICE_NAME,
    "appium:automationName": constant.IOS_AUTOMATION_NAME,
    "appium:app": constant.IOS_APP,
    "appium:noReset": constant.NO_RESET,
    "appium:autoAcceptAlerts": constant.AUTO_ACCEPT_ALERTS
}


class Test():
    driver = ""

    def __init__(self):
        print(">> Setup...")
        self.driver = webdriver.Remote(command_executor="http://115.178.102.190:4723/wd/hub", desired_capabilities=desired_capabilities)

        print("Driver : ", self.driver)

    def listrow1(self):
        time.sleep(1)
        element = self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="UICatalog"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]')
        element.click()

        btn = self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Other"]')
        btn.click()

        choice_btn = self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "Choice Two")
        choice_btn.click()
        print("\n>> first test done")

        self.driver.back()


    def newfunction(self):
        print("this is new function for testing...")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "content-button-row")

        



    def listrow2(self):
        time.sleep(1)
        list2 = self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="UICatalog"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[8]')
        list2.click()

        self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypePickerWheel[@name="Red color component value"]').set_value("90")

        self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypePickerWheel[@name="Green color component value"]').set_value("50")

        self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypePickerWheel[@name="Blue color component value"]').set_value("200")

        color_panel = self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="UICatalog"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')

        print(">> second test done")

        # back_btn = self.driver.find_element(
        #     AppiumBy.XPATH, '//XCUIElementTypeButton[@name="UICatalog"]').click()
        self.driver.back()

    def listrow3(self):
        print(">> input text...")
        list3 = self.driver.find_element(
            AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="UICatalog"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[14]')
        list3.click()

        time.sleep(1)

        try:
            search_inp = self.driver.find_element(
                AppiumBy.XPATH, '//XCUIElementTypeApplication[@name="UICatalog"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeTextField').send_keys("Hello World!")

            submit_btn = self.driver.find_element(
                AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]').click()
        except Exception as e:
            print("Error Generated : ", e)

        print(">> third test done")

        self.driver.back()

    def scroll_down(self):
        time.sleep(1)
        print(">> scrolling down...")

        # # full scroll...
        # driver.execute_script('mobile: scroll', {'direction': 'down',})

        for i in range(1):
            self.driver.swipe(0, 500, 0, 0, 500)
            # #              (startX, startY, endX, endY, duration)

    def scroll_up(self):
        print(">> scrolling up...")
        time.sleep(1)
        self.driver.swipe(0, 400, 0, 900, 500)
        # #              (startX, startY, endX, endY, duration)

    def notification_panel(self):
        obj.driver.swipe(0, 0, 0, 800, 0)
        time.sleep(1)
        obj.driver.swipe(0, 1200, 0, 0, 0)
        time.sleep(1)
        obj.driver.swipe(0, 1200, 0, 800, 0)


obj = Test()

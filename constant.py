
import yaml
from yaml import Loader

with open("config.yaml", "r") as yaml_file:
    data = yaml.load(yaml_file, Loader=Loader)
    
    IOS_PLATFORM_NAME = data["IOS"][0]["platformName"]
    IOS_PLATFORM_VERSION = data["IOS"][1]["platformVersion"]
    IOS_DEVICE_NAME = data["IOS"][2]["deviceName"]
    IOS_AUTOMATION_NAME = data["IOS"][3]["automationName"]
    IOS_APP = data["IOS"][4]["app"]

    NO_RESET = data["noReset"]
    AUTO_ACCEPT_ALERTS = data["autoAcceptAlerts"]

    ANDROID_PLATFORM_NAME = data["ANDROID"][0]["platformName"]
    ANDROID_PLATFORM_VERSION = data["ANDROID"][1]["platformVersion"]
    ANDROID_DEVICE_NAME = data["ANDROID"][2]["deviceName"]
    ANDROID_AUTOMATION_NAME = data["ANDROID"][3]["automationName"]
    ANDROID_APP = data["ANDROID"][4]["app"]
    ANDROID_APP_PACKAGE = data["ANDROID"][5]["appPackage"]
    ANDROID_APP_ACTIVITY = data["ANDROID"][6]["appActivity"]


    # print(IOS_PLATFORM_NAME)
    # print(IOS_PLATFORM_VERSION)
    # print(IOS_DEVICE_NAME)
    # print(IOS_AUTOMATION_NAME)
    # print(IOS_APP)

    print(ANDROID_PLATFORM_NAME)
    print(ANDROID_PLATFORM_VERSION)
    print(ANDROID_DEVICE_NAME)
    print(ANDROID_APP)
    print(ANDROID_APP_PACKAGE)
    print(ANDROID_APP_ACTIVITY)

    # print(NO_RESET)
    # print(AUTO_ACCEPT_ALERTS)


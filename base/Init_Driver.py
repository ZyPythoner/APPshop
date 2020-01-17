from appium import webdriver


def init_driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7',
        'deviceName': '*****',
        'appPackage': 'com.tpshop.malls',
        'appActivity': 'com.tpshop.malls.SplashActivity',
        'resetKeyboard': True,
        'unicodeKeyboard': True,
        'noReset': True,
        'automationName': 'Uiautomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver

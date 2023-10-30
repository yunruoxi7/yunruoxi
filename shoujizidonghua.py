from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

desired_caps={
    'platformName':'Android',#设备系统
    'platformVersion':'9',#安卓系统版本
    'deviceName':'emulator-5556',#设备名
    'appPackage':'tv.danmaku.bili',#打开的设备应用
    'appActivity':'.MainActivityV2',#打开方式
    'unicodeKeyboard':True,#正常输入英文
    'noReset':True,
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.1.0.1:4723/wd/hub', desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements(By.ID, "text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element(By.ID, 'expand_search').click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element(By.ID, 'search_src_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)
# 选择（定位）所有视频标题
eles = driver.find_elements(By.ID, 'title')

for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()
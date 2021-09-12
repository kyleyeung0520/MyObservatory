# coding: utf-8
'''
python version:3.7
coding tool:pycharm
author:kyle yeung
mobile phone:xiaomi 9
date:2021-09-11
'''

import time
import uiautomator2 as u2

global d # 定义手机设备为全局变量

# 连接手机adb
try:
    d = u2.connect(r'28de743a0920')
except Exception as e:
    print(e)

# 获取测试手机信息并打印
phone_info = d.info
for item in phone_info.items():
    print(item)

# 通过包名启动MyObservatory app
d.app_start('hko.MyObservatory_v1_0')
time.sleep(5)

# 通过u2启动MyObservatory app
# d(resourceId="com.miui.home:id/icon_icon", description="MyObservatory").click()
# time.sleep(3)

# 截取app启动成功页
img = d.screenshot() #屏幕截图
imgName='启动页'
img.save('imgName.png')#图片保存在当前项目的文件夹下边

# 进入个人中心
d(description="Navigate up").click()
time.sleep(3)

# 滚动动屏幕，定位未来9天天气条目
# d(scrollable=True).scroll.to(description="9-Day Forecast")
# time.sleep(3)

# 从x1，y1坐标滑动至x2，y2坐标，以便定位未来9天天气条目
d.swipe(0.531, 0.763, 0.527, 0.448)

# 进入检查未来9天天气信息
d(resourceId="hko.MyObservatory_v1_0:id/text", text="9-Day Forecast").click()
time.sleep(3)

# 未来9天天气信息垂直向后滑动到页面底部
# d(scrollable=True).scroll.vert.backward(steps=10)
# d(scrollable=True).scroll.toEnd()

d.swipe(0.531, 0.863, 0.531, 0.163)# 滑动第一次
time.sleep(2)
img_1 = d.screenshot() #屏幕截图
imgName_1='未来9天天气列表'
img_1.save('imgName_1.png')#图片保存在当前项目的文件夹下边

d.swipe(0.531, 0.863, 0.531, 0.163)# 滑动第二次
time.sleep(2)
img_2 = d.screenshot() #屏幕截图
imgName_2='未来9天天气列表'
img_2.save('imgName_2.png')#图片保存在当前项目的文件夹下边


# 关闭app
d.app_stop('hko.MyObservatory_v1_0')

# 清除app数据
# d.app_clear('hko.MyObservatory_v1_0')







import os
import time
import Image


def screencap():
    os.system('adb shell screencap -p /sdcard/screen.png')
    os.system('adb pull /sdcard/screen.png')


def qu_guang_dian():
    print('====== 去逛店 ======')
    for i in range(1, 11):
        screencap()
        img = Image.open('screen.png')
        if img.getpixel((830, 1645)) == (207, 144, 124, 255):
            print('已完成11次去逛店任务')
            break
        else:
            os.system('adb shell input tap 912 1652')  # 点击逛店
            print('第{}次去逛店...'.format(i))
            time.sleep(1)
            print('进入店铺,浏览页面中，请等待15s...')
            os.system('adb shell input swipe 576 1783 621 1019 500')  # 从上往下滑动，开始计时
            time.sleep(16)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回

def renqihuichang():
    print('====== 进入人气会场 ======')
    for i in range(1, 8):
        screencap()
        img = Image.open('screen.png')
        if img.getpixel((836, 1841)) == (207, 144, 124, 255):
            print('已完成8次人气会场任务')
            break
        else:
            os.system('adb shell input tap 836 1819')  # 点击逛店
            print('第{}次去逛店...'.format(i))
            time.sleep(4)
            print('进入店铺,浏览页面中，请等待15s...')
            os.system('adb shell input swipe 576 2200 621 400 1000')  # 从上往下滑动，开始计时
            time.sleep(16)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
def tesechang():
    print('====== 进入特色会场 ======')
    for i in range(1, 20):
        screencap()
        img = Image.open('screen.png')
        if img.getpixel((837, 2023)) == (207, 144, 124, 255):
            print('已完成特色会场任务')
            break
        else:
            os.system('adb shell input tap 836 2009')  # 点击逛店
            print('第{}次去特色会场...'.format(i))
            time.sleep(4)
            print('进入店铺,浏览页面中，请等待15s...')
            os.system('adb shell input swipe 576 2200 621 400 1000')  # 从上往下滑动，开始计时
            time.sleep(19)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
def dapaichang():
    print('====== 进入大牌会场 ======')
    for i in range(1, 20):
        screencap()
        img = Image.open('screen.png')
        if img.getpixel((833, 2206)) == (207, 144, 124, 255):
            print('已完成大牌会场任务')
            break
        else:
            os.system('adb shell input tap 836 2206')  # 点击逛店
            print('第{}次去大牌会场...'.format(i))
            time.sleep(4)
            print('进入店铺,浏览页面中，请等待15s...')
            os.system('adb shell input swipe 576 2200 621 400 1000')  # 从上往下滑动，开始计时
            time.sleep(19)
            os.system('adb shell input keyevent KEYCODE_BACK')  # 返回

os.system('adb shell input tap 983 1366')  # 点击进入种福果
time.sleep(2)
os.system('adb shell input tap 996 1655')  # 点击集福气
time.sleep(2)
screencap()
img = Image.open('screen.png')
if img.getpixel((833, 1446)) == (207, 144, 124, 255):
    print('已完成主会场任务')
else:
    os.system('adb shell input tap 855 1459')  # 点击进入年货主会场
    print('进入年货主会场,浏览页面中，请等待15s...')
    time.sleep(16)
    os.system('adb shell input keyevent KEYCODE_BACK')  # 返回
qu_guang_dian()
renqihuichang()
tesechang()
dapaichang()

import urllib.request as urllib
import time
import cv2
import os

def find_captcha():

    im = cv2.imread("whole.png")
    #change parameters if you do not have a 1080p screen.
    cropped = im[500:580,1000:1150]
    cv2.imshow("captcha.png",cropped)
    cv2.waitKey()

    value = input("\n\n\nEnter captcha:")

    os.remove('whole.png')
    return value


def catch_captcha(web,id):
    #uncomment the following branch instead of the done method if the site has an ssl cert.
    #img = web.find_element_by_id(id)
    #src = img.get_attribute('src')

    #urllib.urlretrieve(src, "captcha.png")
    web.save_screenshot('whole.png')
    val = find_captcha()
    web.find_element_by_id(id).send_keys(val)

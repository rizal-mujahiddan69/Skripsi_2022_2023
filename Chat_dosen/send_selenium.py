from pprint import pprint
from selenium import webdriver
from chat_dosen import chat_dos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import chromedriver_binary
import datetime
import os
import time

# Selenium 4.3.0
# * Deprecated find_element_by_* and find_elements_by_* are now removed (#10712)
# * Deprecated Opera support has been removed (#10630)
# * Fully upgraded from python 2x to 3.7 syntax and features (#10647)
# * Added a devtools version fallback mechanism to look for an older version when mismatch occurs (#10749)
# * Better support for co-operative multi inheritance by utilising super() throughout
# * Improved type hints throughout

def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end
start = datetime.time(8, 0, 0)
end = datetime.time(17, 0, 0)

# masukkan class chat_dosen ke selenium yaa

chat_dosku = chat_dos('data_chat_dosen.conf') 
tulisan = chat_dosku.tulis()

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")
print("Scan Me heula , setelah itu tekan enter")
input()

# def reps():
#     print("Do you want to send more msg to anyone")
#     askUser = input("Press y for Yes and n for No : ")
#     if (askUser == 'Y' or askUser == 'y'):
#         msg()
#     elif (askUser == 'N' or askUser == 'n'):
#         print("Thank you see you soon")
#     else:
#         print("Please Enter Valid option :\n")
#         reps()

def msg():
    # name = input('\nEnter Group/User Name: ')
    # message = input("Enter your message to group/user: ")

    name = chat_dosku.nama_dosen
    message = tulisan
    print(name)
    # Find Whom to message     
    try:
        # Count = int(input("Enter the message count:"))
        Count = 1
        user = driver.find_element("xpath","//span[@title='{}']".format(name))
        user.click()
    except:
        msg()

    text_box = driver.find_element(By.CLASS_NAME,'p3_M1')

    #Send Button
    current = datetime.datetime.now().time()
    if(time_in_range(start, end, current)):
        for i in range(Count):
            text_box.send_keys(message)
            driver.find_element(By.CLASS_NAME,"_1Ae7k").click()
    else:
        print("Ingat Waktu Rizal")
    # reps()

msg()
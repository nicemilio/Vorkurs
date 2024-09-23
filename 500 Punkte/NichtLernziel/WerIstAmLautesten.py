import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def change_mac(interface="en0"):
    try:
        subprocess.call(f"sudo ifconfig {interface} down", shell=True)
        subprocess.call(f"sudo macchanger -r {interface}", shell=True)
        subprocess.call(f"sudo ifconfig {interface} up", shell=True)
        print(f"MAC address for {interface} changed successfully")
    except Exception as e:
        print(f"Failed to change MAC address: {e}")

def reset_mac(interface="en0"):
    try:
        subprocess.call(f"sudo ifconfig {interface} down", shell=True)
        subprocess.call(f"sudo macchanger -p {interface}", shell=True)
        subprocess.call(f"sudo ifconfig {interface} up", shell=True)
        print(f"MAC address for {interface} reset successfully")
    except Exception as e:
        print(f"Failed to reset MAC address: {e}")


driver = webdriver.Safari()

for x in range(0, 10000):
    driver.get("https://www.menti.com/al3k17ru81pc")
    driver.implicitly_wait(5)
    elem = driver.find_element(By.NAME, 'wordcloud-input')
    elem.send_keys("Entry")
    elem.send_keys(Keys.RETURN)
    time.sleep(0.5)
    change_mac()

reset_mac()


driver.quit()
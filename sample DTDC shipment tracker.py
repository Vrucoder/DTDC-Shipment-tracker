# tesseract links: http://bit.ly/2PD8s8d, http://bit.ly/2rI24oj
# tesseract not found error: https://stackoverflow.com/questions/50655738/how-do-i-resolve-a-tesseractnotfounderror
# raise tesseract error: https://stackoverflow.com/questions/54725151/pytesseract-tesseracterror-usage-python-pytesseract-py-l-lang-input-file
# SyntaxError: (unicode error): replace "\" with "/"

# for selenium screenshot refer to: https://pypi.org/project/Selenium-Screenshot/
# for more info on regex, go to: sololearn > python > regular expressions > special sequences > part 2.



import re
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from Screenshot import Screenshot_Clipping
from selenium import webdriver


pytesseract.pytesseract.tesseract_cmd = (
    r"path where the tesseract.exe file has located"
)

def Consignquery(consign_num):
    driver = webdriver.Chrome(executable_path= r"path containing the "'chromedriver.exe' "file")
    time.sleep(1)

    # open new window(it's a tab)
    driver.execute_script("window.open('');")
    time.sleep(1.75)
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://www.dtdc.in/tracking/tracking_results.asp')
    time.sleep(2)
    # to dismiss the public notice overlay

    elem = driver .find_element(By.XPATH,'//*[@id="myvideo"]/div/div/div[1]/p/button').click()

    # to select the "consignment number" radio button.
    elem = driver .find_element(By.XPATH,'//*[@id="TrkType2"]').click

    # clear the input text box & input the consignment number
    elem = driver .find_element(By.XPATH,'//*[@id="contentPanel"]/div/div/div/form/table/tbody/tr[2]/td[2]/textarea')
    time.sleep(2)
    elem.clear()
    time.sleep(2)
    elem.send_keys(consign_num)
    time.sleep(2)

    # find the track button and click it.
    driver.find_element_by_xpath('//*[@id="contact-area"]/input').click()
    time.sleep(10)

    # for taking the full webpage screenshot. define the path.
    pic = Screenshot_Clipping.Screenshot()
    img_url = pic.full_Screenshot(driver, save_path=r'', image_name='xyz.png')
    print(img_url)
    time.sleep(40)

    # to refresh the page
    # driver.refresh()


    #to get the current link
    #print(driver.current_url)

    # close the active tab
    driver.close()
    time.sleep(1.2)
    # Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])
    driver.get("http://google.in")
    time.sleep(3)
    # Close the only tab, will also close the browser.
    driver.close()

    # I could've used the multi-line comment, but I stick to this, as sometimes multiline comment produces an error (EOF while scanning the file).
    # to go backward or forward
    # driver.back()
    # driver.forward()

    # to scroll down & up
    # driver.send_keys(Key.END)
    # driver.send_keys(key.HOME)
#________________________________________________________________________________________________________________________________

# this part fetches the consignment number from the image, uses pytesseract module.
# argument filename = entire file path with the target image file included
def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    # stores the whole extracted string in the 'text' variable.
    text = pytesseract.image_to_string(Image.open(filename))
    # now defining the pattern. DTDC consignment number is always single word characer followed by 8 digits.
    pattern = r"\w{1}\d{8}"
    # checks for the pattern with the entire extracted string.
    match = re.search(pattern, text)
    # if there is a positive match, it prints that.
    if match:
        consign_num = match.group()
        print('The consignment number detected is:', consign_num)
        time.sleep(4.5)
        Consignquery(consign_num)

path = str(input("Please copy paste the path with the image included: "))

ocr_core('path')






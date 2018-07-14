
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import lxml


class RenewLogin:
    unameXpath = "//input[@id='userid']"
    passXpath = "//input[@id='password']"
    loginButton = "//input[@class='btn']"
    renewallButton = "//input[@class='btn' and @value='Renew all']"

    bracuLibrary = "http://library.bracu.ac.bd/cgi-bin/koha/opac-main.pl"
    renewPage = "http://library.bracu.ac.bd/cgi-bin//koha/opac-user.pl"


    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.browser = None
        self.key_actions = None
        self.webdriver_path = ''
        self.targetUrl = ''
        print("inside constructor\n")

    def set_browser(self):
        self.browser=webdriver.Chrome("C:\\Users\\Sadman\\Downloads\\Compressed\\chromedriver.exe")
        self.key_actions=webdriver.ActionChains(self.browser)
        print("inside setBrowser\n")


    def library_login(self):
        print("inside libraryLogin\n")
        self.browser.get(RenewLogin.bracuLibrary)
        print(1)
        uname_element = self.browser.find_element_by_xpath(RenewLogin.unameXpath)
        print(2)
        pass_element = self.browser.find_element_by_xpath(RenewLogin.passXpath)
        print(3)
        loginbutton_element = self.browser.find_element_by_xpath(RenewLogin.loginButton)
        print(4)


        uname_element.send_keys(self.userid)
        pass_element.send_keys(self.password)
        print("passed id and pass\n")
        loginbutton_element.click()
        print("clicked\n")
        sleep(2)

    def click_renewall(self):
        self.browser.get(RenewLogin.renewPage)
        renewall_element = self.browser.find_element_by_xpath(RenewLogin.renewallButton)
        print("Renewed!!")
        renewall_element.click()

    def close_browser(self):
        self.browser.close()







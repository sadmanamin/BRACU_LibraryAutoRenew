import getpass
from RenewLogin import RenewLogin
uname = input('Insert you BRACU ID : ')
password = getpass.getpass('Insert your password : ')


if __name__ == '__main__':
    print("inside main\n")
    renew = RenewLogin(uname,password)
    renew.set_browser()
    renew.library_login()
    renew.click_renewall()
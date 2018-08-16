from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
import webbrowser
import os
from os.path import expanduser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("Hype_Pickups Supreme Bot")
        MainWindow.resize(520, 520)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.Window_2 = QtWidgets.QWidget(self.centralWidget)
        self.Window_2.setGeometry(QtCore.QRect(10, 10, 501, 471))
        self.Window_2.setObjectName("Window_2")
        self.Item_Code_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Item_Code_2.setGeometry(QtCore.QRect(40, 50, 421, 21))
        self.Item_Code_2.setObjectName("Item_Code_2")
        self.Name_3 = QtWidgets.QLineEdit(self.Window_2)
        self.Name_3.setGeometry(QtCore.QRect(10, 170, 131, 21))
        self.Name_3.setObjectName("Name_3")
        self.Phone_Number_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Phone_Number_2.setGeometry(QtCore.QRect(370, 170, 111, 21))
        self.Phone_Number_2.setObjectName("Phone_Number_2")
        self.Address_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Address_2.setGeometry(QtCore.QRect(20, 230, 151, 21))
        self.Address_2.setObjectName("Address_2")
        self.Postal_Code_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Postal_Code_2.setGeometry(QtCore.QRect(370, 230, 111, 21))
        self.Postal_Code_2.setObjectName("Postal_Code_2")
        self.Size_3 = QtWidgets.QComboBox(self.Window_2)
        self.Size_3.setGeometry(QtCore.QRect(70, 100, 361, 26))
        self.Size_3.setEditable(True)
        self.Size_3.setObjectName("Size_3")
        self.Size_3.addItem("")
        self.Size_3.addItem("")
        self.Size_3.addItem("")
        self.Size_3.addItem("")
        self.Size_3.addItem("")
        self.Apartment_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Apartment_2.setGeometry(QtCore.QRect(220, 230, 101, 21))
        self.Apartment_2.setObjectName("Apartment_2")
        self.Email_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Email_2.setGeometry(QtCore.QRect(170, 170, 171, 21))
        self.Email_2.setObjectName("Email_2")
        self.Google_Log_In_2 = QtWidgets.QSpinBox(self.Window_2)
        self.Google_Log_In_2.setGeometry(QtCore.QRect(50, 420, 48, 24))
        self.Google_Log_In_2.setObjectName("Google_Log_In_2")
        self.Item_Codes_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Item_Codes_Label_2.setGeometry(QtCore.QRect(220, 30, 71, 16))
        self.Item_Codes_Label_2.setObjectName("Item_Codes_Label_2")
        self.Size_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Size_Label_2.setGeometry(QtCore.QRect(230, 80, 31, 16))
        self.Size_Label_2.setObjectName("Size_Label_2")
        self.Name_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Name_Label_2.setGeometry(QtCore.QRect(40, 150, 60, 16))
        self.Name_Label_2.setObjectName("Name_Label_2")
        self.Email_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Email_Label_2.setGeometry(QtCore.QRect(240, 150, 41, 16))
        self.Email_Label_2.setObjectName("Email_Label_2")
        self.Phone_Number_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Phone_Number_Label_2.setGeometry(QtCore.QRect(380, 150, 91, 16))
        self.Phone_Number_Label_2.setObjectName("Phone_Number_Label_2")
        self.Address_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Address_Label_2.setGeometry(QtCore.QRect(70, 210, 60, 16))
        self.Address_Label_2.setObjectName("Address_Label_2")
        self.Apartment_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Apartment_Label_2.setGeometry(QtCore.QRect(200, 210, 141, 16))
        self.Apartment_Label_2.setObjectName("Apartment_Label_2")
        self.Zip_Postal_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Zip_Postal_Label_2.setGeometry(QtCore.QRect(370, 210, 101, 16))
        self.Zip_Postal_Label_2.setObjectName("Zip_Postal_Label_2")
        self.City_2 = QtWidgets.QLineEdit(self.Window_2)
        self.City_2.setGeometry(QtCore.QRect(20, 290, 151, 21))
        self.City_2.setObjectName("City_2")
        self.City_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.City_Label_2.setGeometry(QtCore.QRect(80, 270, 31, 16))
        self.City_Label_2.setObjectName("City_Label_2")
        self.Country_2 = QtWidgets.QComboBox(self.Window_2)
        self.Country_2.setGeometry(QtCore.QRect(220, 290, 111, 31))
        self.Country_2.setObjectName("Country_2")
        self.Country_2.addItem("")
        self.Country_2.addItem("")
        self.Country_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Country_Label_2.setGeometry(QtCore.QRect(250, 270, 51, 16))
        self.Country_Label_2.setObjectName("Country_Label_2")
        self.State_Prov_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.State_Prov_Label_2.setGeometry(QtCore.QRect(380, 270, 91, 16))
        self.State_Prov_Label_2.setObjectName("State_Prov_Label_2")
        self.Card_Number_2 = QtWidgets.QLineEdit(self.Window_2)
        self.Card_Number_2.setGeometry(QtCore.QRect(20, 350, 141, 21))
        self.Card_Number_2.setText("")
        self.Card_Number_2.setObjectName("Card_Number_2")
        self.Card_Number_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Card_Number_Label_2.setGeometry(QtCore.QRect(50, 330, 81, 16))
        self.Card_Number_Label_2.setObjectName("Card_Number_Label_2")
        self.Card_Month_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Card_Month_Label_2.setGeometry(QtCore.QRect(200, 330, 81, 16))
        self.Card_Month_Label_2.setObjectName("Card_Month_Label_2")
        self.Card_Year_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Card_Year_Label_2.setGeometry(QtCore.QRect(300, 330, 81, 16))
        self.Card_Year_Label_2.setObjectName("Card_Year_Label_2")
        self.CVV_2 = QtWidgets.QLineEdit(self.Window_2)
        self.CVV_2.setGeometry(QtCore.QRect(420, 350, 51, 21))
        self.CVV_2.setObjectName("CVV_2")
        self.CVV_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.CVV_Label_2.setGeometry(QtCore.QRect(430, 330, 31, 16))
        self.CVV_Label_2.setObjectName("CVV_Label_2")
        self.Google_Sign_In_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Google_Sign_In_Label_2.setGeometry(QtCore.QRect(10, 390, 391, 16))
        self.Google_Sign_In_Label_2.setObjectName("Google_Sign_In_Label_2")
        self.Card_Month_2 = QtWidgets.QComboBox(self.Window_2)
        self.Card_Month_2.setGeometry(QtCore.QRect(200, 350, 71, 26))
        self.Card_Month_2.setObjectName("Card_Month_2")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Month_2.addItem("")
        self.Card_Year_2 = QtWidgets.QComboBox(self.Window_2)
        self.Card_Year_2.setGeometry(QtCore.QRect(300, 350, 81, 26))
        self.Card_Year_2.setObjectName("Card_Year_2")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Card_Year_2.addItem("")
        self.Hype_Pickups_Label_2 = QtWidgets.QLabel(self.Window_2)
        self.Hype_Pickups_Label_2.setGeometry(QtCore.QRect(170, 0, 181, 20))
        self.Hype_Pickups_Label_2.setObjectName("Hype_Pickups_Label_2")
        self.State_Province_2 = QtWidgets.QComboBox(self.Window_2)
        self.State_Province_2.setGeometry(QtCore.QRect(380, 290, 91, 26))
        self.State_Province_2.setStyleSheet("")
        self.State_Province_2.setObjectName("State_Province_2")
        self.State_Province_2.setEditable(True)
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.State_Province_2.addItem("")
        self.Item_Codes_btn = QtWidgets.QPushButton(self.Window_2)
        self.Item_Codes_btn.setGeometry(QtCore.QRect(360, 420, 131, 51))
        self.Item_Codes_btn.setObjectName("Item_Codes_btn")
        #****************
        self.Item_Codes_btn.clicked.connect(self.CODES)
        #****************
        self.Start_Button_2 = QtWidgets.QPushButton(self.Window_2)
        self.Start_Button_2.setGeometry(QtCore.QRect(140, 420, 221, 51))
        self.Start_Button_2.setAutoFillBackground(False)
        self.Start_Button_2.setObjectName("Start_Button_2")
        #****************
        self.Start_Button_2.clicked.connect(self.BOT)
        #****************
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 520, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuContact_Me = QtWidgets.QMenu(self.menuHelp)
        self.menuContact_Me.setObjectName("menuContact_Me")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionInstagram_woj_prod = QtWidgets.QAction(MainWindow)
        self.actionInstagram_woj_prod.setObjectName("actionInstagram_woj_prod")
        self.menuContact_Me.addAction(self.actionInstagram_woj_prod)
        self.menuHelp.addAction(self.menuContact_Me.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def BOT(self):
        Item_code = (self.Item_Code_2.text())
        Size = (self.Size_3.currentText())
        Name = (self.Name_3.text())
        Email = (self.Email_2.text())
        Tel = (self.Phone_Number_2.text())
        Address = (self.Address_2.text())
        Apt = (self.Apartment_2.text())
        Zip = (self.Postal_Code_2.text())
        City = (self.City_2.text())
        Country = (self.Country_2.currentText())
        State = (self.State_Province_2.currentText())
        Credit = (self.Card_Number_2.text())
        Month = (self.Card_Month_2.currentText())
        Year = (self.Card_Year_2.currentText())
        CVV = (self.CVV_2.text())
        Time = (self.Google_Log_In_2.text())
        
        chrome_options = Options()
        chrome_options.add_argument("--disable-infobars")
        
        User = expanduser("~")
        
        driver = webdriver.Chrome(executable_path=(User)+'/Downloads/chromedriver', chrome_options=chrome_options) #choose whichever location you want for the chromedriver.
        time.sleep(float(Time))
        URL = "https://www.supremenewyork.com/shop/all"

        wait = WebDriverWait(driver, 10)

        if Size.count(',') == (0):
            Size1 = Size
            Size = Size1

        if Size.count(',') == (1):
            Size1,Size2 = Size.split(',')
    
        if Size.count(',') == (2):
            Size1,Size2,Size3 = Size.split(',')

        if Size.count(',') == (3):
            Size1,Size2,Size3,Size4 = Size.split(',')

        if Size.count(',') == (4):
            Size1,Size2,Size3,Size4,Size5 = Size.split(',')
    
        def Item_Finder():
            #refreshes until found
            while True:
                try:
                    driver.find_element_by_css_selector('img[alt="'+ (Item_code[:11]) +'"]').click()
                    break

                except NoSuchElementException:
                    driver.refresh()
                
          
            wait.until(EC.presence_of_element_located((By.NAME, 'commit')))

            if Size1 == ('One Size'):
                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
            else:
                #selects size
                select = Select(driver.find_element_by_id('s'))
                select.select_by_visible_text(Size1)
                
                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
               
        def Item_Finder1():
            while True:
                try:
                    driver.find_element_by_css_selector('img[alt="'+ (Item_code[12:23]) +'"]').click()
                    break

                except NoSuchElementException:
                    driver.refresh()
                
            wait.until(EC.presence_of_element_located((By.NAME, 'commit')))

            if Size2 == ('One Size'):
                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
            else:
                #selects size
                select = Select(driver.find_element_by_id('s'))
                select.select_by_visible_text(Size2)

                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))

        def Item_Finder2():
            while True:
                try:
                    driver.find_element_by_css_selector('img[alt="'+ (Item_code[24:35]) +'"]').click()
                    break

                except NoSuchElementException:
                    driver.refresh()
                
            wait.until(EC.presence_of_element_located((By.NAME, 'commit')))

            if Size3 == ('One Size'):
                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
            else:
                #selects size
               select = Select(driver.find_element_by_id('s'))
               select.select_by_visible_text(Size3)

               #adds to cart
               driver.find_element_by_name('commit').click()

               #waits for Cart to Load
               wait.until(EC.visibility_of_element_located((By.ID, "cart")))

        def Item_Finder3():
            while True:
                try:
                    driver.find_element_by_css_selector('img[alt="'+ (Item_code[36:47]) +'"]').click()
                    break

                except NoSuchElementException:
                   driver.refresh()
                
            wait.until(EC.presence_of_element_located((By.NAME, 'commit')))

            if Size4 == ('One Size'):
                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
            else:
               #selects size
                select = Select(driver.find_element_by_id('s'))
                select.select_by_visible_text(Size4)

                #adds to cart
                driver.find_element_by_name('commit').click()

               #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))

        def Item_Finder4():
            while True:
                try:
                    driver.find_element_by_css_selector('img[alt="'+ (Item_code[48:59]) +'"]').click()
                    break

                except NoSuchElementException:
                    driver.refresh()
                
            wait.until(EC.presence_of_element_located((By.NAME, 'commit')))

            if Size5 == ('One Size'):
               #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))
            else:
                #selects size
                select = Select(driver.find_element_by_id('s'))
                select.select_by_visible_text(Size5)

                #adds to cart
                driver.find_element_by_name('commit').click()

                #waits for Cart to Load
                wait.until(EC.visibility_of_element_located((By.ID, "cart")))

        def Checkout():
            time.sleep(1)
            #goes to checkout
            driver.get('https://www.supremenewyork.com/checkout')
            #autofill
            fill = ("document.getElementById('order_billing_name').value = '" + str(Name) + "';")
            email1 = ("document.getElementById('order_email').value = '" + str(Email) + "';")
            tel1 = ("document.getElementById('order_tel').value = '" + str(Tel) + "';")
            address = ("document.getElementById('bo').value = '" + str(Address) + "';")
            apt = ("document.getElementById('oba3').value = '" + str(Apt) + "';")
            _zip = ("document.getElementById('order_billing_zip').value = '" + str(Zip) + "';")
            city = ("document.getElementById('order_billing_city').value = '" + str(City) + "';")
            card = ("document.getElementById('nnaerb').value = '" + str(Credit) + "';")
            month = ("document.getElementById('credit_card_month').value = '" + str(Month) + "';")
            year = ("document.getElementById('credit_card_year').value = '" + str(Year) + "';")
            cvv = ("document.getElementById('orcer').value = '" + str(CVV) + "';")

            driver.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(Country)
            driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(State)

            fill+= email1 + tel1 + address + apt + _zip + city + card + month + year + cvv
            driver.execute_script(fill)
            
            #clicks on checkbox
            driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    
        def Checkout0():
            #goes to checkout
            driver.get('https://www.supremenewyork.com/checkout')
            #autofill 
            fill = ("document.getElementById('order_billing_name').value = '" + str(Name) + "';")
            email1 = ("document.getElementById('order_email').value = '" + str(Email) + "';")
            tel1 = ("document.getElementById('order_tel').value = '" + str(Tel) + "';")
            address = ("document.getElementById('bo').value = '" + str(Address) + "';")
            apt = ("document.getElementById('oba3').value = '" + str(Apt) + "';")
            _zip = ("document.getElementById('order_billing_zip').value = '" + str(Zip) + "';")
            city = ("document.getElementById('order_billing_city').value = '" + str(City) + "';")
            card = ("document.getElementById('nnaerb').value = '" + str(Credit) + "';")
            month = ("document.getElementById('credit_card_month').value = '" + str(Month) + "';")
            year = ("document.getElementById('credit_card_year').value = '" + str(Year) + "';")
            cvv = ("document.getElementById('orcer').value = '" + str(CVV) + "';")

            driver.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(Country)
            driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys(State)

            fill+= email1 + tel1 + address + apt + _zip + city + card + month + year + cvv
            driver.execute_script(fill)
            
            #clicks on checkbox
            driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
                          
               
        def Cart():
            driver.get(URL)
            Item_Finder()
    
        def Cart_More1():
            driver.get(URL)
            Item_Finder1()
    
        def Cart_More2():
           driver.get(URL)
           Item_Finder2()

        def Cart_More3():
            driver.get(URL)
            Item_Finder3()

        def Cart_More4():
            driver.get(URL)
            Item_Finder4()
    

        #Carts 1 Item
        if Item_code.count(',') == (0):
            Cart()
            Checkout0()

        #Carts 2 Items
        if Item_code.count(',') == (1):
            Cart()
            Cart_More1()
            Checkout()

       #Carts 3 Items
        if Item_code.count(',') == (2):
            Cart()
            Cart_More1()
            Cart_More2()
            Checkout()

        #Cart 4 Items
        if Item_code.count(',') == (3):
            Cart()
            Cart_More1()
            Cart_More2()
            Cart_More3()
            Checkout()
    
        #Cart 5 Items
        if Item_code.count(',') == (4):
            Cart()
            Cart_More1()
            Cart_More2()
            Cart_More3()
            Cart_More4()
            Checkout()    

    def CODES(self):
        url = ('https://docs.google.com/document/d/1FXwgDE0lNYlrDG0I0aE8Z5KnMHPdYIYdnFf_jiVdNK0/edit')
        webbrowser.open_new_tab(url)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Size_3.setItemText(0, _translate("MainWindow", "Small"))
        self.Size_3.setItemText(1, _translate("MainWindow", "Medium"))
        self.Size_3.setItemText(2, _translate("MainWindow", "Large"))
        self.Size_3.setItemText(3, _translate("MainWindow", "XLarge"))
        self.Size_3.setItemText(4, _translate("MainWindow", "One Size"))
        self.Item_Codes_Label_2.setText(_translate("MainWindow", "Item Code"))
        self.Size_Label_2.setText(_translate("MainWindow", "Size"))
        self.Name_Label_2.setText(_translate("MainWindow", "Full Name"))
        self.Email_Label_2.setText(_translate("MainWindow", "Email"))
        self.Phone_Number_Label_2.setText(_translate("MainWindow", "Phone Number"))
        self.Address_Label_2.setText(_translate("MainWindow", "Address"))
        self.Apartment_Label_2.setText(_translate("MainWindow", "Apartment # (optional)"))
        self.Zip_Postal_Label_2.setText(_translate("MainWindow", "Zip/Postal Code"))
        self.City_Label_2.setText(_translate("MainWindow", "City"))
        self.Country_2.setItemText(0, _translate("MainWindow", "USA"))
        self.Country_2.setItemText(1, _translate("MainWindow", "CANADA"))
        self.Country_Label_2.setText(_translate("MainWindow", "Country"))
        self.State_Prov_Label_2.setText(_translate("MainWindow", "State/Province"))
        self.Card_Number_Label_2.setText(_translate("MainWindow", "Card Number"))
        self.Card_Month_Label_2.setText(_translate("MainWindow", "Expiry Month"))
        self.Card_Year_Label_2.setText(_translate("MainWindow", " Expiry Year"))
        self.CVV_Label_2.setText(_translate("MainWindow", "Cvv"))
        self.Google_Sign_In_Label_2.setText(_translate("MainWindow", "Seconds needed to sign into google (optional but recomended)"))
        self.Card_Month_2.setItemText(0, _translate("MainWindow", "01"))
        self.Card_Month_2.setItemText(1, _translate("MainWindow", "02"))
        self.Card_Month_2.setItemText(2, _translate("MainWindow", "03"))
        self.Card_Month_2.setItemText(3, _translate("MainWindow", "04"))
        self.Card_Month_2.setItemText(4, _translate("MainWindow", "05"))
        self.Card_Month_2.setItemText(5, _translate("MainWindow", "06"))
        self.Card_Month_2.setItemText(6, _translate("MainWindow", "07"))
        self.Card_Month_2.setItemText(7, _translate("MainWindow", "08"))
        self.Card_Month_2.setItemText(8, _translate("MainWindow", "09"))
        self.Card_Month_2.setItemText(9, _translate("MainWindow", "10"))
        self.Card_Month_2.setItemText(10, _translate("MainWindow", "11"))
        self.Card_Month_2.setItemText(11, _translate("MainWindow", "12"))
        self.Card_Year_2.setItemText(0, _translate("MainWindow", "2018"))
        self.Card_Year_2.setItemText(1, _translate("MainWindow", "2019"))
        self.Card_Year_2.setItemText(2, _translate("MainWindow", "2020"))
        self.Card_Year_2.setItemText(3, _translate("MainWindow", "2021"))
        self.Card_Year_2.setItemText(4, _translate("MainWindow", "2022"))
        self.Card_Year_2.setItemText(5, _translate("MainWindow", "2023"))
        self.Card_Year_2.setItemText(6, _translate("MainWindow", "2024"))
        self.Card_Year_2.setItemText(7, _translate("MainWindow", "2025"))
        self.Card_Year_2.setItemText(8, _translate("MainWindow", "2026"))
        self.Card_Year_2.setItemText(9, _translate("MainWindow", "2027"))
        self.Card_Year_2.setItemText(10, _translate("MainWindow", "2028"))
        self.Card_Year_2.setItemText(11, _translate("MainWindow", "2029"))
        self.Card_Year_2.setItemText(12, _translate("MainWindow", "2030"))
        self.Hype_Pickups_Label_2.setText(_translate("MainWindow", "Hype_Pickups Supreme Bot"))
        self.State_Province_2.setItemText(0, _translate("MainWindow", "--USA--"))
        self.State_Province_2.setItemText(1, _translate("MainWindow", "AL"))
        self.State_Province_2.setItemText(2, _translate("MainWindow", "AK"))
        self.State_Province_2.setItemText(3, _translate("MainWindow", "AS"))
        self.State_Province_2.setItemText(4, _translate("MainWindow", "AZ"))
        self.State_Province_2.setItemText(5, _translate("MainWindow", "AR"))
        self.State_Province_2.setItemText(6, _translate("MainWindow", "CA"))
        self.State_Province_2.setItemText(7, _translate("MainWindow", "CO"))
        self.State_Province_2.setItemText(8, _translate("MainWindow", "CT"))
        self.State_Province_2.setItemText(9, _translate("MainWindow", "DE"))
        self.State_Province_2.setItemText(10, _translate("MainWindow", "DC"))
        self.State_Province_2.setItemText(11, _translate("MainWindow", "FM"))
        self.State_Province_2.setItemText(12, _translate("MainWindow", "FL"))
        self.State_Province_2.setItemText(13, _translate("MainWindow", "GA"))
        self.State_Province_2.setItemText(14, _translate("MainWindow", "GU"))
        self.State_Province_2.setItemText(15, _translate("MainWindow", "HI"))
        self.State_Province_2.setItemText(16, _translate("MainWindow", "ID"))
        self.State_Province_2.setItemText(17, _translate("MainWindow", "IL"))
        self.State_Province_2.setItemText(18, _translate("MainWindow", "IN"))
        self.State_Province_2.setItemText(19, _translate("MainWindow", "IA"))
        self.State_Province_2.setItemText(20, _translate("MainWindow", "KS"))
        self.State_Province_2.setItemText(21, _translate("MainWindow", "KY"))
        self.State_Province_2.setItemText(22, _translate("MainWindow", "LA"))
        self.State_Province_2.setItemText(23, _translate("MainWindow", "ME"))
        self.State_Province_2.setItemText(24, _translate("MainWindow", "MH"))
        self.State_Province_2.setItemText(25, _translate("MainWindow", "MD"))
        self.State_Province_2.setItemText(26, _translate("MainWindow", "MA"))
        self.State_Province_2.setItemText(27, _translate("MainWindow", "MI"))
        self.State_Province_2.setItemText(28, _translate("MainWindow", "MN"))
        self.State_Province_2.setItemText(29, _translate("MainWindow", "MS"))
        self.State_Province_2.setItemText(30, _translate("MainWindow", "MO"))
        self.State_Province_2.setItemText(31, _translate("MainWindow", "MT"))
        self.State_Province_2.setItemText(32, _translate("MainWindow", "NE"))
        self.State_Province_2.setItemText(33, _translate("MainWindow", "NV"))
        self.State_Province_2.setItemText(34, _translate("MainWindow", "NH"))
        self.State_Province_2.setItemText(35, _translate("MainWindow", "NJ"))
        self.State_Province_2.setItemText(36, _translate("MainWindow", "NM"))
        self.State_Province_2.setItemText(37, _translate("MainWindow", "NY"))
        self.State_Province_2.setItemText(38, _translate("MainWindow", "NC"))
        self.State_Province_2.setItemText(39, _translate("MainWindow", "ND"))
        self.State_Province_2.setItemText(40, _translate("MainWindow", "MP"))
        self.State_Province_2.setItemText(41, _translate("MainWindow", "OH"))
        self.State_Province_2.setItemText(42, _translate("MainWindow", "OK"))
        self.State_Province_2.setItemText(43, _translate("MainWindow", "OR"))
        self.State_Province_2.setItemText(44, _translate("MainWindow", "PW"))
        self.State_Province_2.setItemText(45, _translate("MainWindow", "PA"))
        self.State_Province_2.setItemText(46, _translate("MainWindow", "PR"))
        self.State_Province_2.setItemText(47, _translate("MainWindow", "RI"))
        self.State_Province_2.setItemText(48, _translate("MainWindow", "SC"))
        self.State_Province_2.setItemText(49, _translate("MainWindow", "SD"))
        self.State_Province_2.setItemText(50, _translate("MainWindow", "TN"))
        self.State_Province_2.setItemText(51, _translate("MainWindow", "TX"))
        self.State_Province_2.setItemText(52, _translate("MainWindow", "UT"))
        self.State_Province_2.setItemText(53, _translate("MainWindow", "VT"))
        self.State_Province_2.setItemText(54, _translate("MainWindow", "VI"))
        self.State_Province_2.setItemText(55, _translate("MainWindow", "VA"))
        self.State_Province_2.setItemText(56, _translate("MainWindow", "WA"))
        self.State_Province_2.setItemText(57, _translate("MainWindow", "WV"))
        self.State_Province_2.setItemText(58, _translate("MainWindow", "WI"))
        self.State_Province_2.setItemText(59, _translate("MainWindow", "WY"))
        self.State_Province_2.setItemText(60, _translate("MainWindow", "-CANADA-"))
        self.State_Province_2.setItemText(61, _translate("MainWindow", "AB"))
        self.State_Province_2.setItemText(62, _translate("MainWindow", "BC"))
        self.State_Province_2.setItemText(63, _translate("MainWindow", "MB"))
        self.State_Province_2.setItemText(64, _translate("MainWindow", "NB"))
        self.State_Province_2.setItemText(65, _translate("MainWindow", "NL"))
        self.State_Province_2.setItemText(66, _translate("MainWindow", "NT"))
        self.State_Province_2.setItemText(67, _translate("MainWindow", "NS"))
        self.State_Province_2.setItemText(68, _translate("MainWindow", "NU"))
        self.State_Province_2.setItemText(69, _translate("MainWindow", "ON"))
        self.State_Province_2.setItemText(70, _translate("MainWindow", "PE"))
        self.State_Province_2.setItemText(71, _translate("MainWindow", "QC"))
        self.State_Province_2.setItemText(72, _translate("MainWindow", "SK"))
        self.State_Province_2.setItemText(73, _translate("MainWindow", "YT"))
        self.Item_Codes_btn.setText(_translate("MainWindow", "Get Item Codes"))
        self.Start_Button_2.setText(_translate("MainWindow", "Start"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuContact_Me.setTitle(_translate("MainWindow", "Contact Me"))
        self.actionInstagram_woj_prod.setText(_translate("MainWindow", "Instagram @woj_prod"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.settings = QtCore.QSettings()
        restore(self.settings)

    def closeEvent(self, event):
        save(self.settings)
        super().closeEvent(event)


def restore(settings):
    finfo = QtCore.QFileInfo(settings.fileName())

    if finfo.exists() and finfo.isFile():
        for w in QtWidgets.qApp.allWidgets():
            mo = w.metaObject()
            if w.objectName() and not w.objectName().startswith("qt_"):
                settings.beginGroup(w.objectName())
                for i in range(mo.propertyCount(), mo.propertyOffset() - 1, -1):
                    prop = mo.property(i)
                    if prop.isWritable():
                        name = prop.name()
                        val = settings.value(name, w.property(name))
                        w.setProperty(name, val)
                settings.endGroup()


def save(settings):
    for w in QtWidgets.qApp.allWidgets():
        mo = w.metaObject()
        if w.objectName() and not w.objectName().startswith("qt_"):
            settings.beginGroup(w.objectName())
            for i in range(mo.propertyCount()):
                prop = mo.property(i)
                name = prop.name()
                if prop.isWritable():
                    settings.setValue(name, w.property(name))
            settings.endGroup()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

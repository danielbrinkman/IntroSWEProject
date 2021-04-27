__author__ = "Tyler Bauer AKA tbauer5011"
__copyright__ = "Copyright 2021, Tyler Bauer. All rights reserved."
__version__ = "1.0."
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from django.shortcuts import render, redirect
from selenium.webdriver.common.keys import Keys
from django.http import request
driver = webdriver.Chrome(executable_path=r'D:\Desktop\IntroSWEProject\main_project\chromedriver.exe')
driver.get('http://127.0.0.1:8000/')
p = "Profile"

class testbot(unittest.TestCase):

    def test_5_reservation_without_login(self):
        time.sleep(3)
        try:
            driver.get('http://127.0.0.1:8000/make_reservation/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
        except Exception as e:
            loggedin = False
        self.assertFalse(loggedin)
        time.sleep(1)

    def test_1_failed_login_blank(self):
        time.sleep(3)
       
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//*[text()="Login"]').click()
                time.sleep(1)

            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertFalse(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_2_failed_login_blank_pass(self):
        
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="username"]').send_keys("testtest")
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Login"]').click()
                time.sleep(1)
            
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            self.assertFalse(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_3_failed_login_blank_user(self):
        
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="password"]').send_keys("testtest")
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Login"]').click()
                time.sleep(1)
            
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertFalse(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_4_failed_login_incorrect(self):
        
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="username"]').send_keys("testtest")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="password"]').send_keys("testtest")
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Login"]').click()
                time.sleep(1)

            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertFalse(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_6_register_fail(self):
        
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//*[text()="Register"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="username"]').send_keys("testtest")
                time.sleep(1)

            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertFalse(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_7_register_succeed(self):
        
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                time.sleep(1)
                driver.find_element_by_xpath('//*[text()="Register"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="username"]').send_keys("hello")
                time.sleep(1)
                driver.find_element_by_xpath('//*[@name="password1"]').send_keys("nononono")
                time.sleep(1)
                driver.find_element_by_xpath('//*[@name="password2"]').send_keys("nononono")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="email"]').send_keys("test@test.com")
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Register"]').click()
                time.sleep(1)

            if "Your account has been created." in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertTrue(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)

    def test_8_success_login(self):
       
        try:
            driver.get('http://127.0.0.1:8000/login/')
            time.sleep(3)
            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
                driver.find_element_by_xpath('//input[@name="username"]').send_keys("hello")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="password"]').send_keys("nononono")
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Login"]').click()
                time.sleep(1)

            if p in driver.page_source:
                loggedin = True
            else:
                loggedin = False
            
            self.assertTrue(loggedin)
            time.sleep(1)
        except Exception as e:
            print(e)



    def test_9_reservation_with_login(self):
        try:
                driver.get('http://127.0.0.1:8000/make_reservation/')
                time.sleep(3)
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="peopleCount"]').send_keys("5")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="reservationName"]').send_keys("Bill")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="comments"]').send_keys("Send A lot of bread.")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="reservationTime"]').send_keys("04012021")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="reservationTime"]').send_keys(Keys.TAB)
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="reservationTime"]').send_keys("3333")
                time.sleep(1)
                driver.find_element_by_xpath('//input[@name="reservationTime"]').send_keys(Keys.ARROW_UP)
                time.sleep(1)
                driver.find_element_by_xpath('//button[text()="Confirm"]').click()
                time.sleep(1)
                driver.get('http://127.0.0.1:8000/profile/')
                time.sleep(3)
                
                if "User: " in driver.page_source:
                    profile = True
                else:
                    profile = False
                self.assertTrue(profile)
                time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    unittest.main()
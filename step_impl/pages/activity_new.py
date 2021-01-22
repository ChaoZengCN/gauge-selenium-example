#!/usr/bin/python3
# coding=utf8

import logging
from time import sleep

from selenium import webdriver
from step_impl.pages.log_module import Root_Log
# from log_module import Root_Log

Root_Log.setup_logging()


class Activity_New(object):

    driver_Path = '/usr/bin/chromedriver'
    browser_Path = '/usr/bin/google-chrome'

    chrome_options = webdriver.chrome.options.Options()
    chrome_options.binary_location = browser_Path
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=driver_Path,options=chrome_options)
    driver.implicitly_wait(10)

    def login(self):
        self.driver.get(r'http://tomato.harsons.cn/app/card-test/#/register/login')
        try:
            name = self.driver.find_element_by_xpath('//*[@id="login-container"]/div[5]/form/div[4]/div/div/div/button/span').text
            if name == '登 录':
                logging.debug('进行登录操作...')
                logging.debug('输入用户名： 000zdk')
                self.driver.find_element_by_xpath('//*[@id="loginName"]').send_keys('000zdk')
                sleep(1)
                logging.debug('输入密码: 1')
                self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('1')
                sleep(1)
                logging.debug('点击登录按钮...')
                self.driver.find_element_by_xpath('//*[@id="login-container"]/div[5]/form/div[4]/div/div/div/button/span').click()
                check_text = self.driver.find_element_by_xpath('//*[@id="rc-tabs-test-tab-/index/index"]').text
                if check_text == '首页':
                    logging.info('登录成功...')
                    return True
                else:
                    logging.error('登录失败...')
                    return False
            else:
                logging.error('检测到不是登录页...')
                return False
        except:
            logging.error('登录失败...')
            return False
        self.driver.quit()


if __name__ == "__main__":
    a = Activity_New()
    a.login()

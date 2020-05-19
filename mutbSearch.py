# coding:utf-8
# 保存する場合、utf-8で保存しないと、
# https://teratail.com/questions/120137
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


#インポートされた際にプログラムが動かないようにするために、以下のように if __name__ == "__main__": というif文を書きます。
#https://blog.pyq.jp/entry/Python_kaiketsu_180207
#import hello した：hello.py 内部で __name__ は "hello" という文字列になる
#python hello.py した：hello.py 内部で __name__ は "__main__" という文字列になる
if __name__ == "__main__":

    driver = webdriver.Chrome()

    driver.get('https://www.direct.tr.mufg.jp/ib/dfw/cst/ib/login/GLG01010101.do')
    
    #リンクテキスト名の要素を取得
    element = driver.find_element_by_partial_link_text("ログイン")
    #取得した要素をクリック
    element.click()
    
    #ログインID入力
    #searchElement = driver.element_by_name("input_login_1")
    #searchElement.send_keys('12345678')
    #searchElement.submit()
    #・find_element_by_id：引数に取得したい要素で使われているid属性値を指定することで、要素を取得できる
    #・send_keys：検索テキストボックスに引数を入力
    driver.find_element_by_id('input_login_1').send_keys("12345678")
    driver.find_element_by_id('input_login_2').send_keys("abcdef")

    driver.find_element_by_id("forward()").click()


#############################################################################################

    #リンクテキスト名がqの要素取得
    #  ・引数に取得したい要素で使われているname属性値を指定することで、要素を取得できる
    #searchElement = driver.find_element_by_name("q")
    #searchElement.send_keys('selenium')
    #searchElement.submit()

    #リンクテキスト名が"Gmail"の要素を取得
    #  ・引数に取得したい要素で使われているリンクテキスト名（anchorタグ上のテキスト）を
    #    指定することで、要素を取得できる
    #  ・引数とリンクテキスト名が完全一致する場合に要素を取得する
    #https://www.seleniumqref.com/api/python/window_set/Python_quit.html
    #element = driver.find_element_by_link_text("Gmail")

    #Gmailのリンクをクリック
    #element.click()

    #全てのウィンドウを閉じる
    #    driver.quitforward()
# coding:utf-8
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get('https://google.co.jp/')
    
    #リンクテキスト名がqの要素取得
    #  ・引数に取得したい要素で使われているname属性値を指定することで、要素を取得できる
    searchElement = driver.find_element_by_name("q")

    #リンクテキスト名が"Gmail"の要素を取得
    #  ・引数に取得したい要素で使われているリンクテキスト名（anchorタグ上のテキスト）を
    #    指定することで、要素を取得できる
    #  ・引数とリンクテキスト名が完全一致する場合に要素を取得する
    #element = driver.find_element_by_link_text("Gmail")

    #Gmailのリンクをクリック
    #element.click()



    searchElement.send_keys('selenium')

    searchElement.submit()

#全てのウィンドウを閉じる
#    driver.quit()
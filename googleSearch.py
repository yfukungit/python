# coding:utf-8
from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.get('https://google.co.jp/')
    
    #�����N�e�L�X�g����q�̗v�f�擾
    #  �E�����Ɏ擾�������v�f�Ŏg���Ă���name�����l���w�肷�邱�ƂŁA�v�f���擾�ł���
    searchElement = driver.find_element_by_name("q")

    #�����N�e�L�X�g����"Gmail"�̗v�f���擾
    #  �E�����Ɏ擾�������v�f�Ŏg���Ă��郊���N�e�L�X�g���ianchor�^�O��̃e�L�X�g�j��
    #    �w�肷�邱�ƂŁA�v�f���擾�ł���
    #  �E�����ƃ����N�e�L�X�g�������S��v����ꍇ�ɗv�f���擾����
    #element = driver.find_element_by_link_text("Gmail")

    #Gmail�̃����N���N���b�N
    #element.click()



    searchElement.send_keys('selenium')

    searchElement.submit()

#�S�ẴE�B���h�E�����
#    driver.quit()
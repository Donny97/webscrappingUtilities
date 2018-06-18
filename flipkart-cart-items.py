from selenium import webdriver
from selenium.webdriver import ActionChains
import time
def fk_search():
	browser = webdriver.Firefox()
	browser.get('https://www.flipkart.com/account/login?ret=/')
	user = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div/div[2]/div/form/div[1]/input')
	user.send_keys('Email ID')
	password = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div/div[2]/div/form/div[2]/input')
	password.send_keys('password')
	login = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div/div[2]/div/form/div[3]/button')
	login.click()
	time.sleep(3)

	element = browser.find_element_by_xpath('/html/body/div/div/header/div[3]/div/ul/li[1]/a')
	hover = ActionChains(browser).move_to_element(element)
	hover.perform()

	time.sleep(3)
	nextbtn = browser.find_element_by_xpath('/html/body/div/div/header/div[3]/div/ul/li[1]/ul/li/ul/li[4]/ul/li[3]/a')
	nextbtn.click()
	time.sleep(3)

	forward = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/div/div[2]/div/div[2]/section/ul/li[2]')
	forward.click()
	time.sleep(3)

	posts = browser.find_elements_by_class_name('_2cLu-l')
	for post in posts:
		print(post.text)

	me = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div')
	me.click()

	profile = browser.find_element_by_xpath('/html/body/div/div/header/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/ul/li[1]/a')
	profile.click()
	time.sleep(3)

	logout = browser.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[1]/div/div[2]/div[6]/div/a')
	logout.click()

fk_search()
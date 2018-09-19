from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#elem=driver.find_element_by_id('pthdr2home')

driver=webdriver.Firefox()

#try:
driver.get('http://115.114.127.54:8080/psp/bitcsprd/?cmd=login&languageCd=UKE')
elem=driver.find_element_by_xpath("//a[@title='English']")
elem.click()
elem=driver.find_element_by_id('userid')
elem.send_keys("B21282")
elem=driver.find_element_by_id('pwd')
elem.send_keys("@bioshock")
elem.send_keys(Keys.ENTER)
#except Exception as e:
#	if driver.find_element_by_id("login_error")!= "":
#		print("Incorrect Password")
##		print("Server Down")
#	else:
#		print("Unknown Exception")
#
#	driver.close()
#
try:
	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"pthdr2home")))
	elem.click()

	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.NAME,"TargetContent")))

#elem=driver.find_element_by_name('TargetContent')
	var=elem.get_attribute('src')
	driver.get(var)

	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"DERIVED_SSS_SCR_SSS_LINK_ANCHOR7")))

#elem=driver.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR7')
	elem.click()

	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"SSR_DUMMY_RECV1$sels$0")))

#elem=driver.find_element_by_id('SSR_DUMMY_RECV1$sels$0')
	elem.click() 

	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"DERIVED_AA2_B_ATTEND_ROSTER")))

#elem=driver.find_element_by_id('DERIVED_AA2_B_ATTEND_ROSTER')
	elem.click()
except TimeoutException as e:
	print("Timed out. Retrying")
	driver.close()
import sys
import os 
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

login=""
Password=""
delay=60

def main():
	op=Options()
	op.headless=True
	driver=webdriver.Firefox(options=op)
	driver.set_window_size(850,900)
	try:
		global login 
		global Password
		if (len(sys.argv)==1):
			raise Exception("Enter the username and Password")
		login=sys.argv[1]
		Password=sys.argv[2]
		print "Please wait. Fetching your information. Depending upon the server it may take 2-3 minutes"
		connect(login,Password,driver)		
		get_attendance(driver)
	except Exception as e:
		print(e.args)
		driver.close()

def connect(login,Password,driver):
	driver.get('http://115.114.127.54:8080/psc/bitcsprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.B_SS_ATTEND_ROSTER.GBL?Page=B_SS_ATTEND_ROSTER&Action=U&TargetFrameName=None')
	elem=driver.find_element_by_xpath("//a[@title='English']")
	elem.click()
	elem=driver.find_element_by_id('userid')
	elem.clear()
	elem.send_keys(login)
	elem=driver.find_element_by_id('pwd')
	elem.clear()
	elem.send_keys(Password)
	elem.send_keys(Keys.ENTER)
	
	#WebDriverWait(driver,120).until(lambda x: x.execute_script("return document.readystate") != "complete")
	WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID,"SSR_DUMMY_RECV1$sels$0")))
	#time.sleep(2)
	if(driver.title=="Oracle | PeopleSoft Enterprise Sign-in"):
	#	WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.ID,"login_error")))
		if driver.find_element_by_id("login_error").text!= "":
			raise Exception("Invalid username or Password")
		elif driver.find_element_by_id("discovery_error").text!= "":
			raise Exception("Server Down")
		else:
			raise Exception("Unknown Error")

def get_attendance(driver):
	try:
		#elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"pthdr2home")))
		#elem.click()
	
		#elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.NAME,"TargetContent")))
	#var=elem.get_attribute('src')
#		driver.get(var)
	
	#	elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"DERIVED_SSS_SCR_SSS_LINK_ANCHOR7")))
	#	elem.click()
	
		elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"SSR_DUMMY_RECV1$sels$0")))
		elem.click() 
		elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"DERIVED_AA2_B_ATTEND_ROSTER")))
		elem.click()
		elem=WebDriverWait(driver,120).until(EC.presence_of_element_located((By.ID,"CLASS_TBL_VW$scroll$0")))
		driver.save_screenshot("screen.png")
		if sys.platform == 'linux2':
			subprocess.call(["xdg-open","screen.png"])
		else:
			os.startfile(file)
		driver.close()
	except selenium.common.exceptions.TimeoutException:
		print("Timed out. Terminating")
		driver.close()


main()
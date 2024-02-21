# Create a search page object class

from selenium.webdriver.common.by import By

class SearchPage:
    #Locators
#Syntax: Variable Name=locator
    expand_btn_xpath="//span[normalize-space()='Expand all']"
    name_input_xpath="//input[@class='ipc-textfield__input' and @aria-label='Name']"
    birth_date_input_xpath="//input[@name='birth-date-start-input']"
    birth_day_input_xpath = "//input[@class='ipc-textfield__input' and @aria-label='Enter birthday']"
    awards_button_xpath = "//div[@id='awardsAccordion']//button[2]"
    page_button_xpath = "//div[@id='pageTopicsAccordion']//button[1]"
    birth_place_select_xpath = "//select[@id='within-topic-dropdown-id']"
    birth_place_option_xpath = "//option[@value='BIRTH_PLACE']"
    gender_button_xpath = "//div[@id='genderIdentityAccordion']//button[1]"
    search_button_xpath = "//button[@aria-label='See results']"

    #constructor
#Constructor which will iniate the driver.
#Use of constructor is which will executed automatically whenever we created an object of the class.
    def __init__(self,driver):
        self.driver=driver

    #action methods
    def disableExpandBtn(self):
        self.driver.find_element(By.XPATH,self.expand_btn_xpath).click()

    def setNameInput(self,name):
        nametext=self.driver.find_element(By.XPATH,self.name_input_xpath)
        nametext.clear()
        nametext.send_keys(name)

    def setBirthDate(self, birthdate):
        birthdatetext = self.driver.find_element(By.XPATH, self.birth_date_input_xpath)
        birthdatetext.clear()
        birthdatetext.send_keys(birthdate)

    def setBirthDay(self, birthday):
        birthdaytext = self.driver.find_element(By.XPATH, self.birth_day_input_xpath)
        birthdaytext.clear()
        birthdaytext.send_keys(birthday)

    def setAwardsBtn(self):
        self.driver.find_element(By.XPATH, self.awards_button_xpath).click()

    def setPageBtn(self):
        self.driver.find_element(By.XPATH,self.page_button_xpath).click()

    def setBirthPlaceSelect(self):
        self.driver.find_element(By.XPATH,self.birth_place_select_xpath).click()

    def setBirthPlaceOption(self):
        self.driver.find_element(By.XPATH,self.birth_place_option_xpath).click()

    def setGenderBtn(self):
        self.driver.find_element(By.XPATH,self.gender_button_xpath).click()

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

WebdriverPath = r"C:\Users\stawowcz\Desktop\moje\sofomo_zadanie\chromedriver.exe"
MainWebUrl = "http://automationpractice.com/"
SignInUrl = "header_user_info"
EmailCreateUrl = "email_create"
SubmitCreateUrl = "SubmitCreate"
LoginEmailUrl = "email"
LoginPassUrl = "passwd"
InvalidEmailAdress = "1@!@!sssssss"
CreateAccountUrl = "http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation"
MrUrl = "id_gender1"
MrsUrl = "id_gender2"
CustomerFirstNameIdUrl = "customer_firstname"
CustomerLastNameIdUrl = "customer_lastname"
CreateEmailIdUrl = "email"
CreatePassIdUrl = "passwd"
DaysArrowIdUrl = "days"
MonthArrowIdUrl = "months"
YearArrorIdUrl = "years"
NewsellerIdUrl = "uniform-newsletter"
OptinIdUrl = "optin"
FirstNameIdUrl = "firstname"
LastNameIdUrl = "lastname"
CompanyIdUrl = "company"
AdressIdUrl = "address1"
Adress2IdUrl = "address2"
CityIdUrl = "city"
StateIdUrl = "id_state"
PostcodeIdUrl = "postcode"
CountryIdUrl = "id_country"
AdInfoIdUrl = "other"
PhoneIdUrl = "phone"
PhoneMobileIdUrl = "phone_mobile"
MyAddresIdUrl = "alias"
RagisterIdUrl = "submitAccount"
SubmitLoginIdUrl = "SubmitLogin"
ForgotPassClassUrl = "lost_password form-group"
ForgotPassEmailId = "email"
ForgotPassEmailXpathsBtnUrl = "/html/body/div/div[2]/div/div[3]/div/div/form/fieldset/p/button"
ForgotYourPaswordLinkUrl = "Forgot your password?"
HomeButtonXpathUrl = "/html/body/div/div[2]/div/div[3]/div/ul/li/a"
LoggedUserXpath = "/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a"
SignOutXpathUrl = "/html/body/div/div[1]/header/div[2]/div/div/nav/div[2]/a"
LoggedUserUrl = "http://automationpractice.com/index.php?controller=my-account"
WebPageSubHeaderUrl = "/html/body/div/div[2]/div/div[3]/div/div/form/div[1]/h3"
EmailAlreadyUsedValueUrl = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[1]/ol/li"
EmptyEmailAdressValueURL = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[1]/ol/li"
InvalidEmailAdressValueURL = "/html/body/div/div[2]/div/div[3]/div/div/div[1]/form/div/div[1]"
ErrorsValueAllFieldsEmptyUrl ="/html/body/div/div[2]/div/div[3]/div/div/p"
SuccessfullySignUpUrl = "/html/body/div/div[2]/div/div[3]/div/p"
StarsEncryptedPassUrl = "/html/body/div/div[2]/div/div[3]/div/form/div[1]/div[5]/label/sup"
FirstNameIsRequiredUrl = "/html/body/div/div[2]/div/div[3]/div/div/ol/li/b"
TenErrorsValueAllFieldsEmptyUrl = "/html/body/div/div[2]/div/div[3]/div/div/p"
AutehenticationTitleUrl = "/html/body/div/div[2]/div/div[3]/div/div[1]/ol/li"
InvalidEmailLoginUrl = "/html/body/div/div[2]/div/div[3]/div/div[1]/ol/li"
AuthenticationFailedInLoginUrl = "/html/body/div/div[2]/div/div[3]/div/div[1]"
PasswordIsRequiredLoginUrl = "/html/body/div/div[2]/div/div[3]/div/div[1]/ol/li"
EmailIsRequiredUrl = "/html/body/div/div[2]/div/div[3]/div/div[1]/ol/li"
InvalidEmailInPasRetrUrl = "/html/body/div/div[2]/div/div[3]/div/div/div/ol/li"
ConfirmationEmailTextUrl = "/html/body/div/div[2]/div/div[3]/div/div/p"




class Test_Sofomo:

#First step before registration form
#Check if Email fields is visible, automated in tect_case1
#Check if framse is highlighted in red if it is empty, automated in tect_case1
#Check if framse is highlighted in blue if it is fullfiled properly, automate in test_case1
#Check if frames are highlighted in blue when cursor in on it automated in test_case1  
#Check if placeholder are red when it is empty automated in test_case1

    def test_case1(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(MainWebUrl)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_class_name(SignInUrl)).click()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast1_case1.png')
        self.driver.find_element_by_id(EmailCreateUrl).click()
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast1_case2.png')
        self.driver.find_element_by_id(LoginEmailUrl).click()
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast1_case3.png')
        self.driver.find_element_by_id(LoginPassUrl).click()
        time.sleep(2)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast1_case4.png')
        status = self.driver.find_element_by_id(LoginPassUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        time.sleep(1)
        self.driver.quit()

    #Click create an account with good email address, automated in test case2
    def test_case2(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(MainWebUrl)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_class_name(SignInUrl)).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jakubtest123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test2_case1.png')
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test2_case2.png')
        status = self.driver.find_element_by_xpath(WebPageSubHeaderUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False

        self.driver.quit()

    #Click create an account with already used email address, automateded in test case 3
    def test_case3(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(MainWebUrl)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_class_name(SignInUrl)).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("test_1@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test3_case1.png')
        time.sleep(3)
        status = self.driver.find_element_by_xpath(EmailAlreadyUsedValueUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Click create an account without email, automated test_case4
    def test_case4(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(MainWebUrl)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_class_name(SignInUrl)).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test4_case1.png')
        status = self.driver.find_element_by_xpath(EmptyEmailAdressValueURL).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Click create an account with invalid email address, to do
    def test_case5(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(MainWebUrl)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(lambda driver: self.driver.find_element_by_class_name(SignInUrl)).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(EmailCreateUrl).send_keys(InvalidEmailAdress)
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test5_case1.png')
        time.sleep(3)
        status = self.driver.find_element_by_xpath(InvalidEmailAdressValueURL).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Second step
    #Check if all fields are visibled in form like firstname, lastname, password, to do
    #Check if all required fields has star stamp,
    #Check if all placeholder are empty by default expect this that you fullfiled previously, automate
    #Check if it is confirm password label, automate
    def test_case6(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jstawowcztest1231@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test6_case1.png')
        time.sleep(5)
        self.driver.quit()

    def test_case6_1(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jstawowcztest1231@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 700)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test6_case2.png')
        time.sleep(10)
        self.driver.quit()

    def test_case6_2(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jstawowcztest1231@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test6_case3.png')
        time.sleep(5)
        self.driver.quit()

    def test_case6_3(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jstawowcztest1231@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1500)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test6_case4.png')
        time.sleep(5)
        self.driver.quit()

    #Check if the frames are highlighted in blue when they are fullfield, automated in test_case7
    #Check if it was unsuccessfull registration after left all fields empty, automated in test_case7
    #Check if "Sign up for our newsletter!", "Receive special offers from our partners!
    #" works are clickable (to automate) automated in test_case7
    #Check if registration message is visible after click on register button, automated in test_case7
    #Check if there are proper validation message after left empty all fields, automated in test_case7
    def test_case7(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jstawowcztest1231@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(MrUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case1.png')
        time.sleep(3)
        self.driver.find_element_by_id(MrsUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case2.png')
        self.driver.find_element_by_id(CustomerFirstNameIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case3.png')
        self.driver.find_element_by_id(CustomerLastNameIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case4.png')
        self.driver.find_element_by_id(CreateEmailIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case5.png')
        self.driver.find_element_by_id(CreatePassIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case6.png')
        self.driver.find_element_by_id(DaysArrowIdUrl).click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case7.png')
        self.driver.find_element_by_id(MonthArrowIdUrl).click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case8.png')
        self.driver.find_element_by_id(YearArrorIdUrl).click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case9.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case10.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case11.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case12.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case13.png')
        self.driver.find_element_by_id(FirstNameIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case14.png')
        self.driver.find_element_by_id(LastNameIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case15.png')
        self.driver.find_element_by_id(CompanyIdUrl).click()
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case16.png')
        self.driver.find_element_by_id(AdressIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case17.png')
        self.driver.find_element_by_id(Adress2IdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case18.png')
        self.driver.find_element_by_id(CityIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case19.png')
        self.driver.find_element_by_id(StateIdUrl).click()
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case20.png')
        self.driver.find_element_by_id(PostcodeIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case21.png')
        self.driver.find_element_by_id(CountryIdUrl).click()
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case22.png')
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case23.png')
        self.driver.find_element_by_id(AdInfoIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case24.png')
        self.driver.find_element_by_id(PhoneIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case25.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case26.png')
        self.driver.find_element_by_id(MyAddresIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case27.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case28.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test7_case29.png')
        status = self.driver.find_element_by_xpath(ErrorsValueAllFieldsEmptyUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #CHeck if combobox is expended down when cursos is on it,  automated test_case8
    #Check if password is encrypted, automated test_case8 
    #Check if data prosesses to server after fullfilling all fields and signup is successull, automated in test_case8
    def test_case8(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jakub1222333678@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(MrUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case1.png')
        time.sleep(3)
        self.driver.find_element_by_id(CustomerFirstNameIdUrl).send_keys("Jan")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case3.png')
        self.driver.find_element_by_id(CustomerLastNameIdUrl).send_keys("Jankowski")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case4.png')
        self.driver.find_element_by_id(CreatePassIdUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case6.png')
        element = self.driver.find_element_by_id(DaysArrowIdUrl)
        drp = Select(element)
        drp.select_by_value("30")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case7.png')
        element = self.driver.find_element_by_id(MonthArrowIdUrl)
        drp = Select(element)
        drp.select_by_index(7)
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case8.png')
        element = self.driver.find_element_by_id(YearArrorIdUrl)
        drp = Select(element)
        drp.select_by_value("2000")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case9.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case10.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case11.png')
        self.driver.find_element_by_id(CompanyIdUrl).send_keys("Dobra")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case16.png')
        self.driver.find_element_by_id(AdressIdUrl).send_keys("Boleslawiecka 1")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case17.png')
        self.driver.find_element_by_id(Adress2IdUrl).send_keys("Boleslawiecka 2")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case18.png')
        self.driver.find_element_by_id(CityIdUrl).send_keys("Wroclaw")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case19.png')
        element = self.driver.find_element_by_id(StateIdUrl)
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case20.png')
        self.driver.find_element_by_id(PostcodeIdUrl).send_keys(54200)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case21.png')
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case23.png')
        self.driver.find_element_by_id(AdInfoIdUrl).send_keys("Additional info")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case24.png')
        self.driver.find_element_by_id(PhoneIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case25.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case26.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case28.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test8_case29.png')
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if it was successfull registration after fullfiling all fields except this without requireds star stamp, automated in test_case9
    def test_case9(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jasakub12342130@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(CustomerFirstNameIdUrl).send_keys("Jan")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case1.png')
        self.driver.find_element_by_id(CustomerLastNameIdUrl).send_keys("Jankowski")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case2.png')
        self.driver.find_element_by_id(CreatePassIdUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case3.png')
        self.driver.find_element_by_id(AdressIdUrl).send_keys("Boleslawiecka 1")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case4.png')
        self.driver.find_element_by_id(CityIdUrl).send_keys("Wroclaw")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case5.png')
        element = self.driver.find_element_by_id(StateIdUrl)
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case6.png')
        self.driver.find_element_by_id(PostcodeIdUrl).send_keys(54200)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case7.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case8.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case9.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test9_case10.png')
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if login are going to be unssuccessfylly without any of required field
    def test_case10(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jakubbu12345326@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(MrUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case1.png')
        time.sleep(3)
        self.driver.find_element_by_id(CustomerLastNameIdUrl).send_keys("Jankowski")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case2.png')
        self.driver.find_element_by_id(CreatePassIdUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case3.png')
        element = self.driver.find_element_by_id(DaysArrowIdUrl)
        drp = Select(element)
        drp.select_by_value("30")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case4.png')
        element = self.driver.find_element_by_id(MonthArrowIdUrl)
        drp = Select(element)
        drp.select_by_index(7)
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case5.png')
        element = self.driver.find_element_by_id(YearArrorIdUrl)
        drp = Select(element)
        drp.select_by_value("2000")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case6.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case7.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case8.png')
        self.driver.find_element_by_id(CompanyIdUrl).send_keys("Dobra")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case9.png')
        self.driver.find_element_by_id(AdressIdUrl).send_keys("Boleslawiecka 1")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case10.png')
        self.driver.find_element_by_id(Adress2IdUrl).send_keys("Boleslawiecka 2")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case11.png')
        self.driver.find_element_by_id(CityIdUrl).send_keys("Wroclaw")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case12.png')
        element = self.driver.find_element_by_id(StateIdUrl)
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case13.png')
        self.driver.find_element_by_id(PostcodeIdUrl).send_keys(54200)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case14.png')
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case15.png')
        self.driver.find_element_by_id(AdInfoIdUrl).send_keys("Additional info")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case16.png')
        self.driver.find_element_by_id(PhoneIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case17.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case18.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case19.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test10_case20.png')
        status = self.driver.find_element_by_xpath(FirstNameIsRequiredUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    # Check if registration is unsuccessfull with password less than 5 position automated in test_case11
    # Verify that digit in last name and first name  cause an error automated in test_case11
    # Check if registration is unsuccessfull with wrong format mobile phone, automated in test_case11
    # Check if registration is unsuccessfull with wrong format of postcode, automated in test_case11
    def test_case11(self):
        
        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("###$!jakub1234567@gmail.com")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(MrUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case1.png')
        time.sleep(3)
        self.driver.find_element_by_id(CustomerFirstNameIdUrl).send_keys("Jan5")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case3.png')
        self.driver.find_element_by_id(CustomerLastNameIdUrl).send_keys("Jankowski5")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case4.png')
        self.driver.find_element_by_id(CreatePassIdUrl).send_keys("k#12")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case6.png')
        element = self.driver.find_element_by_id(DaysArrowIdUrl)
        drp = Select(element)
        drp.select_by_value("30")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case7.png')
        element = self.driver.find_element_by_id(MonthArrowIdUrl)
        drp = Select(element)
        drp.select_by_index(7)
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case8.png')
        element = self.driver.find_element_by_id(YearArrorIdUrl)
        drp = Select(element)
        drp.select_by_value("2000")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case9.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case10.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case11.png')
        self.driver.find_element_by_id(CompanyIdUrl).send_keys("%Dobra")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case16.png')
        self.driver.find_element_by_id(AdressIdUrl).send_keys("$$Boleslawiecka 1")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case17.png')
        self.driver.find_element_by_id(Adress2IdUrl).send_keys("@#Boleslawiecka 2")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case18.png')
        self.driver.find_element_by_id(CityIdUrl).send_keys("!@12Wroclaw")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case19.png')
        element = self.driver.find_element_by_id(StateIdUrl)
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case20.png')
        self.driver.find_element_by_id(PostcodeIdUrl).send_keys("@55555")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case21.png')
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case23.png')
        self.driver.find_element_by_id(AdInfoIdUrl).send_keys("################@2121Additional info")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case24.png')
        self.driver.find_element_by_id(PhoneIdUrl).send_keys("222-222-22@")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case25.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).send_keys("@22222222")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case26.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case28.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test11_case29.png')
        status = self.driver.find_element_by_xpath(TenErrorsValueAllFieldsEmptyUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    # Check if there is not difference with letter size in all fields, automated in test_case12
    def test_case12(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("JAKKUB123321@GMAIL.COM")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.find_element_by_id(MrUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case1.png')
        time.sleep(3)
        self.driver.find_element_by_id(CustomerFirstNameIdUrl).send_keys("JAN")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case3.png')
        self.driver.find_element_by_id(CustomerLastNameIdUrl).send_keys("JANKOWSKI")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case4.png')
        self.driver.find_element_by_id(CreatePassIdUrl).send_keys("K1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case6.png')
        element = self.driver.find_element_by_id(DaysArrowIdUrl)
        drp = Select(element)
        drp.select_by_value("30")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case7.png')
        element = self.driver.find_element_by_id(MonthArrowIdUrl)
        drp = Select(element)
        drp.select_by_index(7)
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case8.png')
        element = self.driver.find_element_by_id(YearArrorIdUrl)
        drp = Select(element)
        drp.select_by_value("2000")
        time.sleep(3)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case9.png')
        self.driver.find_element_by_id(NewsellerIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case10.png')
        self.driver.find_element_by_id(OptinIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case11.png')
        self.driver.find_element_by_id(CompanyIdUrl).send_keys("DOBRA")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case16.png')
        self.driver.find_element_by_id(AdressIdUrl).send_keys("BOLESLAWIECKA 1")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case17.png')
        self.driver.find_element_by_id(Adress2IdUrl).send_keys("BOLESLAWIECKA 2")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case18.png')
        self.driver.find_element_by_id(CityIdUrl).send_keys("WROCLAW")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case19.png')
        element = self.driver.find_element_by_id(StateIdUrl)
        drp = Select(element)
        drp.select_by_visible_text("Alabama")
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case20.png')
        self.driver.find_element_by_id(PostcodeIdUrl).send_keys(54200)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case21.png')
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case23.png')
        self.driver.find_element_by_id(AdInfoIdUrl).send_keys("ADDITIONAL INFO")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case24.png')
        self.driver.find_element_by_id(PhoneIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case25.png')
        self.driver.find_element_by_id(PhoneMobileIdUrl).send_keys(222222222)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case26.png')
        element = self.driver.find_element_by_id(RagisterIdUrl)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case28.png')
        self.driver.find_element_by_id(RagisterIdUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test12_case29.png')
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()
        
    # Check if the system distinguishes capital and small letter in already used email, automated in test_case13
    def test_case13(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("JAKUB123@GMAIL.COM")
        self.driver.find_element_by_id(SubmitCreateUrl).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test13_case1.png')
        self.driver.find_element_by_id(EmailCreateUrl).clear()
        self.driver.find_element_by_id(EmailCreateUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/test13_case2.png')
        status = self.driver.find_element_by_xpath(EmailAlreadyUsedValueUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()
    
    # SIGNIN TEST
    # Check if cursor is focus on email placeholder, automated in test_case14
    # Check if form contains element like username password, sign in button, forgot your password, automated in test_case14
    # Check if all fields are empty and unmarked by default automated in test_case14
    def test_case14(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast14_case1.png')
        status = self.driver.find_element_by_xpath(AutehenticationTitleUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is able to login with valid credential automated in test_case15
    def test_case15(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast15_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast15_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast15_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is unable to login with invalid credential automated in test_case16
    def test_case16(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast16_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k123")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast16_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast16_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(InvalidEmailLoginUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is unable to login with proper username and invalid password automated in test_case17
    def test_case17(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast17_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234@")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast17_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast17_case3.png')
        status = self.driver.find_element_by_xpath(AuthenticationFailedInLoginUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is unable to login with invalid username and proper password  automated in test_case18
    def test_case18(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast18_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast18_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast18_case3.png')
        status = self.driver.find_element_by_xpath(InvalidEmailLoginUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is unable to login with proper username and empty password automated in test_case19
    def test_case19(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast19_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast19_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast19_case3.png')
        time.sleep(1)
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast18_case3.png')
        status = self.driver.find_element_by_xpath(PasswordIsRequiredLoginUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is unable to login with empty email and proper 
    # password automated in test_case20
    def test_case20(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast20_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast20_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast20_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(EmailIsRequiredUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    # Check if space are not allowed in password, 
    # space are not visible by system
    def test_case21(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast21_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("   k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast21_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast21_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert False
        else:
            assert True
        self.driver.quit()

    #Check if validation field is as excepted when email field is empty in retrieving password form
    #Check if all fields and button and clickable in retrieving password form
    def test_case22(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_link_text(ForgotYourPaswordLinkUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast22_case1.png')
        self.driver.find_element_by_id(ForgotPassEmailId).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast22_case2.png')
        self.driver.find_element_by_xpath(ForgotPassEmailXpathsBtnUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast22_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(InvalidEmailInPasRetrUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    # Check if confirmation email of changing password was sent. 
    # Automated in test_case23, email was not sent
    def test_case23(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_link_text(ForgotYourPaswordLinkUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast23_case1.png')
        self.driver.find_element_by_id(ForgotPassEmailId).send_keys("jstawowcz@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast23_case2.png')
        self.driver.find_element_by_xpath(ForgotPassEmailXpathsBtnUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast23_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(ConfirmationEmailTextUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()
        
    #Check if user is still log in  after clicking refresh button automated in test_cas24 
    #Check if user is still log in after clicking back and forward button browser button  automated in test_case24
    #Check if user is still log in after clicking home button 
    def test_case24(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case3.png')
        self.driver.refresh()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case4.png')
        time.sleep(3)
        self.driver.back()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case5.png')
        self.driver.forward()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case6.png')
        self.driver.find_element_by_xpath(HomeButtonXpathUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case7.png')
        self.driver.find_element_by_xpath(LoggedUserXpath).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast24_case8.png')
        time.sleep(3)
        status = self.driver.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is still log out after clicking log out button automated in test_case25
    #Check if user is after loga out is not log in after clicking back button automated in test_case25
    def test_case25(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case3.png')
        self.driver.find_element_by_xpath(SignOutXpathUrl).click()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case4.png')
        time.sleep(3)
        self.driver.back()
        self.driver.execute_script("window.scrollTo(0, 300)")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case5.png')
        time.sleep(2)
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast25_case6.png')
        time.sleep(3)
        status = self.driver.find_element_by_xpath(EmailIsRequiredUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()

    #Check if user is still log in after closing of explorer
    def test_case26(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast26_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("k1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast26_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast26_case3.png')
        time.sleep(3)
        self.driver.quit()
        self.driver2 = webdriver.Chrome(WebdriverPath)
        self.driver2.set_page_load_timeout(10)
        self.driver2.get(LoggedUserUrl)
        time.sleep(3)
        self.driver2.execute_script("window.scrollTo(0, 300)") 
        self.driver2.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast26_case4.png')
        status = self.driver2.find_element_by_xpath(SuccessfullySignUpUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver2.quit()

    #Check if password is case sensitive
    def test_case27(self):

        self.driver = webdriver.Chrome(WebdriverPath)
        self.driver.set_page_load_timeout(10)
        self.driver.get(CreateAccountUrl)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 300)") 
        self.driver.find_element_by_id(LoginEmailUrl).send_keys("jakub123@gmail.com")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast27_case1.png')
        self.driver.find_element_by_id(LoginPassUrl).send_keys("K1234")
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast27_case2.png')
        self.driver.find_element_by_id(SubmitLoginIdUrl).click()
        self.driver.save_screenshot('C:/Users/stawowcz/Desktop/moje/sofomo_zadanie/test_pictures/tast27_case3.png')
        time.sleep(1)
        status = self.driver.find_element_by_xpath(AuthenticationFailedInLoginUrl).is_displayed()
        if status == True:
            assert True
        else:
            assert False
        self.driver.quit()


        
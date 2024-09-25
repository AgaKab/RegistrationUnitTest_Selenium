from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from selenium.webdriver.support.select import Select

# Dane testowe
email = "tester@testowanie.pl"
gender = "female"
last_name = "Nowakowskystein"
password = "djknfjDDj879s"
birth_day = "13"
birth_month = "1"
birth_year = "1990"

# Dokumentacja przypadku test. w Wordzie

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Warunki wstępne
        self.driver = webdriver.Chrome()
        self.driver.get("https://watermark.pinta.pro/prestashop16/en/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def testNoNameEntered(self):
        # Kroki
        # 1.Kliknij sign-in
        sign_in_a = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
        print(type(sign_in_a))
        sign_in_a.click()
        sleep(5)

        # Wpisz e-maiL
        email_create_box = self.driver.find_element(By.ID, "email_create")
        email_create_box.send_keys(email)
        sleep(5)

        # Kliknij "create an account"
        create_button = self.driver.find_element(By.NAME, "SubmitCreate")
        create_button.click()

        # Wybierz płeć
        if gender == "female":
            self.driver.find_element(By.ID,"id_gender2").click()
        else:
            self.driver.find_element(By.ID, "id_gender1").click()

        # Wpisz nazwisko
        last_name_input = self.driver.find_element(By.XPATH, '//input[@id="customer_lastname"]')
        last_name_input.send_keys(last_name)

        # Sprawdz czy email jest taki sam jak podany wczesniej
        email_check = self.driver.find_element(By.ID,"email")
        email_value = email_check.get_attribute("value")
        print(email_value)
        self.assertEqual(email, email_value)

        # Wpisz hasło
        password_box = self.driver.find_element(By.NAME, "passwd")
        password_box.send_keys(password)

        # Wybierz date urodzenia
        day_select = Select(self.driver.find_element(By.ID, "days"))
        day_select.select_by_value(birth_day)

        month_select = Select(self.driver.find_element(By.ID, "months"))
        month_select.select_by_value(birth_month)

        year_select = Select(self.driver.find_element(By.ID, "years"))
        year_select.select_by_value(birth_year)


        # Kliknij register
        self.driver.find_element(By.ID, "submitAccount").click()



        # REZULTAT
        # Info. że jeden błąd
        error_notice = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger']/p").text
        self.assertEqual("There is 1 error", error_notice)

        # Info. że nie ma imienia
        # find_elementS - wyrzuca wszystkie elemanty znalezione w postaci listy
        no_name_notice = self.driver.find_elements(By.XPATH, "//div[@class='alert alert-danger']/ol/li")
        self.assertEqual(1, len(no_name_notice))
        self.assertEqual("firstname is required.", no_name_notice[0].text)


    def tearDown(self):
        self.driver.quit()





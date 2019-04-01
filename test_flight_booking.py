# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from flight_details import Booking
from flight_details import Payment



class TestFlightBooking(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(executable_path='drivers/chromedriver')
        self.wd.implicitly_wait(30)

    def test_flight_booking(self):
        self.open_home_page()
        self.login(username="mercury", password="mercury")
        self.flight_booking(Booking(from_port="London",
                                departure_month="April",
                                departure_date="7",
                                to_port="New York",
                                return_month= "April",
                                return_date= "20"))
        self.flight_purchase(Payment(pas_first_name="helen",
                                 pas_last_name="conor",
                                 meal_option="Vegetarian",
                                 cc_type="Visa",
                                 cc_number="4678576578",
                                 cc_exp_month="07",
                                 cc_exp_year="2010",
                                 bill_address="12 Normanbyroad",
                                 city="Auckland",
                                 zip_code="3192",
                                 country="NEW ZEALAND"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='$588 USD'])[1]/following::img[4]").click()

    def flight_purchase(self, payment):
        wd = self.wd
        wd.find_element_by_name("reserveFlights").click()
        wd.find_element_by_name("passFirst0").click()
        wd.find_element_by_name("passFirst0").clear()
        wd.find_element_by_name("passFirst0").send_keys(payment.pas_first_name)
        wd.find_element_by_name("passLast0").clear()
        wd.find_element_by_name("passLast0").send_keys(payment.pas_last_name)
        wd.find_element_by_name("pass.0.meal").click()
        Select(wd.find_element_by_name("pass.0.meal")).select_by_visible_text(payment.meal_option)
        wd.find_element_by_name("creditCard").click()
        Select(wd.find_element_by_name("creditCard")).select_by_visible_text(payment.cc_type)
        wd.find_element_by_name("creditnumber").click()
        wd.find_element_by_name("creditnumber").clear()
        wd.find_element_by_name("creditnumber").send_keys(payment.cc_number)
        wd.find_element_by_name("cc_exp_dt_mn").click()
        Select(wd.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text(payment.cc_exp_month)
        wd.find_element_by_name("cc_exp_dt_yr").click()
        Select(wd.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text(payment.cc_exp_year)
        wd.find_element_by_name("cc_frst_name").click()
        # billing address
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Billing Address'])[1]/following::tr[1]").click()
        wd.find_element_by_name("billAddress1").clear()
        wd.find_element_by_name("billAddress1").send_keys(payment.bill_address)
        wd.find_element_by_name("billCity").click()
        wd.find_element_by_name("billCity").clear()
        wd.find_element_by_name("billCity").send_keys(payment.city)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='State/Province:'])[1]/following::td[1]").click()
        wd.find_element_by_name("billState").click()
        wd.find_element_by_name("billState").clear()
        wd.find_element_by_name("billState").send_keys("")
        wd.find_element_by_name("billZip").click()
        wd.find_element_by_name("billZip").clear()
        wd.find_element_by_name("billZip").send_keys(payment.zip_code)
        wd.find_element_by_name("billCountry").click()
        Select(wd.find_element_by_name("billCountry")).select_by_visible_text(payment.country)
        wd.find_element_by_name("buyFlights").click()

    def flight_booking(self, booking):
        wd = self.wd
        wd.find_element_by_name("tripType").click()
        wd.find_element_by_xpath("//select[@name='passCount']").click()
        wd.find_element_by_name("passCount").click()
        # from port
        wd.find_element_by_name("fromPort").click()
        Select(wd.find_element_by_name("fromPort")).select_by_visible_text(booking.from_port)
        wd.find_element_by_name("fromMonth").click()
        Select(wd.find_element_by_name("fromMonth")).select_by_visible_text(booking.departure_month)
        wd.find_element_by_name("fromDay").click()
        Select(wd.find_element_by_name("fromDay")).select_by_visible_text(booking.departure_date)
        wd.find_element_by_name("toPort").click()
        # to destionation
        Select(wd.find_element_by_name("toPort")).select_by_visible_text(booking.to_port)
        wd.find_element_by_name("toMonth").click()
        Select(wd.find_element_by_name("toMonth")).select_by_visible_text(booking.return_month)
        wd.find_element_by_name("toDay").click()
        Select(wd.find_element_by_name("toDay")).select_by_visible_text(booking.return_date)
        # select airline
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Airline:'])[1]/preceding::input[2]").click()
        wd.find_element_by_name("airline").click()
        Select(wd.find_element_by_name("airline")).select_by_visible_text("Blue Skies Airlines")
        wd.find_element_by_name("findFlights").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 361'])[1]/preceding::input[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Blue Skies Airlines 631'])[1]/preceding::input[1]").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("userName").click()
        wd.find_element_by_name("userName").clear()
        wd.find_element_by_name("userName").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://newtours.demoaut.com/mercurysignon.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
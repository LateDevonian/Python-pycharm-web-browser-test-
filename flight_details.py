class Booking:
    def __init__(self, from_port, departure_month, departure_date, to_port, return_month, return_date):
        self.from_port = from_port
        self.departure_month = departure_month
        self.departure_date = departure_date
        self.to_port = to_port
        self.return_month = return_month
        self.return_date = return_date

class Payment:
    def __init__(self, pas_first_name, pas_last_name, meal_option, cc_type, cc_number, cc_exp_month,
                 cc_exp_year, bill_address, city, zip_code, country):
        self.pas_first_name = pas_first_name
        self.pas_last_name = pas_last_name
        self.meal_option = meal_option
        self.cc_type = cc_type
        self.cc_number = cc_number
        self.cc_exp_month = cc_exp_month
        self.cc_exp_year = cc_exp_year
        self.bill_address = bill_address
        self.city = city
        self.zip_code = zip_code
        self.country = country


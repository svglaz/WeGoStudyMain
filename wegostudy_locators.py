import datetime
from faker import Faker
fake = Faker(locale=['en_CA','en_US'])

app = 'WeGoStudy'
wegostudy_url = 'http://34.233.225.85/'
wegostudy_home_page_title = 'WeGoStudy'
user_email = 'chris.velasco78@gmail.com'
user_password = '123cctb'
partner_home_page = 'http://34.233.225.85/partner/home'
partner_student_details_page = 'http://34.233.225.85/partners/student_details'
partner_new_student_page = 'http://34.233.225.85/partners/student_details/new'

first_name = fake.first_name()
middle_name = fake.first_name()
last_name = fake.last_name()
preferred_name = f'{first_name} {last_name}'
full_name = f'{first_name} {middle_name} {last_name}'
date_of_birth = '20000101'
passport_number = '123456'
phone_number = fake.phone_number()


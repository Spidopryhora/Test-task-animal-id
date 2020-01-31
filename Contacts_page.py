from robot.libraries.BuiltIn import BuiltIn
from Generic_page import Generic_page

_bi = BuiltIn()

class Contacts_locators:

    topic_dropdown = 'css = select#subject_select'
    chip_field = 'css = input#contactform-transponder'
    descr_field = 'css = textarea#contactform-body'
    submit_button = 'css = button#contact-button'
    #----------user test data--------------------
    registered_chip_vaule = 'WC15804595785230'
    success_submission_message = 'Дякуємо Вам за звернення до нас. Ми відповімо вам як можна швидше'
    contacts_page = '/contact'

class Contacts_page(Generic_page):
    def user_navigates_to_contacts_page(self):
        self.go_to_page(Contacts_locators.contacts_page)

    def user_select_change_animal_data(self):
        _bi.run_keyword('Select From List By Value', Contacts_locators.topic_dropdown, '2')

    def user_fill_in_chip_field(self):
        self.wait_and_type(Contacts_locators.chip_field, Contacts_locators.registered_chip_vaule)
    
    def user_fill_in_descr_field(self):
        self.wait_and_type(Contacts_locators.descr_field, 'Test message')

    def user_submit_form(self):
        self.wait_and_click(Contacts_locators.submit_button)

    def verify_succes_submission_message(self):
        _bi.run_keyword('Wait until page contains', Contacts_locators.success_submission_message)
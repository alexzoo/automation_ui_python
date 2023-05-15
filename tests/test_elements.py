import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements:
    class TestTextBox:
        def test_test_box(self, driver):
            # Arrange
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            # Act
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # Assert
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert output_full_name == full_name, 'Full name is not correct'
            assert output_email == email, 'Email is not correct'
            assert output_current_address == current_address, 'Current address is not correct'
            assert output_permanent_address == permanent_address, 'Permanent address is not correct'

    class TestCheckBox:
        def test_check_box(self, driver):
            # Arrange
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            # Act
            check_box_page.expand_all()
            check_box_page.click_random_checkboxes()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            # Assert
            assert input_checkboxes == output_result, 'Checkboxes are not correct'

    class TestRadioButton:

        def test_radio_button(self, driver):
            # Arrange
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            # Act
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            # Assert
            assert output_yes == 'Yes', 'Yes not selected'
            assert output_impressive == 'Impressive', 'Impressive not selected'
            assert output_no == 'No', 'No not selected'

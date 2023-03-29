from pages.elements_page import TextBoxPage


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





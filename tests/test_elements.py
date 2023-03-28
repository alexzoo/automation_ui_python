from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_test_box(self, driver):
            # Arrange
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()

            full_name = "John Doe"
            email = 'asa@mail.com'
            current_address = '123 Main St'
            permanent_address = '456 Main St'
            # Act
            text_box_page.fill_all_fields(full_name, email, current_address, permanent_address)
            # Assert
            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_filled_form()
            assert output_full_name == full_name
            assert output_email == email
            assert output_current_address == current_address
            assert output_permanent_address == permanent_address





import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    TestUploadAndDownloadFilePage


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

    class TestWebTables:

        def test_web_tables(self, driver):
            # Arrange
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            # Act
            person = web_tables_page.add_new_person()
            result = web_tables_page.check_new_added_person()
            # Assert
            assert person in result, 'Person not added'

        def test_web_table_search_person(self, driver):
            # Arrange
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            # Act
            new_person = web_tables_page.add_new_person()[random.randint(0, 5)]
            web_tables_page.search_person(new_person)
            result = web_tables_page.check_searched_person()
            # Assert
            assert new_person in result, 'Person not found'

        def test_web_table_update_person(self, driver):
            # Arrange
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            # Act
            last_name = web_tables_page.add_new_person()[1]
            web_tables_page.search_person(last_name)
            age = web_tables_page.update_person()
            result = web_tables_page.check_searched_person()
            # Assert
            assert age in result, 'Person not updated'

        def test_web_table_delete_person(self, driver):
            # Arrange
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            # Act
            email = web_tables_page.add_new_person()[3]
            web_tables_page.search_person(email)
            web_tables_page.delete_person()
            result = web_tables_page.check_deleted_person()
            # Assert
            assert result == 'No rows found', 'Person not deleted'

    class TestButtons:

        def test_different_click_on_the_buttons(self, driver):
            # Arrange
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            # Act
            double = buttons_page.click_on_the_button('double')
            right = buttons_page.click_on_the_button('right')
            click = buttons_page.click_on_the_button('click')
            # Assert
            assert double == 'You have done a double click', 'Double button not clicked'
            assert right == 'You have done a right click', 'Right Button not clicked'
            assert click == 'You have done a dynamic click', 'Click Button not clicked'

    class TestLinks:

        def test_click_on_the_links(self, driver):
            # Arrange
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            # Act
            href_link, url = links_page.check_new_tab_link()
            # Assert
            assert href_link == url, 'Link not opened'

        def test_broken_link(self, driver):
            # Arrange
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            # Act
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            # Assert
            assert response_code == 400, 'Link not broken'

    class TestUploadAndDownloadFile:

        def test_upload_file(self, driver):
            # Arrange
            upload_page = TestUploadAndDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            # Act
            filename, result = upload_page.upload_file()
            # Assert
            assert filename == result, 'File not uploaded'

        def test_download_file(self, driver):
            # Arrange
            download_page = TestUploadAndDownloadFilePage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            # Act
            download_page.download_file()
            time.sleep(5)
            # Assert
            assert download_page.check_downloaded_file() == 'test.txt', 'File not downloaded'
import os
import random

import requests

from generator.generator import generated_person, generated_file
from locators import elements_page_locators
from pages.base_page import BasePage

import time


class TextBoxPage(BasePage):
    locators = elements_page_locators.TextBoxPageLocators

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(
            self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(
            self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(
            self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(
            self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(
            self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = elements_page_locators.CheckBoxPageLocators

    def expand_all(self):
        self.element_is_visible(self.locators.BUTTON_EXPAND_ALL).click()

    def click_random_checkboxes(self):
        list_of_elements = self.elements_are_visible(self.locators.ITEMS_LIST)
        count = 21
        while count != 0:
            item = list_of_elements[random.randint(
                1, len(list_of_elements) - 1)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for item in checked_list:
            title_item = item.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = elements_page_locators.RadioButtonPageLocators

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.RADIO_BUTTON_YES,
                   'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
                   'no': self.locators.RADIO_BUTTON_NO}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablesPage(BasePage):
    locators = elements_page_locators.WebTablesPageLocators

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.PEOPLE_LIST)
        data = []
        for people in people_list:
            data.append(people.text.splitlines())
        return data

    def search_person(self, keyword):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_searched_person(self):
        delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        row = delete_button.find_element('xpath', self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return str(age)

    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_is_present(self.locators.NO_ROWS_DATA).text


class ButtonsPage(BasePage):
    locators = elements_page_locators.ButtonsPageLocators

    def click_on_the_button(self, type_click):
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
            return self.checked_clicked_on_the_button(self.locators.DOUBLE_CLICK_MESSAGE)

        elif type_click == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.checked_clicked_on_the_button(self.locators.RIGHT_CLICK_MESSAGE)

        elif type_click == 'click':
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.checked_clicked_on_the_button(self.locators.CLICK_ME_MESSAGE)

    def checked_clicked_on_the_button(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = elements_page_locators.LinksPageLocators

    def check_new_tab_link(self):
        link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            link.click()
            self.switch_to_tab(1)
            url = self.get_current_url()
            return link_href, url

        else:
            return link_href, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_GATEWAY_LINK).click()
        else:
            return request.status_code


class TestUploadAndDownloadFilePage(BasePage):
    locators = elements_page_locators.UploadAndDownloadFilePageLocators

    def upload_file(self):
        filename, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text
        return filename.split('/')[-1], text.split('\\')[-1]






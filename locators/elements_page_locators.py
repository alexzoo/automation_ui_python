from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    # form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created form
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    BUTTON_EXPAND_ALL = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
    ITEMS_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablesPageLocators:
    # form fields
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # created form
    PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')

    # search
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'

    # update
    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    NO_ROWS_DATA = (By.CSS_SELECTOR, 'div[class="rt-noData"]')


class ButtonsPageLocators:
    # buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')
    # messages
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_ME_MESSAGE = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    HOME_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_GATEWAY_LINK = (By.CSS_SELECTOR, 'a[id="bad-request"]')


class UploadAndDownloadFilePageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

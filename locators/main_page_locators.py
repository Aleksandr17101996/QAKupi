from selenium.webdriver.common.by import By


class SearchPageLocators:
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'button[id="account-init-button"]')
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, 'button[class="styled__StyledButton-sc-rogkzj-0 gVbfQQ"]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input[name="email"]')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[name="password"]')
    INPUT_AGAIN_PASSWORD = (By.CSS_SELECTOR, 'input[name="passwordAgain"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[data-testid="sign-up-button"]')
    MESSAGE_REGISTRATE = (By.CSS_SELECTOR, 'h2[class="styled__StyledTypography-sc-1ym9bng-0 bEfCcE styled__Header-sc-ybs1xh-0 kOkxXX"]')
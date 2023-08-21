from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest

driver = webdriver.Chrome()


class TestPromptHero:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        sleep(10)
        driver.close()

    def test_prompt(self, test_setup):
        driver.get("https://prompthero.com/")
        search = driver.find_element(By.NAME, "q")
        search.send_keys("Dark Scary Atmosphere")
        search.send_keys(Keys.ENTER)
        sleep(5)

        # The image that we're trying yo get hold of
        driver.find_element(By.ID, "prompt-card-image-backdrop-4ae9caa7ad7").click()
        sleep(5)

        # link of the image
        image_link = driver.find_element(By.CLASS_NAME, "img-fluid")
        print("")
        print(f'Image Link: {image_link.get_attribute("src")}')
        sleep(5)

        # Name of the User
        username = driver.find_element(By.CLASS_NAME, "align-items-center").text
        print("Username:", username)
        sleep(5)

        # driver.find_element(By.CLASS_NAME, "close").click()
        # Prompt Content
        content = driver.find_element(By.CSS_SELECTOR, ".the-prompt b").text
        print(f"Prompt Content: {content}")
        sleep(5)

        # Generation parameters of the image
        generation_parameters = driver.find_elements(By.CSS_SELECTOR, ".metadata span")
        for param in generation_parameters:
            print(f"Generation Parameters: {param.text}")
        sleep(5)

        # Model used in creating the image
        model_used = driver.find_element(By.CSS_SELECTOR, ".d-inline span")
        print(f"Model Used: {model_used.text}")


""" I've tried 2nd round of assignment with all of my capability and understanding of webscraping using selenium. 
I was not familiar with pytest but I did a little bit of googling and tried to complete it. Thank You."""

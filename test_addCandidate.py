# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddCandidate():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addCandidate(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys("Admin")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("admin123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-main-menu-item-wrapper:nth-child(5) .oxd-text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary:nth-child(1)").click()
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("Maria")
    self.driver.find_element(By.NAME, "middleName").send_keys("Fernanda")
    self.driver.find_element(By.NAME, "lastName").send_keys("Avendaño")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form-row:nth-child(3) .oxd-grid-item:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-input--focus").send_keys("Interview")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys("Charles  Carter")
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form-row:nth-child(2) .oxd-grid-item:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button--secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Candidates").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-table-card-cell-checkbox .oxd-icon").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(1) > .oxd-icon").click()
  

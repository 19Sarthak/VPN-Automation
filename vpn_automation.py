from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess

def switch_vpn(country):
    try:
        command = f"nordvpn -c -g {country}"
        subprocess.run(command, shell=True, check=True)
        print(f"Switched VPN to {country}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to switch VPN: {e}")

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def search_keyword(driver, keyword):
    driver.get("https://duckduckgo.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        ad_link = driver.find_element(By.CSS_SELECTOR, "a[data-testid='ad-link']")
        ad_link.click()
        print(f"Clicked on ad link for keyword: {keyword}")
    except Exception as e:
        print(f"No ad link found for keyword: {keyword} - {e}")

def main():
    keywords = ["buy laptop", "best smartphones", "cheap flights"]
    countries = ["United States", "Canada", "Germany"]

    for country in countries:
        switch_vpn(country)
        driver = setup_browser()

        for keyword in keywords:
            search_keyword(driver, keyword)

        driver.quit()

if __name__ == "__main__":
    main()

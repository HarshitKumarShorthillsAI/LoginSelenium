from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Initialize WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_linkedin(email, password):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        # Open LinkedIn login page
        driver.get("https://www.linkedin.com/login")
        time.sleep(5)  # Wait for the page to load

        # Find and fill the email field
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)
        time.sleep(2)  # Pause after entering email

        # Find and fill the password field
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        time.sleep(2)  # Pause after entering password

        # Press Enter to log in
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)  # Wait for login process

        # Check if login is successful by looking for an element that appears after login
        try:
            driver.find_element(By.XPATH, "//*[text()='Start a post']")  # Element found only on homepage
            print("✅ Login successful!")
        except NoSuchElementException:
            print("❌ Login failed: Incorrect email or password.")
            driver.quit()
            return

        # Wait a bit and close browser
        time.sleep(5)
        print("🎉 LinkedIn login completed successfully!")

    except NoSuchElementException as e:
        print("⚠️ Element not found error:", e)
    except TimeoutException:
        print("⚠️ The page took too long to load. Check your internet connection.")
    except Exception as e:
        print("⚠️ An unexpected error occurred:", e)
    finally:
        driver.quit()

# Call function with your LinkedIn email and password

# Call function with your LinkedIn email and password
login_linkedin("kumarharshit8225@gmail.com", "prajapat")

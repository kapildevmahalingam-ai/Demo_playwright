from playwright.sync_api import sync_playwright
from datetime import datetime
import time


# Navigate to https://www.cricbuzz.com/ site
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/")
    page.screenshot(path="screenshot.png")
    print("Step 1: Successfully launched the browser and navigated to the website")

    # Click on the "Live Scores" link
    page.click("text=Live Scores")
    #page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("Step 2: Clicked on the 'Live Scores' link")

    # Click on the first match in the list
    page.click("text=Scorecard")
    #page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("Step 3: Clicked on the 'First match scorecard' link")

    # Click on the second innings match in the list
    page.click("text=IND (2nd Inn)")
    #page.wait_for_load_state("networkidle")
    time.sleep(2)
    print("Step 4: Clicked on the 'Second innings' link")
    
    # Take screenshot of the match details page
    page.screenshot(path="match_details.png")
    
    print("Step 5: Successfully took a screenshot of the match details page")

    # Close the browser
    browser.close()
    print("Step 6: Successfully closed the browser")

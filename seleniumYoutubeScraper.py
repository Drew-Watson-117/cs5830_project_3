# Code from https://scrapfly.io/blog/web-scraping-with-selenium-and-python/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class IdScraper:

    def __init__(self, fileName, numBatches=10) -> None:
        self.fileName = fileName
        self.numBatches = numBatches

    def get_new_ids(self):
        # configure chrome browser to not load images and javascript
        options = webdriver.ChromeOptions()
        options.headless = True  # hide GUI
        options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
        options.add_argument("start-maximized")  # ensure window is full-screen
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )

        driver = webdriver.Chrome(options=options)

        # driver.get("https://www.youtube.com/@theofficialytchannel")
        driver.get("https://youtube.com")
        # wait for page to load
        element = WebDriverWait(driver=driver, timeout=5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'link[rel="shortcut icon"]'))
        )
        # print(driver.page_source)

        handles = []
        # Get all anchor tags on home page that are a link to a channel
        anchors = driver.find_elements(By.ID, 'avatar-link')
        for a in anchors:
            # The href takes you to the channel
            handles.append(a.get_attribute('href'))
        # Strip the channel id/handle off the url
        for i in range(0,len(handles)):
            chunks = handles[i].split('/')
            handles[i] = chunks[-1]
        # Write ids/handles to a dataframe
        df = pd.DataFrame(handles, columns=['ID'])
        # print(df)
        return df

    # Write dataframe to .csv
    def add_ids(self):
        old_ids = pd.read_csv(self.fileName, index_col=0)
        new_ids = self.get_new_ids()
        ids = pd.concat([old_ids,new_ids], ignore_index=True)
        ids.drop_duplicates(inplace=True)
        ids.to_csv(self.fileName)

    def initial_ids(self):
        error = True
        while error:
            try:
                error = False
                ids = self.get_new_ids()
            except:
                error = True
        ids.to_csv(self.fileName)

    def make_csv(self):
        self.initial_ids()
        for i in range(self.numBatches):
            try:
                self.add_ids()
            except:
                print("Error")


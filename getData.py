from YoutubeScraper import YoutubeScraper
from seleniumYoutubeScraper import IdScraper
import pandas as pd

API_KEY = 'AIzaSyBP0NTMpjGwTqWiMP7Ke8p2XnijyASC8fI'

# Make .csv of youtube channel id's to get from youtube
idScraper = IdScraper("youtuber_ids.csv",30)
idScraper.make_csv()


ids = pd.read_csv("youtuber_ids.csv")

# Get data from youtube's api
scraper = YoutubeScraper(API_KEY,ids["ID"])

scraper.write_to_csv("channel_data.csv")

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# setting up executable path and the the url
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# visit the mars nasa news site
url = "https://redplanetscience.com/"
browser.visit(url)
# optional delay for the loading page
browser.is_element_present_by_css("div.list_text", wait_time = 1)

# setting up html parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one("div.list_text")
# using parent element "div.list_text" to pull content titles
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# Featured Images

# visit url 
url = "https://spaceimages-mars.com/"
browser.visit(url)

#find and click on the full image
full_image_elem = browser.find_by_tag("button")[1]
full_image_elem.click()

#Parse the resulting html with soup
html = browser.html
img_soup = soup(html, "html.parser")

#find the relative image url
img_url_rel = img_soup.find("img", class_="fancybox-image").get("src")
img_url_rel

#use the base URL to create an absolute URL
img_url = f"https://spaceimages-mars.com/{img_url_rel}"
img_url

# getting table from https://galaxyfacts-mars.com/
df = pd.read_html("https://galaxyfacts-mars.com/")[0]
df.columns=["description", "Mars", "Earth"]
df.set_index("description", inplace=True)
df

df.to_html()

#quitting the browser
browser.quit()



from selenium import webdriver
from selenium.webdriver.firefox.options import Options

firefox_options = Options() 
firefox_options.add_argument('--headless')
firefox_options.add_argument("--window-size=3200x20800") # ANYTHING MORE THAN 3200 width my pycharm cant cope (Rendering error)

driver = webdriver.Firefox(options=firefox_options) # webdriver.Firefox(options=options)
# outFileName = (r'D:\08102020 Random Work\NewFolder4PythonOut')
driver.maximize_window()

URL = "https://www.kaggle.com/frecklebars/ml-flow-based-visual-coding-using-ryven/notebook"

driver.get(URL) #time.sleep(0.5)
driver.maximize_window()

driver.get_screenshot_as_file("ryven_exmpl.png")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time

class ApartmentEstateCrawler:
    BASE_URL = "https://www.aruodas.lt/"
    APARTMENTS_URL = "butai/"
    SEARCH_URL = "?search_text="
    def __init__(self, search_text: str) -> None:
        """
        Initializes the ApartmentEstateCrawler object.

        Parameters:
        - search_text (str): The region to search for.
        """
        if type(search_text) is not str:
            raise ValueError("Search text must be string")
        else:
            self.search_text = search_text
        self.mod_search_text = search_text.replace(" ", "%20")
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def get_search_results(self):
        """
        Scrapes real estate data from the specified search region.

        Returns:
        - dict: {"Apartments": objects, "Search_phrase":"Your searchPhrase"};
            objects - List of RealEstateObject instances representing the scraped data.
        """
        url = self.BASE_URL + self.APARTMENTS_URL + self.SEARCH_URL + self.mod_search_text
        self.driver.get(url)
        cookie_element = self.driver.find_element(by="id", value="onetrust-reject-all-handler")
        cookie_element.click()

        objects = []
        start_time = time.time()

        while time.time() - start_time < 60:
            advert_wrapper = self.driver.find_elements(By.CSS_SELECTOR, ".list-row-v2.object-row")
            
            for element in advert_wrapper:
                address_loc = element.find_element(By.CLASS_NAME, "list-adress-v2 ")
                object_link = address_loc.find_element(By.CSS_SELECTOR, "h3 a")
                object_address = object_link.text
                object_url = object_link.get_attribute("href")
                object_price = address_loc.find_element(By.CSS_SELECTOR, "div span.list-item-price-v2").text
                object_area = element.find_element(By.CLASS_NAME, "list-AreaOverall-v2 ").text
                object_no_of_rooms=element.find_element(By.CLASS_NAME, "list-RoomNum-v2 ").text
                object_floor_no=element.find_element(By.CLASS_NAME, "list-Floors-v2 ").text

                obj = ApratmentEstateObject(object_address, object_url, object_price, object_area, object_no_of_rooms, object_floor_no)
                objects.append(obj.__dict__)

            try:
                next_page_button = self.driver.find_element(By.XPATH, "//div[contains(@class, 'pagination')]/a[text()='»']")
            except NoSuchElementException:
                # If the "Next" button is not found, break out of the loop
                break

            if "disabled" in next_page_button.get_attribute("class"):
                # If the "Next" button is disabled, break out of the loop
                break
            else:
                next_page_button.click()
                time.sleep(2)

        return {"Apartments": objects, "Search_phrase":f"{self.search_text}"}

    def close_driver(self):
        """Closes the WebDriver."""
        self.driver.close()

class ApratmentEstateObject:
    """
        Initializes the PlotEstateObject.

        Parameters:
        - address (str): The address of the real estate.
        - url (str): The URL of the real estate listing.
        - price (str): The price of the real estate.
        - area (str): The area of the real estate.
        - no of rooms (str): Number of rooms in apartment.
        - floor no (str): In what floor apartment is.
        """
    def __init__(self, address, url, price, area, no_of_rooms, floor_no):
        self.address = address.replace("\n", " ")
        self.url = url
        self.price = float(price.replace("€", "").replace(" ", ""))
        self.area = area
        self.no_of_rooms = no_of_rooms
        self.floor_no = floor_no
        self.created = str(datetime.now())
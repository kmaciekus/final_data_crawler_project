from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import time
from pandas import DataFrame
from dataclasses import dataclass
from ..utils.error_handler import text_value_error_handler
from ..utils.converters import convert_to_float, convert_to_int

@dataclass
class ApartmentObject:
    """
        Initializes the ApartmentObject.

        Parameters:
        - address (str): The address of the real estate.
        - url (str): The URL of the real estate listing.
        - price (float): The price of the real estate.
        - area (float): The area of the real estate.
        - no of rooms (int): Number of rooms in apartment.
        - floor no (str): In what floor apartment is.
    """
    address:str
    url:str
    price:float
    area:float
    no_of_rooms:int
    floor_no:str
    real_estate_type:str = "Apartment"
    created:str = str(datetime.now())

class ApartmentEstateCrawler:
    BASE_URL = "https://www.aruodas.lt/"
    APARTMENTS_URL = "butai/"
    SEARCH_URL = "?search_text="
    def __init__(self, search_text: str | None = "", time_limit: int | None = None) -> None:
        """
        Initializes the ApartmentEstateCrawler object.

        Parameters:
        - search_text (str): The region to search for (ex.: Vilnius).
        - time_limit (int): Time limit for crawler to get data.
        """
        checked_text=text_value_error_handler(search_text)
        self.search_text = checked_text
        self.mod_search_text = self.search_text.replace(" ", "%20")
        if time_limit == None:
            self.time_limit = time_limit
        else:
            self.time_limit = int(time_limit)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    
    def _handle_cookies(self):
        try:
            cookie_element = self.driver.find_element(by="id", value="onetrust-reject-all-handler")
            cookie_element.click()
        except NoSuchElementException:
            pass

    def _check_time_limit(self, start_time):
        return self.time_limit is not None and time.time() - start_time > self.time_limit
    
    def _extract_apartment_data(self, element):
        address_loc = element.find_element(By.CLASS_NAME, "list-adress-v2 ")
        object_link = address_loc.find_element(By.CSS_SELECTOR, "h3 a")
        object_address = object_link.text.replace("\n", " ")
        object_url = object_link.get_attribute("href")
        object_price = convert_to_float(address_loc.find_element(By.CSS_SELECTOR, "div span.list-item-price-v2").text.replace("€", "").replace(" ", ""))
        object_area = convert_to_float(element.find_element(By.CLASS_NAME, "list-AreaOverall-v2 ").text)
        object_no_of_rooms=convert_to_int(element.find_element(By.CLASS_NAME, "list-RoomNum-v2 ").text) #unique
        object_floor_no=element.find_element(By.CLASS_NAME, "list-Floors-v2 ").text #unique

        return ApartmentObject(object_address, object_url, object_price, object_area, object_no_of_rooms, object_floor_no)
    
    def _get_next_page_button(self):
        try:
            return self.driver.find_element(By.XPATH, "//div[contains(@class, 'pagination')]/a[text()='»']")
        except NoSuchElementException:
            return None

    def get_search_results(self):
        """
        Scrapes real estate data from the specified search region.

        Returns:
            pandas.DataFrame: A DataFrame containing all collected real estates. Each row in the DataFrame represents real estate,
                      with columns corresponding to the details of the real estate as provided by the aroudas.lt.

        Notes:
            - If the request for the first page fails, an empty DataFrame is returned.
            - If the specified time limit is reached before all pages are fetched, the process is terminated, and data
            collected up to that point is returned.
        """
        url = self.BASE_URL + self.APARTMENTS_URL + self.SEARCH_URL + self.mod_search_text
        self.driver.get(url)
        self._handle_cookies()

        objects = []
        start_time = time.time()

        while True:
        
            if self._check_time_limit(start_time):
                print("Time limit exceeded!")
                break
            advert_wrapper = self.driver.find_elements(By.CSS_SELECTOR, ".list-row-v2.object-row")
            
            if not advert_wrapper:
                return DataFrame()
            
            for element in advert_wrapper:

                obj = self._extract_apartment_data(element)
                objects.append(obj.__dict__)

            next_page_button = self._get_next_page_button()

            if not next_page_button or "disabled" in next_page_button.get_attribute("class"):
                break
            else:
                next_page_button.click()
                time.sleep(2)

        return DataFrame(objects)

    def close_driver(self):
        """Closes the WebDriver."""
        self.driver.close()


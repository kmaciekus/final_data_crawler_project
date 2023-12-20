from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PlotEstateCrawler:
    BASE_URL = "https://www.aruodas.lt/"
    SKLYPAI_URL = "sklypai/"
    SEARCH_URL = "?search_text="
    def __init__(self, search_text: str) -> None:
        """
        Initializes the RealEstateScraper object.

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
        - dict: {"Plots": objects, "Search_phrase":"Your searchPhrase"};
            objects - List of RealEstateObject instances representing the scraped data.
        """
        url = self.BASE_URL + self.SKLYPAI_URL + self.SEARCH_URL + self.mod_search_text
        self.driver.get(url)
        cookie_element = self.driver.find_element(by="id", value="onetrust-reject-all-handler")
        cookie_element.click()

        objects = []
        while True:
            advert_wrapper = self.driver.find_elements(By.CSS_SELECTOR, ".list-row-v2.object-row")
            
            for element in advert_wrapper:
                address_loc = element.find_element(By.CLASS_NAME, "list-adress-v2 ")
                object_link = address_loc.find_element(By.CSS_SELECTOR, "h3 a")
                object_address = object_link.text
                object_url = object_link.get_attribute("href")
                object_price = address_loc.find_element(By.CSS_SELECTOR, "div span.list-item-price-v2").text
                object_area = element.find_element(By.CLASS_NAME, "list-AreaOverall-v2 ").text
                object_purpose = element.find_element(By.CLASS_NAME, "list-Intendances-v2 ").text

                obj = PlotEstateObject(object_address, object_url, object_price, object_area, object_purpose)
                objects.append(obj)

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

        return {"Plots": objects, "Search_phrase":f"{self.search_text}"}

    def close_driver(self):
        """Closes the WebDriver."""
        self.driver.close()

class PlotEstateObject:
    """
        Initializes the PlotEstateObject.

        Parameters:
        - address (str): The address of the real estate.
        - url (str): The URL of the real estate listing.
        - price (str): The price of the real estate.
        - area (str): The area of the real estate.
        - purpose (str): The purpose of the real estate (e.g., residential, commercial).
        """
    def __init__(self, address, url, price, area, purpose):
        self.address = address
        self.url = url
        self.price = price
        self.area = area
        self.purpose = purpose
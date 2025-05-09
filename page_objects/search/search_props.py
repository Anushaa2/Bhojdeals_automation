from page_objects.search.search_locators import SearchLocators

class SearchProperties:

    @property
    def search_input(self):
        return self.driver.find_element(*SearchLocators.SEARCH_BOX)

    @property
    def dropdown_click(self):
        return self.driver.find_element(*SearchLocators.DROPDOWN)

    @property
    def dropdown_items(self):
        return self.driver.find_elements(*SearchLocators.DROPDOWN_ITEMS)

    @property
    def filter(self):
        return self.driver.find_element(*SearchLocators.TODAYS_DEAL)

    @property
    def browse_category(self):
        return self.driver.find_element(*SearchLocators.BROWSER_CATEGORY)

    @property
    def browse_cuisine(self):
        return self.driver.find_element(*SearchLocators.BROWSER_CUISINE)

    @property
    def popularity_sort(self):
        return self.driver.find_element(*SearchLocators.SORT_POPULARITY)

    @property
    def price_sort(self):
        return self.driver.find_element(*SearchLocators.SORT_PRICE)

    @property
    def restaurant(self):
        return self.driver.find_element(*SearchLocators.ALL_RESTAURANT)

    @property
    def filter_reset(self):
        return self.driver.find_element(*SearchLocators.RESET)
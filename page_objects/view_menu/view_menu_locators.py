from selenium.webdriver.common.by import By


class ViewMenuLocators(object):
    RESTAURANT=(By.XPATH,"//a/div[contains(@class,'restaurant-type')]")
    # MENU_CATEGORY=(By.XPATH,"//div[@class='category-tab col-md-3 col-xl-2']//li[3]//a[1]")
    MENU_CATEGORY=(By.XPATH,'//div[contains(@class,"category-tab")]//li//a[text()="Mo:Mo"]')

    '''
    //div[contains(@class,"category-tab")]//li//a[text()="Mo:Mo"]
    '''
    # MAP=(By.XPATH,"//ul[@id='__BVID__2846__BV_tab_controls_']//li[2]")




"""
This class models the main weathershopper page.
The page consists of temperature display
"""
from .Base_Page import Base_Page
from .temperature_display import Temperature_Display
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Weathershopper_Main_Page(Base_Page, Temperature_Display):

    #locators
    moist_button = locators.moisturizers_button
    sunscr_button = locators.sunscreens_button
    redirect_moisturizer_url = "moisturizer"
    rredirect_sunscreen_url = "sunscreen"
    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = " "
        self.open(url)

    @Wrapit._exceptionHandler
    def check_moist_button(self):
        "Check if the Buy moisturizers button exists"
        result_flag = self.check_element_present(self.moist_button)
        self.conditional_write(result_flag,
            positive='Buy moisturizers button present on main page',
            negative='Buy moisturizers button not present on main page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def check_sunscr_button(self):
        "Check if the Buy sunscreenss button exists"
        result_flag = self.check_element_present(self.sunscr_button)
        self.conditional_write(result_flag,
            positive='Buy sunscreens button present on main page',
            negative='Buy sunscreenss button not present on main page',
            level='debug')

        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_buy_moisturizer(self):
        result_flag = self.click_element(self.moist_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "buy moisturizer" button',
            negative='Failed to click on "buy moisturizer" button',
            level='debug')

        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_buy_sunscreen(self):
        result_flag = self.click_element(self.sunscr_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "buy sunscreen" button',
            negative='Failed to click on "buy sunscreen" button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_to_moisturizer(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.redirect_moisturizer_url  in self.driver.current_url:
            result_flag = True
            self.switch_page("moisturizer list page")

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_to_sunscreen(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        if self.rredirect_sunscreen_url  in self.driver.current_url:
            result_flag = True
            self.switch_page("sunscreen list page")

        return result_flag

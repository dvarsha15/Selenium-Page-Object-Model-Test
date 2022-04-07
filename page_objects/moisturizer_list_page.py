"""
This class models the moisturizer page
url : moisturizer

"""
import conf.locators_conf as locators
from .Base_Page import Base_Page
from utils.Wrapit import Wrapit

class Moisturizer_List_Page(Base_Page):

    #locators
    moisturizer_heading = locators.moisturizers_heading
    add_max_honey_button = locators.add_max_honey_button
    add_boris_almond_button = locators.add_boris_almond_button
    cart_button = locators.cart_button
    cart_url = "cart"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'moisturizer'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_moisturizer_heading(self):
        "Check if the  moisturizers heading exists on redirected page"
        result_flag = self.check_element_present(self.moisturizer_heading)
        self.conditional_write(result_flag,
            positive='Moisturizers heading present on redirected page',
            negative='Moisturizers heading not present on redirected page',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_max_honey_button(self):
        result_flag = self.check_element_displayed(self.add_max_honey_button)
        if result_flag == True :
            result_flag = self.click_element(self.add_max_honey_button)
            self.conditional_write(result_flag,
                positive='Clicked on the add button of max honey',
                negative='Failed to click on add button of max honey',
                level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_boris_almond_button(self):
        result_flag = self.check_element_displayed(self.add_boris_almond_button)
        if result_flag == True :
            result_flag = self.click_element(self.add_boris_almond_button)
            self.conditional_write(result_flag,
                positive='Clicked on the add button of boris almond',
                negative='Failed to click on add button of boris almond',
                level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_cart_button(self):
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on the cart button',
            negative='Failed to click on cart button',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_to_cart_page(self):
        "Check if we have been redirected to the cart page"
        result_flag = False
        if self.cart_url  in self.driver.current_url:
            result_flag = True
            self.switch_page("cart page")

        return result_flag
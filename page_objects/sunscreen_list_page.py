"""
This class models the sunscreen page
url : sunscreen

"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Sunscreen_List_Page(Base_Page):

      #locators
      sunscreen_heading = locators.sunscreen_heading
      product_price_display = locators.product_price_display
    
      def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'sunscreen'
        self.open(url)

      @Wrapit._exceptionHandler
      def check_sunscreen_heading(self):
        "Check if the  sunscreens heading exists on redirected page"
        result_flag = self.check_element_present(self.sunscreen_heading)
        self.conditional_write(result_flag,
            positive='Sunscreens heading present on redirected page',
            negative='Sunscreens heading not present on redirected page',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      def get_sunscreen_smallest_price(self):
        "check total price on cart page"
        product_price_list = []
        for i in range(2,4):
          for j in range(1,4):
              i = str(i)
              j = str(j)
              price_display_locator = ("xpath,//div[contains(@class,'row')][", i, "]//div[", j, "]//p[2]")
              price_display_locator =  "".join(price_display_locator)
              product_price = self.get_text(price_display_locator)
              product_price = product_price.decode("utf-8").split()
              product_price = product_price[len(product_price)-1]
              self.write('product_price:%s'%product_price)
              product_price_list.append(str(product_price))

        min_price = min(product_price_list)
  
        return min_price

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def click_add_sunscreen_smallest_price(self,locator):
        result_flag = self.check_element_displayed(locator)
        if result_flag == True:
            result_flag = self.click_element(locator)
            self.conditional_write(result_flag,
                positive='Clicked on the add button of smallest price sunscreen',
                negative='Failed to click on add button of smallest price sunscreen',
                level='debug')

        return result_flag
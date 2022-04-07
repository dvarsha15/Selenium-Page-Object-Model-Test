"""
This class models the cart page and a frame on the same page (form)
url : cart

"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Cart_Page(Base_Page):
      #locators
      cart_total_price = locators.cart_total_price
      pay_with_card_button = locators.pay_with_card_button
      stripe_com_heading = locators.srtipe_com_heading
      email_textbox = locators.email_textbox
      card_number_textbox = locators.card_mumber_textbox
      expiry_mm_yy_textbox = locators.expiry_mm_yy_textbox
      cvc_textbox = locators.cvc_textbox
      close_button = locators.close_button

      def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'cart'
        self.open(url)

      @Wrapit._exceptionHandler
      def get_total_price(self):
        "check total price on cart page"
        total_price = self.get_text(self.cart_total_price)
        total_price = total_price.decode("utf-8").split()
        
        return total_price[2]

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def click_pay_with_card_button(self):
         "click on 'pay with card' button on cart page"
         result_flag = self.click_element(self.pay_with_card_button)
         self.conditional_write(result_flag,
            positive='Clicked on the pay with card button',
            negative='Failed to click on pay with card button',
            level='debug')
         self.switch_frame(index=0)

         return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def check_stripe_com_heading(self):
        "Check if the heading stripe.com exists on new frame"
        result_flag = self.check_element_present(self.stripe_com_heading)
        self.conditional_write(result_flag,
            positive='Stripe.com heading present on form ',
            negative='Stripe.com heading not present',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def set_email(self,email):
        "Set the email in the form"
        result_flag = self.set_text(self.email_textbox,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def set_card_number(self,card_number):
        card_number = str(card_number)
        "Set the card number in the form"
        "set first digit with default clear flag (True)"
        result_flag = self.set_text(self.card_number_textbox,card_number[0])
        "set remaining all digits with clear flag = False"
        for i in range(1, (len(card_number))-1):
            result_flag = self.set_text(self.card_number_textbox,card_number[i],clear_flag=False)
        self.conditional_write(result_flag,
            positive='Set the card number to: %s'%card_number,
            negative='Failed to set the card number in the form',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def set_expiry_mm_yy(self,expiry):
        expiry = str(expiry)
        "Set the email in the form"
        result_flag = self.set_text(self.expiry_mm_yy_textbox,expiry[0])
        for i in range(1, 4):
          result_flag = self.set_text(self.expiry_mm_yy_textbox,expiry[i],clear_flag=False)
          self.wait(1)
        self.conditional_write(result_flag,
            positive='Set the expiry month and year to: %s'%expiry,
            negative='Failed to set the expiry month and year in the form',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def set_cvc(self,cvc):
        "Set the CVC in the form"
        result_flag = self.set_text(self.cvc_textbox,cvc)
        self.conditional_write(result_flag,
            positive='Set the CVC to: %s'%cvc,
            negative='Failed to set the CVC in the form',
            level='debug')

        return result_flag

      @Wrapit._exceptionHandler
      @Wrapit._screenshot
      def click_close_button(self):
        "Click on 'Close' button of form"
        result_flag = self.click_element(self.close_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "close" button',
            negative='Failed to click on "close" button',
            level='debug')

        return result_flag
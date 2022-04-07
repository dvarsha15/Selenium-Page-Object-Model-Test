"""
    Automated test to select products on redirected page (moisturizer) of weathershopper (moisturizer or sunscreen) 
    and add to cart
    steps:
        1. open the page - buy moisturizer 
        2. select a product
        3. add to cart the selected product
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
import conf.checkout_form as conf
import pytest

@pytest.mark.GUI
def test_check_tepmerature_and_navigate(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #1. Create a test object and check temperature
        test_obj = PageFactory.get_page_object("Main Page")

        #Set start_time with current time
        start_time = int(time.time())

        #2. get data from conf
        email = conf.email
        card_number = conf.card_number
        expiry = conf.expiry_mm_yy
        cvc = conf.cvc

        #3. click on buy moisturizer button
        result_flag = test_obj.click_buy_moisturizer()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Buy moisturizer button \n",
                            negative=" Failed to click on Buy moisturizer button")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #4. check if redirected successfully
        result_flag = test_obj.check_redirect_to_moisturizer()
        test_obj.log_result(result_flag,
                        positive="Successfully redirected to the moisturizer page\n",
                        negative="Failed to redirect to the moisturizer page")
        if result_flag == True :
            #5. click on add button of max honey if redirected successfully
            result_flag = test_obj.click_add_max_honey_button()
            if result_flag == True :
                test_obj.log_result(result_flag,
                                positive="Successfully clicked on max honey 'Add' button \n",
                                negative=" Failed to click on max honey 'Add' button")
                test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
            #6. else click on add boris almond
            else :
                result_flag = test_obj.click_add_boris_almond_button()
                test_obj.log_result(result_flag,
                            positive="Successfully clicked on boris almond 'Add' button \n",
                            negative=" Failed to click on boris almond 'Add' button\n Required moisturizer not found on page")
                test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))


        #7. click on cart button
        if result_flag == True :
            result_flag = test_obj.click_cart_button()
            test_obj.log_result(result_flag,
                                positive="Successfully clicked on Cart button \n",
                                negative=" Failed to click on Cart button")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #8. check if redirected successfully
        result_flag = test_obj.check_redirect_to_cart_page()
        test_obj.log_result(result_flag,
                        positive="Successfully redirected to cart page\n",
                        negative="Failed to redirect to cart page")
        
        #9. check total price on cart page
        total_price = test_obj.get_total_price()
        test_obj.write('Total price : %s'%total_price)

        #10. click on pay with card button
        if int(total_price) > 0 :
            result_flag = test_obj.click_pay_with_card_button()
            test_obj.log_result(result_flag,
                                positive="Successfully clicked on pay with card button \n",
                                negative=" Failed to click on pay with card button")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #11. check for heading on checkout form (frame on cart page)
        result_flag = test_obj.check_stripe_com_heading()
        test_obj.log_result(result_flag,
                                positive="Stripe.com heading present on form \n",
                                negative=" Stripe.com heading is not present")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        

        #12. set email in form
        if result_flag == True :
            result_flag = test_obj.set_email(email)
            test_obj.log_result(result_flag,
                                    positive="Successfully set email in the form\n",
                                    negative=" Failed to set email in the form")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

            #13. set card number in form
            result_flag = test_obj.set_card_number(card_number)
            test_obj.log_result(result_flag,
                                    positive="Successfully set card number in the form\n",
                                    negative=" Failed to set card number in the form")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

            #14. set expiry month and year in form
            result_flag = test_obj.set_expiry_mm_yy(expiry)
            test_obj.log_result(result_flag,
                                    positive="Successfully set expiry month and year in the form\n",
                                    negative=" Failed to set expiry month and year in the form")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

            #15. set cvc in form
            result_flag = test_obj.set_cvc(cvc)
            test_obj.log_result(result_flag,
                                    positive="Successfully set the CVC in the form\n",
                                    negative=" Failed to set the CVC in form")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

            #16. close the checkout form
            test_obj.wait(2)
            result_flag = test_obj.click_close_button()
            test_obj.log_result(result_flag,
                                    positive="Successfully closed the checkout form\n",
                                    negative=" Failed to close the checkout form")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))


        #17. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter


    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    assert expected_pass == actual_pass, "Test failed: %s"%__file__
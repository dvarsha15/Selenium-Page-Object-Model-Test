"""
    Automated test to select products on redirected page (sunscreen) of weathershopper (moisturizer or sunscreen) 
    and add to cart
    steps:
        1. open the page - buy sunscreen
        2. select the product of lowest price
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

        # Set start_time with current time
        start_time = int(time.time())

        #2. click on buy moisturizer button
        result_flag = test_obj.click_buy_sunscreen()
        test_obj.log_result(result_flag,
                            positive="Successfully clicked on Buy sunscreen button \n",
                            negative=" Failed to click on Buy sunscreen button")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #3. check if redirected successfully
        result_flag = test_obj.check_redirect_to_sunscreen()
        test_obj.log_result(result_flag,
                        positive="Successfully redirected to the sunscreen page\n",
                        negative="Failed to redirect to the sunscreen page")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #4. get the add button of smallest price sunscreen
        min_price = test_obj.get_sunscreen_smallest_price()
        min_price = str(min_price)
        test_obj.write('Smallest price:%s'%min_price)
        add_button_of_smallest_price_locator = ("xpath,//button[contains(@onclick,'", min_price,"')]" )
        add_button_of_smallest_price_locator = "".join(add_button_of_smallest_price_locator)
        name_of_sunscreen_smallest_price_locator = (add_button_of_smallest_price_locator, "//preceding-sibling::p[2]")
        name_of_sunscreen_smallest_price_locator = "".join(name_of_sunscreen_smallest_price_locator)
        name_of_sunscreen_smallest_price = test_obj.get_text(name_of_sunscreen_smallest_price_locator)
        test_obj.write('Name of smallest price sunscreen: %s'%name_of_sunscreen_smallest_price.decode("utf-8"))
        #5. Click on add button of smallest price sunscreen
        result_flag = test_obj.click_add_sunscreen_smallest_price(add_button_of_smallest_price_locator)
        test_obj.log_result(result_flag,
                    positive="Successfully clicked on add button of smallest price sunscreen \n",
                    negative=" Failed to click on add button of smallest price sunscreen")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))


        #6. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter


    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    assert expected_pass == actual_pass, "Test failed: %s"%__file__
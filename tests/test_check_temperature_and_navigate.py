"""
Automated test to check temperature and navigates to one of the list pages
steps:
    1. open weathershopper main page
    2. check temperature
    3. click on "Buy moisturizer" or "Buy sunscreen" according to temperature

"""

import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
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

        #2. Check the buy moisturizer button on main page
        result_flag = test_obj.check_moist_button()
        test_obj.log_result(result_flag,
                            positive="Buy moisturizer button is present on main page!\n",
                            negative="Buy moisturizer button is not present on main page!")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
        #3. Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #4.compare temperature value
        result_flag = test_obj.compare_temperature()
        if (result_flag == True):
            result_flag = test_obj.click_buy_moisturizer()
            test_obj.log_result(result_flag,
                            positive="Successfully clicked on Buy moisturizer button \n",
                            negative=" Failed to click on Buy moisturizer button")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
            #5. Check Moisturizer heading on redirected page
            result_flag = test_obj.check_redirect_to_moisturizer()
            test_obj.log_result(result_flag,
                            positive="Successfully redirected to the moisturizer page\n",
                            negative="Failed to redirect to moisturizer page")
            if result_flag == True :
                result_flag = test_obj.check_moisturizer_heading()
                test_obj.log_result(result_flag,
                            positive="Moisturizers heading is present on redirected page!\n",
                            negative="Moisturizers heading is not present on redirected page!")
                test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        else:
            result_flag = test_obj.click_buy_sunscreen()
            test_obj.log_result(result_flag,
                            positive="Successfully clicked on Buy sunscreen button \n",
                            negative=" Failed to click on Buy sunscreen button")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
            #6. Check sunscreen heading on redirected page
            result_flag = test_obj.check_redirect_to_sunscreen()
            test_obj.log_result(result_flag,
                            positive="Successfully redirected to the sunscreen page\n",
                            negative="Failed to redirect to the sunscreen page")
            if result_flag == True :
                result_flag = test_obj.check_sunscreen_heading()
                test_obj.log_result(result_flag,
                            positive="Sunscreens heading is present on redirected page!\n",
                            negative="Sunscreens heading is not present on redirected page!")
                test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        
         
        #7. Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter


        
    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))
    assert expected_pass == actual_pass, "Test failed: %s"%__file__
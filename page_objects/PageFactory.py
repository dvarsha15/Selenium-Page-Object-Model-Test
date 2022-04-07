"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. weathershopper main page
2. moisturizer list page
3. sunscreen list page
4. cart page
"""

from page_objects.weathershopper_main_page import Weathershopper_Main_Page
from page_objects.moisturizer_list_page import Moisturizer_List_Page
from page_objects.sunscreen_list_page import Sunscreen_List_Page
from page_objects.cart_page import Cart_Page
from page_objects.zero_page import Zero_Page
import conf.base_url_conf

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "main page":
            test_obj = Weathershopper_Main_Page(base_url=base_url)
        elif page_name == "moisturizer list page":
            test_obj = Moisturizer_List_Page(base_url=base_url)
        elif page_name == "sunscreen list page":
            test_obj = Sunscreen_List_Page(base_url=base_url)
        elif page_name == "cart page":
            test_obj = Cart_Page(base_url=base_url)
        return test_obj

    get_page_object = staticmethod(get_page_object)
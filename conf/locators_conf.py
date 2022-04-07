#Common locator file for all locators

#temperature_display
temperature = "xpath,//span[@id='temperature']"

#weathershopper_main_page
moisturizers_button = "xpath,//button[text()='Buy moisturizers']"
sunscreens_button = "xpath,//button[text()='Buy sunscreens']"

#moisturizer_list_page
moisturizers_heading = "xpath,//h2[text()='Moisturizers']"
add_max_honey_button = "xpath,//button[contains(@onclick,'Max honey')]"
add_vassily_aloe_button = "xpath,//button[contains(@onclick,'Vassily Aloe')]"
add_mikhail_natural_button = "xpath,//button[contains(@onclick,'Mikhail Natural')]"
add_boris_almond_button = "xpath,//button[contains(@onclick,'Boris Almond')]"



#sunscreen_list_page
sunscreen_heading = "xpath,//h2[text()='Sunscreens']"
product_price_display = "xpath,//*[contains(text(),'Price')]"

price_display = "xpath,//div[contains(@class,'row')][2]//div[1]//p[2]"

#cart page
cart_button = "xpath,//button[@onclick='goToCart()']"
cart_total_price = "xpath,//p[contains(text(),'Total: Rupees')]"
pay_with_card_button = "xpath,//button[@type='submit']"

#cart_page frame
srtipe_com_heading = "xpath,//h1[text()='Stripe.com']"
email_textbox = "xpath,//input[@id='email']"
card_mumber_textbox = "id,card_number"
expiry_mm_yy_textbox = "id,cc-exp"
cvc_textbox = "id,cc-csc"
close_button = "xpath,//a[contains(@class,'close')]"
        
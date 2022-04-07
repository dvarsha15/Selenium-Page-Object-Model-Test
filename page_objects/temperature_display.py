"""
This class models the temperature display on weathershopper main page

"""

import conf.locators_conf as locators
from utils.Wrapit import Wrapit

class Temperature_Display:

    #locators
    moist_button = locators.moisturizers_button
    sunscr_button = locators.sunscreens_button
    temp = locators.temperature

    @Wrapit._exceptionHandler
    def get_temperature(self):
        "check temperature on main page"
        temperature = self.get_text(self.temp)
        temperature = temperature.decode("utf-8").split()
        
        return temperature[0]
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def compare_temperature(self):
        """ 
        compare temperature value with threshold value 30
        For less than 30,  click on 'Buy moisturizer' 
        For greater than 30, click on 'Buy sunscreen'
        """
        temperature = self.get_temperature()
        self.write('Temperature value : %s'%temperature)
        result_flag = False
        if (int(temperature) <= 30):
            result_flag = True
        
        return result_flag
        
        
   
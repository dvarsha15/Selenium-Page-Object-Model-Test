**Python based Selenium Test Automation Framework** 
------

This framework can be used to write selenium and python automation scripts to test web applications 

This automation test is implemented by referring the [github repository](https://github.com/qxf2/qxf2-page-object-model) qxf2-page-object-model for testing [weathershopper application](https://weathershopper.pythonanywhere.com/).
The test is written in __python__ and __Selenium__ is used to automate the tests. The framework design is based on __Page Object Model__(POM). 

If you want to work on Page Object Model or Test Automation, this framework will be useful for you.

------
Setup
------

The setup has two parts:

1. Prerequisites
2. Setup for Selenium Automation

__1. Prerequisites__

a) Install Python 3.x

b) Add Python 3.x to your PATH environment variable

c) If you do not have it already, get pip (NOTE: Most recent Python distributions come with pip)

d) pip install -r requirements.txt to install dependencies

__2. Setup for Selenium Automation__

a) Get setup with your browser driver. If you don't know how to, please try:

   > [For Chrome](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [For Firefox]( https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)

#Note: Check Firefox version & Selenium version compatibility before downloading geckodriver.

__If your setup goes well__, you should run a simple test with this command:

1. Chrome: `python -m pytest -k check_temperature --browser Chrome`

2. Firefox: `python -m pytest -k check_temperature --browser Firefox`

-------------------
Repository details
-------------------
a) Directory structure of our current Templates

   ./

	|__conf: For all configurations and credential files

	|__log: Log files for all tests

	|__page_objects: Contains our Base Page, different Page Objects, DriverFactory, PageFactory

	|__screenshots: For screen shots

	|__tests: Put your tests in here

	|__utils: All utility modules (email_util,TestRail, BrowserStack, Base Logger, post_test_reports_to_slack) are kept in this folder

    ---------------------------
COMMANDS FOR RUNNING TESTS
---------------------------

a)py.test [options]

	-s	used to display the output on the screen			E.g: python -m pytest -s (This will run all the tests in the directory and subdirectories)
	--base_url  used to run against specific URL			E.g: python -m pytest --base_url http://YOUR_localhost_URL (This will run against your local instance)
	--ver/-O	used to run against different browser versions/os versions	E.g: python -m pytest --ver 44 -O 8 (This will run each test 4 times in different browser version(default=45 & 44) and OS(default=7 & 8) combination)
	-h	help for more options 						E.g: python -m pytest -h
	-k      used to run tests which match the given substring expresion 	E.g: python -m pytest -k select_sunscreen  (This will trigger test_select_sunscreen_of_lowest_price.py test)
	

b)python tests/test_check_temperature_and_navigate.py (can also be used to run standalone test)

c)python tests/test_check_temperature_and_navigate.py --browser Chrome (to run against chrome)





"""
Implementing the questionaty library to fetch the users choices for different arguments
"""
import sys
import questionary
from clear_screen import clear
#from conf import api_example_conf
from conf import browser_os_name_conf as conf
from conf import remote_credentials

def display_gui_test_options(browser,browser_version,os_version,
                             os_name,remote_flag,testrail_flag,tesults_flag):
    "Displays the selected options to run the GUI test"
    print("Browser selected:",browser)
    if browser_version == []:
        print("Browser version selected: None")
    else:
        print("Browser version selected:",browser_version)
    if os_name == []:
        print("OS selected: None")
    else:
        print("OS selected:",os_name)
    if os_version == []:
        print("OS version selected: None")
    else:
        print("OS version selected:",os_version)
    print("Remote flag status:",remote_flag)
    print("Testrail flag status:",testrail_flag)
    print("Tesults flag status:",tesults_flag)

def set_default_flag_gui(browser,browser_version,os_version,os_name,
                         remote_flag,testrail_flag,tesults_flag):
    "This checks if the user wants to run the test with the default options or no"

    questionary.print("\nDefault Options",style="bold fg:green")
    questionary.print("**********",style="bold fg:green")
    display_gui_test_options(browser,browser_version,os_version,
                             os_name,remote_flag,testrail_flag,tesults_flag)
    questionary.print("**********",style="bold fg:green")

    default = questionary.select("Do you want to run the test with the default set of options?",
                                  choices=["Yes","No"]).ask()
    default_flag = True if default == "Yes" else False

    return default_flag

def get_user_response_gui():
    "Get response from user for GUI tests"
    response = questionary.select("What would you like to change?",
                                   choices=["Browser","Browser Version","Os Version",
                                   "Os Name","Remote flag status","Testrail flag status",
                                   "Tesults flag status","Set Remote credentials",
                                   "Revert back to default options","Run","Exit"]).ask()

    return response

def ask_questions_gui(browser,browser_version,os_version,os_name,remote_flag,
                      testrail_flag,tesults_flag):
    """This module asks the users questions on what options they wish to run
       the test with and stores their choices"""
    clear()
    while True:
        questionary.print("\nUse up and down arrow keys to switch between options.\
                           \nUse Enter key to select an option",
                           style="bold fg:yellow")
        questionary.print("\nSelected Options",style="bold fg:green")
        questionary.print("**********",style="bold fg:green")
        display_gui_test_options(browser, browser_version, os_version, os_name,
                                 remote_flag, testrail_flag, tesults_flag)
        questionary.print("**********",style="bold fg:green")
        response = get_user_response_gui()
        clear()
        if response == "Browser":
            browser=questionary.select("Select the browser",
                                        choices=conf.browsers).ask()
            browser_version = []
            if remote_flag == "Y":
                questionary.print("Please select the browser version",
                                   style="bold fg:darkred")

        if response == "Browser Version":
            if remote_flag == "Y":
                browser_version = get_browser_version(browser)
            else:
                questionary.print("Browser version can be selected only when running the test remotely.\
                                   \nPlease change the remote flag status inorder to use this option",
                                   style="bold fg:red")

        if response == "Remote flag status":
            remote_flag = get_remote_flag_status()
            if remote_flag == "Y":
                browser = "chrome"
                os_name = "Windows"
                os_version = "10"
                browser_version = "65"
                questionary.print("The default remote test options has been selected",
                                   style="bold fg:green")

        if response == "Os Version":
            os_version = get_os_version(os_name)

        if response == "Os Name":
            if remote_flag == "Y":
                os_name, os_version = get_os_name(remote_flag)
            else:
                questionary.print("OS Name can be selected only when running the test remotely.\
                                  \nPlease change the remote flag status inorder to use this option",
                                   style="bold fg:red")

        if response == "Testrail flag status":
            testrail_flag = get_testrailflag_status()

        if response == "Tesults flag status":
            tesults_flag = get_tesultsflag_status()

        if response == "Set Remote credentials":
            set_remote_credentials()

        if response == "Revert back to default options":
            browser, os_name, os_version,  browser_version, remote_flag, testrail_flag, tesults_flag = gui_default_options()
            questionary.print("Reverted back to the default options",style="bold fg:green")

        if response == "Run":
            if remote_flag == "Y":
                if browser_version == []:
                    questionary.print("Please select the browser version before you run the test",
                                       style="bold fg:darkred")
                elif os_version == []:
                    questionary.print("Please select the OS version before you run the test",
                                       style="bold fg:darkred")
                else:
                    break
            else:
                break

        if response == "Exit":
            sys.exit("Program interrupted by user, Exiting the program....")

    return browser,browser_version,remote_flag,os_name,os_version,testrail_flag,tesults_flag

def get_testrailflag_status():
    "Get the testrail flag status"
    testrail_flag = questionary.select("Enter the testrail flag",
                                        choices=["Yes","No"]).ask()

    if testrail_flag == "Yes":
        testrail_flag = "Y"
    else:
        testrail_flag = "N"

    return testrail_flag

def get_tesultsflag_status():
    "Get tesults flag status"
    tesults_flag = questionary.select("Enter the tesults flag",
                                       choices=["Yes","No"]).ask()

    if tesults_flag == "Yes":
        tesults_flag = "Y"
    else:
        tesults_flag = "N"

    return tesults_flag

def set_remote_credentials():
    "set remote credentials file to run the test on browserstack or saucelabs"
    platform = questionary.select("Select the remote platform on which you wish to run the test on",
                                   choices=["Browserstack","Saucelabs"]).ask()
    if platform == "Browserstack":
        platform = "BS"
    else:
        platform = "SL"
    username = questionary.text("Enter the Username").ask()
    password = questionary.password("Enter the password").ask()
    with open("conf/remote_credentials.py",'w') as cred_file:
        cred_file.write("REMOTE_BROWSER_PLATFORM = '%s'\
                         \nUSERNAME = '%s'\
                         \nACCESS_KEY = '%s'"%(platform,username,password))
    questionary.print("Updated the credentials successfully",
                       style="bold fg:green")

def get_remote_flag_status():
    "Get the remote flag status"
    remote_flag = questionary.select("Select the remote flag status",
                                      choices=["Yes","No"]).ask()
    if remote_flag == "Yes":
        remote_flag = "Y"
    else:
        remote_flag = "N"

    return remote_flag

def get_browser_version(browser):
    "Get the browser version"
    if browser == "chrome":
        browser_version=questionary.select("Select the browser version",
                                            choices=conf.chrome_versions).ask()

    elif browser == "firefox":
        browser_version=questionary.select("Select the browser version",
                                            choices=conf.firefox_versions).ask()

    elif browser == "safari":
        browser_version = questionary.select("Select the browser version",
                                              choices=conf.safari_versions).ask()

    return browser_version

def get_os_version(os_name):
    "Get OS Version"
    if os_name == "windows":
        os_version = questionary.select("Select the OS version",
                                         choices=conf.windows_versions).ask()
    elif os_name == "OS X":
        if remote_credentials.REMOTE_BROWSER_PLATFORM == "SL":
            os_version = questionary.select("Select the OS version",
                                             choices=conf.sauce_labs_os_x_versions).ask()
        else:
            os_version = questionary.select("Select the OS version",
                                             choices=conf.os_x_versions).ask()
    else:
        os_version= []
        questionary.print("Please select the OS Name first",
                           style="bold fg:darkred")

    return os_version

def get_os_name(remote_flag):
    "Get OS Name"
    os_name = questionary.select("Enter the OS version",choices=conf.os_list).ask()
    os_version = []
    if remote_flag == "Y":
        questionary.print("Please select the OS Version",style="bold fg:darkred")

    return os_name, os_version

def gui_default_options():
    "The default options for GUI tests"
    browser = conf.default_browser[0]
    os_name = []
    os_version = []
    browser_version = []
    remote_flag = "N"
    testrail_flag = "N"
    tesults_flag = "N"

    return browser, os_name, os_version,  browser_version, remote_flag, testrail_flag, tesults_flag

def get_sessionflag_status():
    "Get the session flag status"
    session_flag=questionary.select("Select the Session flag status",
                                     choices=["True","False"]).ask()
    if session_flag == "True":
        session_flag = True
    if session_flag == "False":
        session_flag = False

    return session_flag


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


def input_names():
    forward_names = []
    defense_names = []
    number_of_forwards = int(input("How many forwards are on your team?: "))

    for i in range(number_of_forwards):
        name = str(input("Enter the Full Name of the forward: "))
        forward_names.append(name)

    number_of_defense = int(input("How many defensemen are on your team?: "))
    for x in range(number_of_defense):
        dname = str(input("please type the full name of the defenseman: "))
        defense_names.append(dname)

    return forward_names, defense_names


def init_driver():
    driver = webdriver.Chrome('C:\\Users\Josh-\Downloads\chromedriver')
    driver.wait = WebDriverWait(driver, 5)
    return driver


def login(driver):
    driver.get('http://fantasy.espn.com/hockey/league?leagueId=60935874')
    time.sleep(1)
    driver.switch_to.frame('disneyid-iframe')
    driver.find_element_by_xpath(
        '//*[@id="did-ui-view"]/div/section/section/form/section/div[1]/div/label/span[2]/input').send_keys(
        'email')  # EMAIL HERE
    driver.find_element_by_xpath(
        '//*[@id="did-ui-view"]/div/section/section/form/section/div[2]/div/label/span[2]/input').send_keys(
       'password')  # PASSWORD HERE
    # click next to login
    driver.find_element_by_xpath('//*[@id="did-ui-view"]/div/section/section/form/section/div[3]/button').click()
    time.sleep(1)  # wait before switching frame to default
    driver.switch_to_default_content()  # change back to default frame
    driver.find_element_by_link_text('My Team').click()  # switch to my team page
    time.sleep(3)  # wait for team page to load
    # right arrow button to change date
    driver.find_element_by_xpath('//*[@id="espn-analytics"]/div'
                                 '/div[5]/div[2]/div[2]/div/div/div/div[1]/div[1]/nav/div[2]/div/div/button[2]').click()
    time.sleep(1)  # wait for the new dates to show up
    # clicking next day
    driver.find_element_by_xpath('//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div'
                                 '/div[1]/div[1]/nav/div[2]/div/div/div/div/div[30]/div/div[1]/span[2]/span').click()


def set_lineup(driver):
    forward_names, defense_names = input_names()

    bench_move_button = [
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[17]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[18]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[19]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[20]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[21]/td[3]/div/div']

    forwards_here_button = [
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[1]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[2]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[3]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[4]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[5]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[6]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[7]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[8]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[9]/td[3]/div/div']

    defense_here_button = [
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[10]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[11]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[12]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[13]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[14]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[15]/td[3]/div/div',
        '//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr[16]/td[3]/div/div']

    player_data_list = driver.find_elements_by_xpath('//*[@id="espn-analytics"]/div/div[5]/div[2]/div[2]/div/div/div/'
                                                     'div[3]/div[1]/section/table/tbody/tr/td[1]/table/tbody/tr')
    forward_on_ice_data_list = [player_data_list[i] for i in range(0, 9)]
    defense_on_ice_data_list = [player_data_list[i] for i in range(9, 16)]
    bench_data_list = [player_data_list[i] for i in range(16, 21)]

    
    i = 0
    for benched_row in bench_data_list:

        if 'PM' in benched_row.text:
            # click on move for the player with a game tonight
            driver.find_element_by_xpath(bench_move_button[i]).click()
            if benched_row.text.splitlines()[1] in forward_names:
                x = 0
                for forward_iced_row in forward_on_ice_data_list:
                    if 'PM' not in forward_iced_row.text:
                        element = driver.find_element_by_xpath(forwards_here_button[x])
                        driver.execute_script("window.scrollTo(0,400)")
                        time.sleep(1)
                        element.click()
                        time.sleep(1)
                        driver.execute_script("window.scrollTo(0,900)")
                        time.sleep(1)
                        break
                    x += 1
            if benched_row.text.splitlines()[1] in defense_names:
                z = 0
                for defense_iced_row in defense_on_ice_data_list:

                    if 'PM' not in defense_iced_row.text:
                        element = driver.find_element_by_xpath(defense_here_button[z])
                        driver.execute_script("window.scrollTo(0,700)")
                        time.sleep(1)
                        element.click()
                        time.sleep(1)
                        driver.execute_script("window.scrollTo(0,900)")
                        break
                    z += 1
        i += 1


d = init_driver()
login(d)
set_lineup(d)



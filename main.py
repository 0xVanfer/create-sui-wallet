from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


# any with one upper letter and length>8
password = "Asf453jkb4jk3bS"
# file name to save the memories and addresses
file_name = "mnemonic"
# the address already has 50,000,000 SUI
faucet_mnemonic = "USE YOUR OWN MNEMONIC WITH 50000000 SUI"


def df_to_csv(df, name):
    # save dataframe as csv
    df.to_csv(name + '.csv', index=False)


def csv_to_df(name):
    # read csv to dataframe
    df = pd.read_csv(name + '.csv')
    return df


def add_to_csv(file_name, add_text):
    # add a line to file_name.csv
    # should be like [xx,xx,xx]
    df = csv_to_df(file_name)
    l = len(df)
    df.loc[l] = add_text
    df_to_csv(df, file_name)


def click(driver, xpath, time_to_sleep):
    # click once
    # if click more times, try another method
    button = driver.find_element(By.XPATH, xpath)
    print('click on "' + button.text + '"')
    clicking = ActionChains(driver).click(button)
    clicking.perform()
    time.sleep(time_to_sleep)


def new_window(driver, url):
    # create a new window by the url
    # remember to switch to the new window!
    driver.execute_script('window.open("'+url+'")')


def switch_to_window(driver, window_number):
    # switch to another window, start from 0
    driver.switch_to.window(driver.window_handles[window_number])
    print('switched to window numer:', str(window_number))


def input_text(driver, xpath, text):
    key = driver.find_element(By.XPATH, xpath)
    key.send_keys(text)


def CreateDriver():
    # new driver
    option = webdriver.ChromeOptions()
    option.add_extension("./sui_wallet.crx")
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    time.sleep(3)
    return driver


def CreateNewWalletWindow(driver):
    url = "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/welcome"
    new_window(driver, url)
    switch_to_window(driver, 1)
    driver.close()
    time.sleep(3)
    switch_to_window(driver, 1)
    try:
        LogOut(driver)
    finally:
        return


def LogIn(driver, mnemonic):
    click(driver, '/html/body/div/div/div/div/div/div[2]/a', 0)
    click(driver, "/html/body/div/div/div/div[2]/a", 0)
    input_text(driver, "/html/body/div/div/div/form/label/textarea", mnemonic)
    click(driver, "/html/body/div/div/div/form/button", 0)
    input_text(driver,
               "/html/body/div/div/div/form/label[1]/input", password)
    input_text(driver,
               "/html/body/div/div/div/form/label[2]/input", password)
    click(driver, "/html/body/div/div/div/form/div[2]/button[2]", 1)
    click(driver, "/html/body/div/div/div/button", 0)


def LogOut(driver):
    click(driver, "/html/body/div/div/div/div[1]/a[2]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/a[1]/div[2]", 0)
    click(driver, "/html/body/div/div/div/div[2]/div/div[2]/div/button", 1)


def GetSUI(driver, addrToSend):
    LogIn(driver, faucet_mnemonic)
    click(driver, "/html/body/div/div/div/div[2]/main/div/div[2]/a[2]", 0)
    # input amount, must over 10000
    input_text(driver,
               "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[1]/div[1]/input", "12345")
    click(driver,
          "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[2]/div/button", 0)
    # input address
    input_text(driver,
               "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/textarea", addrToSend)
    # send sui, wait for pending
    click(driver,
          "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[2]/div/button", 7)
    click(driver, "/html/body/div/div/div/div[2]/main/div/button/i", 0)
    LogOut(driver)


def CreateNewWallet(driver):
    click(driver, '/html/body/div/div/div/div/div/div[2]/a', 0)
    click(driver, "/html/body/div/div/div/div[1]/a", 0)

    input_text(
        driver, "/html/body/div/div/div/form/div/fieldset/label[1]/input", password)
    input_text(
        driver, "/html/body/div/div/div/form/div/fieldset/label[2]/input", password)

    click(
        driver, "/html/body/div/div/div/form/div/fieldset/label[3]/span[1]", 0)
    click(driver, "/html/body/div/div/div/form/button", 1)
    mnemonic = driver .find_element(
        By.XPATH, "/html/body/div/div/div/div[2]").text
    mnemonic = str.replace(mnemonic, "COPY", "")
    mnemonic = str.replace(mnemonic, "\n", "")
    click(driver, "/html/body/div/div/div/button", 0)
    click(driver,
          "/html/body/div/div/div/div[2]/nav/div[2]/a[3]", 1)
    full_addr = driver .find_element(
        By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/a").get_attribute("href")
    addr = full_addr[41:]
    LogOut(driver)
    return mnemonic, addr


def MintNFT(driver, mnemonic):
    LogIn(driver, mnemonic)
    # nft
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[3]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    # click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[2]/i", 1)
    LogOut(driver)


def CreateHundred(driver):
    CreateNewWalletWindow(driver)
    for i in range(0, 100):
        mnemonic, addr = CreateNewWallet(driver)
        GetSUI(driver, addr)
        MintNFT(driver, mnemonic)
        add_to_csv(file_name, [mnemonic, addr])


def main():
    # df = pd.DataFrame(columns=["mnemonic", "addr"])
    # df_to_csv(df, file_name)
    start = time.time()
    driver = CreateDriver()
    for i in range(0, 10000):
        try:
            CreateHundred(driver)
        except:
            continue

    end = time.time()
    print("time used:", end-start)


main()

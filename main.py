from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


# Any password with one upper letter and length>8.
password = "Asf453jkb4jk3bS"
# File name to save the memories and addresses.
file_name = "mnemonic"


def df_to_csv(df, name):
    # Save dataframe as csv.
    df.to_csv(name + '.csv', index=False)


def csv_to_df(name):
    # Read csv to dataframe.
    df = pd.read_csv(name + '.csv')
    return df


def add_to_csv(file_name, add_text):
    # Add a line to file_name.csv
    # Should be like [xx,xx,xx]
    df = csv_to_df(file_name)
    l = len(df)
    df.loc[l] = add_text
    df_to_csv(df, file_name)


def click(driver, xpath, time_to_sleep):
    # Click once.
    # If click more times, try another method.
    button = driver.find_element(By.XPATH, xpath)
    print('click on "' + button.text + '"')
    clicking = ActionChains(driver).click(button)
    clicking.perform()
    time.sleep(time_to_sleep)


def new_window(driver, url):
    # Create a new window by the url.
    # Remember to switch to the new window!
    driver.execute_script('window.open("'+url+'")')


def switch_to_window(driver, window_number):
    # Switch to another window, start from 0.
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


def CreateNewWallet(driver):
    click(driver, '/html/body/div/div/div/div/div/div[2]/a', 0)
    click(driver, "/html/body/div/div/div/div[1]/a", 0)
    # Input any password.
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
    # Get the address.
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[3]", 1)
    full_addr = driver .find_element(
        By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/a").get_attribute("href")
    addr = full_addr[42:]
    return mnemonic, addr


def TransferSUI(driver):
    1


def MintTestToken(driver):
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[1]", 1)
    # Switch to test net.
    click(driver, "/html/body/div/div/div/div[1]/a[2]/span[3]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/a[2]/div[2]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[4]/button", 0)
    click(driver, "/html/body/div/div/div/div[1]/a[2]/span[1]", 0)
    # May take a while to switch to test net.
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[1]/i", 5)
    # Request test token, may take long.
    click(driver, "/html/body/div/div/div/div[2]/main/div/div[4]/button", 0)
    # Try for at most 5 minutes.
    for i in range(0, 30):
        time.sleep(10)
        balance = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/main/div/div[1]/div/div/span[1]").text
        if balance != "0":
            break
        print("balance still 0")
    # Now you should have got the test token. Return whether minted successfully.
    # True for success, False for fail.
    return balance != "0"


def MintThreeNFTs(driver):
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[3]", 1)
    # Mint nfts.
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)


def CreateHundred(driver):
    CreateNewWalletWindow(driver)
    for i in range(0, 100):
        # Create a new wallet.
        mnemonic, addr = CreateNewWallet(driver)
        # Mint test tokens. If success, mint nfts; if fail, log out and try another.
        success = MintTestToken(driver)
        if success:
            MintThreeNFTs(driver)
            add_to_csv(file_name, [mnemonic, addr])
        # Always log out.
        LogOut(driver)


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

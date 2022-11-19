from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time


# Any password with one upper letter and length>8.
password = "Asf453jkb4jk3bS"
# File name to save the memories and addresses.
# xxx.csv.
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
    # New a driver with extension sui_wallet.
    option = webdriver.ChromeOptions()
    option.add_extension("./sui_wallet.crx")
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    time.sleep(5)
    return driver


def CreateNewWalletWindow(driver):
    # Create a new window and switch to it.
    url = "chrome-extension://opcgpfmipidbgpenhmajoajpbobppdil/ui.html#/welcome"
    new_window(driver, url)
    switch_to_window(driver, 1)
    driver.close()
    time.sleep(5)
    switch_to_window(driver, 1)
    try:
        LogOut(driver)
    finally:
        return


def SetWalletSleepTime(driver):
    # The wallet will lock after 5 minutes, change it to 30 minutes(max).
    click(driver, "/html/body/div/div/div/div[1]/a[2]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/a[1]/div[2]", 0)
    # Delete default "5" and set the number to 30.
    input_text(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/form/div/input", "\b30")
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div/button", 0)
    click(driver, "/html/body/div/div/div/div[1]/a[2]", 0)


def LogIn(driver, mnemonic):
    # Log in an account with mnemonic.
    click(driver, '/html/body/div/div/div/div/div/div[2]/a', 0)
    click(driver, "/html/body/div/div/div/div[2]/a", 0)
    input_text(driver, "/html/body/div/div/div/form/label/textarea", mnemonic)
    click(driver, "/html/body/div/div/div/form/div[2]/button", 0)
    input_text(driver,
               "/html/body/div/div/div/form/label[1]/input", password)
    input_text(driver,
               "/html/body/div/div/div/form/label[2]/input", password)
    click(driver, "/html/body/div/div/div/form/div[2]/button[2]", 1)
    click(driver, "/html/body/div/div/div/button", 0)


def LogOut(driver):
    # Log out an account.
    click(driver, "/html/body/div/div/div/div[1]/a[2]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/a[1]/div[2]", 0)
    # After logging out, it can take a while for the page to reload.
    click(driver, "/html/body/div/div/div/div[2]/div/div[2]/div/button", 5)


def CreateNewWallet(driver):
    # Create a new wallet.
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
    # Get mnemonic.
    mnemonic = driver .find_element(
        By.XPATH, "/html/body/div/div/div/div[2]").text
    mnemonic = str.replace(mnemonic, "COPY", "")
    mnemonic = str.replace(mnemonic, "\n", "")
    click(driver, "/html/body/div/div/div/button", 0)
    # Get the address.
    # The address shown in the wallet is not complete. Use blockscan link to read the address.
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[3]", 1)
    full_addr = driver .find_element(
        By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/a").get_attribute("href")
    # Do not understand why, link length is not constant.
    addr = full_addr[41:]
    if len(addr) != 42:
        addr = full_addr[42:]
    return mnemonic, addr


def SendSUI(driver, sendAmount, receiver):
    # If sent successfully, return True, else return False.
    try:
        click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[1]/i", 0)
        click(
            driver, "/html/body/div/div/div/div[2]/main/div/div[2]/a[2]/div/i", 0)
        input_text(
            driver, "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[1]/div[1]/input", sendAmount)
        # Continue. If insufficient, button will be grey.
        click(
            driver, "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[2]/div/button", 0)
        # Fill in address.
        input_text(
            driver, "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/textarea", receiver)
        # Send, may take a while. WAIT.
        click(
            driver, "/html/body/div/div/div/div[2]/main/div/div[2]/form/div[2]/div/button", 20)
        try:
            # There are two types of tx result. Sent successful window may not pop up.
            click(driver, "/html/body/div/div/div/div[2]/main/div/button/i", 0)
            return True
        except:
            return True
    except:
        return False


def SwitchToTestNet(driver):
    # Switch to test net.
    click(driver, "/html/body/div/div/div/div[1]/a[2]/span[3]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/a[2]/div[2]", 0)
    click(
        driver, "/html/body/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[4]/button", 0)
    click(driver, "/html/body/div/div/div/div[1]/a[2]/span[1]", 0)
    # May take a while to switch to test net. WAIT.
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[1]/i", 10)


def MintTestToken(driver):
    click(driver, "/html/body/div/div/div/div[2]/nav/div[2]/a[1]", 1)
    SwitchToTestNet(driver)
    # Request test token, may take long.
    click(driver, "/html/body/div/div/div/div[2]/main/div/div[4]/button", 0)
    # Try for at most 5 minutes.
    # You can add the time to up to 30 minutes, or the wallet will fall asleep.
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
    # Mint nfts. WAIT.
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)
    click(
        driver, "/html/body/div/div/div/div[2]/main/div/div/section/div/div[1]/button", 5)


def CreatePack(driver):
    CreateNewWalletWindow(driver)
    mns = pd.DataFrame(columns=["mnemonic", "addr"])
    # Max 10.
    # After 10 wallets, the balance will be 0.00001, not enough for minting nfts.
    walletLength = 10

    # Create wallets first and save in dataframe.
    for i in range(0, walletLength):
        mn, addr = CreateNewWallet(driver)
        mns.loc[len(mns)] = [mn, addr]
        print("NO."+str(i), "wallet created.")
        LogOut(driver)

    # Log in the first wallet and get test SUI.
    LogIn(driver, mns["mnemonic"][0])
    SetWalletSleepTime(driver)
    success = MintTestToken(driver)
    if not success:
        LogOut(driver)
        return
    # Mint nfts.
    MintThreeNFTs(driver)
    add_to_csv(file_name, mns.loc[0])
    # Send balance to next wallet.
    # If you want to leave more balance in your wallets, reduce the amount to send.
    success = SendSUI(driver, "0.000055", mns["addr"][1])
    if not success:
        LogOut(driver)
        return
    LogOut(driver)

    # Later wallets.
    for i in range(1, walletLength):
        LogIn(driver, mns["mnemonic"][i])
        SwitchToTestNet(driver)
        MintThreeNFTs(driver)
        add_to_csv(file_name, mns.loc[i])
        # Send SUI to next wallet.
        # If you want to leave more balance in your wallets, reduce the amount to send.
        # Use 0.000055-0.000005*i will let the string to be 5e-5.
        success = SendSUI(driver, "0.0000"+str(55-i*5), mns["addr"][i+1])
        if not success:
            LogOut(driver)
            return
        LogOut(driver)


def main():
    # df = pd.DataFrame(columns=["mnemonic", "addr"])
    # df_to_csv(df, file_name)
    start = time.time()
    driver = CreateDriver()
    for i in range(0, 10000):
        try:
            CreatePack(driver)
        except:
            continue

    end = time.time()
    print("time used:", end-start)


main()

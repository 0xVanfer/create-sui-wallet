# Create SUI wallet.

Updated on Nov.18.2022

In one round, create 20 wallets with 3 nfts.

Highly efficient, compared with previous versions.

<!-- Each IP has a limit on requesting test token. You may wait for an hour or change your IP to get another wallet. -->

## Chrome、Chromedriver

Must have chrome driver

1. [download](https://chromedriver.chromium.org/downloads)

    Chrome and chrome driver must be the same version.

2. Install

    For mac:

    Save the corresponding version into "usr/local/bin" and run:

    > $ xattr -d com.apple.quarantine chromedriver

## pip

> pip3 install selenium

> pip3 install pandas

## crx

sui_wallet.crx is the 22.11.9.0_3 version.

To package it yourself:

1. visit chrome://version/

2. get your file path, like "/Users/vanfer/Library/Application Support/Google/Chrome/Default"

3. Find "Extentions/opcgpfmipidbgpenhmajoajpbobppdil"

4. copy the path of file "22.11.9.0_0"

5. visit chrome://extensions/

6. package it in dev mode and get your crx file

7. copy the crx file and paste here

## Run

> python3 -m main

## Bugs

Transactions may take several seconds, so if your program breaks because of bad network condition,
find "WAIT" in main.py, and edit the time to sleep.

###### Support

ethereum address: 0x8888888856cf9a441D638dc41fBd460D2d3b912D

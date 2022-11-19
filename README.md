# Create SUI wallet.

Updated on Nov.19.2022

Create wallets with 3 nfts and save the mnemonic and address to [mnemonic.csv](mnemonic.csv).

Highly efficient, compared with previous versions.

<!-- Each IP has a limit on requesting test token. You may wait for an hour or change your IP to get another wallet. -->

## Preparation

#### Chrome、Chromedriver

Must have chrome driver

1. [download](https://chromedriver.chromium.org/downloads)

    Chrome and chrome driver must be the same version.

2. Install

    For mac:

    Save the corresponding version into "usr/local/bin" and run:

    > $ xattr -d com.apple.quarantine chromedriver

#### Python packages

> pip3 install selenium

> pip3 install pandas

#### crx

sui_wallet.crx is the 22.11.9 version.

Users do not have to worry about it, but in case of file broken or locked, you can alse package it your self.

0. Install sui wallet extension. ID: opcgpfmipidbgpenhmajoajpbobppdil

1. Visit chrome://version/

2. Get your file path, like "/Users/vanfer/Library/Application Support/Google/Chrome/Default"

3. Find "Extentions/opcgpfmipidbgpenhmajoajpbobppdil"

4. Copy the path of file "22.11.9.0_0"

5. Visit chrome://extensions/

6. Package it in dev mode and get your crx file. Named as 22.11.9.0_0.crx

7. Copy the crx file and paste here, rename as sui_wallet.crx.

## Run

Make sure you have google chrome and chrome driver installed.

Make sure you have selenium and pandas installed(pip3).

> python3 -m main

## Bugs

Transactions may take several seconds, so if your program breaks because of bad network condition,
find "WAIT" in main.py, and edit the time to sleep.

###### Support

ethereum address: 0x8888888856cf9a441D638dc41fBd460D2d3b912D

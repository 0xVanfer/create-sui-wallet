# Create SUI wallet.

Updated on Nov.16.2022

Create a SUI wallet and mint 3 test NFTs.

This version is stable, and will not break.

Around 3 minutes to create a new wallet.

Each IP has a limit on requesting test token. You may wait for an hour or change your IP to get another wallet.

TODO: One claim can afford several wallets' mint. Transfer the balance to next wallet created if balance is enough.

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

You can also create it yourself by visiting chrome://extensions/ and package it as a new crx file.

## Run

> python3 -m main

###### Support

ethereum address: 0x8888888856cf9a441D638dc41fBd460D2d3b912D

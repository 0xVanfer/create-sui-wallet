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

sui_wallet.crx is the v0.2.0 version.

Not up to date, but still can use.

You can also create it yourself by visiting chrome://extensions/ and package it as a new crx file.

## Before Starting

Change the constant "faucet_mnemonic" in [main.py](./main.py) to your own mnemonic with 50,000,000 SUI.(air drop)

## Run

> python3 -m main

###### Support

ethereum address: 0x8888888856cf9a441D638dc41fBd460D2d3b912D

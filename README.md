# crypto-value-scraping
This projects scrapes the actual value of the define digital assets in the script from CoinMarketCap.

The script takes care of reading from "https://coinmarketcap.com/" the value of the selected Cryptos, saving them and writing them to a .csv file with the correct European formatting (commas count as decimal separators). The price is in euros (EUR), since this is the value that is returned by the functions created.
The project consists of three files:
- main.py
- Crypto_Url.py
- csv_Writing.py

N.B. In order to use the script you must run the file 'main.py' from the terminal.

In case you want to add more coins, you need to enter the Crypto_Url.py file and in the function 'url_object()' add a new parameter entry line as follows:

....
	data.append(["LINK COINMARKETCAP'S CRYPTO PAGE DEDICATED TO COIN," "priceValue___11gHJ," "CURRENCY NAME," "SAME CURRENCY SYMBOL"])
....

import Crypto_Url
import csv
import csv_Writing


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url_list = Crypto_Url.url_object()
    count = 0
    
    csv_path = './CryptoValue.csv'

    with open(csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Column1.name', 'Column1.symbol', 'Column1.price_usd'])

        for i in url_list:
            price = Crypto_Url.url_data(url_list[count])
            print(url_list[count][2] + ': ' + price.text)
            res = csv_Writing.csv_append(writer, url_list[count], price.text[1:])
            count += 1


print(bcolors.OKGREEN + '\nCrypto Value Scraping ended successfully!!!\n' + bcolors.ENDC);
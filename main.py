import Crypto_Url
import csv
import csv_Writing

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    url_list = Crypto_Url.url_object()
    count = 0

    #csv_path = '/Users/andrea/Budget Plan/Investimenti/Crypto/CryptoValue.csv'
    csv_path = './CryptoValue.csv'

    with open(csv_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Column1.name', 'Column1.symbol', 'Column1.price_usd'])

        for i in url_list:
            price = Crypto_Url.url_data(url_list[count])
            print(url_list[count][2] + ': ' + price.text)
            res = csv_Writing.csv_append(writer, url_list[count], price.text[1:])
            count += 1



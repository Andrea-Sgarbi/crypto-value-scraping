import locale


def csv_append(csv, info, price):
    price = price.replace(',', '')
    locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
    temp = locale.atof(price)
    price_value = f"{locale.format('%.8f', temp)}"
    csv.writerow([info[2], info[3], price_value])
    return 0
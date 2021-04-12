import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import re
import os
import kaggle

def create_final_table():

    def download_dataset():
        '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
        this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
        Takes: url from kaggle
        Returns: a folder with the downloaded and unzipped csv
        '''

        #Gets the name of the dataset.zip
        url = 'https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021'

        #Gets the name of the dataset.zip
        endopint = url.split("/")[-1]
        user = url.split("/")[-2]

        #Download, decompress and leaves only the csv
        download = f"kaggle datasets download -d {user}/{endopint}"
        decompress = f"tar -xzvf {endopint}.zip"
        delete = f"del {endopint}.zip"

        for i in [download, decompress, delete]:
            os.system(i)

        #Move the csv to uour data folder
        move_and_delete = "move 2021.csv data/"
        delete_csv = 'del *.csv'
        os.system(delete_csv)
        print('Database downloaded')
        return os.system(move_and_delete)
            
    download_dataset()
    
    def crypto_scrapping():
        '''With this function we look up for the table located in yahoo finance web page and we compile this information and create
        a dataset. Once we have this dataset we change the date column from month (word) to month (number).
        '''
        url_btc = "https://es.finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR"
        html = requests.get(url_btc)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]
        tabla_btc = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_btc.append(crypto)

        tabla_btc = pd.DataFrame(tabla_btc)
        tabla_btc.head()

        for value in range(0, len(tabla_btc)):
            tabla_btc['crypto'] = 'bitcoin'


        url_eth = "https://es.finance.yahoo.com/quote/ETH-EUR/history?p=ETH-EUR"
        html = requests.get(url_eth)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_eth = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_eth.append(crypto)

        tabla_eth = pd.DataFrame(tabla_eth)
        tabla_eth.head()

        for value in range(0, len(tabla_eth)):
            tabla_eth['crypto'] = 'ethereum'

        url_bch = "https://es.finance.yahoo.com/quote/BCH-EUR/history?p=BCH-EUR"
        html = requests.get(url_bch)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_bch = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_bch.append(crypto)

        tabla_bch = pd.DataFrame(tabla_bch)
        tabla_bch.head()

        for value in range(0, len(tabla_bch)):
            tabla_bch['crypto'] = 'bitcoincash'

        url_ksm = "https://es.finance.yahoo.com/quote/KSM-EUR/history?p=KSM-EUR"
        html = requests.get(url_ksm)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_ksm = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_ksm.append(crypto)

        tabla_ksm = pd.DataFrame(tabla_ksm)
        tabla_ksm.head()

        for value in range(0, len(tabla_ksm)):
            tabla_ksm['crypto'] = 'kusama'

        url_bnb = "https://es.finance.yahoo.com/quote/BNB-EUR/history?p=BNB-EUR"
        html = requests.get(url_bnb)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_bnb = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_bnb.append(crypto)

        tabla_bnb = pd.DataFrame(tabla_bnb)
        tabla_bnb.head()

        for value in range(0, len(tabla_bnb)):
            tabla_bnb['crypto'] = 'binance_coin'

        url_ltc = "https://es.finance.yahoo.com/quote/LTC-EUR/history?p=LTC-EUR"
        html = requests.get(url_ltc)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_ltc = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_ltc.append(crypto)

        tabla_ltc = pd.DataFrame(tabla_ltc)
        tabla_ltc.head()

        for value in range(0, len(tabla_ltc)):
            tabla_ltc['crypto'] = 'lite_coin'

        url_btg = "https://es.finance.yahoo.com/quote/BTG-EUR/history?p=BTG-EUR"
        html = requests.get(url_btg)
        soup = BeautifulSoup(html.content,"html.parser")

        table = soup.find_all('table')[0]
        body = table.find_all('tbody')[0]

        tabla_btg = []
        for f in body.find_all("tr"): #lista con las filas de la  tabla
            fila = [e for e in f.find_all("td")] # elementos dentro de la fila
            if len(fila) > 0 :
                crypto = {
                    "date": fila[0].text.strip(),
                    "open": (fila[1].text),
                    "max_v": (fila[2].text),
                    "min_v": (fila[3].text),
                    "close": (fila[4].text),
                    "volume": (fila[6].text)

                }
                tabla_btg.append(crypto)

        tabla_btg = pd.DataFrame(tabla_btg)
        tabla_btg.head()

        for value in range(0, len(tabla_btg)):
            tabla_btg['crypto'] = 'bitcoin_gold'

        crypto_table = pd.concat([tabla_btc, tabla_eth, tabla_bch, tabla_ksm, tabla_bnb, tabla_ltc, tabla_btg])

        crypto_table.to_csv('data/crypto_table.csv', index=False)

        crypto_table = pd.read_csv("data/crypto_table.csv",encoding = "ISO-8859-1", dtype=str)
        crypto_table.columns = crypto_table.columns.str.rstrip() #Eliminamos si hubiera espacio al final de cada titulo de columna

        crypto_table["date"] = [str(fecha.replace('ene.', '-01-')) for fecha in crypto_table["date"]] 
        crypto_table["date"] = [str(fecha.replace('feb.', '-02-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('mar.', '-03-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('abr.', '-04-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('may.', '-05-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('jun.', '-06-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('jul.', '-07-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('ago.', '-08-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('sept.', '-09-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('oct.', '-10-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('nov.', '-11-')) for fecha in crypto_table["date"]]
        crypto_table["date"] = [str(fecha.replace('dic.', '-12-')) for fecha in crypto_table["date"]]


        def date_convert(date_to_convert):
            return datetime.datetime.strptime(date_to_convert, '%d -%m- %Y').strftime('%Y-%m-%d')

        crypto_table.date = crypto_table.date.apply(date_convert)

        crypto_table.to_csv('data/crypto_table_2.csv', index=False)
        
        print('Crypto_table created')
        
        return crypto_table 
    
    def data_tweets():
        '''With this function we read the dataset that we have previously downloaded and we start making some cleaning in order to join it 
        with our yahoo finance table.
        '''
        tweets = pd.read_csv("data/2021.csv",encoding = "ISO-8859-1", dtype=str)
        tweets.columns = tweets.columns.str.rstrip() #Eliminamos si hubiera espacio al final de cada titulo de columna

        tweets = tweets[['date' , 'tweet']]

        patron_date = r"([0-9]{4}-[0-9]{2}-[0-9]{2})"

        def coincidencia(patron, string):
            """
            Search regex pattern and return it in lowercase .
            patron:
                regex pattern
            Returns:
                pattern group lowercase
            """
            dni = re.search(patron, string)
            if dni is None:
                return 0
            return dni.group().lower()

        tweets['date'] = tweets.date.apply(lambda x: coincidencia(patron_date, x))

        def date_convert(date_to_convert):
             return datetime.datetime.strptime(date_to_convert, '%Y-%m-%d').strftime('%Y-%m-%d')

        tweets.date = tweets.date.apply(date_convert)

        tweets.date = pd.to_datetime(tweets.date)

        new_time = tweets.loc[:, "date"] >= '31-12-2020'
        tweets = tweets.loc[new_time]

        tweets = tweets.loc[tweets.loc[:, "date"] >= '31-12-2020']

        patron_key = r"(\bbitcoin\b|\bcrypto\b|\bcryptocurrency\b|coin)"

        tweets['key_tweets'] = tweets.tweet.apply(lambda x: coincidencia(patron_key, x))  

        def date_convert(date_to_convert):
             return datetime.datetime.strptime(str(date_to_convert), '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

        tweets.date = tweets.date.apply(date_convert)

        tweets.to_csv('data/tweets_table.csv', index=False)
        
        print('Data_tweets created')
        return tweets
    
    def final_database():
        '''With this function we join both dataset to create a final one with all the information that we need
        '''
        crypto_table = pd.read_csv("data/crypto_table_2.csv",encoding = "ISO-8859-1", dtype=str)
        tweets_table = pd.read_csv("data/tweets_table.csv",encoding = "ISO-8859-1", dtype=str)

        final_table = crypto_table.set_index('date').join(tweets_table.set_index('date'))

        final_table.to_csv('data/final_table.csv', index='date')

        return final_table
    
    crypto_scrapping()
    
    data_tweets()
    
    final_database()
    
    return print('Final_database created')


create_final_table()
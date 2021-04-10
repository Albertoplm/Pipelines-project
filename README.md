# Pipelines-project

![portada](https://github.com/Albertoplm/Pipelines-project/blob/main/images/portada.jpg)

## Is Elon Musk that influential? 

In this project I have join two databases one from yahoo finance with cryptocurrency information and othe one with the tweets of Elon Musk, **the aim of this project it´s to check if the increased on the price of cryptocurrencies are related with the tweets of Elon Musk, and of course to now more about the evolution on this market in the last months.**

As I was saying I create a database with the information of yahoo finance about cryptocurrencies, to get this information I used the method of web scrapping, so I was abled to create a full table compiling this information. On the other hand I download a database with the tweets historical data of Elon Musk here you can find the url: (https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021)

To elaborate and clean the databases I have used some really usefull libraries:
- requests: https://docs.python-requests.org/es/latest/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pandas: https://pandas.pydata.org/
- Datetime: https://www.php.net/manual/es/class.datetime.php
- Re: https://docs.python.org/3/library/re.html

Note: In the repo you will find two different Jupiters, one with the elaborating process of the database and the other one with the Visualization process. Also you can find the data (.csv) and the images.

The final version of the database is composed of (with a total sample of xxxx cases):

   - DATE: (x)
   - OPEN: (x)
   - MAX_V: (x)
   - MIN_V: (x)
   - CLOSE: (x)
   - VOLUME: (x)
   - CRYPTO: (x)
   - TWEET: (x)
   - KEY_TWEET: (x)
# Pipelines-project

![portada](https://github.com/Albertoplm/Pipelines-project/blob/main/images/portada.jpg)

## Is Elon Musk that influential? 

**The aim of this project is to check if the rise in the price of cryptocurrencies is related to Elon Musk's tweets and, of course, to learn more about the evolution of this market in recent months.** In order to achieve the goal of this project I have joined two databases one from yahoo finance with cryptocurrency information and othe one with the tweets of Elon Musk.

As I was saying I create a database with the information of yahoo finance about cryptocurrencies, to get this information I used the method of web scrapping, so I was abled to create a full table compiling this information. On the other hand I downloaded a database with the historical data of Elon Musk's tweets, you can find it [here](https://www.kaggle.com/ayhmrba/elon-musk-tweets-2010-2021)

To elaborate and clean the databases I have used some really usefull libraries:
- [Requests](https://docs.python-requests.org/es/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas](https://pandas.pydata.org/)
- [Datetime](https://www.php.net/manual/es/class.datetime.php)
- [Re](https://docs.python.org/3/library/re.html)

Note: In the repo you will find Creating_final_table.py that creates the final table (the one with the yahoo finance and the tweets information), five different Jupiters, Cleaning_tweets_final.ipynb(cleans the tweets dataset), Join_tables.ipynb(Join both tables, Tweets and Yahoo Finance), WebScrapping.ipynb(creates a database based on Yahoo Finance), Visualization.ipynb(Creates all the graphs for better understanding) . Also you can find the data (.csv) and the images.

The final version of the database is composed of:

   - DATE:
   - OPEN:
   - MAX_V: 
   - MIN_V:
   - CLOSE: 
   - VOLUME: 
   - CRYPTO: 
   - TWEET: 
   - KEY_TWEET: 
   
   
### Market evolution

![Crypto_all](https://github.com/Albertoplm/Pipelines-project/blob/main/images/Crypto_all.svg)
We can notice that the cryptocurrency market is super volatile.

### Market VS Elon Musk (02-03)

![Crypto_all_02-03](https://github.com/Albertoplm/Pipelines-project/blob/main/images/Crypto_all_02-03.svg)
Here we appreciate the relations that has a tweet of Elon Musk related to cryptocurrencies with the market price
### Market VS Elon Musk (03-04)

![Crypto_all_03-04](https://github.com/Albertoplm/Pipelines-project/blob/main/images/Crypto_all_03-04.svg)
Here we appreciate the relations that has a tweet of Elon Musk related to cryptocurrencies with the market price
# sQuare
A Forum-based web app with credis and Blockchain systems. \
Developed with python 3.9 and Django 3.2

# Description
This is a demo project, developed following the blockahin dev course from Start2Impact platform (https://www.start2impact.it/percorsi/blockchain/) with the intent of mixing different aspects of front-end and back-end web developing, 
such as Django framework, databases, blockchain interacion, APIs, user interfaces and html templates.\
\
The website is now LIVE ! \
Check it out at: https://bd74-151-81-108-41.ngrok.io
 \
Below a list of the features of sQuare !


## Main Board
Users can freely post on the main board, called sQuare.\
Post can be Public or Private: public posts can be seen by all others registered users,
while Secret posts can be see only by the users who have the "Listening" feature active (see below)

A content-filter is activated, at the moment, every posts containing forbidden words , in either the title or the post's body" will be rejectet and not posted.\
Forbidden words:
```buildoutcfg
    Hack
```
## Ethereum backed
Every post is saved on the ropsten Ethereum testnet by the wallet address:
```buildoutcfg
    0x26B9301b177C7C055EebE2aD8Db06C0ED3743310 
```
https://ropsten.etherscan.io/address/0x26B9301b177C7C055EebE2aD8Db06C0ED3743310

And can be explored at  https://ropsten.etherscan.io + /tx/"tx_id"\
a direct link to the user's post is provided at the users's personal page.

## In-app Credits Systems:
Users can use credits to interact with the website, in particular, Credits can be spent to unlock special features or can be used in the betting system.\
Upon registration, 10 credits are sent to every new user

## Listening Feature
Users can spend Credits to unlock the ability to see Secret posts, otherwise invisibile.\
10 credits = 10 minutes of Listening\
Listening minutes can be cumulated if the user desires to spend more credits

## Betting system :
Through to the CoinJeck API ( https://www.coingecko.com/en/api), users can bet Credits on the variation of the price of Bitcoin and Ethereum's crypto currencies.\
The price is updated from the API every 10 minutes, and users can bet in favour of the price rising or dropping from the previous update.\
When the prices update, winning bets will double the Credits of the bid, while loosing corresponds to the lost of the bid amount

## Data explorer
The section called "Explorer" , in the navbar, serves a JSON representation of some contents of the website\
All the users can view the content posted within the last hour,
while admins can acces all the existing posts, as well as all the Users Info 

## !! NOTE AL CORRETTORE !!
```buildoutcfg
    Ciao !
    Nell'archivio caricato alla consegna del progetto, c'è un file: "note al correttore.txt"
    con altre info personali sulla realizzazione e credenziali per un admin user del sito hostato con ngrok

    Corretto il tutto, questo messaggio si autodistruggerà :)
    Grazie !
```

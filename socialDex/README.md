# sQuare
A Forum-based web app with credis and Blockchain systems, developed with python 3.9 and Django 3.2

# Features
This project includes features related to the Blockchain eviroment, suche as:

## Main Board Bard
Users can freely post on the main board, called sQuare.
Post can be Public or Private: public posts can be seen by all others registered users,
while Secret posts can be see only by the users who have the "Listening" feature active (see below)

Every post is saved on the ropsten Ethereum testnet and can be seen at  https://ropsten.etherscan.io + /tx/"tx_id" ( a direct link is provided at the users's personal page)

A content-filter is activated, at the moment, every posts containing forbidden words , in either the title or the post's body" will be rejectet and not posted.
Forbidden words:
    "Hack"

## In-app Credits Systems:
Users can use credits to interact with the website, in particular, Credits can be spent to unlock special features or can be used in the betting system.
Upon registration, 10 credits are sent to every new user

## Listening Feature
Users can spend Credits to unlock the ability to see Secret posts, otherwise invisibile.
10 credits = 10 minutes of Listening
Listening minutes can be cumulated if the user desires to spend more credits

## Betting system :
Throught to the CoinJeck API ( https://www.coingecko.com/en/api), users can bet Credits on the variation of the price of Bitcoin and Ethereum's crypto currencies.
The price is updated from the API every 10 minutes, and users can bet in favour of the price rising or dropping from the previous update.
When the prices update, winning bets will double the Credits of the bid, while loosing corresponds to the lost of the bid amount

## Data explorer
The section called "JSON" serves a JSON representation of some contents of the website
All the users can view the content posted within the last hour,
while admins can acces all the existing posts, as well as all the Users Info 

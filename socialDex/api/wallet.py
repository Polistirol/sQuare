from web3 import Web3


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/945570ed18a2491c8774c2a463f65aca"))
    address = "0x26B9301b177C7C055EebE2aD8Db06C0ED3743310"
    privateKey  = "0x4deadbee7ecd831598c9e6bc5c0b892ae6d9da23fbaac6a3922c512591dd180b"
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0,"ether")
    signedTx= w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice = gasPrice,
        gas = 100000,
        to = "0x0000000000000000000000000000000000000000",
        value = value,
        data=message.encode("utf-8")
        ),privateKey)
    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    return txId

#The following class is a test wallet class, it's not used in this project atm
'''
class SiteWallet:
    def __init__(self):
        self.w3 = ""
        self.account = ""
        self.privateKey = ""
        self.address = ""
        self.transactions = []
    
    def restoreS2I(self):
        self.w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/945570ed18a2491c8774c2a463f65aca"))
        self.address = "0x26B9301b177C7C055EebE2aD8Db06C0ED3743310"
        self.privateKey  = "0x4deadbee7ecd831598c9e6bc5c0b892ae6d9da23fbaac6a3922c512591dd180b"
        #self.account = self.w3.eth.accounts.privateKeyToAccount(self.privateKey)
        print("Course account has been restored: \nAddress: %s \nPrivate Key: %s \n" %(self.address , self.privateKey))

    def restore(self,url,address,privatekey):
        self.w3 = url
        self.address = address
        self.privateKey  =  privatekey
        self.account = web3.eth.accounts.privateKeyToAccount(self.privateKey)
        print("Account has been restored: \nAddress: %s \nPrivate Key: %s \n" %(self.address , self.privateKey))


    def createNew(self):
        self.account = w3.eth.account.create()
        self.privateKey = account.privateKey.hex()
        self.address = account.address
        print("New account has been created: \nAddress: %s \nPrivate Key: %s \n" %(self.address , self.privateKey))


    def sendTransaction(self,message):
        w3 = self.w3
        nonce = w3.eth.getTransactionCount(self.address)
        gasPrice = w3.eth.gasPrice
        value = w3.toWei(0,"ether")
        signedTx= w3.eth.account.signTransaction(dict(
            nonce=nonce,
            gasPrice = gasPrice,
            gas = 100000,
            to = "0x0000000000000000000000000000000000000000",
            value = value,
            data=message.encode("utf-8")
            ),self.privateKey)
        tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        txId = w3.toHex(tx)
        #tx_dict= w3.eth.get_transaction(txId)
        #self.addToTxPool(tx_dict)
        return txId
    
    def addToTxPool(self, tx):
        newTransaction = {
            "Id" : len(self.transactions) + 1,
            "Sender": self.address,
            "Receiver" : tx["to"],
            "Hash" : tx["hash"],
            "Content" : SiteWallet.decode_eth(tx["input"]) 
        }
        self.transactions.append(newTransaction)
    
    @staticmethod
    def decode_eth(encodedText):
        encodedText = encodedText[2:] # remove the 0x at the beginning
        byteStep = bytes.fromhex(encodedText)
        message = byteStep.decode("ASCII") 
        return message
'''







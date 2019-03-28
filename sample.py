from web3 import Web3, HTTPProvider

# chainAddress = input("Blockchain URL:")
# web = Web3(HTTPProvider(chainAddress))
web = Web3(HTTPProvider('http://localhost:7545'))
print("Connected to the blockchain at port 7545")
print("Current HashRate: " + str(web.eth.hashrate))
print("Current Block: " + str(web.eth.blockNumber))
print("Current coinbase address: " + str(web.eth.coinbase))

myAddress = "0xB635170DE4C29B2a048Ef789F50Ccd8bbC030036A5"
myPrivKey = "26e6b1e0541f269731d9ca87b18feaf1f01c1d4b9a02c9a50d6574fabd9e6c2b"


while True:
    x = input("Menu:\n 1.Set Address \n 2.Set PrivateKey\n 3.Fetch Balance for Address\n 4.Get HashRate\n 5.Get Accounts\n 6.Get Balance for all accounts \n 7.Send Transaction (NOTE : Only use when Address and Private Key are Set)\n 8.Create Account with passphrase \n:")
    if x == "exit":
        break

    elif x == "1":
        myAddress = input(":")
        continue

    elif x == "2":
        myPrivKey = input(":")
        continue

    elif x == "3":
        balAddress = input("Enter Address to check balance: ")
        print(str(web.eth.getBalance(balAddress)) + " Wei")
        continue

    elif x == "4":
        print("\nCurrent HashRate: " + str(web.eth.hashrate) + "\n")
        continue

    elif x == "5":
        print("Accounts on Chain: \n")
        for i in web.eth.accounts:
            print(i)

        continue

    elif x == "7":
        myAddress = input("\nEnter your address: ")
        myPrivKey = input("Enter your private Key")
        sendAddress = input("Enter the Receiver's Address :")
        amount = input("Enter Amount :")
        signed_txn = web.eth.account.signTransaction(dict(
            nonce=web.eth.getTransactionCount(myAddress),
            gasPrice=web.eth.gasPrice,
            gas=100000,
            to=sendAddress,
            value=web.toWei(amount, 'ether')
        ),
            myPrivKey)

        web.eth.sendRawTransaction(signed_txn.rawTransaction)
        continue

    elif x == "6":
        print("\n")
        for i in web.eth.accounts:
            bal = web.fromWei(web.eth.getBalance(i), 'ether')
            print(i + "  Balance: " + str(bal))

        print("\n")
        continue

    elif x == "8":
        phrase = input("Enter passphrase: ")
        newAddress = web.personal.newAccount(phrase)
        print("New Account Created\n Address of new Account: " + str(newAddress) + "\nBalance:" + str(web.eth.getBalance(newAddress)))

        continue

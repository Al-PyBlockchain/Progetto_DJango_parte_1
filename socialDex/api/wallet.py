from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/67aa10cf484b4363a011977efca05310'))
account = w3.eth.account.create()
private_key = account.privateKey.hex()
address = account.address

print(f'Your address: {address}\nYour key: {private_key}')
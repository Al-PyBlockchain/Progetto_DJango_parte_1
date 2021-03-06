from web3 import Web3

def send_transaction(message):
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/67aa10cf484b4363a011977efca05310'))   # <- faucet ethereum
    # address e private_key generati mandando in esecuzione api/wallet.py
    address = '0xE0c1Af6D3C5223b37CC815A680D32084E6A77F49'
    private_key = '0x610203383852af25ee7373c518f881bdf3c77a2b3493750c935be73a6883ec25'
    nonce = w3.eth.getTransactionCount(address)
    gas_price = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signed_tx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gas_price=gas_price,
        gas=1000000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), private_key)

    tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_id = w3.toHex(tx)
    return tx_id

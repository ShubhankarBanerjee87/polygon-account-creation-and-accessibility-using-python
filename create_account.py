"""
Create  mnemonic and private key and address

pip install mnemonic
pip install eth-account
pip install web3

"""
from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3

Account.enable_unaudited_hdwallet_features()
# Generate a new mnemonic passphrase
mnemonic = Mnemonic("english").generate()

# Derive private key from mnemonic
private_key = Account.from_mnemonic(mnemonic)._private_key.hex()

# Derive address from private key
address = Account.from_key(private_key).address

print("Mnemonic:", mnemonic)
print("Private Key:", private_key)
print("Address:", address)


"""
In this code we are checking address and private key with the help of mnemonic_Phrase.
Note: Address and Private key is already generated.

pip install eth-account


"""

from eth_account import Account

mnemonic = "tiger, pot, cold, shutter, cone, shine, happy, lion, drive, eternal, dizzy, mouse "  # Replace with your actual mnemonic phrase

#The use of the Mnemonic features of Account is disabled by default until its API stabilizes. To use these features, please enable them by running `Account.enable_unaudited_hdwallet_features()` and try again.

# Enable it to use

Account.enable_unaudited_hdwallet_features()
# Derive a private key and Ethereum address from the mnemonic
account = Account.from_mnemonic(mnemonic)

privkey = account._private_key.hex()

address = account.address

print("Private key:", privkey)
print("Address:", address)

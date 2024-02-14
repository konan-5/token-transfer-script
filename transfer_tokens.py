from web3 import Web3, HTTPProvider
import json
from dotenv import load_dotenv
import os

load_dotenv()

# Load environment variables
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Private key for the sender's Ethereum address
RPC_URL = os.getenv('RPC_URL')  # URL of the Ethereum RPC provider
AMOUNT = os.getenv('AMOUNT')  # Amount of tokens to transfer
TOKEN_CONTRACT_ADDRESS = os.getenv('TOKEN_CONTRACT_ADDRESS')  # Address of the ERC20 token contract
ERC20_ABI_PATH = 'abi/ERC20.json'  # Path to the ERC20 token ABI file

# Connect to the Ethereum network
w3 = Web3(HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("Failed to connect to the Ethereum network")
    exit()

# Load ERC20 token contract
with open(ERC20_ABI_PATH, 'r') as file:
    token_abi = json.load(file)
token_contract = w3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=token_abi)
decimals = token_contract.functions.decimals().call()

# Get the sender's address from private key
from_address = w3.eth.account.from_key(PRIVATE_KEY).address

# Read addresses from file
with open('addresses.txt', 'r') as file:
    addresses = file.read().splitlines()

amount = int(float(AMOUNT) ** decimals)

# Transfer tokens to each address
for address in addresses:
    nonce = w3.eth.get_transaction_count(from_address)

    # Build the transaction
    tx = token_contract.functions.transfer(address, amount).build_transaction({
        'chainId': w3.eth.chain_id,
        'gas': 2000000,
        'gasPrice': w3.to_wei('50', 'gwei'),
        'nonce': nonce,
    })

    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Sent {AMOUNT} tokens to {address}. Transaction hash: {tx_hash.hex()}")

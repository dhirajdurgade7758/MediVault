from web3 import Web3
from django.conf import settings
import json

# Connect to Ethereum node (Ganache/Testnet/Mainnet)
web3 = Web3(Web3.HTTPProvider(settings.BLOCKCHAIN_PROVIDER))

# Load contract details correctly
with open(settings.SMART_CONTRACT_ABI, "r") as file:
    abi_data = json.load(file)

# Extract ABI correctly
if "contracts" in abi_data:
    abi = abi_data["contracts"]["PatientRecords.sol"]["PatientRecords"]["abi"]
else:
    abi = abi_data  # If it's already a list

# Initialize contract
contract = web3.eth.contract(address=settings.SMART_CONTRACT_ADDRESS, abi=abi)

def store_record_on_blockchain(patient_name, diagnosis, treatment, ipfs_hash):
    """Stores a medical record on blockchain and returns transaction hash"""
    sender = settings.BLOCKCHAIN_ACCOUNT
    
    # Build transaction
    txn = contract.functions.storeRecord(patient_name, diagnosis, treatment, ipfs_hash).build_transaction({
        'from': sender,
        'nonce': web3.eth.get_transaction_count(sender),
        'gas': 500000,
        'gasPrice': web3.to_wei('5', 'gwei')
    })

    # Sign transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=settings.BLOCKCHAIN_PRIVATE_KEY)

    # Send transaction
    txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Wait for receipt
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    
    return txn_receipt.transactionHash.hex()

def get_record_from_blockchain(record_id):
    """Fetches a record from blockchain by ID"""
    return contract.functions.getRecord(record_id).call()

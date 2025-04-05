from web3 import Web3
import json

# Connect to Ganache (or use Infura for testnet/mainnet)
ganache_url = "http://127.0.0.1:7545"  # Change to Infura/Testnet if needed
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load compiled contract
with open("PatientRecords.json", "r") as file:
    contract_data = json.load(file)

try:
    abi = contract_data["contracts"]["PatientRecords.sol"]["PatientRecords"]["abi"]
    bytecode = contract_data["contracts"]["PatientRecords.sol"]["PatientRecords"]["evm"]["bytecode"]["object"]
except KeyError:
    raise KeyError("❌ ABI or Bytecode not found. Check the compiled JSON structure.")

# Deploy contract
account = web3.eth.accounts[0]
contract = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = contract.constructor().transact({"from": account})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"Contract deployed at {contract_address}")

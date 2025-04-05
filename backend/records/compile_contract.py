import json
import os
from solcx import compile_standard, install_solc
from web3 import Web3

# Solidity version (Change if needed)
SOLIDITY_VERSION = "0.8.0"

# Install Solidity compiler version
install_solc(SOLIDITY_VERSION)

# Define contract file path
CONTRACT_FILE = "PatientRecords.sol"
COMPILED_JSON_FILE = "PatientRecords.json"
ABI_FILE = "PatientRecords_abi.json"

# Read the Solidity contract
file_path = os.path.join(os.path.dirname(__file__), CONTRACT_FILE)

try:
    with open(file_path, "r") as file:
        contract_source_code = file.read()
except FileNotFoundError:
    raise FileNotFoundError(f"❌ Contract file '{CONTRACT_FILE}' not found. Ensure it's in the same directory.")

# Compile the contract
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {CONTRACT_FILE: {"content": contract_source_code}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"],
                }
            }
        },
    },
    solc_version=SOLIDITY_VERSION,
)

# Save the compiled contract data
with open(COMPILED_JSON_FILE, "w") as file:
    json.dump(compiled_sol, file, indent=4)

# Extract the contract name dynamically
try:
    contract_data = compiled_sol["contracts"][CONTRACT_FILE]
    contract_name = list(contract_data.keys())[0]  # Get the first contract name dynamically
    abi = contract_data[contract_name]["abi"]
    bytecode = contract_data[contract_name]["evm"]["bytecode"]["object"]
except KeyError:
    raise KeyError("❌ Compilation failed or contract structure is incorrect. Check Solidity syntax.")

# Save ABI separately
with open(ABI_FILE, "w") as abi_file:
    json.dump(abi, abi_file, indent=4)

print(f"✅ Smart contract '{contract_name}' compiled successfully!")
print(f"📄 ABI saved to '{ABI_FILE}'")
print(f"📄 Compiled data saved to '{COMPILED_JSON_FILE}'")

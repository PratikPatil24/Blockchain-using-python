import web3
import json

# Web3 Instance
w3 = web3.Web3(web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
print(w3)

# Wallet
acc1 = "0x4176dE8743a6B7a2636B9b8244E2CC70ab5FB34C"
acc2 = "0xDaFA8475C7CF6362de7bac726E714124be5C5eFd"

# Hospital Record Contract Address
hospitalRecordContractAddress = "0x0CfFCf7cbE4D57C18F2114D9436703d89AEe8637"

# Contract

with open("./HospitalRecord.json", "r") as file:
    hospitalRecordFile = file.read()

parsedHospitalRecordFile = json.loads(hospitalRecordFile)


hospitalRecordContract = w3.eth.contract(
    hospitalRecordContractAddress, abi=parsedHospitalRecordFile["abi"])
print(hospitalRecordContract)

# Read Users
userPratik = hospitalRecordContract.functions.users(acc1).call()
print(userPratik)

# Add User
txn = hospitalRecordContract.functions.addUser("pratik2").build_transaction({
    "maxFeePerGas": 3000000000,
    "maxPriorityFeePerGas": 2000000000,
    "gas": 100000,
    "nonce": w3.eth.get_transaction_count(acc2),
})

signed_txn = w3.eth.account.sign_transaction(
    txn, private_key='c521c7f8d016b35327c6623c95469271a3b1a06c197dd9942ed6f5586680a075')

txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

print("---------------")
userPratik2 = hospitalRecordContract.functions.users(acc2).call()
print(userPratik2)

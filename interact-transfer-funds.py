import web3

# Polygon -> Docs and search RPC URL
# Ethereum -> Infura Service will provide RPC

# Web3 Instance
w3 = web3.Web3(web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
print(w3)

acc1 = "0x4176dE8743a6B7a2636B9b8244E2CC70ab5FB34C"
acc2 = "0xDaFA8475C7CF6362de7bac726E714124be5C5eFd"

# MATIC Balance
print(w3.eth.get_balance(acc1))
print(w3.eth.get_balance(acc2))

txn = {
    "from": acc1,
    "to": acc2,
    "value": 200,
    "maxFeePerGas":3000000000,
    "maxPriorityFeePerGas":2000000000,
    "gas":100000,
    "nonce": w3.eth.get_transaction_count(acc1),
    "chainId": 80001
}

signed_tx = w3.eth.account.sign_transaction(txn, private_key = 'b710a8debaca1ff880d9d434c8af6288f3c9113a7ef6525d20391bafcbd9da7e')

# print(signed_tx)

txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
# print(txn_receipt)

# MATIC Balance
print(w3.eth.get_balance(acc1))
print(w3.eth.get_balance(acc2))

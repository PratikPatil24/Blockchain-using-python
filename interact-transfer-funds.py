import web3

# Web3 Instance
w3 = web3.Web3(web3.HTTPProvider('https://rpc-mumbai.maticvigil.com/'))
print(w3.client_version)

# Wallet
acc1 = "0x4176dE8743a6B7a2636B9b8244E2CC70ab5FB34C"
acc2 = "0xDaFA8475C7CF6362de7bac726E714124be5C5eFd"
print(w3.eth.get_balance(acc1))
print(w3.eth.get_balance(acc2))

value = w3.to_wei(0.0001, "ether")
txn = {
  "from": acc1,
  "to": acc2,
  "value": 100,
  "maxFeePerGas":3000000000,
  "maxPriorityFeePerGas":2000000000,
  "gas":100000,
  "nonce": w3.eth.get_transaction_count(acc1),
  "chainId": 80001
}

signed_tx = w3.eth.account.sign_transaction(txn, private_key='b710a8debaca1ff880d9d434c8af6288f3c9113a7ef6525d20391bafcbd9da7e')


txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
w3.eth.wait_for_transaction_receipt(txn_hash)
print(w3.eth.get_balance(acc1))
print(w3.eth.get_balance(acc2))

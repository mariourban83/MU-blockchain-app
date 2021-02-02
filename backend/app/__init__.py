import os
import random
import requests
from flask import Flask, jsonify, request

from backend.blockchain.blockchain import Blockchain
from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
from backend.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
wallet = Wallet()
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

@app.route("/")
def route_default():
    return 'Welcome to Blockchain'

@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = "test transaction data"
    blockchain.add_block(transaction_data)
    block =blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())

@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    transaction_data = request.get_json()
    transaction = Transaction(
        wallet,
        transaction_data['recipient'],
        transaction_data['amount']
        )

    pubsub.broadcast_transaction(transaction)
    
    return jsonify(transaction.to_json())

# Set Flask ports to run multiple peer app instances 
ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    print(f'\n -- result.json(): {result.json()}')

    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n --- Sucessfully synchronized the local chain ---')
    except Exception as e:
        print(f'\n ---!! -- Error while synchronizing : {e} -- !!---')



app.run(port=PORT)
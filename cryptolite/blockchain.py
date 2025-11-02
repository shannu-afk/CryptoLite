import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # create the genesis block
        self.create_block(previous_hash='0')

    def create_block(self, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash,
            'hash': '',
        }

        block['hash'] = self.hash(block)
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # ✅ add a transaction to the pending list
    def add_transaction(self, sender, receiver, amount):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        }
        self.pending_transactions.append(transaction)
        return self.get_previous_block()['index'] + 1

    def get_previous_block(self):
        return self.chain[-1]

    # ✅ mine a block: confirm all pending transactions
    def mine_block(self):
        previous_block = self.get_previous_block()
        previous_hash = previous_block['hash']
        block = self.create_block(previous_hash)
        return block

    # ✅ calculate total balance for a given wallet address
    def get_balance(self, address):
        balance = 0.0
        for block in self.chain:
            for transaction in block['transactions']:
                if transaction['receiver'] == address:
                    balance += transaction['amount']
                if transaction['sender'] == address:
                    balance -= transaction['amount']
        return round(balance, 4)

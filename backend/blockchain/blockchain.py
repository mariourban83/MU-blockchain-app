
from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.config import MINING_REWARD_INPUT

class Blockchain:
    '''
    Blockchain : public ledger of transactions, implemented as list of blocks
    '''
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block= self.chain[-1]

        self.chain.append(Block.mine_block(last_block, data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        '''
        Replace the local chain with incoming one if :
            - The incomming chain is longer than local one
            - The incomming chain is formatted properly
        '''
        if len(chain) <=len(self.chain):
            raise Exception('Cannot replace, the incomming chain must be longer')

        try:
            Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace, the incomming chain is invalid : {e}')

        self.chain = chain

    def to_json(self):
        '''
        Serialize(simplify complex data) into a list of blocks
        '''
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        '''
        Deserialize a list of serialized blocks into a Blockchain instance.
        The result will contain a chain list of Block instances.
        '''
        blockchain = Blockchain()
        blockchain.chain = list(map(lambda block_json: Block.from_json(block_json), chain_json))

        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        '''
        Validate the incoming chain by enforcing:
        - Chain must begin with genesis block
        - Every block must be formatted correctly
        '''

        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

    @staticmethod
    def is_valid_transaction_chain(chain):
        '''
        Enforce the rules of chain composed of blocks of transactions
            Each transaction must only appear once in the chain
            There can only be one mining reward per mined block
            Each transaction must be valid
            '''
        transaction_ids = set()

        for block in chain():
            has_mining_reward = False

            for transaction_json in block.data:
                transaction = Transaction.from_json(transaction_json)

                if transaction.input == MINING_REWARD_INPUT:
                    if has_mining_reward:
                        raise Exception('There can only be one mining reward per block' \
                            f'Check block with hash : {block.hash}')
                    has_mining_reward = True

                if transaction.id in transaction_ids:
                    raise Exception(f'Transaction {transaction.id} is not unique')

                transaction_ids.add(transaction.id)

                Transaction.is_valid_transaction(transaction)

#  testing only
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)

if __name__ == '__main__':
    main()
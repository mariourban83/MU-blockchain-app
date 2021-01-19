import time
from backend.util.crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': []
}

class Block:
    '''
    Block: a unit of storage that stores transactions in a blockchain.
    '''
    def __init__(self, timestamp, last_hash, hash, data,):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash},'
            f'data: {self.data})'
        )

    @staticmethod
    def mine_block(last_block, data):
        '''
        Mines a block based on the last block and data
        '''

        timestamp = time.time()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        '''
        Genereate very first block of the chain
        '''
        return Block(**GENESIS_DATA)


# testing only
def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'testString')
    print(block)

if __name__ == '__main__':
    main()
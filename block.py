import time


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
        hash = f'{timestamp}-{last_hash}'

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        '''
        Genereate very first block of the chain
        '''
        return Block(1, 'genesis_last_hash', 'genesis_hash', [])



# testing only
def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'testString')
    print(block)

if __name__ == '__main__':
    main()
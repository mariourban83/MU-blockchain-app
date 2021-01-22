
from backend.blockchain.block import Block

class Blockchain:
    '''
    Blockchain : public ledger of transactions, implemented as list of blocks
    '''
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        last_block= self.chain[-1]

        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    @staticmethod
    def is_valid_chain(chain):
        '''
        Validate the incoming chain by enforcing:
        - Chain must beggin with genesis block
        - Every block must be formatted correctly
        '''

        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)


#  testing only
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)

if __name__ == '__main__':
    main()
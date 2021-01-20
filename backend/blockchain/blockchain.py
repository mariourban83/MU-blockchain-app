
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

#  testing only
def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    blockchain.add_block('three')
    blockchain.add_block('four')
    # blockchain.add_block('five')
    # blockchain.add_block('six')

    print(blockchain)

if __name__ == '__main__':
    main()
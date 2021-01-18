class Block:
    '''
    Block: a unit of storage that stores transactions in a blockchain.
    '''
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block-data: {self.data}'

# testing only
def main():
    block = Block('testBlock')
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == '__main__':
    main()
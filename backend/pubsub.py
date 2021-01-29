import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-405984c8-5dd8-11eb-9654-ced561075670"
pnconfig.publish_key = "pub-c-239c24fb-f759-4694-876a-e9becb21396b"

CHANNELS = {
    'TEST' : 'TEST',
    'BLOCK' : 'BLOCK'
}

class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain


    def message(self, pubnub, message_object):
        print(f'\n Channel: {message_object.channel} | Message : {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)
            
            try:
                self.blockchain.replace_chain(potential_chain)
                print(f'\n -- Sucessfully replaced local chain')
            except Exception as e:
                print(f'\n -- Did not replace the chain: {e}')

                
        

class PubSub():
    '''
    Handles publish/subscribe layer of the application.
    Provides communication between the nodes of blockchain network
    '''
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        self.pubnub.add_listener(Listener(blockchain))

    def publish(self, channel, message):
        '''
        Publish the message object to the channel
        '''
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        '''
        Broadcast block object to all nodes
        '''
        self.publish(CHANNELS['BLOCK'], block.to_json())

def main():
    pubsub = PubSub()

    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], { 'foo' : 'bar'})

if __name__ == '__main__':
    main()
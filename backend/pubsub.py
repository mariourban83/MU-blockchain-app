import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-405984c8-5dd8-11eb-9654-ced561075670"
pnconfig.publish_key = "pub-c-239c24fb-f759-4694-876a-e9becb21396b"
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incomming message_object : {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({ 'foo' : 'bar'}).sync()

if __name__ == '__main__':
    main()
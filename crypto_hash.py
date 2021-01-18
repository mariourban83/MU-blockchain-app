import hashlib
import json

def crypto_hash(data):
    '''
    Return sha-256 hash of the given data
    '''
    stringified_data = json.dumps(data)
    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

# testing functionality
def main():
    print(f"crypto_hash([1]): {crypto_hash([1])}")

if __name__ == '__main__':
    main()
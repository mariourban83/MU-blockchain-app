from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    # Check if same hash is produced for same data but of different order
    assert crypto_hash(1, [2], 'three') == crypto_hash('three', [2], 1)
    
    # Check if function produce always same hash
    assert crypto_hash('test') == '4d967a30111bf29f0eba01c448b375c1629b2fed01cdfcc3aed91f1b57d5dd5e'
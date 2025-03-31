import pygost.gost28147 as ci

def dump_encrypted(s):
    print(':'.join(hex(ord(x))[2:] for x in str(s)))

KEY = 'NikitaShevchenkoNikitaShevchenko'.encode('utf-8')
PLAINTEXT = 'Padding oracle attacks exploit padding schemes._'.encode('utf-8')

encrypted_text = ci.ecb(KEY, PLAINTEXT, ci.encrypt)

dump_encrypted(encrypted_text)

decrypted_text = ci.ecb(KEY, encrypted_text, ci.decrypt)

print(decrypted_text.decode('utf-8'))

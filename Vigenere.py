import itertools

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            
            shift = ord(key[i % key_length].lower()) - ord('a')
            
            
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

ciphertext = "" #密文
dictionary = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  
max_key_length = 8  # 密钥范围

for key_length in range(1, max_key_length + 1):
    for key in itertools.product(dictionary, repeat=key_length):
        possible_key = "".join(key)
        decrypted_text = vigenere_decrypt(ciphertext, possible_key)
        if "flag{" in decrypted_text:
            print(f"Key: {possible_key}, Decrypted Text: {decrypted_text}")
            break

from typing import List, Tuple, Sequence

abc_caps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z", "", "'", ":", ")", ",", ".", " "]
abc = [letter.lower() for letter in abc_caps]


def chartonum(text: str) -> List[int]:
    '''Map every char in a string with an integer mod len(abc_caps)
    '''
    abc_in_nums = []
    text = text.lower()
    for char in text:
        for i in range(len(abc)):
            if char == abc[i]:
                abc_in_nums.append(i)
    return abc_in_nums


def find_mod_inv(e, p, q):
    '''Find modular inverse
    '''
    m = (p - 1) * (q - 1)
    for x in range(1, m):
        if ((e % m) * (x % m) % m == 1):
            return x
    print("Couldn't find modular inverse hence this combination is not possible.")
    exit()


def initialise() -> None:
    global p,q,m,e
    # Primes p,q
    p = int(input("p: "))
    q = int(input("q: "))

    # Encryption number
    e = int(input("e: "))

    # Modulo
    m = p*q


def E(x: str) -> List[int]:
    '''Encrypt a string
    '''
    x = chartonum(x)
    cypher_text = []

    for num in x:
        cypher_text.append(pow(num, e) % m)
    return cypher_text


def D(x: List[int]) -> str:
    '''Decrypt
    '''
    d = find_mod_inv(e, p, q)
    output = ''

    for char in x:
        output += abc[pow(char, d) % m]
    return output


def main():
    choice = input('Press "e" to encrypt or "d" to decrypt: ')
    if choice == 'e':
        initialise()
        print(E(input('Insert string to encrypt: ')))
        print(f'Encrypted with primes {p,q} and e = {e}. Save this for later.')
    elif choice == 'd':
        initialise()
        string_decrypt = input('Insert list of encrypted letters into numbers (format: 97 40 54 0): ')
        list_decrypt = [int(x) for x in string_decrypt.split()]
        print(D(list_decrypt))
    else:
        exit()


main()

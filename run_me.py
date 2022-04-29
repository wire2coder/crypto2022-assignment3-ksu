# python 3
import random


# encryption and decryption
def RSA(text1: str, e_d: int, n: int):
    unencrypted_dec_value = []
    output_text = ''
    output_num_list = []

    for one_thing in text1:
        num1 = ord(one_thing)
        unencrypted_dec_value.append(ord(one_thing))  # for debugging

        output = (num1 ** e_d) % n
        output_num_list.append(output)
        one_letter = chr(output)
        output_text += one_letter

    return output_text, output_num_list


# calculate 'phi'
def Phi(p, q):
    phi_num = (p - 1) * (q - 1)
    return phi_num


# get the 'encryption key' for 'public use'
def public(phi_num: int):
    # e -> gcd(e,phi_num)==1      ; 1 < e < phi_num
    e = 2
    while e < phi_num:
        # check if this is the required `e` value
        gcd1 = gcd(e, phi_num)
        if gcd1 == 1:
            return e
        # else : increment and continue
        e += 1


# get 'decryption key' for 'private use'
def private(e: int, phi_num: int):
    # d1 <- e*d1 mod% phi_num = 1        ; 1 < d1 < phi_num
    d1 = 2
    while d1 < phi_num:
        # check if this is the required `d1` value
        current_d_value = ((d1 * e) % phi_num)
        if current_d_value == 1:
            return d1
        # else : increment and continue
        d1 += 1


# calculate the GCD
def gcd(x: int, y: int):
    # GCD by Euclidean method
    small_number, big_number = (x, y) if x < y else (y, x)

    while small_number != 0:
        temp = big_number % small_number
        big_number = small_number
        small_number = temp

    return big_number


# making a 'list' of prime numbers
# and randomly pick 2
def prime(input1=500):
    import time
    start_time = time.time()

    prime_list = []
    start1 = 0

    for i in range(start1, input1):
        if i == 0 or i == 1:
            continue  # 'go' back to the 'for' line
        else:
            asdf1 = int(i / 2) + 1;
            for j in range(2, asdf1):
                if i % j == 0:
                    break  # 'break' out of 'FOR j' loop, go to 'FOR i' loop
            else:
                prime_list.append(i)

    print('*' * 70)
    print("--- %s seconds for making prime numbers ---" % (time.time() - start_time))
    print('*' * 70)

    if len(prime_list) == 0:
        print("There are no prime numbers in this range")
        return -1  # return 'some error'

    p1, p2 = random.sample(prime_list, 2)
    return p1, p2


# main function, program starts HERE
if __name__ == "__main__":
    # p, q = map(int, input().split())
    # e_text_or_d_text = input()

    ## SET INPUTS HERE
    e_text_or_d_text = ['Encryption', 'Digital Signature']
    range1 = 500

    prime_p, prime_q = prime(range1)
    gcd1 = gcd(prime_p, prime_q)  # checking that both numbers are PRIME NUMBER

    if gcd1 == 1:
        n = prime_p * prime_q
        phi_num = Phi(prime_p, prime_q)

        # e -> gcd(e,phi_num)==1      ; 1 < e < phi_num
        # d1 -> e*d1 = 1(mod phi_num)        ; 1 < d1 < phi_num
        e = public(phi_num)
        d1 = private(e, phi_num)

        for asdf in e_text_or_d_text:
            cipher_text, dec_list_cipher = RSA(asdf, e, n)
            plain_text, dec_list_plain = RSA(cipher_text, d1, n)

            print(f"input 'range': {range1}")
            print(f"p value: {prime_p}, q value: {prime_q}")
            print(f"e value: {e}, d value: {d1}")
            print(f"n=(p*q) value: {n}, phi(n): {phi_num}")
            print("")
            print("Encrypted text: ", cipher_text)
            print("Decrypted (Plain text): ", plain_text, "\n")

            print(f'debug wait')

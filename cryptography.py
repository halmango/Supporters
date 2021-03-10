def my_codebook():
    code_book = {'@' : 'a', '+' : 'c', 'z' : 'd', 'W' : 'e', 'K' : 'g', 'P' : 'h', '^' : 'i', 'B' : 'j', '?' : 'l',
                 '(' : 'm', 'U' : 'n', '-' : 'o', '/' : 'p', '>' : 'r', '%' : 's', '*' : 't', '}' : 'u', '[' : 'w', ':' : 'y', 'Q' : '!'} # 암호문:평문 이 멤버인 딕셔너리
    encbook = {} # 딕셔너리 정의(암호화 할 때 쓸 꺼)
    for i in code_book: 
        val = code_book[i] 
        encbook[val] = i # 암호화는 평문을 암호문으로 바꾸는 과정, 평문:암호문 으로 바꿔 넣어줌
    return encbook, code_book

def encrypt(msg, encbook): # 암호화
    for j in msg: # 메세지의 평문 j
        if j in encbook: # j(평문) 가 encbook에 있다면
            msg = msg.replace(j, encbook[j]) # 암호문으로 바꾸기
    return msg

def decrypt(msg, code_book): # 복호화
    for j in msg:
        if j in code_book:
          msg = msg.replace(j, code_book[j])
    return msg

if __name__=='__main__': # 메인 함수
    f = open("original_txtfile.txt", 'rt') # 파일 열기
    plaintext = f.read()
    f.close()

    encbook, code_book = my_codebook() 
    plaintext = encrypt(plaintext, encbook)

    ciphertext = encrypt(plaintext, encbook)
    print(ciphertext)

    deciphertext = decrypt(ciphertext, code_book)
    print(deciphertext)


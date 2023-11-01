def criptografar_mensagem(mensagem):
    palavras = mensagem.split()
    palavras_criptografadas = []

    for palavra in palavras:
        if len(palavra) == 1:
            palavra_criptografada = str(ord(palavra[0]))
        elif len(palavra) >= 2:
            primeiro_caractere = str(ord(palavra[0]))
            palavra_criptografada = primeiro_caractere + palavra[-1] + palavra[2:-1] + palavra[1]

        palavras_criptografadas.append(palavra_criptografada)

    return " ".join(palavras_criptografadas)

def test_criptografar_mensagem():
    assert criptografar_mensagem("Hello") == '72olle'
    assert criptografar_mensagem("good") == '103doo'
    assert criptografar_mensagem("hello world") == '104olle 119drlo'
    assert criptografar_mensagem("A") == '65'

if __name__ == '__main__':
    test_criptografar_mensagem()
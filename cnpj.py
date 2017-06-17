import re


class Cnpj:
    def validador(self, cnpj):

        # defining some variables
        lst_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        lst_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        filtro = re.compile('([0-9]+)')
        cnpj = ''.join(filtro.findall(cnpj))

        # finding out the digits
        verificadores = cnpj[-2:]

        # verifying the lenght of the cnpj
        if len(cnpj) != 14:
            return False

        # calculating the first digit
        soma = 0
        id = 0
        for numero in cnpj:

            # to do not raise indexerrors
            try:
                lst_validacao_um[id]
            except IndexError:
                break

            soma += int(numero) * int(lst_validacao_um[id])
            id += 1

        soma = soma % 11
        if soma < 2:
            digito_um = 0
        else:
            digito_um = 11 - soma

        digito_um = str(digito_um)  # converting to string, for later comparison

        # calculating the second digit
        # suming the two lists
        soma = 0
        id = 0

        # suming the two lists
        for numero in cnpj:

            # to do not raise indexerrors
            try:
                lst_validacao_dois[id]
            except:
                break

            soma += int(numero) * int(lst_validacao_dois[id])
            id += 1

        # defining the digit
        soma = soma % 11
        if soma < 2:
            digito_dois = 0
        else:
            digito_dois = 11 - soma

        digito_dois = str(digito_dois)

        # returnig
        return bool(verificadores == '{}{}'.format(digito_um, digito_dois))

    def formator(self, cnpj=''):

        filtro = re.compile('([0-9]+)')
        cnpj = ''.join(filtro.findall(cnpj))

        return "%s.%s.%s/%s-%s" % (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])


if __name__ == '__main__':
    print(Cnpj().validate('64623626000137'))
    print(Cnpj().validate('41.161.794/0001-52'))
    print(Cnpj().format('64623626000137'))
    print(Cnpj().format('41.161.794/0001-52'))

import re


class ValidaCpf:
    def formatador(self, cpf):

        valido = re.match('\d{11}', str(cpf))

        if not valido:
            return False
        else:
            return "{}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    def validador(self, cpf):

        valido = re.match('\d{11}', str(cpf))

        if not valido:
            return False

        cpf_invalidos = [11 * str(i) for i in range(10)]
        if cpf in cpf_invalidos:
            return False

        lstcpf = [int(x) for x in cpf]

        cpf = lstcpf[:9]

        while len(cpf) < 11:

            r = sum([(len(cpf) + 1 - i) * v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpf.append(f)

        if bool(cpf == lstcpf):
            return True
        else:
            return False

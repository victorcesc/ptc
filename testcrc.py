#!/usr/bin/python3

import crc

teste = bytearray()
teste.append(1)
teste.append(0)
fcs = crc.CRC16(teste)
msg = fcs.gen_crc()
print('Mensagem com FCS:', msg)

fcs.clear()
fcs.update(msg)
print('Resultado da verificação da mensagem com FCS:', fcs.check_crc())

msg=msg[:-1]
fcs.clear()
fcs.update(msg)
print('Resultado da verificação da mensagem com FCS após modificá-la:', fcs.check_crc())


import asn1tools

# com pila a especificação
spec = asn1tools.compile_files('msg2.asn1', codec='der')

# cria uma mensagem na forma de um dicionário !
msg = {'nome': 'blabla...', 'qtdes':[2,4,6,8,10]}

# Codifica a mensagem
data = spec.encode('Algo', msg)

# Mostra a mensagem codificada
print(data)

# Grava a mensagem em um arquivo
open('msg.data','wb').write(data)


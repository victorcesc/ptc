from subcamada import Subcamada

class Enquadramento(Subcamada):
    def __init__(self,porta_serial,t_out):
        Subcamada.__init__(self,porta_serial,t_out)
        # outras deficinicoes

    def envia(self,quadro):
        #envia um quadro
        pass

    def handle(self):
        
        #Ao termino das operacoes para enviar para a camada superior
        self.upper.envia(dados)

    def handle_timeout(self):
        pass
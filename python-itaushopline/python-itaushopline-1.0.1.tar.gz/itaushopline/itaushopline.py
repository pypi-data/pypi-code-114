from unicodedata import normalize
import random
from lxml import html
import requests

class ItauShopline():

    def __init__(self, codigo, chave, **kwargs):
        self.KEYS_MAP={
        'pedido': 8, 
        'valor': 10, 
        'observacao': 40,
        'nome': 30,
        'codigo_inscricao': 2,
        'numero_inscricao': 14, 
        'endereco': 40,
        'bairro': 15,
        'cep': 8,
        'cidade': 15,
        'estado': 2,
        'vencimento': 29,
        'url_retorno': 60,
        'obs_1': 60,
        'obs_2': 60,
        'obs_3': 60
    }
        self.codigo = codigo
        self.chave = chave
        self.chave_itau = 'SEGUNDA12345ITAU'

    def tirar_acento(self,text):
        clean_text = normalize('NFKD',text).encode('ASCII','ignore').decode('ASCII')
        return clean_text

    def clean_date(self,data):
        return data.strftime('%d%m%Y')

    def clean_valor(self,valor):
        return str(valor).replace('.','').rjust(10,'0')

    def clean_pedido(self,pedido):
        return str(pedido).rjust(8,'0')

    def clean_inscri(self, x):
        return str(x).rjust(2,'0')

    def random_char(self):
        char_list = 'abcdefghijklmnopqrstuvwxyz'.upper()
        rnd = random.choice(char_list)
        return rnd


    def operacao(self, token, chave):
        self.idxs = []
        self.asc_codes = []
        self.start(chave)

        l=0

        data_chave = []

        for j in range(1,len(token)+1):
            k = j % 256
            l = (l + self.idxs[k]) % 256
            i = self.idxs[k]
            self.idxs[k]= self.idxs[l]
            self.idxs[l]= i
            char = int(ord(token[j-1:j]) ^ int(self.idxs[(self.idxs[k] + self.idxs[l]) % 256]))
            data_chave.append(chr(char))

        return ''.join(data_chave)

    def start(self,chave):
        for j in range(0,256):
            self.idxs.append('')
            self.asc_codes.append('')
            self.asc_codes[j] = ord(chave[j % len(chave):(j % len(chave))+1])
            self.idxs[j] = j

        l = 0

        for k in range(0,256):
            l = (l + self.idxs[k]+self.asc_codes[k]) % 256

            i = self.idxs[k]
            self.idxs[k] = self.idxs[l]
            self.idxs[l] = i
            
    def converte(self,chave):
        data_random =[str(self.random_char())]

        for j in range(0, len(chave)):
            data_random.append(str(ord(str(chave[j:j+1]))))
            data_random.append(str(self.random_char()))

        return ''.join(data_random)


    def consultar(self):
        url = 'https://shopline.itau.com.br/shopline/consulta.aspx'
        page = requests.post(url, data={'DC':self.dc})
    
        tree = html.fromstring(page.content)
        
        data1 = tree.xpath('//td[@class="txt_cinza_n"]/text()')
        data2 = tree.xpath('//td[@class="txt_lrj"]/b/text()')
        data1 = [x.replace('\n','').replace('\r','').strip(' ') for x in data1]
        data1 = [x.encode('iso-8859-1') for x in data1]
        data1 = [x.decode('utf-8') for x in data1]
        data2 = [x.replace('\n','').replace('\r','').strip(' ') for x in data2]

        context = {}
        for i,j in zip(data2,data1):
            context[i] = j

        return context

    def init(self, **kwargs):
        self.data = kwargs
        try:
            if(len(self.chave) != 16 and len(self.codigo) != 26):
                raise Exception('Valores de Entrada inválidos! (chave/código)')
        except Exception:
            print(Exception)
            exit()

        try:
            for key in kwargs.keys():
                if key not in self.KEYS_MAP.keys():
                    raise Exception('Valores de Entrada inválidos! (informações)')
        except Exception:
            print(Exception)
            exit()

        for key in kwargs.keys():

            if key == 'nome':
                kwargs[key] = self.tirar_acento(kwargs[key])
            if key == 'vencimento':
                kwargs[key] = self.clean_date(kwargs[key])
            if key == 'valor':
                kwargs[key] = self.clean_valor(kwargs[key])
            if key == 'pedido':
                kwargs[key] = self.clean_pedido(kwargs[key])
            if key == 'codigo_inscricao':
                kwargs[key] = self.clean_inscri(kwargs[key])

            if type(kwargs[key]) == type('MrPowerUp'):
                kwargs[key] = kwargs[key][0:self.KEYS_MAP[key]]

        chave1 = self.operacao(''.join([kwargs[key] for key in kwargs.keys()]),self.chave)
        chave2 = self.operacao(''.join([self.codigo, chave1]),self.chave_itau)
        self.dc = self.converte(chave2)

        return self.dc
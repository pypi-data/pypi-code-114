import numpy as np
import matplotlib.pyplot as plt

class termolinguistico:
  def __init__(self,nome,tipo,intervalo):
    self.nome = nome
    self.tipo = tipo
    self.inter = intervalo
  
  def pertinencia(self,x):
    if self.tipo == "triangular": 
      if x > self.inter[0] and x <= self.inter[1]: return (x-self.inter[0])/(self.inter[1]-self.inter[0])
      elif x >= self.inter[1] and x <= self.inter[2]: return (self.inter[2]-x)/(self.inter[2]-self.inter[1])
      else: return 0

    elif self.tipo == "trapezoidal":
      if x > self.inter[0] and x <= self.inter[1]: return (x-self.inter[0])/(self.inter[1]-self.inter[0])
      if x >= self.inter[1] and x <= self.inter[2]: return 1
      elif x >= self.inter[2] and x <= self.inter[3]: return (self.inter[3]-x)/(self.inter[3]-self.inter[2])
      else: return 0
    
    elif self.tipo == "gaussiano":
      if x >= (self.inter[0]-self.inter[1]) and x <= (self.inter[0]+self.inter[1]): return np.exp( -( (x-self.inter[0])**2 )/(self.inter[2]**2) )
      else : return 0

class variavellinguistica:
  
  def __init__(self,nome,universo):
    self.nome = nome
    self.universo = universo
    self.termos = []

  def adicionar(self,nome,tipo,intervalo): 
    tl = termolinguistico(nome,tipo,intervalo)
    self.termos.append(tl)

  def mostrarTermos(self): 
    tnomes = []
    for i in self.termos: tnomes.append( i.nome )
    return tnomes

  def grafico(self):
    for i in self.termos:
      aux = []
      for j in self.universo: aux.append( i.pertinencia(j) )
      plt.plot(self.universo,aux,label = i.nome)
    
    plt.title(self.nome)
    plt.legend()
    plt.show()    

class controlador:
  
  def __init__(self,regras,vetvariaveislinguisticas,valores):
        self.regras = regras
        self.valores = valores
        self.vetvl = vetvariaveislinguisticas
        self.baseregras = []
        self.gerarBaseRegras() 
  
  def gerarBaseRegras(self): 
        for i in self.regras: self.baseregras.append( i.split() )

  def mapeia(self):
        entao = [ i.index("então") for i in self.baseregras]
        
        mapa = []
        aux = []
        k = 0
        for i in self.baseregras: 
            for j in i[0:entao[k]:2]:
                aux.append( self.vetvl[k].mostrarTermos().index(j) )
                k +=1
            mapa.append(aux)
            aux = [] 
            k = 0
        
        aux1 = []
        aux2 = []
        k=0
        for i in mapa:
            for j in i:
                aux1.append(self.vetvl[k].termos[j].pertinencia(self.valores[k]))
                k +=1
            aux2.append(aux1)
            aux1=[]
            k = 0 
        return aux2
        
  def ativarbase(self):
        #mapeamento das regras nos termos
        regrasativadas=[]
        for i in range(len(self.mapeia())):
            if not all(k==0 for k in self.mapeia()[i]):  regrasativadas.append(i)
        return regrasativadas

  def mamdani(self, df = "centroide"):
    tl = 0
    aux = 0
    aux1 = []
    aux2 = []
    for ra in self.ativarbase():
      while aux < len(self.baseregras[ra]) - 2:
        indice = self.vetvl[tl].mostrarTermos().index(self.baseregras[ra][aux])
        aux1.append( self.vetvl[tl].termos[indice].pertinencia(self.valores[tl]) )
        aux += 2
        tl += 1
      aux2.append(min(aux1))
      tl,aux = 0,0
      aux1 = []

    aux1 = []
    aux3  = []
    k = 0
    for ra in self.ativarbase():
      indice = self.vetvl[-1].mostrarTermos().index(self.baseregras[ra][-1])
      for i in self.vetvl[-1].universo: 
        if self.vetvl[-1].termos[indice].pertinencia(i) <= aux2[k] :aux1.append( self.vetvl[-1].termos[indice].pertinencia(i) )
        else: aux1.append( aux2[k] )
      aux3.append(aux1)
      aux1 = []
      k += 1

    aux1 = []
    k,j=0,0
    while k < len(aux3[0]):
      aux = 0
      for j in aux3: aux = max(j[k],aux)
      aux1.append(aux)
      k += 1

    aux3.append(aux1)
      
    if df == "centroide":
      ct = self.vetvl[-1].universo * np.array(aux3[-1])
      return sum(ct)/sum(np.array(aux3[-1]))
    
    if df == "centro dos maximos":
      alturamax = max(aux3[-1])
      i = self.vetvl[-1].universo[ aux3[-1].index(alturamax) ]
      k = aux3[-1].index(alturamax)
      f = i
      while aux3[-1][k] <= aux3[-1][k+1]: 
        f = self.vetvl[-1].universo[ k+1 ]
        k +=1
      return (i+f)/2

    if df == "media dos maximos":
      alturamax = max(aux3[-1])
      i = self.vetvl[-1].universo[ aux3[-1].index(alturamax) ]
      k = aux3[-1].index(alturamax)
      n = 0
      f = i
      while aux3[-1][k] <= aux3[-1][k+1]: 
        f += self.vetvl[-1].universo[ k+1 ]
        k +=1
        n +=1
      return f/n
  
  def tsk(self,vet):
    m = [min(i) for i in self.mapeia()] 
    denominador = sum(m)
    n = []
    for i in range(len(self.regras)): n.append(vet[i](self.valores) * m[i]) 
    numerador = sum(n)
    return numerador/denominador 
   
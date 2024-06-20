from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome , categoria):
        self._nome = nome.title() #Apenas a Primeira letra é maiscula
        self._categoria = categoria.upper() #Todas letras ficaram maisculas
        self._avaliacao = []
        self._cardapio =[]
        self._ativo = False
        Restaurante.restaurantes.append(self)     
        
    def __str__(self) -> str:
        return f'{self._nome} - {self._categoria} - {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)}   {"Categoria".ljust(25)} {"Avaliação".ljust(25)} {"Status"} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(26)}   {restaurante._categoria.ljust(26)}   {str(restaurante.media_avaliacao).ljust(19)}   {restaurante.ativo}')
                    
       
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property  
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_avaliacao = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_avaliacao/quantidade_notas, 1)
        return media
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    
    @property
    def exibir_cardapio(self):
        print(f' Nome do Restaurante - {self._nome}')
        print('''
              *** CARDAPIO ***
              ''')
        
        for  i,item in enumerate(self._cardapio, start =1):
            
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} / Preço: {item._preco} / Descrição : {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} / Preço: {item._preco} / Tamanho : {item.tamanho}'
                print(mensagem_bebida)
        
    
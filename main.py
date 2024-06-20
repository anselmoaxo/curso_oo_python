from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

  
pizzaria = Restaurante('Pizzaria da Mooca', 'Pizza')
pizza = Prato('Pizza de Mussarela', 65.00, 'Muita mussarela')
bebida = Bebida('Coca-cola', 9.50, '600ml')

pizzaria.adicionar_no_cardapio(pizza)
pizzaria.adicionar_no_cardapio(bebida)
    
def main():
    pizzaria.exibir_cardapio
    
    
    
if __name__ ==  '__main__':
    main()
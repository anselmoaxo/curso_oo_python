from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

  
pizzaria = Restaurante('Pizzaria da Mooca', 'Pizza')
pizza = Prato('Pizza de Mussarela', 90.00, 'Muita mussarela')
pizza.aplicar_desconto()
bebida = Bebida('Coca-cola', 10.0, '600ml')
bebida.aplicar_desconto()

pizzaria.adicionar_no_cardapio(pizza)
pizzaria.adicionar_no_cardapio(bebida)
    
def main():
    pizzaria.exibir_cardapio
    
    
    
if __name__ ==  '__main__':
    main()
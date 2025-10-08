from product import Product
from typing import Optional

"""Essa classe é a responsável pelo gerenciamento do fluxo de produtos imbutidos em uma Linha de Produção. Basicamente funciona como uma lista que possui
algumas funcionalidades especiais para controlar esse fluxo."""
class ProductionLine:
    
    """Inicializamos a classe com o auxilio de algumas estruturas nativas, como listas e dicionários (pois é mais rápido acessar os valores dos números de série
    através de pares chave-valor)"""
    def __init__(self, steps: list[str] ): 
        #Utilizo Type Hint para especificar que tipo de dado eu espero nos argumentos, nesse caso, uma lista
        self.production_steps: list[str] = ["Start"] + steps + ["Finished"] #Lista das etapas
        self.products_in_progress: dict[int, Product] = {} #Dicionário para o acesso de produtos que estão na linha de produção
        self.finished_products: list[Product] = [] #Lista para os produtos que foram finalizados
    
    """Método de adição de produtos na linha de produção"""
    def add_new_product(self):
        new_product = Product()
        self.products_in_progress[new_product.serial_number] = new_product

        print(f"New product has added in the Production Line: {new_product}")
        
        return new_product
    
    """Método de controle de fluxo de produtos na linha de produção"""   
    def line_process(self):
        #Basicamente, utilizamos uma estrutura de repetição para percorrer os produtos através do número de série. Como foi utilizado um dicionário, podemos
        #simplesmente utilizar as chaves como se tivessemos uma lista desses produtos
        for serial_number in list(self.products_in_progress.keys()):
            product = self.products_in_progress[serial_number]
            try:
                current_index = self.production_steps.index(product.current_step)
            except ValueError:
                print(f"Warning: Step '{product.current_step}' from product {product.serial_number} not found on the Production Line")
                continue
        #Aqui, estamos controlando o fluxo de etapas de cada produto, fazendo com que as etapas sejam passadas fase pós fase, até que fazemos a verificação da fase
        #final, que nesse caso é a fase 'Finished'. Com isso, encerramos o processo de fabricação desse produto
        if current_index < len(self.production_steps) - 1:
            next_step = self.production_steps[current_index + 1]
            product.next_step(next_step)
            if next_step == "Finished":
                self._finish_product(product)
        else:
            print(f"Product {product.serial_number} is already in the final step")

    """Método de finalização do processo de construção do produto. Resumidamente, encerramos o processo de produção de um produto a partir da etapa 
    'Finished', o que faz com que ele seja removido do dicionário de produtos que estão na linha de produção para a lista de produtos finalizados"""
    def _finish_product(self, product: Product):
        print(f"Finished: {product} completed production")
        self.finished_products.append(product)
        del self.products_in_progress[product.serial_number]

    """Método de ordenação de produtos utilizando uma função lambda que ordena os produtos com base no número de série"""
    def sort_finished_products(self):
        #Nesse caso aqui, como os números de série não se repetem, o sort() é suficiente para realizar essa ordenação de forma simples
        self.finished_products.sort(key=lambda p: p.serial_number)

    """Método de busca com base no número de série ou no objeto em si, que nesse caso é a instância da classe Product"""
    def find_finished_product(self, serial_number: int) -> Optional[Product]:
        #Basicamente, apenas percorremos a lista de produtos finalizados comparando os números de série
        for product in self.finished_products:
            if product.serial_number == serial_number:
                return product
        return None        
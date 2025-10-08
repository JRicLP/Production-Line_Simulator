from stack import Stack

"""Essa classe é o TAD, basicamente, funciona a partir da simulação de um produto e suas etapas"""
class Product:
    #Adicionei essa variável de classe como um valor especial para a criação de números de série que não se repitam
    _next_serial_number = 1

    """Inicializamos o nosso produto atribuindo um número de série, a etapa inicial 'Start', e o histórico de etapas"""
    def __init__(self):

        self.serial_number = Product._next_serial_number
        #Atualizando a variável de classe para evitar a repetição de números de série
        Product._next_serial_number += 1

        self.current_step = "Start"

        self.step_history = Stack()
        self.step_history.push(self.current_step)
        
    """Método responsável pelo avanço de etapas do produto e registro no histórico"""
    def next_step(self, next_step):
        
        self.current_step = next_step
        self.step_history.push(self.current_step)

        print(f"Product {self.serial_number} advanced to the step: {self.current_step}" )
        
    """Método responsável pelo retorno de etapas do produto, retornando para a última etapa que foi passada"""
    def undo_step(self):
        #Verificando se existe alguma etapa no histórico de etapas para poder retornar
        if len(self.step_history) <= 1:
            return f"Product {self.serial_number} is at the 'Start' step. Nothing to undo."

        removed_step = self.step_history.pop()
        self.current_step = self.step_history.peek()
        print(f"Product {self.serial_number}: Step '{removed_step}' undone. Returned to: '{self.current_step}'")

    """Método responsável pela representação do produto"""
    def __str__(self):
        return f"Product: {self.serial_number} | Current Step: {self.current_step}"
        
"""Essa é a classe Node que será utilizada como estrutura básica da Pilha"""
class Node:
   
    """Inicializamos com o Dado armazenado e referências para o termo anterior e posterior da estrutura"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""Essa é a classe Stack, a estrutura base da Pilha"""
class Stack:
    
    """Inicializamos com a referência do Topo da Pilha e do seu Tamanho"""
    def __init__(self, is_internal_history=False):
        
        #Aqui, foi utilizada uma flag para verificar se a pilha criada é uma instância da classe ou uma pilha interna para o histórico
        #evitando que o método fique chamando ele mesmo, como uma recursão
        self.top = None
        self._size = 0

        #Desse modo, quando o programa detecta que é uma pilha interna, valida-se a criação dessa pilha para o histórico
        if not is_internal_history:
            self._history = Stack(is_internal_history=True)
        else:
            self._history = None # 
    
    """Método de adição de novos elementos no topo da pilha"""
    def push(self, element, _from_undo=False):
        #Aqui, foi adicionada uma flag para controlar o histórico de processos, já que, por exemplo, no caso de um defeito
        #os processos nos quais o elemento passou são refeitos com o undo_pop(), o que limpa o histórico para recriá-lo
        new_node = Node(element)
        
        if self.top is not None:
            new_node.next = self.top
            self.top.prev = new_node
        
        self.top = new_node
        self._size += 1
        #Aqui, basicamente verifico se o push tuilizado foi do método undo_pop() ao invés do pop(), o que faria com que tivessemos uma situação
        #de retorno a uma determinada fase do processo de construção e não de avanço nas etaapas
        if self._history is not None and not _from_undo and not self._history.is_empty():
            self._history = Stack(is_internal_history=True)
    
    """Método de remoção de elementos do topo da pilha"""
    def pop(self):

        if self.is_empty():
            raise IndexError("The stack is empty")
        
        removed_data = self.top.data
        
        #Aqui, basicamente, fazemos o encadeamento das etapas que o produto irá passar, fazendo com que ela seja removida do topo da pilha
        if self._history is not None:
            self._history.push(removed_data)
        
        self.top = self.top.next
        self._size -= 1
        
        if self.top is not None:
            self.top.prev = None
        
        return removed_data
    
    """Esse é um método de 'retorno' do último elemento removido da Pilha"""
    def undo_pop(self):
        #Aqui, verificamos se houve algum processo anteriormente removido da pilha principal para poder adicionar na pilha auxilair
        if self._history is None or self._history.is_empty():
            print("There are no elements to return.")
            return
        #Aqui, utilizamos uma pilha auxiliar que adiciona os elementos que foram removidos do topo da pilha principal
        last_popped_element = self._history.pop()
        #Aqui, eu altero o valor da flag para validar que o push foi do método undo_pop() e não do pop(), o que reflete na organização do
        #histórico de etapas
        self.push(last_popped_element, _from_undo=True)

    """Método para exibição do elemento que se encontra no topo da Pilha"""
    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.top.data
    
    """Método de verificação da Pilha, para saber se está vazia"""
    def is_empty(self):
        return self._size == 0
    
    """Método para retornar o tamanho da Pilha"""
    def __len__(self): 
        return self._size
    
    """Método de representação da estrutura da Pilha"""
    def __repr__(self):
        #Basicamente, utilizamos um ponteiro para percorrer a Pilha e desse modo adicionar a uma String que é retornada posteriormente
        r = ""
        pointer = self.top
        while pointer is not None:
            r += str(pointer.data) + "\n"
            pointer = pointer.next
        return r
    
    """Método de retorno para a representação da Pilha"""
    def __str__(self): 
        return self.__repr__()
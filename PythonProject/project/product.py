from stack import Stack

class Product:

    _special_serial_number = 1

    def __init__(self):

        self.serial_number = Product._special_serial_number
        Product._special_serial_number += 1

        self.current_step = "Start"

        self.step_history = Stack()
        self.step_history.push(self.current_step)
        
    
    def next_step(self, next_step):
        
        self.current_step = next_step
        self.step_history.push(self.current_step)

        print(f"Product {self.serial_number} advanced to the step: {self.current_step}" )
        

    def undo_step(self):
        
        if len(self.step_history) <= 1:
            return f"Product {self.serial_number} is at the 'Start' step. Nothing to undo."

        removed_step = self.step_history.pop()
        self.current_step = self.step_history.peek()
        print(f"Product {self.serial_number}: Step '{removed_step}' undone. Returned to: '{self.current_step}'")


    def __str__(self):
        return f"Product: {self.serial_number} - Actual Step: {self.current_step}"
        
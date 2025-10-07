from product import Product
from typing import Optional


class ProductionLine:

    def __init__(self, steps: list[str] ):
        self.production_steps: list[str] = ["Start"] + steps + ["Finished"]
        self.products_in_progress: dict[int, Product] = {}
        self.finished_products: list[Product] = []
    
    def add_new_product(self):
        new_product = Product()
        self.products_in_progress[new_product.serial_number] = new_product

        print(f"New product has added in the Production Line: {new_product}")
        
        return new_product
        
    def line_process(self):
        print("Processing the Production Line...")

        for serial_number in list(self.products_in_progress.keys()):
            product = self.products_in_progress[serial_number]
            try:
                current_index = self.production_steps.index(product.current_step)
            except ValueError:
                print(f"Warning: Step '{product.current_step}' from product {product.serial_number} not found on the Production Line")
                continue
        if current_index < len(self.production_steps) - 1:
            next_step = self.production_steps[current_index + 1]
            product.next_step(next_step)
            if next_step == "Finished":
                self._finish_product(product)
        else:
            print(f"Product {product.serial_number} is already in the final step")

    def _finish_product(self, product: Product):
        print(f"Finished: {product} completed production")
        self.finished_products.append(product)
        del self.products_in_progress[product.serial_number]

    def sort_finished_products(self):
        print("Ordering stock of finished products...")
        self.finished_products.sort(key=lambda p: p.serial_number)

    def find_finished_product(self, serial_number: int) -> Optional[Product]:
        
        for product in self.finished_products:
            if product.serial_number == serial_number:
                return product
        return None        
    
    def exibir_status(self):
        
        print("\n" + "="*30)
        print("Production Line Status:")
        print("="*30)
        
        print(f"\n Products in progress ({len(self.products_in_progress)}):")
        if self.products_in_progress:
            for product in self.products_in_progress.values():
                print(f"   - {product}")
        else:
            print("   - None.")
            
        print(f"\n Finished products ({len(self.finished_products)}):")
        if self.finished_products:
            for product in self.finished_products:
                print(f"   - {product}")
        else:
            print("   - None.")
        print("="*30)
        
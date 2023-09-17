#!/usr/bin/env python3

class Shoe:
    def __init__(self,size) -> None:
        self.size = size
        
    def change_size(self,new_size):
        self.size = new_size

bata_shoe = Shoe(42)
print(bata_shoe.size)

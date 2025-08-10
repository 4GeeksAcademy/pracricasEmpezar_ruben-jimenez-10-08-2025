class Product:
    def __init__(self, id: int, name:str,year:str,brand:str):
        self.id= id
        self.name=name
        self.year=year
        self.brand=brand
    
    def serializer(self):
        return{
            "id":self.id,
            "name":self.name,
            "year":self.year,
            "brand":self.brand
        }

        
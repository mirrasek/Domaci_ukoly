import math
from abc import ABC, abstractmethod


class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

    def __str__(self):
        return f"{self.name} (koeficient {self.locality_coefficient})"


class Property(ABC):
    @abstractmethod
    def __init__(self, locality):
        self.locality = locality 
    
    @abstractmethod
    def calculate_tax(self):
        pass

class Estate(Property):
    estate_coefficients = {
        "land" : 0.85,
        "building site" : 9,
        "forrest" : 0.35,
        "garden" : 2
        }
    
    estate_names = {
        "land": "Zemědělský pozemek",
        "building site": "Stavební pozemek",
        "forrest": "Lesní pozemek",
        "garden": "Zahrada"
    }
    
    def __init__(self, locality, estate_type, area):
        super().__init__(locality)  
        self.estate_type = estate_type
        self.area = area

    def calculate_tax(self):
       estate_coeficient = Estate.estate_coefficients[self.estate_type]
       tax = self.area * estate_coeficient * self.locality.locality_coeficient
       return math.ceil(tax)
    
    def __str__(self):
        estate_name = Estate.estate_names[self.estate_type]
        return f"{estate_name}, lokalita {self.locality}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

class Residence(Property):
    def __init__(self, locality, area, commercial):    
        super().__init__(locality) 
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        if self.commercial == True:
            tax = self.area *self.locality.locality_coeficient * 15 * 2
        else:
            tax = self.area *self.locality.locality_coeficient * 15
        return int(tax)
    
    def __str__(self):
        if self.commercial == True:
            return f"Kancelář/obchodní prostor, lokalita {self.locality}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
        else:
            return f"Byt/dům, lokalita {self.locality}, {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

class TaxReport:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.property_list = []

    def add_property(self, property_object):
        self.property_list.append(property_object)
    
    def calculate_tax(self):
        total_tax = 0
        for property_object in self.property_list:
            total_tax += property_object.calculate_tax()
        return total_tax

locality_1 = Locality ("Manětín", 0.8)
locality_2 = Locality ("Brno", 3)

estate_1 = Estate(locality_1, "land", 900)
residence_1 = Residence(locality_1, 120, False)
residence_2 = Residence(locality_2, 90, True)

report_1 = TaxReport("Zuzana Nová")
report_2 = TaxReport ("Petr Kadlec")

report_1.add_property(estate_1)
report_1.add_property(residence_1)
report_2.add_property(residence_2)

print(estate_1.calculate_tax())
print(residence_1.calculate_tax())
print(residence_2.calculate_tax())

print(estate_1)
print(residence_1)
print(residence_2)

print(f"{report_1.owner_name} - daň {report_1.calculate_tax()} Kč.")
print(f"{report_2.owner_name} - daň {report_2.calculate_tax()} Kč.")

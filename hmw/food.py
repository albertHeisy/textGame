# you need to make something int, beacuse default entry is string !
class Food:
    # inicijalizacija => koji elementi ce ciniti kalsu
    def __init__(self,name,carbs,protein,fat):
        self.name = name
        self.carbs = int(carbs)
        self.protein = int(protein)
        self.fat = int(fat)
    
    # bez ovog nemozemo dobiti ime, nego nam u pritu baca adresu
    def __str__(self):
        return self.name

    # ukupno kalorija u namjernici
    def calories(self):
        return self.carbs * 4 + self.protein * 4 + self.fat * 9

class Recipe:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
    
    # vraca ukuopno kalorija u receptu 
    def calories(self):
        cals = 0
        for food in self.ingredients:
            cals += food.calories()
        return cals

    def __str__(self):
        return self.name

# funkcija za printanje bilo kojeg recepta !imena vaijabla su mi ostale iz maina al to nema veze!            
def magic_print(kolac):
    print('Za {} potrebne su vam sljedece namjernice:'.format(kolac.name))
    for br,namj in enumerate(kolac.ingredients, 1):
        print(str(br)+'.'+str(namj)+' cals: '+str(namj.calories()))
    print('Navedeni recept ima {} kalorija.'.format(kolac.calories()))



def main():
    # stvaranje namjernica kao klasa Food
    jabuka = Food('Jabuka', '10', '5', '1')
    kruska = Food('Kruska', '7', '5', '2')
    coko = Food('Cokolada', '100', '3', '500')

    # stvaranje shoping liste za kolac
    namjernice = [jabuka,kruska,coko]
    voce = [jabuka,kruska]

    # test jel sam skuzio kak funkcionira prica oko klasa
    print('Ja sam {} i imam {} kalorija'.format(jabuka.name, jabuka.calories()))

    # stvaranje recepta pomocu klase
    kolac = Recipe('Vocni kolac',namjernice)
    salata = Recipe('Vocna salata', voce)
    
    # ispisisavanje recepta pomocu funkcije 
    magic_print(kolac)
    print()
    magic_print(salata)

main()

veg = input("Is anyone in your party vegetarian? (yes/no) ").lower()
vegan = input("Is anyone in your party vegan? (yes/no) ").lower()
glutenfree = input("Is anyone in your party gluten-free? (yes/no) ").lower()

print("here are your restaurant choices :")

if (veg == "no" and vegan == "no" and glutenfree == "no"):
    print("\t Joe's Gourmet Burgers")
if (veg == "yes" and glutenfree == "yes"):
    print("\t Main Street Pizaa Company")
if (veg == "yes" and glutenfree == "yes"):
    print("\t Corner Cafe")
    print("\t The Chef's Kitchen")
if (veg == "yes" and glutenfree == "no"):
    print("\t Mama's Fine Italian")

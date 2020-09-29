

def dict_values(dict):

    print(f"dict_values({dict})\n")

    for key , values in dict.items():

        str = ""

        for i in values:

           str += i +" "

        print(f"{key}: {str}\n*****\n")


dict_values({120:("Visal","Borey","Sovann"), 130:("Hout","Mouyleng","Pidor"),140:("Nary","Misora","Masaaki")})

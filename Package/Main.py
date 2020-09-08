import Package.Data as Data

if __name__ == '__main__':

    input_date = input("Introduce tu fecha de Nacimiento con el siguiente formato: dd/mm/aa")
    str_date = input_date.split("/")
    name = ""
    try:
        for index, item in enumerate(str_date):
            if index == 0:
                name = Data.first_name(int(item))
            elif index == 1:
                name += " " + Data.middle_name(int(item))
            else:
                name += " " + Data.last_name(int(item[1:]))

    except ValueError:
        print("¡No has introducido correctamente el formato!")
    except KeyError:
        print("¡No has introducido correctamente la fecha!")
    except Exception as e:
        print(type(e).__name__)

    print(name)


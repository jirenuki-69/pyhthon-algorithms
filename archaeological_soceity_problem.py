def calculate_year_symbols(year_range):
    """Función para calcular el número mínimo de símbolos necesarios para representar un rango de años en numeración romana."""
    A, B = year_range.split('-')
    A_year, A_type = int(A[:-2]), A[-2:]
    B_year, B_type = int(B[:-2]), B[-2:]

    # Año cero no existe en numeración romana, se trata como año 1BC
    if A_year == 0:
        A_year = 1

    # Función para convertir un número entero en numeración romana
    def int_to_roman(num):
        print(num)
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        print(roman_num)
        return roman_num

    # Calcular el número mínimo de símbolos necesarios para el rango de años
    symbols = 0

    # Años en el mismo tipo (AD o BC)
    if A_type == B_type:
        if A_year <= B_year:
            symbols = len(int_to_roman(B_year - A_year + 1))
        else:
            symbols = len(int_to_roman(A_year - B_year + 1))

    # Años en tipos diferentes (AD y BC)
    else:
        # Años AD mayores que años BC
        if A_type == 'AD':
            symbols = len(int_to_roman(B_year)) + \
                len(int_to_roman(A_year))
        # Años BC mayores que años AD
        else:
            symbols = len(int_to_roman(A_year)) + \
                len(int_to_roman(B_year))

    return symbols


# Ejemplos de uso
year_range_1 = "1BC-1AD"
result_1 = calculate_year_symbols(year_range_1)
print("Resultado para", year_range_1, "es:", result_1)

year_range_2 = "753BC-747BC"
result_2 = calculate_year_symbols(year_range_2)
print("Resultado para", year_range_2, "es:", result_2)

year_range_3 = "2000AD-2012AD"
result_3 = calculate_year_symbols(year_range_3)
print("Resultado para", year_range_2, "es:", result_3)

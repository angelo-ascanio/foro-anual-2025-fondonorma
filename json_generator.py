import json

values = [
    ["9XY0YI3R", "10975865", "María", "González", "Petrobras"],
    ["9CG6IS8W", "15644029", "Ana", "Rodríguez", "Pemex"],
    ["5UX7QC2Z", "23292047", "Sofía", "Pérez", "América Móvil"],
    ["9CQ5FR0W", "8965950", "Valentina", "Hernández", "JBS S.A."],
    ["8BD8MB3K", "16895203", "Isabella", "García", "Vale S.A."],
    ["5LD9BX9I", "11068827", "Camila", "Martínez", "Walmart"],
    ["8PO0BQ0I", "18209249", "Mariana", "Sánchez", "Empresas Copec"],
    ["0ZZ8FO4R", "29343856", "Elizabeth", "López", "Fomento Económico Mexicano"],
    ["4YD7OH9R", "13639191", "Nicole", "Díaz", "Techint Argentina"],
    ["1VG2ZI2O", "10246737", "Victoria", "Rojas", "Ultrapar"],
    ["5EP8XA7L", "29442827", "José", "Ramírez", "PDVSA"],
    ["5DP2RT9P", "11929770", "Juan", "Castillo", "YPF"],
    ["1EU5ND0O", "22032048", "Luis", "Gómez", "Raizen"],
    ["2SM5MH9O", "27684505", "Carlos", "Romero", "General Motors"],
    ["2WB5YB5T", "19980172", "Miguel", "Fernández", "Ecopetrol"],
    ["2IZ2LA8P", "21795753", "Gabriel", "Torres", "Grupo Ipiranga"],
    ["1SS9RV4C", "15213696", "Diego", "Mendoza", "Grupo Alfa"],
    ["9AT0ZJ7D", "29887440", "Antonio", "Medina", "Almecenes Éxito"],
    ["9IH3RE3L", "15268794", "Jesús", "Moreno", "Polar"],
    ["3JL6UY3P", "18925015", "Francisco", "Gutiérrez", "Nestlé"],
]

converted_values = [
    {
        "hash": entry[0],
        "ID": entry[1],
        "Nombre": entry[2],
        "Apellido": entry[3],
        "Empresa": entry[4]
    }
    for entry in values
]

json_data = json.dumps(converted_values, indent=4)

# Save to a JSON file
with open("output.json", "w") as json_file:
    json_file.write(json_data)

print("Data has been converted and saved to output.json")
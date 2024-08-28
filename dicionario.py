cliente = {
    "nome" : "Evandro",
    "email" : "evandro@gmail.com",
    "telefone" : "22997222660",
    "endereco" : "Rua A"
}
#print(cliente)

#print(cliente["nome"])
#resultado =(cliente.get("email"))
#resultado = cliente.keys()
#resultado = cliente.values()
#cliente["endereco"] = "Rua B"
#print(cliente)

#cliente.update({"endereco" : "Rua Nova"})
#print(cliente)

#cliente.pop("endereco")
#cliente.clear()
#cliente.keys()


for i, j in cliente.items():
 print(i,j)
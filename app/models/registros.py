# Super Classe Registros para referenciar o armazenamento no banco de dados.

class Registro():

    #Concentra os dados comuns a todos os registros.
    # id, , origem, data e etc.

    pass


class Reserva():

    # A classe central do sistema herda atributos de registro e rastreabilidade
    # contem informações de data de entrada, saida, quarto reservado e etc.



    pass


class Pagamento():

    # Pagamento realizado para uma reserva.
    
    pass


class Adicional():
    
    # Item ou serviço extra cobrado em uma reserva (ex: consumo de um frigobar, etc).

    pass


class Bloqueio():

    # Indisponibilização temporária de um quarto.

    pass
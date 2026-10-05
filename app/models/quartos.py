# Super Classe Quartos como referência para armazenamento no banco de dados.

class Quarto():

    # Classe base abstrata de um quarto.

    def __init__( # parâmetros do método construtor
        self,
        numero: str,
        capacidade: int,
        diaria: float,
        status: char,
        bloqueios: list,
        observacoes: str,
        
    ):
        self.numero = numero # método construtor
        self.capacidade = capacidade
        self.diaria = diaria
        self.status - status
        self.bloqueios = bloqueios
        self.observacoes = observacoes

        # ================================ métodos =============================

        # ==== número do apto ====
        @property
        def numero(self):
            return self.numero

        @numero.setter
        def numero(self, endereco: str):

            if not endereco or not str(endereco).strip():
                raise ValueError("O número do quarto não pode ser vazio.")
            self.__numero = str(endereco).strip()

        # ==== capacidade de hospedes ====
        @property
        def capacidade(self):
            return self.capacidade

        @capacidade.setter
        def capacidade(self, quantidade: int):
            if not isinstance(quantidade, int) or quantidade <= 0:
                raise ValueError("A capacidade do quarto deve ser um número inteiro positivo.")
            self.__capaciadade = quantidade

        # ==== diária do quarto ====
        @property
        def diaria(self):
            return self.diaria

        @diaria.setter
        def diaria(self, valor: float):
            if not isinstance(valor, (int, float)) or valor < 0:
                raise ValueError("O valor da diária deve ser um número positivo.")
            self.__diaria = float(valor)

        # ==== status do quarto ====
        @property
        def status(self):
            return self.status

        @status.setter
        def status(self, situacao: char):
            if not isinstance(situacao, str) or len(situacao) != 1:
                raise ValueError("O status do quarto deve ser um único caractere.")
            self.__status = situacao

        # ==== observações do quarto ====
        @property
        def observacoes(self):
            return self.observacoes

        @observacoes.setter
        def observacoes(self, obs: str):
            if not isinstance(obs, str):
                raise ValueError("As observações devem ser uma string.")
            self.__observacoes = obs.strip()

        # ============================ métodos especiais ==============================
        def __str__(self) -> str:                   # Representação do quarto em string
            return f"Quarto {self.numero} ({self.status}) - R$ {self.diaria:.2f}/noite"

        def __lt__(self, outro: "Quarto"):          # Permite a comparação de quartos pela diária
            if not isinstance(outro, Quarto):
                return NotImplemented
            return self.diaria < outro.diaria

        def __repr__(self) -> str:                  # Representação do quarto para rastreio.   
            return (
                f"Quarto(numero={self.numero!r}, capacidade={self.capacidade},\ndiaria={self.diaria}, status={self.status!r})"
            )

        def __eq__(self, outro: object) -> bool:    # Compara se dois quartos são iguais pelo número.
            if not isinstance(outro, Quarto):
                return NotImplemented
            return self.numero == outro.numero

        def __hash__(self) -> int:                  # Retorna o hash do quarto baseado no número.
            return hash(self.numero)
        
class Simples(Quarto):
    # Quarto do tipo simples (basiquinho)
    pass
class Duplo(Quarto):
    # Quarto do tipo duplo (para casal, familia)
    pass
class Luxo(Quarto):
    # Quarto do tipo luxo (nível superior)
    pass
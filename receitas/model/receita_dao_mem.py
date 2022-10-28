from .receita_model import Receita, ReceitaSemId, ReceitaNaoEncontrada

# Isto não é um banco de dados de verdade, mas vamos fingir que é.
# Vamos deixar a SQL e o banco de dados de verdade para o terceiro semestre.
class BancoDeDadosReceita:

    def __init__(self) -> None:
        self.__banco_de_dados: dict[int, Receita] = {}
        self.__contador = 0

    def criar(self, dados: ReceitaSemId) -> Receita:
        self.__contador += 1
        nova = dados.com_id(self.__contador)
        self.__banco_de_dados[self.__contador] = nova
        return nova

    def editar(self, atualizada: Receita) -> Receita:
        if atualizada.id_receita not in self.__banco_de_dados:
            raise ReceitaNaoEncontrada
        self.__banco_de_dados[atualizada.id_receita] = atualizada
        return atualizada

    def excluir(self, id_receita: int) -> bool:
        if id_receita not in self.__banco_de_dados: return False
        del self.__banco_de_dados[id_receita]
        return True

    def buscar_por_id(self, id_receita: int) -> Receita:
        if id_receita in self.__banco_de_dados:
            return self.__banco_de_dados[id_receita]
        raise ReceitaNaoEncontrada

    def listar(self, busca: str) -> list[Receita]:

        busca_limpa: list[str] = []
        for termo in busca.split("\n"):
            if termo.strip() != "":
                busca_limpa.append(termo.upper())

        # Caso fácil: Listar tudo.
        if len(busca_limpa) == 0:
            return list(self.__banco_de_dados.values())

        # Caso mais complicado: Fazer busca textual.
        resultado: list[Receita] = []
        for receita in self.__banco_de_dados.values():
            for termo in busca_limpa:
                if termo in receita.nome_bolo.upper() \
                        or termo in receita.ingredientes.upper() \
                        or termo in receita.modo_preparo.upper():
                    resultado.append(receita)
                    break
        return resultado
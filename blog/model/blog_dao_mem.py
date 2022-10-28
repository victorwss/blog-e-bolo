from .blog_model import Materia, MateriaSemId, MateriaNaoEncontrada

# Isto não é um banco de dados de verdade, mas vamos fingir que é.
# Vamos deixar a SQL e o banco de dados de verdade para o terceiro semestre.
class BancoDeDadosMateria:

    def __init__(self) -> None:
        self.__banco_de_dados: dict[int, Materia] = {}
        self.__contador = 0

    def criar(self, dados: MateriaSemId) -> Materia:
        self.__contador += 1
        nova = dados.com_id(self.__contador)
        self.__banco_de_dados[self.__contador] = nova
        return nova

    def editar(self, atualizada: Materia) -> Materia:
        if atualizada.id_materia not in self.__banco_de_dados:
            raise MateriaNaoEncontrada
        self.__banco_de_dados[atualizada.id_materia] = atualizada
        return atualizada

    def excluir(self, id_materia: int) -> bool:
        if id_materia not in self.__banco_de_dados: return False
        del self.__banco_de_dados[id_materia]
        return True

    def buscar_por_id(self, id_materia: int) -> Materia:
        if id_materia in self.__banco_de_dados:
            return self.__banco_de_dados[id_materia]
        raise MateriaNaoEncontrada

    def listar(self, busca: str) -> list[Materia]:

        busca_limpa: list[str] = []
        for termo in busca.split("\n"):
            if termo.strip() != "":
                busca_limpa.append(termo.upper())

        # Caso fácil: Listar tudo.
        if len(busca_limpa) == 0:
            return list(self.__banco_de_dados.values())

        # Caso mais complicado: Fazer busca textual.
        resultado: list[Materia] = []
        for materia in self.__banco_de_dados.values():
            for termo in busca_limpa:
                if termo in materia.titulo.upper() \
                        or termo in materia.autores.upper() \
                        or termo in materia.conteudo.upper():
                    resultado.append(materia)
                    break
        return resultado
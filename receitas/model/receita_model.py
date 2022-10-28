from typing import Sequence
from dataclasses import dataclass

# Estas classes modelam os dados e as regras de negócio da nossa aplicação.

# Use Receita(**algum_dicionario_aqui) para criar instâncias desta classe a partir de um dicionário.
@dataclass(frozen = True)
class Receita:
    id_receita:   int
    nome_bolo:    str
    ingredientes: str
    modo_preparo: str
    url_foto:     str

    def __post_init__(self) -> None:
        if type(self.id_receita  ) != int                                   : raise TypeError
        if type(self.nome_bolo   ) != str or self.nome_bolo.strip   () == "": raise TypeError
        if type(self.ingredientes) != str or self.ingredientes.strip() == "": raise TypeError
        if type(self.modo_preparo) != str or self.modo_preparo.strip() == "": raise TypeError
        if type(self.url_foto    ) != str or self.url_foto.strip    () == "": raise TypeError

    @staticmethod
    def __split_lines(txt: str) -> Sequence[str]:
        paragrafos = txt.split("\n")
        reconstruindo: list[str] = []
        for p in paragrafos:
            ps = p.strip()
            if ps != "":
                reconstruindo.append(ps)
        return tuple(reconstruindo)

    @property
    def vazia(self) -> bool:
        return False

    @property
    def ingredientes_lista(self) -> Sequence[str]:
        return Receita.__split_lines(self.ingredientes)

    @property
    def modo_preparo_lista(self) -> Sequence[str]:
        return Receita.__split_lines(self.modo_preparo)

# Use ReceitaSemId(**algum_dicionario_aqui) para criar instâncias desta classe a partir de um dicionário.
@dataclass(frozen = True)
class ReceitaSemId:
    nome_bolo:    str
    ingredientes: str
    modo_preparo: str
    url_foto:     str

    def __post_init__(self) -> None:
        if type(self.nome_bolo   ) != str or self.nome_bolo.strip   () == "": raise TypeError
        if type(self.ingredientes) != str or self.ingredientes.strip() == "": raise TypeError
        if type(self.modo_preparo) != str or self.modo_preparo.strip() == "": raise TypeError
        if type(self.url_foto    ) != str or self.url_foto.strip    () == "": raise TypeError

    def com_id(self, id_receita: int) -> Receita:
        return Receita(id_receita, self.nome_bolo, self.ingredientes, self.modo_preparo, self.url_foto)

class ReceitaVazia:
    @property
    def id_receita(self) -> int: return -1

    @property
    def nome_bolo(self) -> str: return "Nova receita de bolo"

    @property
    def ingredientes(self) -> str: return ""

    @property
    def modo_preparo(self) -> str: return ""

    @property
    def url_foto(self) -> str: return ""

    @property
    def vazia(self) -> bool: return True

    @property
    def ingredientes_lista(self) -> Sequence[str]: return ()

    @property
    def modo_preparo_lista(self) -> Sequence[str]: return ()

class ReceitaNaoEncontrada(Exception):
    pass
from typing import Sequence
from dataclasses import dataclass

# Estas classes modelam os dados e as regras de negócio da nossa aplicação.

# Use Materia(**algum_dicionario_aqui) para criar instâncias desta classe a partir de um dicionário.
@dataclass(frozen = True)
class Materia:
    id_materia: int
    titulo:     str
    autores:    str
    conteudo:   str
    url_foto:   str

    def __post_init__(self) -> None:
        if type(self.id_materia) != int                               : raise TypeError
        if type(self.titulo    ) != str or self.titulo.strip  () == "": raise TypeError
        if type(self.autores   ) != str or self.autores.strip () == "": raise TypeError
        if type(self.conteudo  ) != str or self.conteudo.strip() == "": raise TypeError
        if type(self.url_foto  ) != str or self.url_foto.strip() == "": raise TypeError

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
    def autores_lista(self) -> Sequence[str]:
        return Materia.__split_lines(self.autores)

    @property
    def conteudo_lista(self) -> Sequence[str]:
        return Materia.__split_lines(self.conteudo)

# Use MateriaSemId(**algum_dicionario_aqui) para criar instâncias desta classe a partir de um dicionário.
@dataclass(frozen = True)
class MateriaSemId:
    titulo:   str
    autores:  str
    conteudo: str
    url_foto: str

    def __post_init__(self) -> None:
        if type(self.titulo  ) != str or self.titulo.strip  () == "": raise TypeError
        if type(self.autores ) != str or self.autores.strip () == "": raise TypeError
        if type(self.conteudo) != str or self.conteudo.strip() == "": raise TypeError
        if type(self.url_foto) != str or self.url_foto.strip() == "": raise TypeError

    def com_id(self, id_materia: int) -> Materia:
        return Materia(id_materia, self.titulo, self.autores, self.conteudo, self.url_foto)

class MateriaVazia:
    @property
    def id_materia(self) -> int: return -1

    @property
    def titulo(self) -> str: return "Nova matéria do blog"

    @property
    def autores(self) -> str: return ""

    @property
    def conteudo(self) -> str: return ""

    @property
    def url_foto(self) -> str: return ""

    @property
    def vazia(self) -> bool: return True

    @property
    def autores_lista(self) -> Sequence[str]: return ()

    @property
    def conteudo_lista(self) -> Sequence[str]: return ()

class MateriaNaoEncontrada(Exception):
    pass
from abc import ABC, abstractmethod


class Busca(ABC):
    @abstractmethod
    def recuperar(self, dados):
        pass

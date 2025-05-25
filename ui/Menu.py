from abc import abstractmethod,ABC

class Menu(ABC):

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def visualizar_menu(self):
        pass

    @abstractmethod
    def opciones(self):
        pass

    @abstractmethod
    def tratar_opciones(self, opcion:int):
        pass

    @abstractmethod
    def recoger_menu_opciones(self) -> int:
        pass
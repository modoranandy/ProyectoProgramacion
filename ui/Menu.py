from abc import abstractmethod,ABC

class Menu(ABC):

    @abstractmethod
    def _main(self):
        pass

    @abstractmethod
    def _visualizar_menu(self):
        pass

    @abstractmethod
    def _opciones(self):
        pass

    @abstractmethod
    def _tratar_opciones(self):
        pass

    @abstractmethod
    def _recoger_menu_opciones(self) -> int:
        pass
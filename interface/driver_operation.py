from interface.penolakan_operation import PenolakanOperation
from abc import ABC, abstractmethod

class DriverOperation(PenolakanOperation, ABC):
    
    @abstractmethod
    def menolak_pesanan(self) -> None:
        #isi method ini boleh diganti dengan "pass" saja
        pass
        
    @abstractmethod
    def mengantarkan_pesanan(self) -> None:
        pass
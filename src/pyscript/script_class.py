from abc import ABC, abstractmethod
from typing import Any

import logging as lg

class PYScript(ABC):
    def __init__(self, name: str, command: str, description: str) -> None:
        """Init of script class

        Args:
            name (str): Script name
            command (str): Script short command (ex.: hello-world)
            description (str): Script description (simple)
        """
        self.name = name
        self.command = command
        self.description = description
        
        self.logger = lg.getLogger(f"pyscript.{self.command}")
        
    
    @abstractmethod
    def run(self) -> Any:
        pass
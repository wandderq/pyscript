from typing import Any
from pyscript import PYScript

class HelloWorld(PYScript):
    def __init__(self) -> None:
        super().__init__(
            name='Hello, world!',
            command='hello-world',
            description='Just says hello to whole world'
        )
    
    def run(self) -> Any:
        self.logger.info('Hello, world!')  
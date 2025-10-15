import os
import re
import sys
import shutil
import logging as lg

from pyscript import utils, __encoding__
from pyscript.script_class import PYScript
from pyscript.exceptions import InvalidScriptError
from pyscript.const import SCRIPTS_PATH

class PYScriptCore:
    def __init__(self) -> None:
        self.logger = lg.getLogger('pyscript.core')
    
    def get_scripts(self) -> list[PYScript]:
        scripts_path = os.path.expanduser(SCRIPTS_PATH)
        os.makedirs(scripts_path, exist_ok=True)
        sys.path.append(scripts_path)
        
        scripts = []
        
        for file_name in os.listdir(scripts_path):
            file_path = os.path.join(scripts_path, file_name)

            if not os.path.isfile(file_path):
                self.logger.debug(f'Skipping non-file object in {SCRIPTS_PATH}')
                continue
            
            script = self.parse_script(file_path)
            if script:
                scripts.append(script)
        
        return scripts
    
    def print_scripts(self, scripts: list[PYScript]) -> None:
        if not scripts:
            utils.printf(f'\033[31mNo scripts were found in the directory: {os.path.expanduser(SCRIPTS_PATH)}\033[0m')
            return

        utils.printf('ID: \033[32mCommand\033[0m Description')
        utils.printf('-' * os.get_terminal_size().columns)
        for id, script in enumerate(scripts, start=1):
            utils.printf(f'{id}: \033[32m{script.command}\033[0m {script.description}')
        
        utils.printf('')
    
    def run_script(self, scripts: list[PYScript], script_command: str) -> None | int:
        for script in scripts:
            if not script.command == script_command:
                continue
            
            self.logger.info(f'Launching script: {script.name}')
            return script.run()
        
        self.logger.error(f'Script not found: {script_command}')
    
    def parse_script(self, script_path: str) -> PYScript | None:
        class_pattern = re.compile(r'^class ([a-zA-Z0-9_]*)\((\w*\.)?PYScript\):$')
        script: PYScript | None = None
        
        try:
            with open(script_path, 'r', encoding=__encoding__) as file:
                for line in file:
                    class_match = re.match(class_pattern, line)
                    if class_match:
                        class_name = class_match.group(1)
                        break
                
                if not class_match:
                    raise InvalidScriptError('Can\'t find any script class with PYScript parent class')
                
                script_lib = __import__(os.path.splitext(os.path.basename(script_path))[0])
                script = getattr(script_lib, class_name)()
                
                return script
        
        except Exception as e:
            self.logger.error(f'Error during parsing {script_path}: {e}. Cause: {e.__cause__}')
            return
    
    def move_script(self, script_path: str) -> None:
        src = script_path
        dest = os.path.join(
            os.path.expanduser(SCRIPTS_PATH),
            os.path.basename(script_path)
        )
        
        utils.printf(f"Script file {src} will be moved to scripts dir: {dest}. Are you sure about that?")
        if input('(y/n) > ').lower().strip() == 'y':
            shutil.move(src, dest)
            
        else:
            utils.printf('Abort')
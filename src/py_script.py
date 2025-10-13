import sys
import os
import re
import pyscript.utils as utils
import logging as lg

from pyscript.exceptions import InvalidScriptError
from pyscript.script_class import PYScript
from pyscript.const import SCRIPTS_PATH
from argparse import ArgumentParser

from pyscript import __version__, __encoding__

logger = utils.setup_logger('pyscript')

class PYScriptCore:
    def __init__(self) -> None:
        self.argparser = ArgumentParser(
            description='Universal scripts launcher and manager',
            epilog='See https://github.com/wandderq/pyscript (unavailable)'
        )
        self.argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode (debug logs)')
        self.argparser.add_argument('-V', '--version', action='store_true', help='Get pyscript version and some other stuff')
        
        
        # subparsers setup
        self.subparsers = self.argparser.add_subparsers(dest='command', metavar='')
        
        run_parser = self.subparsers.add_parser('run', help='Run PYScript script')
        run_parser.add_argument('script', type=str, help='Script name')
        
        list_parser = self.subparsers.add_parser('list', help='Show all available scripts')
    
    def get_scripts(self) -> list[PYScript]:
        scripts_path = os.path.expanduser(SCRIPTS_PATH)
        os.makedirs(scripts_path, exist_ok=True)
        sys.path.append(scripts_path)
        
        class_pattern = re.compile(r'^class ([a-zA-Z0-9_]*)\(PYScript\):$')
        scripts = []
        
        for file_name in os.listdir(scripts_path):
            file_path = os.path.join(scripts_path, file_name)

            if not os.path.isfile(file_path):
                logger.debug(f'Skipping non-file object in {SCRIPTS_PATH}')
                continue
            
            try:
                with open(file_path, 'r', encoding=__encoding__) as file:
                    for line in file:
                        class_match = re.match(class_pattern, line.strip())
                        if class_match:
                            class_name = class_match.group(1)
                            break
                            
                    if not class_match:
                        raise InvalidScriptError('Can\'t find any script class with PYScript parent class')
                
                scriptlib = __import__(os.path.splitext(file_name)[0])
                script: PYScript = getattr(scriptlib, class_name)()
                
                scripts.append(script)
                
            
            except Exception as e:
                logger.error(f'Error during script parsing: {e}. Cause: {e.__cause__}')
                continue
        
        return scripts
    
    def print_scripts(self, scripts: list[PYScript]) -> None:
        utils.printf('ID: \033[32mCommand\033[0m Description')
        utils.printf('-' * os.get_terminal_size().columns)
        for id, script in enumerate(scripts, start=1):
            utils.printf(f'{id}: \033[32m{script.command}\033[0m {script.description}')
    
    def run_script(self, scripts: list[PYScript], script_command: str) -> None | int:
        for script in scripts:
            if not script.command == script_command:
                continue
            
            logger.info(f'Launching script: {script.name}')
            return script.run()
        
        logger.error(f'Script not found: {script_command}')
    
    def run(self) -> None | int:
        args = self.argparser.parse_args()
        
        if args.verbose:
            logger.setLevel(lg.DEBUG)
        
        if args.version:
            utils.printf(f'PYScript v{__version__}')
            utils.printf(f'Scripts path: {os.path.expanduser(SCRIPTS_PATH)}')
            return 0
        
        if args.command == 'run':
            scripts = self.get_scripts()
            self.run_script(scripts, args.script)
        
        if args.command == 'list':
            scripts = self.get_scripts()
            self.print_scripts(scripts)
        
def main(): return PYScriptCore().run()
import sys
import os
import pyscript.utils as utils
import logging as lg

from argparse import ArgumentParser
from pyscript.core import PYScriptCore
from pyscript.const import SCRIPTS_PATH
from pyscript import __version__, __encoding__

logger = utils.setup_logger('pyscript')

class PYScriptCLI(PYScriptCore):
    def __init__(self) -> None:
        super().__init__()
        
        self.argparser = self.init_parser()
    
    def init_parser(self) -> ArgumentParser:
        argparser = ArgumentParser(
            description='Universal scripts launcher and manager',
            epilog='See https://github.com/wandderq/pyscript (unavailable)'
        )
        subparsers = argparser.add_subparsers(dest='command', metavar='')
        
        run_parser = subparsers.add_parser('run', help='Run PYScript script')
        run_parser.add_argument('script', type=str, help='Script name')
        
        list_parser = subparsers.add_parser('list', help='Show all available scripts')
        
        add_parser = subparsers.add_parser('add', help='Check and add new script to scripts list')
        add_parser.add_argument('script_path', metavar='PATH', type=str, help='Path to script file')
        
        argparser.add_argument('-v', '--verbose', action='store_true', help='Verbose mode (debug logs)')
        argparser.add_argument('-V', '--version', action='store_true', help='Get pyscript version and some other stuff')
        
        return argparser
    
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
            return 0
        
        if args.command == 'list':
            scripts = self.get_scripts()
            self.print_scripts(scripts)
            return 0
        
        if args.command == 'add':
            sys.path.append(os.path.dirname(args.script_path))
            script = self.parse_script(args.script_path)
            if script:
                self.move_script(args.script_path)
                return 0
            
            else:
                return 1
        
        logger.warning('Nothing to do! See --help')
        
def main() -> None | int: 
    app = PYScriptCLI()
    return app.run()

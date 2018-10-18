from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.contrib.completers import SystemCompleter

from pygments.lexers.python import Python3Lexer

while True:
    inp = prompt(u'>>>', history=FileHistory('/tmp/history.txt'), auto_suggest=AutoSuggestFromHistory())
    try:
        print(eval(inp))
    except Exception as e:
        print(e.with_traceback(e.__traceback__))

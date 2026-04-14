import sys
from parser import parse_output
from matcher import match_pattern
from formatter import format_hint

#Entry point (orchestrator)

# read the passed output in bugsquancher.zsh
    # sys.argv --> metadata (command is sys.argv[1], exit code is sys.argv[2])
    # sys.stdin --> actual error output sys.stdin.read()
    #
    # Explantion: passes values as positional arguments
    # python3 "$APP_PATH" "$LAST_COMMAND" "$EXIT_CODE"
    # sys.argv[0] = "main.py"
    # sys.argv[1] = LAST_COMMAND
    # sys.argv[2] = EXIT_CODE

command = sys.argv[1]
exit_code = sys.argv[2]
output = sys.stdin.read()

# call the parser  (to clean and extract useful info from the raw output)
parsed = parse_output (output)
# call the matcher
pattern = match_pattern (parsed)
# call the formatter
hint = format_hint(command, exit_code, pattern)
# print final result
if hint:
    print(hint)

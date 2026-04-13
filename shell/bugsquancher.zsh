# Capture Output of terminal (commands, output and exit status) detect failure and pass data to Python

# create a temporary file to capture output
OUTPUT_FILE=$(mktemp)

# DEBUG trap redirect terminal output to file (stderr and stdout)
trap 'exec > >(tee -a "$OUTPUT_FILE") 2>&1' DEBUG

# hook into zsh lifecycle

  # detect failed command
  preexec() {
    LAST_COMMAND="$1" # $1 is the command about to be executed
    # clear output file for new command (Without clearing, the file would accumulate output from all previous commands in the session, not just the current one. using > in shell scripting.)
    > "$OUTPUT_FILE"
  }
  # capture output
  precmd() {
    EXIT_CODE=$?
    if ((EXIT_CODE >0)); then
      # read the captured outpur from the file
      OUTPUT=$(<"$OUTPUT_FILE")
      # call python with variables (command, exit code and output)
      python3 /path/to/bugsquancher.py "$LAST_COMMAND" "$EXIT_CODE" "$OUTPUT"
      fi
  }

  # cleanup on exit
  trap 'rm -f "$OUTPUT_FILE"' EXIT


# print appended output

# Capture Output of terminal (commands, output and exit status) detect failure and pass data to Python

# Script director and app path
SCRIPT_DIR=${${(%):-%x}:A:h}
APP_PATH="$SCRIPT_DIR/../bugsquancher/main.py"

# create a temporary file to capture output
OUTPUT_FILE=$(mktemp)

# hook into zsh lifecycle
preexec() {
  # Save the command line and start capturing the command's output.
  LAST_COMMAND="${1:-${2:-$3}}"
  : > "$OUTPUT_FILE"
  exec {BUGSQUANCHER_STDOUT}>&1 {BUGSQUANCHER_STDERR}>&2
  exec > >(tee -a "$OUTPUT_FILE") 2>&1
}

precmd() {
  EXIT_CODE=$?

  # Restore the terminal before printing our formatted hint.
  if [[ -n ${BUGSQUANCHER_STDOUT:-} ]]; then
    exec >&$BUGSQUANCHER_STDOUT 2>&$BUGSQUANCHER_STDERR
    exec {BUGSQUANCHER_STDOUT}>&- {BUGSQUANCHER_STDERR}>&-
    unset BUGSQUANCHER_STDOUT BUGSQUANCHER_STDERR
  fi

  if (( EXIT_CODE > 0 )) && [[ -n ${LAST_COMMAND:-} ]]; then
    OUTPUT=$(<"$OUTPUT_FILE")
    printf '%s' "$OUTPUT" | python3 "$APP_PATH" "$LAST_COMMAND" "$EXIT_CODE"
  fi
}

# cleanup on exit
trap 'rm -f "$OUTPUT_FILE"' EXIT

import unicodedata
# pure funcitons for cleaning and extracting useful text
# remove noise
# normalize casing if needed
# strip irrelevant lines if needed
# return cleaned error text

# for testing purposes

# test_output = """ERRRrror: failed to push some refs to 'github.com:Hishamkhashman1/cli-helper.git'
# hint: Updates were rejected because the remote contains work that you do not
# hint: have locally. This is usually caused by another repository pushing to
# hint: the same ref. If you want to integrate the remote changes, use
# hint: 'git pull' before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# """

def parse_output(output):
    #Clean and normalize raw command output for downstream pattern matching.
    lines = output.splitlines()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        normalized_line = unicodedata.normalize('NFKC', line)
        casefolded_line = normalized_line.casefold()
        if line and not casefolded_line.startswith(("note:", "warning:","hint:")):
            cleaned_lines.append(casefolded_line)
    return "\n".join(cleaned_lines)


# print (f"Success: {parse_output(test_output)}")

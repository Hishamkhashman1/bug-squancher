# import unicodedata
# # pure funcitons for cleaning and extracting useful text
# # remove noise
# # normalize casing if needed
# # strip irrelevant lines if needed
# # return cleaned error text

# test_output = """
# Note: This is a warning message.
# Traceback (most recent call last):
#   File "/home/hisham/code/Hishamkhashman1/cli-helper/test.py", line 26, in <module>
#     print (parse_output(test_output))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/home/hisham/code/Hishamkhashman1/cli-helper/test.py", line 21, in parse_output
#     normalized_line = unicodedata.normalize('NLP', line)
#                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# """


# def parse_output(test_output):
#     #Clean and normalize raw command output for downstream pattern matching.
#     lines = test_output.splitlines()
#     cleaned_lines = []
#     for line in lines:
#         line = line.strip()
#         normalized_line = unicodedata.normalize('NFKC', line)
#         if line and not line.startswith("Note:"):
#             cleaned_lines.append(normalized_line)
#     return "\n".join(cleaned_lines)

# print(f"Success: {parse_output(test_output)}")

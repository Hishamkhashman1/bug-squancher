# pure logic that returns the best matching pattern

# compares it against known patterns
# for testing import test output
from parser import test_output
# load patterns

from patterns import PYTHON_PATTERN_SEEDS
# compare normalized text against keywords or regex

# return matched pattern or None

def match_pattern(cleaned_output):
    for pattern in PYTHON_PATTERN_SEEDS:
        #if error matches name return recommendation
        if pattern["name"] in cleaned_output:
            return pattern["recommended_command"]
    return None
print (f"🤓 How to squanch it (probably) --> {match_pattern(test_output)}")

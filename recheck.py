# import re
#
# example_data = """
# this line will not match
# abc 1 xyz 0
# this line will not match
# abc 2 xyz 1
# abc 2 xyz 2 will not match xyzxyz
# abc 3 xyz 2
# """
# s_pattern = "xyz"
#
# print type(example_data)
# pat = re.compile(s_pattern)
# # note that you can pre-compile the single pattern
# # you cannot do that with the dynamic patterns
# print type(pat)
# for match_group in re.finditer(pat, example_data):
#     print match_group.group()
#     # n1 = int(match_group.group(1))
#     # n2 = int(match_group.group(2))
#     # if n1 > 0 and n1 == n2 + 1:
#     #     print match_group.group(0)

import re

example_data = """
this line will not match
abc 1 xyz 0
this line will not match
abc 2 xyz 1
abc 2 xyz 2 will not match
abc 3 xyz 2
"""

pattern = "xyz"
match_group = re.search(pattern, example_data)
if match_group:
    print match_group.group()
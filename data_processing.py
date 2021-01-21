import pandas as pd


def list_diff(list1: list, list2: list, type: str = "all") -> list:
    if type == "left":
        left = list(set(list1) - set(list2))
        return left
    if type == "right":
        right = list(set(list2) - set(list1))
        return right
    if type == "all":
        left = list(set(list1) - set(list2))
        right = list(set(list2) - set(list1))
        all = left + right
        return all


assert list_diff([0, 1], [1, 2]) == [0, 2]

un = pd.read_csv("unanimous.csv")
nonun = pd.read_csv("non_unanimous.csv")

assert len(un.columns) == len(nonun.columns)
assert len(list_diff(list(un.columns), list(nonun.columns))) == 0

df = un.append(nonun)
assert df.shape[0] == un.shape[0] + nonun.shape[0]

df.to_csv("judgments.csv")

# 1. Appointing authority
# 2. Parent High Court
# 3. Professional Background in Subordinate Judiciary
# 4. Bar/No Bar

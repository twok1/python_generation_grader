from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data[key] = value
        self.data[value] = key


# twowaydict = TwoWayDict({'apple': 1})

# twowaydict['banana'] = 2

# print(twowaydict['apple'])
# print(twowaydict[1])
# print(twowaydict['banana'])
# print(twowaydict[2])
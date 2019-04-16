class LabeledList():
    def __init__(self, data = None, index = None):
        self.values = data
        self.index = index

    def __str__(self):
        return format("str(self.values)", ">20s") + str(self.index)

    def __getitem__(self,item):
        empty_list = []
        print(self.index)
        for a in item:
            if a in self.index:
                for index in self.index:
                    if index == a:
                        index_val = item.index(a)
                        empty_list.append(self.values[index_val])
        return empty_list
    
    def __setitem__(self, key, value):
        if self.index == key:
            self.values = value
        return self



class DictsSort:
    def __init__(self, arr):
        self.arr = arr

    def add(self, data):
        self.arr.append(data)

    def sort_by_value(self, key):
        return sorted(self.arr, key=lambda x: x[key])
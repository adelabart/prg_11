class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade (self, index_studenta):
        s = self.get_by_index(index_studenta)
        if s <= 49:
            str = "F"
            return str
        elif 50 <= s < 60:
            str = "E"
            return str
        elif 60 <= s < 70:
            str = "D"
            return str
        elif 70<= s < 80:
            str = "C"
            return str
        elif 80 <= s < 90:
            str = "B"
            return str
        else:
            str = "A"
            return str

    def find (self, points):
        skore = self.scores
        indexy = []
        for s in skore:
            if s == points:
                index = skore.index(s)
                indexy.append(index)
        return indexy

    def get_sorted (self):
        new_values = self.scores.copy()
        n = len(new_values)
        for val in range(n - 1):
            for v in range(n - val - 1):
                if new_values[v] > new_values[v + 1]:
                    new_values[v], new_values[v + 1] = new_values[v + 1], new_values[v]
        return new_values








results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
print (results.scores)
print (results.get_grade(2))
print (results.find (42))
print (results.get_sorted ())


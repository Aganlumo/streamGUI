class Video:
    def __init__(self, name, gender, score, length, date):
        self.name = name
        self.gender = gender
        self.score = score
        self.length = length
        self.date = date

    def setName(self, name):
        name

class Serie(Video):
    def __init__(self, name, gender, score, length, date):
        Video.__init__(self, name, gender, score, length, date)


class Movie(Video):
    def __init__(self, name, gender, score, length, date):
        super().__init__(name, gender, score, length, date)

class PollitosEnFuga(Movie):
    def __init__(self):
        super().__init__('Pollitos En Fuga', 'Suspenso Animado', 'Cinco Polliestrellas', 120, 2000)

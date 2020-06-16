class Video:
    def __init__(self, name, gender, score, length, date):
        self.name = name
        self.gender = gender
        self.score = score
        self.length = length
        self.date = date

    # def setName(self, Newname):
    #     self.name=Newname

class Movie(Video):
    def __init__(self, name, gender, score, length, date):
        super().__init__(name, gender, score, length, date)

class Serie(Video):
    def __init__(self, name, gender, score, temporada, date,length,numEpisode,nombreEpisodio):
        super().__init__(nombreEpisodio, gender, score, length, date)
        self.numEpisode=numEpisode
        self.nameS = name
        self.temporada = temporada
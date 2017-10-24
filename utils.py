from csv import reader

file = 'kittens.in'
with open(file, newline='') as f:
    content = reader(f, delimiter=' ')
    content = [[int(number) for number in line] for line in content]


V, E, R, C, X = content[0]
videos = [size for size in content[1]]


class Videos:
    def __init__(self, content):
        self.tab = content[1]


class Endpoints:
    def __init__(self, content, E):
        self.caches = []
        self.datac = []
        self.curline = 2
        for endpoint in range(E):
            self.datac.append(content[self.curline][0])
            nei = content[self.curline][1]
            self.caches.append(content[self.curline+1:self.curline+1+nei])
            self.curline += nei+1

    # def get_caches_lat(self):
    #     dico = {}
    #     for j in range(len(self.caches)):
    #         dico[j] = self.caches[j][1]
    #     return dico

    def get_caches_dic(self):
        dico = {}
        for j in range(len(self.caches)):
            dico[j] = self.caches[j]
        return dico

    def get_datac(self):
        dico = {}
        for j in range(len(self.datac)):
            dico[j] = self.datac[j]
        return dico


class Requests:
    def __init__(self, content, E, R, V, current_line):
        self.mat = [[None for i in range(V)] for j in range(E)]
        self.E = E
        self.V = V
        curline = current_line
        for request in range(R):
            vid, endpoint, nb = content[curline]
            self.mat[endpoint][vid] = nb
            curline += 1

    def get_video_dic(self):
        dico = {}
        for endpoint in range(self.E):
            li = []
            for vid in range(self.V):
                if self.mat[endpoint][vid] is not None:
                    li.append(vid)
            dico[endpoint] = li
        return dico


vid = Videos(content)
a = Endpoints(content, E)
current_line = a.curline
b = Requests(content, E, R, V, current_line)
dataCenterLatence = a.get_datac() # indexé par ... latence avec data center
cacheDic = a.get_caches_dic() # liste des doublets [cache ID, latence]
weightVideoDic = vid.tab
request = b.mat
videoDic = b.get_video_dic()

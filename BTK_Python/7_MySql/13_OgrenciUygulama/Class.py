class Class:
    def __init__(self,id, name, teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def CreateClass(results):
        classList = []
        for row in results:
            classObj = Class(row[0], row[1], row[2])
            classList.append(classObj)
        return classList
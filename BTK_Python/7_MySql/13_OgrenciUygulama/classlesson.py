class ClassLesson:
    def __init__(self,classid, lessonid, teacherid):
        if classid is None:
            self.classid = 0
        else:
            self.classid = classid
        self.lessonid = lessonid
        self.teacherid = teacherid

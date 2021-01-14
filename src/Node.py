class Node:
    key = int()
    info = str()
    tag = int()
    weight = float()
    pos = str()

    def __init__(self, key: int, info=None, tag=None, weight=None, pos=None):
        self.key = int(key)
        self.info = "" if info is None else str(info)
        self.tag = 0 if tag is None else int(tag)
        self.weight = 0 if tag is None else float(weight)
        self.pos = "" if pos is None else self.createPos(pos)

    def createPos(self, pos: tuple):
        string = "{},{},{}".format(pos[0], pos[1], pos[2])
        return string

    def getKey(self) -> int:
        return self.key


    def getPosAsString(self) -> str:
        return self.pos

    def getPos(self) -> tuple:
        if self.pos == "":
            tuple = ()
            return tuple
        else:
            arr = self.pos.split(",")
            my_tuple = (float(arr[0]), float(arr[1]), float(arr[2]))
            return my_tuple

    def getInfo(self) -> str:
        return self.info

    def getWeight(self) -> float:
        return self.weight

    def getTag(self) -> int:
        return self.tag

    def setInfo(self, info: str):
        self.info = info

    def setWeight(self, weight: float):
        self.weight = weight

    def setPos(self, pos: tuple):
        self.pos = self.createPos(pos)

    def setTag(self, tag: int):
        self.tag = tag
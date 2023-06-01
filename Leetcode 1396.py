class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # id -> (startStation, item)
        self.totalMap = {} # (start, end) -> [totalTime, count]

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        start, time = self.checkInMap[id]
        route = (start, endStation)
        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[route][0] += t - time
        self.totalMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
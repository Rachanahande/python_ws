class Car:
    def __init__(self,regno,nogears):
        self.regno = regno
        self.nogears = nogears
        self.is_started = False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print(f"{self.regno} already started...")
        else:
            print(f"{self.regno} started...")
            self.is_started = True
    def stop(self):
        if self.is_started:
            print(f"{self.regno} stopped...")
            self.is_started = False
        else:
            print(f"{self.regno} already stopped...")
    def change_gear(self):
        if self.is_started:
            if self.c_gear < self.nogears :
                self.c_gear += 1
                print(f"{self.regno} changed gear...{self.c_gear}")
            else:
                print(f"{self.regno} car already in top gear...{self.c_gear}")
        else:
            print(f"{self.regno} stopped...you cannot change the gear")
    def showInfo(self):
        print(f"car with regno{self.regno}")

class TheThreeBodies:

    def __init__(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

    def get_plotting_data(self, start=0, stop=None):
        return self.part_of(start, stop)

    def max_axis(self, start=0, stop=None):
        return max(self.b1.r[start, stop].max(),
                   self.b2.r[start, stop].max(),
                   self.b3.r[start, stop].max(),
                   2)

    def part_of(self, start=0, end=None):
        r1_part = self.b1.r[start:end]
        r2_part = self.b2.r[start:end]
        r3_part = self.b3.r[start:end]

        return r1_part, r2_part, r3_part
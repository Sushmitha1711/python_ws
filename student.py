class student:

    def __init__(self,name):
        self.name=name
        self.scores=[]
    
    def avgerage(self):
        return sum(self.scores)/len(self.scores)

stu_1=student("sushmitha")
stu_1.scores.extend([55,56,65])
print(f"{stu_1.avgerage():.2f}")

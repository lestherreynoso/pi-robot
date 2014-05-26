import random
average = 0
count = 0

def runningSum(avg,new):
        global count
        count+=1
        avg-=avg/count
        avg+=new/count

        return avg


average = runningSum(average,new)



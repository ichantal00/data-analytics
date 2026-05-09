candy = ("jolly ranchers", "blobs", "skittles")
flavors = ("strawberry", "berry", "orange")

# the count starts at 0... so strawberry is "0" berry is "1" and orange is "2"...
# in negatives orange is "-1" berry is "-2" and strawbwerry is "-3"...

candy1 = (candy[0], flavors[2])
candy2 = (candy[0], flavors[1])
candy3 = (candy[2], flavors[0])
candy4 = (candy[1], flavors[2])

set = [candy1, candy2, candy3, candy4]

print (f"Today's candy options include: {set} ")

#The order did not change no matter how much i reprint
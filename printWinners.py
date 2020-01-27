def printWinningCandidates(lst):
	if len(lst) == 0:
		return False
	if len(lst) == 1:
		return("the winner is " + lst[0] + "!\n")
	if len(lst) == 2:
		return("the winners are " +  lst[0] + " and " + lst[1] + "!\n")
	else:
		string = ""
		for i in lst[:-1]:
			string += i + ", "
		string += "and " + lst[-1] + "!\n"
		return("the winners are " + string)

def printSPO(lst):
	return False
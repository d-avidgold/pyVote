

def majorityRule(population, candidates):

	return (quota(population, candidates, len(population) / 2))


def minorityRule(population, candidates):

	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	for voter in population:
		vote = population[voter]
		if vote in candidates:
			tally[vote] += 1

	maxsf = len(population)
	for cand in tally:
		if tally[cand] < maxsf:
			maxsf = tally[cand]
			succ = [cand]
		elif tally[cand] == maxsf:
			succ.append(cand)

	if len(succ) == 1:
		print("Under minority rule, the winner is " + succ[0] + "! \n")
		return True

	if len(succ) == 2:
		print("Under minority rule, the winners are " + succ[0] + " and " + succ[1] + "! \n")
		return True

	string = ""
	for i in succ[:-1]:
		string += i + ", "
	string += "and " + succ[-1] + "! \n"
	print("Under minority rule, the winners are " + string)
	return True

def dictatorship(population, candidates, dictator):

	if dictator in population:
		print("With " + dictator + " as dictator, the winner is: " +  population[str(dictator)] + "!\n")
		return True

	else:
		print("Dictator did not vote! Error!! \n")
		return False

def monarchy(population, candidates, mon):

	if mon in candidates:
		print("Clearly, with " + mon + " as monarch, " + mon + " takes the crown! \n")

	else:
		print("Monarch " + mon + " did not run! Error!! \n")
		return False

def quota(population, candidates, quot):

	if type(quot) != int:
		print("Bad quota! \n")
		return False
	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	for voter in population:
		vote = population[voter]
		if vote in candidates:
			tally[vote] += 1

	for cand in tally:
		if tally[cand] >= quot:
			succ.append(cand)

	if not succ:
		print("No candidate met the quota of " + str(quot) + " :( \n")
		return False

	if len(succ) == 1:
		print(succ[0] + " met the quota of " + str(quot) + "! \n")
		return True

	if len(succ) == 2:
		print("All of " + succ[0] + " and " + succ[1] + " met the quota of " + str(quot) + "! \n")
		return True

	string = ""
	for i in succ[:-1]:
		string += i + ", "
	string += "and " + succ[-1]
	print("All of " + string + " met the quota of " + str(quot) + "! \n")
	return True

def plurality(population, candidates):

	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	for voter in population:
		vote = population[voter]
		if vote in candidates:
			tally[vote] += 1

	maxsf = 0
	for cand in tally:
		if tally[cand] > maxsf:
			maxsf = tally[cand]
			succ = [cand]
		elif tally[cand] == maxsf:
			succ.append(cand)

	if len(succ) == 1:
		print("Winner under plurality is " + succ[0] + "! \n")
		return True

	if len(succ) == 2:
		print("The winners under plurality are " + succ[0] + " and " + succ[1] + "! \n")
		return True

	string = ""
	for i in succ[:-1]:
		string += i + ", "
	string += "and " + succ[-1] + "! \n"
	print("The winners under plurality are " + string)
	return True

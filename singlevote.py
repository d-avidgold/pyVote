

def majorityRule(population, candidates):

	votes = {}
	for cand in candidates:
		votes[cand] = 0
	for voter in population:
		votes[population[voter]] += 1
		if votes[population[voter]] > len(population) / 2:
			print("Under majority rule, the winner is: " + population[voter]+ "!\n")
			return True
	print("There is no clear majority winner... \n")
	return False




def minorityRule(population, candidates):

	return "A"

def dictatorship(population, candidates, dictator):

	if dictator in population:
		print("With " + dictator + " as dictator, the winner is: " +  population[str(dictator)] + "!\n")
		return True
	else:
		print("Dictator did not vote! Error \n")
		return False

def monarchy(population, candidates, mon):

	return mon

def quota(population, candidates, quot):

	return "A"

def plurality(population, candidates):

	return "A"
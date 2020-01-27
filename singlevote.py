from printWinners import printWinningCandidates
def boldify(text):
	return '\033[1m' + text + '\033[0m'

def majorityRule(population, candidates, typ):

	size = 0
	for vote in population:
		size += population[vote]
	return (quota(population, candidates, size / 2, typ))


def minorityRule(population, candidates, typ):

	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	if typ == "BALLOTS":
		for voter in population:
			vote = population[voter]
			if vote in candidates:
				tally[vote] += 1

	elif typ == "SCHEDULE":
		for vote in population:
			noVoters = population[vote]
			if vote in candidates:
				tally[vote] += noVoters


	maxsf = len(population)
	for cand in tally:
		if tally[cand] < maxsf:
			maxsf = tally[cand]
			succ = [cand]
		elif tally[cand] == maxsf:
			succ.append(cand)

	return(printWinningCandidates(succ))

def dictatorship(population, candidates, dictator, typ):

	if typ == "SCHEDULE":
		print("Must provide ballots for dictatorship voting!")
		return False

	if dictator in population:
		return(printWinningCandidates([population[str(dictator)]]))

	else:
		print("Dictator did not vote! Error!! \n")
		return False

def monarchy(population, candidates, mon, typ):

	if mon in candidates:
		return(printWinningCandidates([mon]))

	else:
		print("Monarch " + mon + " did not run! Error!! \n")
		return False

def quota(population, candidates, quot, typ):

	if type(quot) != int:
		print("Bad quota! \n")
		return False
	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	if typ == "BALLOTS":
		for voter in population:
			vote = population[voter]
			if vote in candidates:
				tally[vote] += 1

	elif typ == "SCHEDULE":
		for vote in population:
			noVoters = population[vote]
			if vote in candidates:
				tally[vote] += noVoters

	for cand in tally:
		if tally[cand] >= quot:
			succ.append(cand)

	return(printWinningCandidates(succ))

def plurality(population, candidates, typ):

	succ = []
	tally = {}

	for cand in candidates:
		tally[cand] = 0

	if typ == "BALLOTS":
		for voter in population:
			vote = population[voter]
			if vote in candidates:
				tally[vote] += 1

	elif typ == "SCHEDULE":
		for vote in population:
			noVoters = population[vote]
			if vote in candidates:
				tally[vote] += noVoters

	maxsf = 0
	for cand in tally:
		if tally[cand] > maxsf:
			maxsf = tally[cand]
			succ = [cand]
		elif tally[cand] == maxsf:
			succ.append(cand)

	return(printWinningCandidates(succ))

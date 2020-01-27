def bordaCount(population, candidates, typ):

	tallies = {}
	for i in candidates:
		tallies[i] = 0

	if typ == "BALLOTS":
		for voter in population:
			points = len(candidates) - 1
			for cand in population[voter]:
				tallies[cand] += points
				points -= 1


	elif typ == "SCHEDULE":
		for order in population:
			noVoters = population[order]
			lst = order.split(" > ")
			print(lst)
			points = len(candidates) - 1
			for cand in lst:
				tallies[cand] += noVoters * points
				points -= 1

	else:
		print("Error in ballots... Halting...")
		return False

	maxsf = 0
	succ = []
	for cand in tallies:
		if tallies[cand] > maxsf:
			maxsf = tallies[cand]
			succ = [cand]
		elif tallies[cand] == maxsf:
			succ.append(cand)
	print(succ)
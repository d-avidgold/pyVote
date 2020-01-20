from parse import formatCheck, singleParse, rankParse, approvalParse
from singlevote import majorityRule, minorityRule, dictatorship, monarchy, quota, plurality
#from rankedvote import bordaCount

import sys

i = 1
l = len(sys.argv)

funcs = {"singlevote": singleParse, "rankedvote": rankParse, "approvalvote": approvalParse}

while i < l:

	# Check that the next argument is a file with a proper 'type'

	factors = formatCheck(sys.argv[i])

	if not factors or not factors["TYPE"] or factors["TYPE"] not in funcs:
		print("Bad file! " + sys.argv[i] + " does not exist. Halting... \n")
		i = l
		break

	print("\nReading file: " + factors["NAME"] + "\n")
	print("Note comments: " + factors["COMMENTS"] + "\n")

	# Get candidates and ballots from file

	a = funcs[factors["TYPE"]](sys.argv[i])

	if a: 
		[population, candidates] = a
		i += 1

	else:
		print("Error")
		break

	# Then, read flags and apply until next file appears

	if factors["TYPE"] == "singlevote":
		while i < l and (sys.argv[i])[0] == "-":

			if sys.argv[i] == "-maj":
				majorityRule(population, candidates)
				i += 1

			elif sys.argv[i] == "-min":
				minorityRule(population, candidates)
				i += 1

			elif sys.argv[i] == "-dict":
				i += 1
				dictator = sys.argv[i]
				i += 1
				dictatorship(population, candidates, dictator)

			elif sys.argv[i] == "-mon":
				i += 1
				kq = sys.argv[i]
				i += 1
				monarchy(population, candidates, kq)

			elif sys.argv[i] == "-quota":
				i += 1
				quot = int(sys.argv[i])
				i += 1
				quota(population, candidates, quot)

			elif sys.argv[i] == "-plur":
				i += 1
				plurality(population, candidates)

			else:
				print("Bad flag! Halting...")
				i = l
				break

	"""elif type == "rankedvote":

		while i < l and (sys.argv[i])[0] == "-":

			if sys.argv[i] == "borda":
				bordaCount(population, candidates)
				i += 1

			elif"""




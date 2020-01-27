from parse import formatCheck, parseFile
from singlevote import majorityRule, minorityRule, dictatorship, monarchy, quota, plurality
from rankedvote import bordaCount
import sys

i = 1
l = len(sys.argv)

def boldify(text):
	return '\033[1m' + text + '\033[0m'

while i < l:

	# Check that the next argument is a file with a proper 'type'

	factors = formatCheck(sys.argv[i])

	if not factors or not factors["TYPE"] or factors["TYPE"] not in ["singlevote", "rankedvote", "approvalvote"]:
		print("Bad file! " + sys.argv[i] + " does not exist. Halting... \n")
		i = l
		break

	print(boldify("\nReading file: ") + factors["NAME"] + "\n")
	print(boldify("Note comments: ") + factors["COMMENTS"] + "\n")

	# Get candidates and ballots from file

	a = parseFile(sys.argv[i], factors["TYPE"])

	if a: 
		[population, candidates, typ] = a
		i += 1

	else:
		print("Error")
		break

	# Then, read flags and apply until next file appears

	if factors["TYPE"] == "singlevote":
		while i < l and (sys.argv[i])[0] == "-":

			if sys.argv[i] == "-maj":
				strin = majorityRule(population, candidates, typ)
				if not strin:
					print("Under Majority rule, there is no winner...\n")
				else:
					print("Under Majority rule, " + strin)
				i += 1

			elif sys.argv[i] == "-min":
				strin = minorityRule(population, candidates, typ)
				if not strin:
					print("Under Minority rule, there is no winner...\n")
				else:
					print("Under Minority rule, " + strin)
				i += 1

			elif sys.argv[i] == "-dict":
				i += 1
				dictator = sys.argv[i]
				i += 1
				strin = dictatorship(population, candidates, dictator, typ)
				if strin:
					print("With " + dictator + " as dictator, " + strin)

			elif sys.argv[i] == "-mon":
				i += 1
				kq = sys.argv[i]
				i += 1
				strin = monarchy(population, candidates, kq, typ)
				print("With " + kq + " as monarch, " + strin)

			elif sys.argv[i] == "-quota":
				i += 1
				quot = sys.argv[i]
				try:
					quot = int(quot)
				except:
					quot = 'a'
				i += 1
				strin = quota(population, candidates, quot, typ)
				if not strin:
					print("No candidates met the quota of " + str(quot) + "...\n")
				else:
					print("With quota = " + str(quot) + ", " + strin)

			elif sys.argv[i] == "-plur":
				i += 1
				strin = plurality(population, candidates, typ)
				if not strin:
					print("No candidate won a plurality...\n")
				else:
					print("Under plurality, " + strin)

			else:
				print("Bad flag! Halting...")
				i = l
				break

	elif factors["TYPE"] == "rankedvote":

		print(population)

		if sys.argv[i] == "-bord":
			bordaCount(population, candidates, typ)
			i += 1

		break




print '\033[0m'
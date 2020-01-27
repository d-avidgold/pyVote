
def getBallot(rhs, flag):
	if flag == "singlevote":
		return rhs[0]
	if flag == "rankedvote":
		return rhs.split(' > ')
	if flag == "approvalvote":
		return rhs.split(", ")

def formatCheck(file):
	try:
		fid = open(file, "r")
	except:
		return False

	factors = {"NAME": file, "TYPE": False, "COMMENTS": "N/A"}
	line = fid.readline()

	while line:

		line = line.strip()

		if line[0] == "<" and line[-1] == ">":
			factor = line[1:-1]
			line = fid.readline()

			if factor in factors:
				factors[factor] = line.strip()
			line = fid.readline()

		else: line = fid.readline()

	return factors

	fid.close()

def parseFile(file, flag):
	fid = open(file, "r")
	importantFactors = ["SIZE", "CANDIDATES", "VOTERS", "BALLOTS", "SCHEDULE"]
	noCand = 0
	noVoters = 0
	CANDIDATES = []
	VOTERS = {}

	line = fid.readline()

	while line:

		if line[0] == "<" and line[-1] == ">":
			factor = line[1:-1]

			if factor not in importantFactors:
				line = fid.readline()

			else:
				line = (fid.readline()).strip()
				if factor == "CANDIDATES":
					CANDIDATES = line.split(", ")
				if factor == "VOTERS":
					for i in line.split(", "):
						VOTERS[i] = ""
				if factor == "SIZE":
					[noCand, noVoters] == line.split("x")
					noCand = int(noCand)
					noVoters = int(noVoters)
				if factor == "BALLOTS":

					while line:
						[lhs, rhs] = line.split(": ")
						voters = lhs.split(", ")
						cand = getBallot(rhs, flag)
						for i in voters:
							if i not in VOTERS or VOTERS[i]:
								print("Ballot error! Halting... ")
								return False
							else:
								VOTERS[i] = cand
						line = (fid.readline()).strip()

					bors = "BALLOTS"

				if factor == "SCHEDULE":
					while line:
						[lhs, rhs] = line.split(": ")
						voters = int(lhs)
						cand = rhs
						if cand in VOTERS:
							VOTERS[cand] += voters
						else:
							VOTERS[cand] = voters
						line = (fid.readline()).strip()

					bors = "SCHEDULE"

		line = (fid.readline()).strip()

	return [VOTERS, CANDIDATES, bors]


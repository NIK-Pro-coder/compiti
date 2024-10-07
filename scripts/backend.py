import sys
import requests

API_KEY  = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImM3MzdlMDQxLWUxNjYtNGU3ZS04YzcyLWNkZWFhYmM3Mzc3NSIsImlhdCI6MTcyNjg1MjY1Mywic3ViIjoiZGV2ZWxvcGVyL2U4NjJiYzNmLTRmMDctMDJlMi05MmQ5LTk0OTNjZjMxZjFlYyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOTMuNDUuODMuNDAiXSwidHlwZSI6ImNsaWVudCJ9XX0.YJ6t5XoBPQFm_ArKQ5XuJ8ArYwmv8QbCoMOBpWim60reJWI525sTdJCFvzlKKrfcK743AG3XYpoDyZG7pqYcqQ"
HEAD = {
	"Authorization" : f"Bearer {API_KEY}"
}

commands = {}

def addEntry(func) :
	name = func.__name__
	commands[name] = func
	return func

@addEntry
def getPlayer(tag) :
	url = f"https://api.brawlstars.com/v1/players/%23{tag.strip('#')}"
	r = requests.get(url, headers=HEAD)

	print(r.text)

#test club : #29GPQVJCR
@addEntry
def getClub(tag) :
	url = f"https://api.brawlstars.com/v1/clubs/%23{tag.strip('#')}/members"
	r = requests.get(url, headers=HEAD)

	print(r.text)

if __name__=="__main__" :
	cmd = sys.argv[1]
	inputs = sys.argv[2:]

	commands[cmd](*inputs)

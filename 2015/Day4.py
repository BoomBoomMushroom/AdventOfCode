import hashlib
inputData = "ckczppom"

start = "000000" # 6 zeros to start
currentHash = ""
nonce = 0

while currentHash.startswith(start) == False:
    nonce += 1
    stringToConvert = inputData+str(nonce)
    currentHash = hashlib.md5( stringToConvert.encode("utf-8") ).hexdigest()

print("Found nonce: "+str(nonce))
print("That nonce creates the hash: "+currentHash)
import json

print("Tx hash\t\t\t\t\t\t\t\t\tfrom\t\t\t\t\t\tto\t\t\t\t\t\tAmount transfer")

sum = 0
arr = []
target = "0xeca19b1a87442b0c25801b809bf567a6ca87b1da";

with open('info.txt') as json_file:
    data = json.load(json_file)
    for p in data['result']:
    	if p['tokenSymbol'] == "BKTC" and p['from'] == target:
        	print(p['hash'] + "\t" + p['from'] + "\t" + p['to'] + "\t" + p['value'])
        	arr.append(p['to'])
        	sum -= int(p['value'])
        elif p['tokenSymbol'] == "BKTC" and p['to'] == target:
        	print(p['hash'] + "\t" + p['from'] + "\t" + p['to'] + "\t" + p['value'])
        	arr.append(p['from'])
        	sum += int(p['value'])
print("Sum: " + str(sum))

def walletSum(hash):
	wallSum = 0
	with open('info.txt') as json_file:
	    data = json.load(json_file)
	    for p in data['result']:
	    	if p['tokenSymbol'] == "BKTC" and p['from'] == hash:
	        	arr.append(p['to'])
	        	wallSum -= int(p['value'])
	        elif p['tokenSymbol'] == "BKTC" and p['to'] == hash:
	        	wallSum += int(p['value'])
	return wallSum

print("\n\nAddress\t\t\t\t\t\tBalance")
for i in arr:
	print(i + "\t" + str(walletSum(i)))



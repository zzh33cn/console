import os,sys
import json
import subprocess

def clearScreen():
	f_handler=open('out.log','w')
	oldstdout=sys.stdout
	sys.stdout=f_handler 
	os.system('clear')
	sys.stdout=oldstdout 

def inputWrap():
	promote="[chain33] >>> "
	if sys.version_info.major == 3:
		return input(promote)
	else: 
		return raw_input(promote)

def execCmd(cmd):
	#return subprocess.getstatusoutput(cmd)
	info = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	error=info.stderr.read().decode("utf-8")
	ret=0
	if len(error) > 0:
		ret = 1
		return (ret, error)
	return (ret, info.stdout.read().decode("utf-8"))

def readRPCAddr(fileName):
    file = open(fileName)
    while True:
        line = file.readline()
        #print(line)
        if not line:
            return ''

        if line.find('jrpcBindAddr') == 0:
            addrItem = line.split('=')
            #print(addrItem[0])
            #print(addrItem[1])
            return addrItem[1]

config='chain33.toml'

if len(sys.argv) >= 2:
    cfg=sys.argv[1]

print('use configure file: ' + config)

if os.path.exists(config):
    addr=readRPCAddr(config)
    print(config + ' is exist,read json rpc address: ' + addr)
else:
    addr='127.0.0.1:8801'
    print(config  + ' is not exist,use default json rpc address: ' + addr)

rpcUrl='http://'+ addr

cli='./chain33-cli '
if sys.platform == 'win32':
	cli='.\chain33-cli '

cmd_prefix = cli + rpcUrl + ' '

commands = [	
		'clear',
        'setJrpcAddr',
		'raw',	
		'seedGenerate',
		'seedSave',
		'seedGenerateAndSave',
		'version',
		'net',
		'accountList', 
		'accountBalance', 
		'accountCreate', 
		'accountSetlabel', 
		'accountDumpkey',
		'accountImportkey',
		'queryTx', 
		'walletStatus', 
		'walletUnlock', 
		'walletLock',
		'walletSetfee',
		'walletSetpwd',
		'walletAutomine',
		'walletMerge',
		'totalCoins',
		'transferCoin',
		'sendCoinsTransfer',
		'evmDeploy',
		'evmInfo',
		'evmAbiCall',
	    ]
history = []

while True:
	user_input=inputWrap()

	if len(user_input) == 0:
		continue
		
	existInHis = False
	for x in history:
		if x == user_input:
			existInHis = True
			break

	if existInHis:
		pass
	else:
		history.append(user_input)

	user_input = user_input.split()

	cmd=user_input[0]

	if cmd=='clear':
		if sys.platform == 'win32':
			os.system("cls")
			continue
		clearScreen()
	
	if cmd=='setJrpcAddr':
		if len(user_input) != 2:
			print("command usage: setJrpcAddr ip:port")
			continue
		
		cmd_prefix = cli + 'http://' + user_input[1] + ' '
		print('current command prefix is:' + cmd_prefix)
    
	elif cmd=='raw':
		user_input = user_input[1:]
		chain33_cmd = cmd_prefix
		for x in user_input:
			chain33_cmd = chain33_cmd + x + ' '
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)
			print(result)

	elif cmd=='':
		continue

	elif cmd=='quit':
		break

	elif cmd=='help':
		for x in commands:
			print(x)

	elif cmd=='history':
		for x in history:
			print(x)	

	elif cmd=='version':
		chain33_cmd = cmd_prefix + 'version'
		(status, result) = execCmd(chain33_cmd)
		if status == 0 :
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)
	
	elif cmd=='net':
		if len(user_input) != 2:
			print("command usage: net fault|info|time|is_clock_sync|is_sync|peer")
			continue
		chain33_cmd = cmd_prefix
		for x in user_input:
			chain33_cmd = chain33_cmd + x + ' '
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)

	elif cmd=='seedGenerate':
		if len(user_input) != 2:
			print("command usage: seedGenerate 0(english)|1(chinese)")
			continue
		chain33_cmd = cmd_prefix + 'seed generate -l ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		print(result)

	elif cmd=='seedSave':
		if len(user_input) < 3:
			print("command usage: seedSave pwd seed")
			continue
		chain33_cmd = cmd_prefix + 'seed save -p ' + user_input[1] + ' -s '
		user_input = user_input[2:]
		for x in user_input:
			chain33_cmd = chain33_cmd + x + ' '
		(status, result) = execCmd(chain33_cmd)
		print(result)
	
	elif cmd=='seedGenerateAndSave':
		if len(user_input) < 3:
			print("command usage: seedGenerateAndSave 0(english)|1(chinese) pwd ")
			continue
		
		chain33_cmd = cmd_prefix + 'seed generate -l ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		print("generated seed:")
		print(result)
		print("please remember this seed, use it you can manage the wallet,it's very important!!!!!!")
		print("now save the seed with password: " + user_input[2])
		chain33_cmd = cmd_prefix + 'seed save -p ' + user_input[2] + ' -s "' + result + '"'
		(status, result) = execCmd(chain33_cmd)
		print(result)
		
	elif cmd=='accountList':
		chain33_cmd = cmd_prefix + 'account list'
		(status, result) = execCmd(chain33_cmd) 
		if status == 0 :
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)

	elif cmd=='accountBalance':
		if len(user_input) < 2:
			print("command usage: accountBalance address")
			continue
		chain33_cmd = cmd_prefix + 'account balance -a ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		if status == 0 :
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)
	elif cmd=='accountCreate':
		if len(user_input) < 2:
			print("commnad usage: accountCreate label")
			continue
		chain33_cmd = cmd_prefix + 'account create -l ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)

	elif cmd=='accountSetlabel':
		if len(user_input) < 3:
			print("command usage: accountSetlabel address label")
			continue
		chain33_cmd = cmd_prefix + 'account set_label -a ' + user_input[1] + ' -l ' + user_input[2]
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)
	elif cmd=='accountDumpkey':
		if len(user_input) < 2:
			print("command usage: accountDumpkey address")
			continue
		chain33_cmd = cmd_prefix + 'account dump_key -a ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)

	elif cmd=='accountImportkey':
		if len(user_input) < 3:
			print("command usage: accountImportkey privkey label")
			continue
		chain33_cmd = cmd_prefix + 'account import_key -k ' + user_input[1] + ' -l ' + user_input[2]
		(status, result) = execCmd(chain33_cmd)
		if status == 0:
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)

	elif cmd=='queryTx':
		if len(user_input) < 2:
			print("command usage: queryTx txid")
			continue
		chain33_cmd = cmd_prefix + 'tx query -s ' + user_input[1]
		(status, result) = execCmd(chain33_cmd)
		if status == 0 :
			print(result)
		else:
			print("execute command failed:" + chain33_cmd)
	
	elif cmd=='walletStatus':
		chain33_cmd = cmd_prefix + 'wallet status'
		(status, result) = execCmd(chain33_cmd)
		print(result)
	elif cmd=='walletUnlock':
		if len(user_input) < 2 :
			print("command usage: walletUnlock password [timeout]")
			continue

		chain33_cmd= cmd_prefix + 'wallet unlock -p ' + user_input[1]
		if len(user_input) == 3 :
			chain33_cmd=chain33_cmd + ' -t ' + user_input[2]
		(status,result)=execCmd(chain33_cmd)
		print(result)
	elif cmd=='walletLock':
		chain33_cmd= cmd_prefix + 'wallet lock'
		(status,result)=execCmd(chain33_cmd)
		print(result)

	elif cmd=='walletSetfee':
		if len(user_input) < 2 :
			print("command usage: walletSetfee fee")
			continue
		chain33_cmd= cmd_prefix + 'wallet set_fee -a ' + user_input[1]
		(status,result)=execCmd(chain33_cmd)
		print(result)

	elif cmd=='walletSetpwd':
		if len(user_input) < 3 :
			print("command usage: walletSetpwd newpwd oldpwd")
			continue
		chain33_cmd= cmd_prefix + 'wallet set_pwd -n ' + user_input[1] + ' -o ' + user_input[2]
		(status,result)=execCmd(chain33_cmd)
		print(result)

	elif cmd== 'walletAutomine':
		if len(user_input) < 2:
			print("command usage: walletAutomine on(1)|off(0)")
			continue

		chain33_cmd= cmd_prefix + 'wallet auto_mine -f ' + user_input[1]
		(status,result)=execCmd(chain33_cmd)
		print(result)

	elif cmd== 'walletMerge':
		if len(user_input) < 2:
			print("command usage: walletMerge address")
			continue

		chain33_cmd= cmd_prefix + 'wallet merge -t ' + user_input[1]
		(status,result)=execCmd(chain33_cmd)
		print(result)
	elif cmd=='totalCoins':
		chain33_cmd= cmd_prefix + 'stat total_coins'
		(status,result)=execCmd(chain33_cmd)
		print(result)
	elif cmd=='transferCoin':
		if len(user_input) < 4:
			print("command usage: transferCoin addr1 addr2 number [note]")
			continue
		addr1 = user_input[1]
		addr2 = user_input[2]
		coins = user_input[3]

		chain33_cmd= cmd_prefix + 'coins transfer -t ' + addr2 + ' -a ' + coins

		if len(user_input) >= 5:
			chain33_cmd = chain33_cmd + ' -n ' + user_input[4]

		(status, result)=execCmd(chain33_cmd)
		if status != 0:
			print("execute cmd failed:" + chain33_cmd)
			continue
		print("raw transaction:    " + result)
		chain33_cmd2 = cmd_prefix + 'wallet sign -a ' + addr1 + ' -d ' + result
		(status2, result2)=execCmd(chain33_cmd2)
		if status2 != 0:
			print("execute command failed:" + chain33_cmd2)
			continue
		print("signed transaction:    " + result2)
	
		chain33_cmd3 = cmd_prefix + 'wallet send -d ' + result2	
		(status3, result3)=execCmd(chain33_cmd3)
		if status3 != 0:
			print("execute command failed:" + chain33_cmd3)

		print("transaction id:    " + result3)
	elif cmd=='sendCoinsTransfer':
		if len(user_input) < 4:
			print("command usage: sendCoinsTransfer fromKey toAddr amount note")
			continue
		fromKey = user_input[1]
		toAddr = user_input[2]
		amount = user_input[3]

		chain33_cmd= cmd_prefix + 'send coins transfer -k ' + fromKey + ' -t ' + toAddr + ' -a ' + amount
		if len(user_input) == 5:
			chain33_cmd = chain33_cmd + ' -n ' + user_input[4]
		(status, result)=execCmd(chain33_cmd)
		print(result)
	elif cmd=='evmDeploy':
		chain33_cmd= cmd_prefix + 'evm'
		(status, result)=execCmd(chain33_cmd)
		if 'unknown command "evm"' in result:
			print("not support evm command")
			continue
		if len(user_input) < 4:
			print("command usage: evmDeploy contractFileName aliasName creatorAddr")
			continue
		
		if os.access(user_input[1], os.R_OK):
			print(user_input[1] + " is accessible to read")
		else:
			print(user_input[1] + " is not exist or not accessible to read")
			continue
			
		objName = user_input[2]
		if os.access(objName, os.R_OK):
			print(objName + " is exist,please change the name")
			continue
		
		creator = user_input[3]			
			
		file = open(user_input[1])
		content = file.read()
		file.close()
		contract = json.loads(content)
		code=contract["code"]
		alias=contract["alias"]
		abi=contract["abi"]
		set=contract["set"]
		get=contract["get"]
		
		chain33_cmd= cmd_prefix + 'evm create -i ' + code + ' -c ' + creator + ' -s ' + objName + ' -b "' + abi + '" -f 1'
		(status, result)=execCmd(chain33_cmd)
		if status != 0:
			print("execute command failed:" + chain33_cmd)
			continue
		
		print("execute command:" + chain33_cmd)
		print("txid:" + result)
		
		chain33_cmd= cmd_prefix + 'tx query -s ' + result
		(status, result)=execCmd(chain33_cmd)
		if status != 0:
			print("execute command failed:" + chain33_cmd)
			continue
		
		tx = json.loads(result)
		print("tx info:")
		print(tx)
		if tx["receipt"]["tyName"] != "ExecOk":
			print("execute command ok but tx failed:" + chain33_cmd)
			continue
		
		log=tx["receipt"]["logs"][0]["log"]
		contractName=log["contractName"]
		contractAddr=log["contractAddr"]
		contract["creator"] = creator
		contract["contractName"]=contractName
		contract["contractAddr"]=contractAddr
		
		print("code:"+code)
		print("alias:" + alias)
		print("abi:" + abi)
		print("creator:" + creator)
		print("set:" + set)
		print("get:" + get)
		print("contractName:" + contractName)
		print("contractAddr:" + contractAddr)

		with open(objName, "w") as fp:
			fp.write(json.dumps(contract, indent=4))
	
	elif cmd=='evmInfo':
		if len(user_input) < 2:
			print("command usage: evmInfo aliasName")
			continue
		
		name=user_input[1]
		if os.access(name, os.R_OK):
			pass
		else:
			print(name + " is not exist or not accessible to read")
			continue
		
		file = open(name)
		content = file.read()
		file.close()
		contract = json.loads(content)
		
		print(contract)
	elif cmd=='evmAbiCall':
		if len(user_input) < 3:
			print("command usage: evmAbiCall aliasName method(parameters)")
			continue	
			
		name=user_input[1]
		if os.access(name, os.R_OK):
			pass
		else:
			print(name + " is not exist or not accessible to read")
			continue
		
		file = open(name)
		content = file.read()
		file.close()
		contract = json.loads(content)
		code=contract["code"]
		alias=contract["alias"]
		abi=contract["abi"]
		set=contract["set"]
		get=contract["get"]
		contractName=contract["contractName"]
		contractAddr=contract["contractAddr"]
		creator=contract["creator"]
		
		interf = user_input[2]
		chain33_cmd= cmd_prefix + 'evm call -e ' + contractName + ' -b "' + interf + '" -c ' + creator + ' -f 1'
		(status, result)=execCmd(chain33_cmd)
		if status != 0:
			print("execute command failed:" + chain33_cmd)
			continue
		
		#print("txid:" + result)
		
		chain33_cmd= cmd_prefix + 'tx query -s ' + result
		(status, result)=execCmd(chain33_cmd)
		if status != 0:
			print("execute command failed:" + chain33_cmd)
			continue
		
		tx = json.loads(result)
		if tx["receipt"]["tyName"] != "ExecOk":
			print("execute command ok but tx failed:" + chain33_cmd)
			continue
		
		log=tx["receipt"]["logs"][0]["log"]
		tyName=tx["receipt"]["logs"][0]["tyName"]
		if tyName=="LogEVMStateChangeItem":
			log=log=tx["receipt"]["logs"][1]["log"]
			print(interf + " ok")
		elif tyName=="LogCallContract":
			print(log)
		else:
			print("log err:" + log)
	else:
		print("unknow command:"+cmd)

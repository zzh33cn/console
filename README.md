# 使用控制台程序快速体验Chain33区块链及智能合约

## 1 控制台程序介绍  

console程序是为了方便普通用户对于chain33的使用而开发，用户通过console可以以简短的命令完成区块链功能（账户查询，转账，部署evm合约，调用evm合约等），而不必执行繁琐的底层指令，提高chain33区块链的易用性，降低用户使用门槛。

## 2 控制台程序使用说明  

### 2.1 支持平台：  

安装了python3的Linux、Mac、Windows平台。
有的平台默认安装了python2.x的版本，需要安装python3.x的版本，具体可以从互联网上搜索相关教程。

### 2.2 使用步骤：  

1.首先下载console.py程序及sample_contract样例合约到本地chain33目录下。  

2.确保本地chain33程序正在运行，可以进行区块链相关指令操作。  

3.命令行状态到chain33目录中：  

```json
	A. Linux或者Mac中，打开控制台命令行模式，进入chain33目录，通过ls命令可以看到console.py程序、sample_contract、chain33、chain33-cli；  
	B. Windows中，从“开始”菜单在“搜索程序和文件”中输入cmd，按回车，进入command命令行模式，通过cd命令，进入chain33目录，通过dir命令可以看到console.py程序、sample_contract、chain33、chain33-cli；
	C. Windows中，也可以安装git，通过资源管理器图形界面进入chain33目录，可以看到console.py程序、sample_contract、chain33、chain33-cli，通过鼠标右键选择“Git Bash Here”进入类linux的命令行模式，通过ls命令可以看到console.py程序、sample_contract、chain33、chain33-cli；  
```

4.chain33目录中验证chain33正常工作。

  Linux/Mac平台执行指令： ./chain33-cli net is_sync  
  Windows平台cmd命令行执行指令：.\chain33-cli net is_sync  
  Windows平台git bash命令行执行指令：./chain33-cli net is_sync  
  得到结果：true  

5.chain33目录中执行命令:python console.py启动控制台程序，进行各种操作

可看到类似如下输出  

(1) 命令行提示符：  
```json
use configure file: chain33.toml
chain33.toml is exist,read json rpc address: "localhost:8801"

[chain33] >>>
```
说明：启动console.py程序时，可以带参数，指定用哪一个配置文件，也可以不指定参数使用当前目录下的默认配置文件，从中获取chain33节点的json rpc服务ip和端口。如果当前目录不存在配置文件，则使用默认ip和端口：127.0.0.1:8801

(2) help指令可以展示所有的支持的命令(关于目前支持的指令后面有一张表进行详细描述)
```json
[chain33] >>> help
clear
setJrpcAddr
raw
seedGenerate
seedSave
seedGenerateAndSave
version
net
accountList
accountBalance
accountCreate
accountSetlabel
accountDumpkey
accountImportkey
queryTx
walletStatus
walletUnlock
walletLock
walletSetfee
walletSetpwd
walletAutomine
walletMerge
totalCoins
transferCoin
sendCoinsTransfer
evmDeploy
evmInfo
evmAbiCall
[chain33] >>>
```
说明：上述列出的指令，都是可以使用的，输入指令名，console程序会返回和chain33交互的结果；如果需要加参数，console程序会提示指令的用法。

(3) 使用如下命令可以生成并保存seed、设置钱包密码:
```json
[chain33] >>> seedGenerateAndSave 0 tech1234
generated seed:
throw salute lecture cube slush divide ripple fold monitor other wash corn divert wisdom kiss
please remember this seed, use it you can manage the wallet,it's very important!!!!!!
now save the seed with password: tech1234
{
    "isOK": true,
    "msg": ""
}
```
说明：如果直接通过chain33-cli执行指令，要先先生成seed、再保存seed，两个步骤才能完成上述操作，console程序合并成一条指令，减少用户操作的繁琐性。

(4) 使用如下命令查看钱包状态：
```json
[chain33] >>> walletStatus
walletStatus
{
    "isWalletLock": true,
    "isAutoMining": false,
    "isHasSeed": true,
    "isTicketLock": true
}
```
说明：钱包默认处于锁定状态，此时无法使用钱包管理的地址私钥进行签名交易，转账等操作。

(5) 使用如下命令解锁钱包：
```json
[chain33] >>> walletUnlock tech1234
{
    "isOK": true,
    "msg": ""
}
```
说明：wallet管理了本地账户地址和私钥，如果要发起交易（转账，调用合约等），需要通过wallet使用导入到本地的地址私钥对交易进行签名，那么必须要先解锁钱包。


(6) 创建新的账户地址：
```json
[chain33] >>> accountCreate test
{
    "acc": {
        "balance": "0.0000",
        "frozen": "0.0000",
        "addr": "15NSrVFWHLaPFsGBekge8zyYMxtVk8JhF1"
    },
    "label": "test"
}
```
说明：钱包创建好以后，需要创建账户地址，用于存储用户资产或者进行转账交易，调用合约等。

(7) 导出账户地址私钥：
```json
[chain33] >>> accountDumpkey 15NSrVFWHLaPFsGBekge8zyYMxtVk8JhF1
{
    "data": "0xfa816bf080e9d184b17801d2a83a564f49e9183cc0c7106cb788da652d4b99bd"
}
```
说明：从本地钱包导出所管理的某个账户地址对应的私钥，拥有这个私钥，就可以掌管该地址上的资产，进行转账交易等操作，私钥要做好保密存储，不要泄露。

(8) 导入地址私钥：
```json
[chain33] >>> accountImportkey 3990969DF92A5914F7B71EEB9A4E58D6E255F32BF042FEA5318FC8B3D50EE6E8 genesis
{
    "acc": {
        "balance": "100000000.0000",
        "frozen": "0.0000",
        "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
    },
    "label": "genesis"
}
```
说明：可以把已经存在的地址私钥导入到本地钱包中进行管理，从而可以通过本地钱包对私钥对应的账户地址中的资产进行管理，进行转账交易等操作。切记，私钥要保密，避免泄露。

(9) 以accountList为例，该命令会展示当前节点钱包中的账户列表：
```json
[chain33] >>> accountList
{
    "wallets": [
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1K3PRdgKV2x9BCrbathhDKjqRksz8rwXEn"
            },
            "label": "airdropaddr"
        },
        {
            "acc": {
                "balance": "0.0000",
                "frozen": "0.0000",
                "addr": "1J9Q8YCoiAitNic77VusEfz3i6AR5HuiCY"
            },
            "label": "node award"
        },
        {
            "acc": {
                "balance": "99990000.0000",
                "frozen": "0.0000",
                "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
            },
            "label": "genesis"
        },
        {
            "acc": {
                "balance": "10000.0000",
                "frozen": "0.0000",
                "addr": "1KonWZdo4TEu9a7mGEoEQmKAaHBz8opcq5"
            },
            "label": "test"
        }
    ]
}
```
说明：通过该命令可以查看本地钱包管理的账户地址列表，也能看到账户资产。

(10) 查看地址详细的资产：
```json
[chain33] >>> accountBalance 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs
{
    "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "execAccount": [
        {
            "execer": "coins",
            "account": {
                "balance": "100000000.0000",
                "frozen": "0.0000"
            }
        }
    ]
}
```
说明：通过该指令可以看到某个账户地址的资产详情，包括在合约中的资产。


(11) 使用如下命令在账户之间转账：
```json
[chain33] >>> transferCoin 1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs 1KonWZdo4TEu9a7mGE
oEQmKAaHBz8opcq5 10
raw transaction:    0a05636f696e73122e18010a2a108094ebdc032222314b6f6e575a646f34
5445753961376d47456f45516d4b416148427a386f70637135309df5bcbbdef6b9c26a3a22314b6f
6e575a646f345445753961376d47456f45516d4b416148427a386f70637135
signed transaction:    0a05636f696e73122e18010a2a108094ebdc032222314b6f6e575a646
f345445753961376d47456f45516d4b416148427a386f706371351a6d080112210289af2f9d53109
71242402932ab50a985a21036716a356c2419253c247d28832e1a46304402202e3560146bf567fb0
cd56a7372a2b05eaba73cbec059e6604efdacffe4f4415902206956e9942b1eb011d62429ebaa169
08c65bd49e7131f5dc8e4ae50bfa7f2df6728a095baf205309df5bcbbdef6b9c26a3a22314b6f6e5
75a646f345445753961376d47456f45516d4b416148427a386f70637135
transaction id:    0xe8dcd94245c50e15d902cd54ca2b6bab5ba9a4d318e3316f6fefba718be
ea7b7
```
说明：该指令包含了chain33-cli中的构造交易，签名交易，提交交易三个步骤，这里简化成一条指令，方便使用者的操作，降低使用难度。

(12) 使用如下命令查询交易：
```json
[chain33] >>> queryTx 0xe8dcd94245c50e15d902cd54ca2b6bab5ba9a4d318e3316f6fefba71
8beea7b7
{
    "tx": {
        "execer": "coins",
        "payload": {
            "transfer": {
                "cointoken": "",
                "amount": "1000000000",
                "note": null,
                "to": "1KonWZdo4TEu9a7mGEoEQmKAaHBz8opcq5"
            },
            "ty": 1
        },
        "rawpayload": "0x18010a2a108094ebdc032222314b6f6e575a646f345445753961376
d47456f45516d4b416148427a386f70637135",
        "signature": {
            "ty": 1,
            "pubkey": "0x0289af2f9d5310971242402932ab50a985a21036716a356c2419253
c247d28832e",
            "signature": "0x304402202e3560146bf567fb0cd56a7372a2b05eaba73cbec059
e6604efdacffe4f4415902206956e9942b1eb011d62429ebaa16908c65bd49e7131f5dc8e4ae50bf
a7f2df67"
        },
        "fee": "0.0000",
        "expire": 1582205600,
        "nonce": 7675514433404091037,
        "to": "1KonWZdo4TEu9a7mGEoEQmKAaHBz8opcq5",
        "amount": "10.0000",
        "from": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
        "hash": "0xe8dcd94245c50e15d902cd54ca2b6bab5ba9a4d318e3316f6fefba718beea
7b7"
    },
    "receipt": {
        "ty": 2,
        "tyName": "ExecOk",
        "logs": [
            {
                "ty": 3,
                "tyName": "LogTransfer",
                "log": {
                    "prev": {
                        "currency": 0,
                        "balance": "9999000000000000",
                        "frozen": "0",
                        "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
                    },
                    "current": {
                        "currency": 0,
                        "balance": "9998999000000000",
                        "frozen": "0",
                        "addr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs"
                    }
                },
                "rawLog": "0x0a2d1080e0efd899c1e111222231436245565439526e4d356f5
a68574d6a34667855724a5839345674526f747a7673122d1080cc84fc95c1e111222231436245565
439526e4d356f5a68574d6a34667855724a5839345674526f747a7673"
            },
            {
                "ty": 3,
                "tyName": "LogTransfer",
                "log": {
                    "prev": {
                        "currency": 0,
                        "balance": "1000000000000",
                        "frozen": "0",
                        "addr": "1KonWZdo4TEu9a7mGEoEQmKAaHBz8opcq5"
                    },
                    "current": {
                        "currency": 0,
                        "balance": "1001000000000",
                        "frozen": "0",
                        "addr": "1KonWZdo4TEu9a7mGEoEQmKAaHBz8opcq5"
                    }
                },
                "rawLog": "0x0a2b1080a094a58d1d2222314b6f6e575a646f3454457539613
76d47456f45516d4b416148427a386f70637135122b1080b4ff81911d2222314b6f6e575a646f345
445753961376d47456f45516d4b416148427a386f70637135"
            }
        ]
    },
    "height": 40,
    "index": 0,
    "blocktime": 1582205481,
    "amount": "10.0000",
    "fromaddr": "1CbEVT9RnM5oZhWMj4fxUrJX94VtRotzvs",
    "actionname": "transfer",
    "assets": [
        {
            "exec": "coins",
            "symbol": "BTY",
            "amount": 1000000000
        }
    ],
    "txProofs": [
        {
            "proofs": null,
            "index": 0,
            "rootHash": ""
        }
    ],
    "fullHash": "0xae9795d70e15c0ebcce9aca267383a4f83d8becf7a94dfdb5750d7d582243
bb9"
}
[chain33] >>>
```
说明：通过该指令，可以查询某条交易的执行结果及相关信息

(13)  另外，console也提供了raw指令模式。
比如：

```json
[chain33] >>> raw wallet status
{
    "isWalletLock": false,
    "isAutoMining": false,
    "isHasSeed": true,
    "isTicketLock": true
}
```
这条指令其实就对应chain33-cli wallet status的原始指令，这种raw指令模式可以直接调用chain33-cli支持的所有的指令，提供了一种兼容chain33-cli命令的模式，便于使用者在一个console交互程序中执行所有指令。

## 3 console支持的指令说明

|指令名称|说明|用法|参数说明|
|----|----|----|----|
|clear|清理屏幕|clear|无|
|setJrpcAddr|设定jrpc服务地址|setJrpcAddr ip:port|ip:jrpc服务ip;port:jrpc服务端口|
|history|console本次启动以后输入的历史指令|history|无|
|quit|退出console程序|quit||
|raw|直接调用chain33-cli，支持chain33-cli的所有指令|比如chain33-cli wallet status对应raw wallet status||
|seedGenerate|生成seed|seedGenerate 0(english)/1(chinese)|参数0表示英文，参数1表示中文|
|seedSave|保存生成的seed|seedSave pwd seed|pwd:密码；seed:要保存的seed|
|seedGenerateAndSave|生成并保存seed|seedGenerateAndSave lang passwd|lang：0，英文；1：中文；passwd:设定的密码|
|version|查询程序版本信息|version||
|net|查询区块链网络信息| net fault/info/time/is_clock_sync/is_sync/peer|fault:故障数；  info：网络信息;  time:时间信息;  is_clock_sync:时钟是否和网络同步;  is_sync:区块是否同步;  对端节点信息|
|accountList|钱包管理的账户列表|accountList|无|
|accountBalance|账户余额查询|accountBalance address|address:账户地址|
|accountCreate|创建账户| accountCreate label|label:账户标签|
|accountSetlabel|为账户设置标签|accountSetlabel address label|address:账户地址；label:标签|
|accountDumpkey|导出账户私钥|accountDumpkey address|address:账户地址|
|accountImportkey|导入私钥|accountImportkey privkey label|privkey:要导入的私钥； label:导入后账户标签|
|queryTx|查询交易信息| queryTx txid|txid:交易hash|
|walletStatus|查询钱包状态|walletStatus|无|
|walletUnlock|解锁钱包| walletUnlock password [timeout]|password:钱包密码；  timeout:超时时间，0表示不超时|
|walletLock|锁住钱包|walletLock|无|
|walletSetfee|设置交易费用|walletSetfee fee|fee:交易费用|
|walletSetpwd|设置钱包密码|walletSetpwd newpwd oldpwd|newpwd：新密码；oldpwd:旧密码|
|walletAutomine|设置自动挖矿|walletAutomine on(1)/off(0)|on:开启自动挖矿; off:关闭自动挖矿|
|walletMerge|账户余额合并|walletMerge address|address: 合并到的账户地址|
|totalCoins|统计当前总的coin数量|totalCoins|无|
|transferCoin|转账coin|transferCoin addr1 addr2 number [note]|addr1:转出账户;  addr2:转入账户; number:转账数量;  note:转账说明|
|sendCoinsTransfer|转账coin| sendCoinsTransfer fromKey toAddr amount note|fromKey:转出账户;  toAddr:转入账户; number:转账数量;  note:转账说明|
|evmDeploy|部署evm合约|evmDeploy contractFileName aliasName creatorAddr|contractFileName:合约文件名; aliasName: 部署合约的实例名; creatorAddr: 合约创建者地址|
|evmInfo|evm合约信息查询|evmInfo aliasName|aliasName: 已部署的evm合约别名|
|evmAbiCall|调用合约接口|evmAbiCall aliasName method(parameters)|aliasName：已部署合约名称； method(parameters)：调用合约的方法名及参数值|

## 4 使用console快捷部署evm样例合约，极简操作，方便用户体验智能合约

使用控制台程序和样例合约文件，可以快速极简部署evm合约，并调用合约，操作简单难度低，让用户快速亲身体验到智能合约的部署和使用。

### 1. 确保钱包解锁：
```json
[chain33] >>> walletUnlock tech1234
{
    "isOK": true,
    "msg": ""
}
```
### 2. 根据准备好的合约文件部署合约：
```json
[chain33] >>> evmDeploy sample_contract test 1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv
sample_contract is accessible to read

execute command:.\chain33-cli evm create -i 608060405234801561001057600080fd5b5060c68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032 -c 1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv -s test -b "[{\"constant\":false,\"inputs\":[{\"name\":\"x\",\"type\":\"uint256\"}],\"name\":\"set\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"get\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"}]" -f 1

txid:0xdae06b2ab6206ebd31b5ca7b352e8b84f2829076c07dab87e3d4d28889ce4962
tx info:
{
    'tx': {
        'execer': 'evm',
        'payload': {
            'amount': '0',
            'gasLimit': '0',
            'gasPrice': 0,
            'code': '0x608060405234801561001057600080fd5b5060c68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032',
            'alias': 'test',
            'note': '',
            'abi': '[
                {
                    "constant": false,
                    "inputs": [
                        {
                            "name": "x",
                            "type": "uint256"
                        }
                    ],
                    "name": "set",
                    "outputs": [
                        
                    ],
                    "payable": false,
                    "stateMutability": "nonpayable",
                    "type": "function"
                },
                {
                    "constant": true,
                    "inputs": [
                        
                    ],
                    "name": "get",
                    "outputs": [
                        {
                            "name": "",
                            "type": "uint256"
                        }
                    ],
                    "payable": false,
                    "stateMutability": "view",
                    "type": "function"
                },
                {
                    "inputs": [
                        
                    ],
                    "payable": false,
                    "stateMutability": "nonpayable",
                    "type": "constructor"
                }
            ]'
        },
        'rawpayload': '0x22e501608060405234801561001057600080fd5b5060c68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c634300051000322a04746573743af9025b7b22636f6e7374616e74223a66616c73652c22696e70757473223a5b7b226e616d65223a2278222c2274797065223a2275696e74323536227d5d2c226e616d65223a22736574222c226f757470757473223a5b5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a226e6f6e70617961626c65222c2274797065223a2266756e6374696f6e227d2c7b22636f6e7374616e74223a747275652c22696e70757473223a5b5d2c226e616d65223a22676574222c226f757470757473223a5b7b226e616d65223a22222c2274797065223a2275696e74323536227d5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a2276696577222c2274797065223a2266756e6374696f6e227d2c7b22696e70757473223a5b5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a226e6f6e70617961626c65222c2274797065223a22636f6e7374727563746f72227d5d',
        'signature': {
            'ty': 1,
            'pubkey': '0x031c80a392cb7e5201ba6175330703e1c0b49a273adf85c23dd351947c208639ff',
            'signature': '0x3045022100eb0fc648f988f1c6df577c4a836c5da29f8c1911700d0fe0579722a01f43670302207efac058eb24c986bbdba4a7a9e9509cd5cf8ada5075fe4f2f37e69090303877'
        },
        'fee': '1.0000',
        'expire': 1582249439,
        'nonce': 5208488883003648087,
        'to': '19tjS51kjwrCoSQS13U3owe7gYBLfSfoFm',
        'from': '1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv',
        'hash': '0xdae06b2ab6206ebd31b5ca7b352e8b84f2829076c07dab87e3d4d28889ce4962'
    },
    'receipt': {
        'ty': 2,
        'tyName': 'ExecOk',
        'logs': [
            {
                'ty': 603,
                'tyName': 'LogCallContract',
                'log': {
                    'caller': '1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv',
                    'contractName': 'user.evm.0xdae06b2ab6206ebd31b5ca7b352e8b84f2829076c07dab87e3d4d28889ce4962',
                    'contractAddr': '1Bkx91eymBo3E8iCaNQps4bNFHc9gBtZX',
                    'usedGas': '39693',
                    'ret': '0x6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032',
                    'jsonRet': ''
                },
                'rawLog': '0x0a22314c4e416d4e385070567a336436314b747852557532356966723972486237357676124b757365722e65766d2e3078646165303662326162363230366562643331623563613762333532653862383466323832393037366330376461623837653364346432383838396365343936321a2131426b78393165796d426f3345386943614e51707334624e464863396742745a58208db6022ac6016080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032'
            },
            {
                'ty': 601,
                'tyName': 'LogContractData',
                'log': {
                    'creator': '1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv',
                    'name': 'user.evm.0xdae06b2ab6206ebd31b5ca7b352e8b84f2829076c07dab87e3d4d28889ce4962',
                    'alias': 'test',
                    'addr': '1Bkx91eymBo3E8iCaNQps4bNFHc9gBtZX',
                    'code': '0x6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032',
                    'codeHash': '0x86caa23642eb6f934ff1592232a27b04caa8520accb42e19ffa089f01e895447',
                    'abi': '[
                        {
                            "constant": false,
                            "inputs": [
                                {
                                    "name": "x",
                                    "type": "uint256"
                                }
                            ],
                            "name": "set",
                            "outputs": [
                                
                            ],
                            "payable": false,
                            "stateMutability": "nonpayable",
                            "type": "function"
                        },
                        {
                            "constant": true,
                            "inputs": [
                                
                            ],
                            "name": "get",
                            "outputs": [
                                {
                                    "name": "",
                                    "type": "uint256"
                                }
                            ],
                            "payable": false,
                            "stateMutability": "view",
                            "type": "function"
                        },
                        {
                            "inputs": [
                                
                            ],
                            "payable": false,
                            "stateMutability": "nonpayable",
                            "type": "constructor"
                        }
                    ]'
                },
                'rawLog': '0x0a22314c4e416d4e385070567a336436314b747852557532356966723972486237357676124b757365722e65766d2e3078646165303662326162363230366562643331623563613762333532653862383466323832393037366330376461623837653364346432383838396365343936321a0474657374222131426b78393165796d426f3345386943614e51707334624e464863396742745a582ac6016080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032322086caa23642eb6f934ff1592232a27b04caa8520accb42e19ffa089f01e8954473af9025b7b22636f6e7374616e74223a66616c73652c22696e70757473223a5b7b226e616d65223a2278222c2274797065223a2275696e74323536227d5d2c226e616d65223a22736574222c226f757470757473223a5b5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a226e6f6e70617961626c65222c2274797065223a2266756e6374696f6e227d2c7b22636f6e7374616e74223a747275652c22696e70757473223a5b5d2c226e616d65223a22676574222c226f757470757473223a5b7b226e616d65223a22222c2274797065223a2275696e74323536227d5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a2276696577222c2274797065223a2266756e6374696f6e227d2c7b22696e70757473223a5b5d2c2270617961626c65223a66616c73652c2273746174654d75746162696c697479223a226e6f6e70617961626c65222c2274797065223a22636f6e7374727563746f72227d5d'
            }
        ]
    },
    'height': 41,
    'index': 0,
    'blocktime': 1582249319,
    'amount': '0.0000',
    'fromaddr': '1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv',
    'actionname': 'createEvmContract',
    'assets': None,
    'txProofs': [
        {
            'proofs': None,
            'index': 0,
            'rootHash': ''
        }
    ],
    'fullHash': '0x210f2a9142cd565a130ce2878cd0e5883ffe8d8b2ee91e8e2a59c5e2234ec2a5'
}

code:608060405234801561001057600080fd5b5060c68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032
alias:sample
abi:[{\"constant\":false,\"inputs\":[{\"name\":\"x\",\"type\":\"uint256\"}],\"name\":\"set\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"get\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"}]
creator:1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv
set:set
get:get
contractName:user.evm.0xdae06b2ab6206ebd31b5ca7b352e8b84f2829076c07dab87e3d4d28889ce4962
contractAddr1Bkx91eymBo3E8iCaNQps4bNFHc9gBtZX
```

### 3. 使用evmAbiCall指令调用合约的set接口，保存数据：

```json
[chain33] >>> evmAbiCall
command usage: evmAbiCall aliasName method(parameters)
[chain33] >>> evmAbiCall test set(888)
set(888) ok
```

### 4. 使用evmAbiCall指令调用合约的get接口，查询数据：

```json
[chain33] >>> evmAbiCall test get()
{'caller': '1LNAmN8PpVz3d61KtxRUu25ifr9rHb75vv', 'contractName': '', 'contractAddr': '1Bkx91eymBo3E8iCaNQps4bNFHc9gBtZX', 'usedGas': '263', 'ret': '0x0000000000000000000000000000000000000000000000000000000000000378', 'jsonRet': '[{"name":"","type":"uint256","value":888}]'}
```

从上面可以看出，部署及调用合约的步骤及指令极为简化，可以方便用户上手了解。
上述过程也可以通过直接调用chain33-cli的指令来完成，但操作会比较繁琐，对于高级开发者，可以选择console的raw指令，直接调用chain33-cli的指令来完成更多参数设定。

样例合约sample_contract的格式如下：
```json
{	"code":"608060405234801561001057600080fd5b5060c68061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea265627a7a72315820d4df27010b6a834bd33c5ffe98b8b9502bad314767b3e9afa5127dfa8272214364736f6c63430005100032",
	"alias":"sample",
	"abi":"[{\\\"constant\\\":false,\\\"inputs\\\":[{\\\"name\\\":\\\"x\\\",\\\"type\\\":\\\"uint256\\\"}],\\\"name\\\":\\\"set\\\",\\\"outputs\\\":[],\\\"payable\\\":false,\\\"stateMutability\\\":\\\"nonpayable\\\",\\\"type\\\":\\\"function\\\"},{\\\"constant\\\":true,\\\"inputs\\\":[],\\\"name\\\":\\\"get\\\",\\\"outputs\\\":[{\\\"name\\\":\\\"\\\",\\\"type\\\":\\\"uint256\\\"}],\\\"payable\\\":false,\\\"stateMutability\\\":\\\"view\\\",\\\"type\\\":\\\"function\\\"},{\\\"inputs\\\":[],\\\"payable\\\":false,\\\"stateMutability\\\":\\\"nonpayable\\\",\\\"type\\\":\\\"constructor\\\"}]",
	"creator":"",
	"set":"set",
	"get":"get",
	"contractName":"",
	"contractAddr":""
}
```
这是一个合约样例模板，包含了合约的code、abi以及一些方法名称，通过console的命令行可以根据模板的内容来部署实际的合约到区块链上，部署以后的合约可以被调用执行，执行结果可以被查询。

合约模板中的code及abi可以参考https://chain.33.cn/document/67中的例子来生成，用户可以自定义合约作为模板来进行部署及验证。

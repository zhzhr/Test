import requests
import codecs
import json

#读取文件
def getList(filePath):
    with codecs.open(filePath, 'r', 'utf-8') as f:
        list = []        
        line = f.readline()
        list.append(line)

        # while line:
        #     print(line)
        #     line = f.readline()
        #     list.append(line)

        list = f.readlines()
        for i in range(0, len(list)):
            list[i] = list[i].rstrip('\r\n')

        return list


#存储文件
def saveFile(filePath, list):
    with open(filePath, 'a') as wf:
        for item in list:
            wf.write(item)
            wf.write('\n')


#获取机构统一社会信用代码
def getUrlData(keyword):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
        'Accept': 'application/json, text/javascript, */*; q=0.01'
    }

    url = "https://public.creditchina.gov.cn/private-api/catalogSearch?"

    queryParam = {
        '_': '1594883251927',
        'scenes': 'defaultscenario',
        'tableName': 'credit_xyzx_tyshxydm',
        'searchState': '2',
        'entityType': '1,2,4,5,6,7,8',
        'page': '1',
        'pageSize': '10',
        'keyword': keyword
    }

    response = requests.get(url, headers=headers, params=queryParam)

    #返回结果json
    result = json.loads(response.text)

    uscc = "\t无返回结果"

    if result["data"] != None and len(result["data"]["list"]) > 0:
        #取第一条结果的统一社会信用代码值
        uscc = result["data"]["list"][0]["tyshxydm"]
        if uscc == None:
            uscc = "\t无返回结果"
    
    return keyword + "\t" + uscc

#print(getUrlData('渤海财产保险股份有限公司湖北分公司武昌友谊大道营销服务部'))

#'''
sourceFile = "D:/MyProjects/test/org2.txt"
targetFile = "D:/MyProjects/test/result.txt"

orgList = getList(sourceFile)
resultList = []
for item in orgList:
    print("查询机构：" + item)
    resultList.append(getUrlData(item))

    #每100行保存一次
    if len(resultList) == 100:        
        saveFile(targetFile, resultList)
        resultList.clear()

print(resultList)

saveFile(targetFile, resultList)

print("over")
#'''
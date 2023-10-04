import json
import csv
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models



def tencentGeneralHandwritingOCRRequest(SecretId='AKIDpW2YryvgCVebO8i3CBwceV8XggWBdqur',
                                        SecretKey='y3rfJivtVv76qLcfS1LUNXWJuHSPBl9M',
                                        imageUrl="https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/07/31/398A801E17F5FD3ECC6FD6DEACB32683"):

    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        # 李志祥
        # SecretId : AKIDpW2YryvgCVebO8i3CBwceV8XggWBdqur
        # SecretKey: y3rfJivtVv76qLcfS1LUNXWJuHSPBl9M
        cred = credential.Credential(SecretId, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GeneralHandwritingOCRRequest()
        params = {
            "ImageUrl": imageUrl
            # "ImageUrl": "https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/08/06/A9795485163B27E939CB886849699170"
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个GeneralHandwritingOCRResponse的实例，与请求对象对应
        resp = client.GeneralHandwritingOCR(req)
        # 输出json格式的字符串回包
        # print(resp.to_json_string())
        # 返回结果
        res = json.loads(resp.to_json_string())
        ocrResult = ' '.join([i['DetectedText'] for i in res['TextDetections']])
        # print(ocrResult)
        return ocrResult

    except TencentCloudSDKException as err:
        # print(err)
        # print(err.message)
        return err.message
    
def writeCsv(data=[['a', 'b'],['c', 'd']]):
    # header = ['name','age','QQ_num','wechat']data = [['suliang','21','787991021','lxzy787991021']]with open ('information.csv','w',encoding='utf-8',newline='') as fp:    # 写    writer =csv.writer(fp)    # 设置第一行标题头    writer.writerow(header)    # 将数据写入    writer.writerows(data)
    header = ['url', 'tencentOcrResult']
    with open('B端学习机-语文-腾讯结果.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(header)
        writer.writerows(data)
    
def readCsv():
    imageUrls = []
    with open('B端学习机-拓展学科.csv', encoding='utf-8') as fp:
        reader = csv.DictReader(fp)
        for i in reader:
            imageUrls.append(i['\ufeff语文'])
    return imageUrls

# # 任莹翔  1317414067  
# secret_id = "AKID1waAcplQpzsVt0DQO6ZpulNjophLBpDK"
# secret_key = "tV3OaYHm22KVUFm47wYVEqPlskNq57vX"
# # 施倩  1302155235  
# secret_id = "AKIDEJCrJWUFn7yd4MTQEsX9e0BCAwY8YnqM"
# secret_key = "LVTDj4EAtaAYifOuGSQDqLhrpcCYfXEk"
# # 张小艳  1317413935  
# secret_id = "AKIDpaHm6e7WjhYEfplV2JNDqEOK1Thsx15z"
# secret_key = "jDbnnfJiszulSwAKVSAoJaeT3ZKs9DTW"
# # 李宁  1317167965  
# secret_id = "AKIDUs4MRJzRfiifT4ScaLl4C8YvGZoy699A"
# secret_key = "2Qn7OgxBLSXaac4eAe6GRYdq18DEC95x"
# # 郑成祎  1302617457  
# secret_id = "AKIDCGArMdt3tY0GMGySltukQs7A0ECyZzCD"
# secret_key = "tZ1EE2d1DE2cyBE263xgKo7D5nLflkY9"
    
if __name__ == '__main__':
    tencentUsers = [
        {
            'name': '任莹翔  1317414067 ',
            'SecretId': 'AKID1waAcplQpzsVt0DQO6ZpulNjophLBpDK',
            'SecretKey': 'tV3OaYHm22KVUFm47wYVEqPlskNq57vX'
        },
        {
            'name': '施倩  1302155235',
            'SecretId': 'AKIDEJCrJWUFn7yd4MTQEsX9e0BCAwY8YnqM',
            'SecretKey': 'LVTDj4EAtaAYifOuGSQDqLhrpcCYfXEk'
        },
        {
            'name': '张小艳  1317413935',
            'SecretId': 'AKIDpaHm6e7WjhYEfplV2JNDqEOK1Thsx15z',
            'SecretKey': 'jDbnnfJiszulSwAKVSAoJaeT3ZKs9DTW'
        },
        {
            'name': '李宁  1317167965 ',
            'SecretId': 'AKIDUs4MRJzRfiifT4ScaLl4C8YvGZoy699A',
            'SecretKey': '2Qn7OgxBLSXaac4eAe6GRYdq18DEC95x'
        },
        {
            'name': '李志祥  18291859975',
            'SecretId': 'AKIDpW2YryvgCVebO8i3CBwceV8XggWBdqur',
            'SecretKey': 'y3rfJivtVv76qLcfS1LUNXWJuHSPBl9M'
        }
    ]
    # tencentGeneralHandwritingOCRRequest()
    imageUrls = readCsv()
    per_count = 1000
    # for i, index in enumerate(range(0, len(imageUrls), per_count)):
    i = 4
    index = 4000
    fileName = f'result/{index}_{index+per_count}'
    per_image_urls = imageUrls[index:index+per_count]
    per_results = []
    print(fileName)
    print(tencentUsers[i]['name'])
    for ii, url in enumerate(per_image_urls):
        result = tencentGeneralHandwritingOCRRequest(tencentUsers[i]['SecretId'], tencentUsers[i]['SecretKey'], url)
        per_results.append(f'{url}, {result}')
        print(f'进度{ii+1}/{len(per_image_urls)}  {url}, {result}')
    writeable_result = '\n'.join(per_results)
    with open(fileName, 'w') as fp:
        fp.writelines(writeable_result)
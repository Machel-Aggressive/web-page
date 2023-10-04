from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
import os


def convertCookie(Cookie='_ga=GA1.2.2037878103.1673020152; qcloud_uid=f72ace975d8b8d417390920aa1b6fd99%40devS; language=zh; qcmainCSRFToken=H1zqnbsi22; qcloud_visitId=026f45f8d7b7b3dd9d502eb5440c0c33; qcstats_seo_keywords=%E5%93%81%E7%89%8C%E8%AF%8D-%E5%93%81%E7%89%8C%E8%AF%8D-%E8%85%BE%E8%AE%AF%E4%BA%91; _gcl_au=1.1.1154072028.1692279220; uin=o100014503212; tinyid=144115218036494102; loginType=wx; lastLoginIdentity=6fdc2a4803a4df227711eb4b43eee0f4; intl=1; regionId=8; moduleId=1302333866; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22100014503212%22%2C%22first_id%22%3A%2218587c597bad4b-0ec84e196ca698-26021151-2073600-18587c597bbee3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_utm_medium%22%3A%22cpd%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1ODdjNTk3YmFkNGItMGVjODRlMTk2Y2E2OTgtMjYwMjExNTEtMjA3MzYwMC0xODU4N2M1OTdiYmVlMyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEwMDAxNDUwMzIxMiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22100014503212%22%7D%2C%22%24device_id%22%3A%2218587c597bad4b-0ec84e196ca698-26021151-2073600-18587c597bbee3%22%7D; qcloud_from=qcloud.directEnter.home-1692283591484; lastLoginType=wx; skey=uyFbbqplnZXl3t*iCYfQd7nlW4KU5gaIZlNX4Oe69NU_; trafficParams=***%24%3Btimestamp%3D1692285564872%3Bfrom_type%3Dserver%3Btrack%3D2c00beca-f712-4bdc-aca7-d982c94c4b8a%3B%24***; nick=Nicholas%20Lee'):
    middleCookies = [i.strip() for i in Cookie.split(';')]
    res = {}
    for i in middleCookies:
        k, v = i.split('=')
        res[k] = v
    return res

class MyUITest:
    width = 1000
    height = 1000
    # 手机模式
    # mobile_emulation = {'deviceName': 'iPhone 6'}
    # 设置宽高
    mobile_emulation = {'deviceMetrics': {'width': width, 'height': height}}
    options = Options()
    # options.add_experimental_option('mobileEmulation', mobile_emulation)
    # 设置开启调试模式
    # options.add_argument("--auto-open-devtools-for-tabs")
    driver = webdriver.Chrome(options=options)
    # url = 'https://www.latexlive.com/'
    url = 'https://cloud.tencent.com/product/ocr'

    def __init__(self) -> None:
        self.driver.get(self.url)
        CookieDict = convertCookie()
        for k, v in CookieDict.items():
            self.driver.add_cookie({
                'domain': '.tencent.com',
                'expiry': 1692544614,
                'httpOnly': False,
                'name': k,
                'path': '/',
                'sameSite': 'Lax',
                'secure': False,
                'value': v
                })
        self.driver.refresh()

    def isXpathElementExist(self, xpath):
        try:
            self.driver.find_element(By.XPATH, xpath)
            return True
        except:
            return False

    def runTencentGeneralHandWriteOcr(self, imageUrls=['https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/08/03/074A5B6435E445DBA5C53D5F170DD568']):
        ocrResults = []
        # 点击
        choiceAlgButton = self.driver.find_element(By.XPATH, '//*[@id="menu0731"]/div[3]')
        choiceAlgButton.click()
        # 向下滑动滚动条
        self.driver.execute_script('window.scrollTo(0, 800)')
        time.sleep(2)
        for index, url in enumerate(imageUrls):
            try:
                # 输入url
                imgUrlInput = self.driver.find_element(By.XPATH, '//*[@id="demo-app"]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/input')
                imgUrlInput.clear()
                imgUrlInput.send_keys(url)
                # 点击搜索按钮
                searchButton = self.driver.find_element(By.XPATH, '//*[@id="demo-app"]/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div')
                searchButton.click()
                time.sleep(1)
                # 向右滑动滚动条
                self.driver.execute_script('window.scrollTo(800, 800)')
                # 获取结果
                time.sleep(2)
                tableXpath = '//*[@id="demo-app"]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/table'
                if not self.isXpathElementExist(tableXpath):
                    time.sleep(2)
                    ocrResult = '识别失败'
                    noXpath = '//*[@id="demo-app"]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div'
                    if self.isXpathElementExist(noXpath):
                        ocrResult = self.driver.find_element(By.XPATH, noXpath).text
                    ocrResults.append([url, ocrResult])
                else:
                    ocrTable = self.driver.find_element(By.XPATH, tableXpath)
                    ocrTable_list = ocrTable.find_elements(By.TAG_NAME, 'tr')
                    ocrResult = []
                    for tr in ocrTable_list:
                        ocrResult.append(tr.text)
                    ocrResult = ' '.join(ocrResult)
                    ocrResults.append([url, ocrResult])
                # 向左边滑动滚动条
                self.driver.execute_script('window.scrollTo(0, 800)')
                time.sleep(1)
                print(ocrResult, f'进度{index+1}/{len(imageUrls)}')
            except Exception as e:
                print(e)
                self.driver.save_screenshot(os.path.join('result', url.split('/')[-1]+'.png'))
            
        return ocrResults

    
    def close(self):
        self.driver.quit()

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
    


if __name__ == '__main__':
    uiObj = MyUITest()
    # imageUrls = ['https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/08/03/074A5B6435E445DBA5C53D5F170DD568',
    #             'https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/08/01/F702301553925D88945A42E154E64A45',
    #             'https://npad-static-cdn.xdf.cn/material/static/ai/answer/2023/07/31/398A801E17F5FD3ECC6FD6DEACB32683']
    imageUrls = readCsv()
    print('所有图片个数', len(imageUrls))
    ocrResults = uiObj.runTencentGeneralHandWriteOcr(imageUrls)
    print('所有数据都跑完', len(ocrResults))
    writeCsv(ocrResults)
    print('结束')
    uiObj.close()
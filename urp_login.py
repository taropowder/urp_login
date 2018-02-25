import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
import re
matchflag=None
while (matchflag==None):
    username = '********'
    password = '********'
    url = 'https://ca.nuc.edu.cn/zfca/login'
    headers = {
        'origin': "https//ca.nuc.edu.cn",
        'x-devtools-emulate-network-conditions-client-id': "9497628b-38b3-47a8-b563-266e8ccd3a1d",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "https//ca.nuc.edu.cn/zfca/login",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cache-control': "no-cache",
        'postman-token': "7eb9be3a-35b0-2ad5-37ba-564d9b95895a"
    }
    s = requests.session()
    r = s.get(url, verify=False)
    soup = BeautifulSoup(r.content, 'lxml')
    a = soup.select('input[name="lt"]')
    lt = a[0].get('value')
    captcha_url = 'https://ca.nuc.edu.cn/zfca/captcha.htm'
    captcha = s.get(captcha_url, verify=False)
    with open('captcha.jpg', 'wb') as file:
        file.write(captcha.content)
    im = Image.open('captcha.jpg')
    vcode = pytesseract.image_to_string(im)
    postData = {
        'useValidateCode': '1',
        'isremenberme': '0',
        'username': username,
        'password': password,
        'j_captcha_response': vcode,
        'losetime': '',
        'lt': lt,
        '_eventId': 'submit',
        'submit1': '+'
    }
    res = s.post(url, data=postData, headers=headers, verify=False)
    # print(res.status_code)
    # print (res.text)
    with open('flag.html', 'w') as file:
        file.write(res.text)
    referurl = res.url
    matchflag = re.search(r'ticket', referurl)
    if matchflag:
        print(matchflag.group())
    else:
        print("验证码识别错误哈哈哈正在重新识别")
    # print(referurl)
dwr_urpurl="http://i.nuc.edu.cn/dwr/call/plaincall/portalAjax.getAppList.dwr"
headers2 = {
    'origin': "https//ca.nuc.edu.cn",
    'x-devtools-emulate-network-conditions-client-id': "9497628b-38b3-47a8-b563-266e8ccd3a1d",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "*/*",
    'referer': referurl,
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'postman-token': "7eb9be3a-35b0-2ad5-37ba-564d9b95895a"
    }
postData2 = {
        'callCount': '1',
        'page':    '0',
        'httpSessionId':    '',
        'scriptSessionId':   '',
        'c0-scriptName': 'portalAjax',
        'c0-methodName':'getAppList',
        'c0-id':'0',
        'c0-param0':'string:142104994847723324',
        'batchId':'1'
}
r=s.post(dwr_urpurl,headers=headers2,data=postData2)
# print(r.text)
tag=r.text
pattern=pattern = re.compile(r'\?yhlx=student\&login=(\d+)')
m = pattern.findall(tag)
print(m[1])
urp_url="https://ca.nuc.edu.cn/zfca?yhlx=student&login="+m[1]+"&url=zf_loginAction.do\\"
print(urp_url)
urp=s.post(urp_url,data=postData2,headers=headers2)
print(urp.text)
urp_lession_url="http://202.207.177.39:8088/xkAction.do?actionType=6"
headers3 = {
    'x-devtools-emulate-network-conditions-client-id': "9497628b-38b3-47a8-b563-266e8ccd3a1d",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded",
    'accept': "*/*",
    'referer': "http://202.207.177.39:8088/menu/menu.jsp",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'cache-control': "no-cache",
    'postman-token': "7eb9be3a-35b0-2ad5-37ba-564d9b95895a"
    }
urp_lession=s.get(urp_lession_url,headers=headers2)
print(urp_lession.text)
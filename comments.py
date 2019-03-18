# 爬取七里香的歌词评论
# 导入相关模块
import requests, json
# 设置一个初始的commentid
commentid ='song_102065756_1152921504764018089_1552566294'
# 设置各个参数url，params,headers
url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
headers = {
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
for x in range(5):
    params = {
    'g_tk': '5381',
    'loginUin': '0',
    'hostUin': '0',
    'format': 'json',
    'inCharset': 'utf8',
    'outCharset': 'GB2312',
    'notice': '0',
    'platform': 'yqq.json',
    'needNewCode': '0',
    'cid': '205360772',
    'reqtype': '2',
    'biztype': '1',
    'topid': '102065756',
    'cmd': '8',
    'needmusiccrit': '0',
    'pagenum': str(x),
    'pagesize': '25',
    'lasthotcommentid': commentid,
    'domain': 'qq.com',
    'ct': '24',
    'cv': '10101010',
    }
# 访问页面，将获取数据转化为json形式
    res = requests.get(url, params=params, headers=headers)
    js = res.json()
# 匹配歌曲的评论
    list = js['comment']['commentlist']
    for x in list:
        print('----------------\n'+ x['rootcommentcontent'])
    commentid = list[24]['rootcommentid']


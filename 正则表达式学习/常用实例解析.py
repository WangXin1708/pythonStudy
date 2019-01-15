import re
"""
    解析网址
"""
pattern="[a-zA-Z]+://[^\s]*[.com|.cn]"
string="""
<a href="http://www.sina.com">百度首页</a>
"""
result=re.search(pattern,string)
print(result)
"""
    解析电话号码
"""
pattern="\d{4}-\d{7}|\d{3}-\d{8}|\d{11}"
string="13176221906"
result=re.search(pattern,string)
print(result)

"""
    匹配电子邮件地址
"""
string="wangxinel2016@163.com"
string2="91466593@qq.com"
pattern=".*@.*[.com]"
result=re.search(pattern,string)
print(result)
result2=re.search(pattern,string2)
print(result2)
"""
    其他匹配电子邮件的方式
"""
pattern="\w+"
string="srt+skz-ws"
result=re.search(pattern,string)
print(result)
"""
    [.+ -]是. + -中的一个
"""
pattern1="\w+([.+-]\w+)*"
"""
    修改一下string1看看 比如
    string1="iam.sthi"
    string1="iam+sthi"
    string1="iam-sthi"
"""
string1="\n\n\niam-sthi"

result1=re.search(pattern1,string1)
print(result1)



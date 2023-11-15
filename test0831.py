""" 写一个函数，接收秒数，处理成人类友好的方式格式化持续时间。该函数必须接受一个非负整数。如果它是零，它只是返回"now" 。否则，持续时间表示为years 、days 、hours 、minutes 和seconds 的组合 。
举个例子就更容易理解了：
* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
就本题而言，一年是 365 天，一天是 24 小时。
请注意，空格很重要。
细则
生成的表达式由 4 seconds、 1 year等分量组成，一个正整数和一个有效的时间单位之一，由空格分隔。如果整数大于 1，则时间单位以复数形式使用。
组件由逗号和空格 ( ", " ) 分隔。除了最后一个组件用 " and " 分隔， 就像用英文写的一样。
1 second and 1 year 不是正确的，而 1 year and 1 second 是正确 的。
不同的组件有不同的时间单位。所以 5 seconds and 1 second 这样的重复单位写法是错误的。
如果组件的值恰好为零，则组件根本不会出现。因此，1 minute and 0 seconds 是无效的，应该是1 minute 这样编写。
必须“尽可能”使用一个时间单位。这意味着该函数不应该返回61 seconds ，而是应该返回1 minute and 1 second 。所以不要出现366天、24小时、60分、60秒这样的数据。"""
# one:
# def format_duration(seconds: int) -> str:
#     if seconds <= 0:
#         return "now"
#     else:
#         content = {
#             "year": 0,
#             "days": 0,
#             "hour": 0,
#             "minutes": 0,
#             "second": 0
#         }
#         if seconds < 60:
#             content["second"] = seconds
#         while seconds // 60 != 0:
#             content["year"] = seconds // (365 * 24 * 60 * 60)
#             seconds = seconds - content["year"] * (365 * 24 * 60 * 60)
#             content["days"] = seconds // (24 * 60 * 60)
#             seconds = seconds - content["days"] * (24 * 60 * 60)
#             content["hour"] = seconds // (60 * 60)
#             seconds = seconds - content["hour"] * (60 * 60)
#             content["minutes"] = seconds // 60
#             seconds = seconds - content["minutes"] * 60
#             content["second"] = seconds
#         return content

# two:
def format_duration(seconds: int) -> str:
    if seconds <= 0:
        return "now"
    else:
        fcontent = ''
        content = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0
        }
        ltime1 = [365 * 24 * 60 * 60, 24 * 60 * 60, 60 * 60, 60, 1]
        ltime2 = ["year", "day", "hour", "minute", "second"]
        for i in range(len(ltime1)):
            content[i] = seconds // ltime1[i]
            seconds -= content[i] * ltime1[i]
        for j in range(len(ltime2)):
            if content[j] > 1:
                fcontent += str(content[j]) + " " + ltime2[j] + "s" + ", "
            elif content[j] == 1:
                fcontent += str(content[j]) + " " + ltime2[j] + ", "
        fcontent = fcontent[:-2][::-1]
        fcontent = fcontent.replace(",", 'dna ', 1)
        fcontent = fcontent[::-1]
        return fcontent



assert format_duration(0) == "now"
assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
assert format_duration(15731080) == "182 days, 1 hour, 44 minutes and 40 seconds"
assert format_duration(132030240) == "4 years, 68 days, 3 hours and 4 minutes"
assert format_duration(205851834) == "6 years, 192 days, 13 hours, 3 minutes and 54 seconds"
assert format_duration(253374061) == "8 years, 12 days, 13 hours, 41 minutes and 1 second"
assert format_duration(242062374) == "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"
assert format_duration(101956166) == "3 years, 85 days, 1 hour, 9 minutes and 26 seconds"
assert format_duration(33243586) == "1 year, 19 days, 18 hours, 19 minutes and 46 seconds"

from direnumerate import FindPatterns

log = "test.log"
key = "ERROR"

fp = FindPatterns(log)
fp.find_in_log(keyword=key)
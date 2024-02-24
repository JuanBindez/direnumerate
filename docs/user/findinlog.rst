.. _findinlog:

Port Scan:
==========

**If you want to check patterns in logs or other files:**::

        from direnumerate import FindPatterns

        log = "test.log"
        key = "ERROR"

        fp = FindPatterns(log)
        fp.find_in_log(keyword=key)

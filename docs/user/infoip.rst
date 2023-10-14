.. _infoip:

Ip Informations:
=============================

**If you want to check informations about an Ip:**::

        from direnumerate import InfoIp

        ip = "8.8.8.8"

        ipinfo = InfoIp(ip)
        ipinfo.show_info()
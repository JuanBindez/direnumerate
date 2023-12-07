.. _userscan:

User Account Scan:
=============================

**Here you can find user accounts on websites just by passing the username to the search:**::

        from direnumerate import UserScan

        user = "username"

        found = UserScan(user)
        found.found_users()
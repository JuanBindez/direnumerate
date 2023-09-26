def create_wordlist(filename):
    wordlist = [
        "admin",
        "login",
        "images",
        "js",
        "css",
        "config",
        "index",
        "robots.txt",
        "backup",
        "secret",
        "support",
        "contact",
        "blog",
        "forum",
        "product",
        "category",
        "brand",
        "password",
        "123456",
        "qwerty",
        "letmein",
        "access",
        "admin123",
        "administrator",
        "superuser",
        "root",
        "test",
        "guest",
        "demo",
        "webmaster",
        "developer",
        "api",
        "api_key",
        "db",
        "database",
        "user",
        "users",
        "auth",
        "authentication",
        "login.php",
        "wp-admin",
        "wp-login.php",
        "upload",
        "uploads",
        "download",
        "downloads",
        "private",
        "public",
        "static",
        "media",
        "files",
        "file",
        "images/",
        "js/",
        "css/",
        "assets/",
        "images/uploads",
        "userfiles",
        "data",
        "temp",
        "temp/",
        "logs",
        "scripts",
        "web",
        "public_html",
        "secure",
        "private/",
        "backup/",
        "backup_files/",
        "conf",
        "config/",
        "configurations/",
        "install",
        "installer",
        "setup",
        "tmp",
        "db.sql",
        "data.sql",
        "users.sql",
        "passwords.txt",
        "passwd",
        "login.txt",
        "credentials",
        "phpmyadmin",
        "phpMyAdmin",
        "myadmin",
        "myAdmin",
        "panel",
        "control",
        "manager",
        "admin-panel",
        "admin-login",
        "signin",
        "sign-in",
        "login-form",
        "login.html",
        "login.aspx",
        "login.jsp",
        "signin.html",
        "signin.aspx",
        "signin.jsp",
        "register",
        "signup",
        "register.html",
        "register.aspx",
        "signup.html",
        "signup.aspx",
        "forgot-password",
        "forgot-password.html",
        "forgot-password.aspx",
        "reset-password",
        "reset-password.html",
        "reset-password.aspx",
        "contact-us",
        "contact.html",
        "contact.aspx",
        "contact-form",
        "support.html",
        "support.aspx",
        "support-form",
        "about-us",
        "about.html",
        "about.aspx",
        "faq",
        "faq.html",
        "faq.aspx",
        "terms",
        "terms.html",
        "terms.aspx",
        "privacy",
        "privacy.html",
        "privacy.aspx",
        "legal",
        "legal.html",
        "legal.aspx",
        "policy",
        "policy.html",
        "policy.aspx",
        "blog/",
        "news",
        "news.html",
        "news.aspx",
        "articles",
        "articles.html",
        "articles.aspx",
        "events",
        "events.html",
        "events.aspx",
        "products",
        "products.html",
        "products.aspx",
        "services",
        "services.html",
        "services.aspx",
        "portfolio",
        "portfolio.html",
        "portfolio.aspx",
        "gallery",
        "gallery.html",
        "gallery.aspx",
        "download/",
        "downloads/",
        "download-files",
        "download-file",
        "download.html",
        "download.aspx",
        "download.jsp",
        "upload/",
        "uploads/",
        "upload-file",
        "upload.html",
        "upload.aspx",
        "upload.jsp",
        "logout",
        "logout.html",
        "logout.aspx",
        "logout.jsp",
        "signout",
        "signout.html",
        "signout.aspx",
        "signout.jsp",
    ]

    with open(filename, "w") as wordlist_file:
        for word in wordlist:
            wordlist_file.write(word + "\n")
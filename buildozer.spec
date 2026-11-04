[app]
title = NokiaTV
package.name = nokiatv
package.domain = org.nokia.tv
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
version.regex = __version__ = ['"]([^'"]*)['"]
version.filename = %(source.dir)s/main.py
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.permissions = INTERNET,ACCESS_NETWORK_STATE

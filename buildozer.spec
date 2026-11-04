[app]
title = NokiaTV
package.name = nokiatv
package.domain = org.nokia.tv

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*

version = 1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.sdk = 33
android.accept_sdk_license_agreement = True
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET,ACCESS_NETWORK_STATE

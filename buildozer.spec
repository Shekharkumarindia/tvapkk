[app]

# (str) Title of your application
title = NokiaTV

# (str) Package name
package.name = nokiatv

# (str) Package domain (needed for android/ios packaging)
package.domain = org.nokia.tv

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let the .pyc/.pyo files sink)
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.include_patterns = assets/*,images/*,data/*

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if you want to show a loading screen with your app in android
# You should set android.loading_image to use it
android.loading_image = 

# (bool) Fullscreen
fullscreen = 0

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation
#orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build output (i.e. .apk, .aab, .ipa) -- Default is the current directory
bin_dir = ./bin

#
# Android specific
#
[app:android]

# (int) Target Android API, should be as high as possible.
android.api = 33

# (

#!/bin/sh

#
#
# Usage: log.sh <pkgName>
#
#
#
adb shell logcat | grep $1 | grep -E "[intent,broadcast, service]" | tee -a logged.log

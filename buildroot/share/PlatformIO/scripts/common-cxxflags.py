#
# common-cxxflags.py
# Convenience script to apply customizations to CPP flags
#
Import("env")
env.Append(CXXFLAGS=[
  "-Wno-register"
  #"-Wno-incompatible-pointer-types",
  #"-Wno-unused-const-variable",
  #"-Wno-maybe-uninitialized",
  #"-Wno-sign-compare"
])

import datetime
ts = datetime.datetime.now()

import subprocess
revision = (
    subprocess.check_output(["git", "describe", "--tag", "--first-parent"])
    .strip()
    .decode("utf-8")
)
branch = (
    subprocess.check_output(["git", "symbolic-ref", "-q", "--short", "HEAD"])
    .strip()
    .decode("utf-8")
)

env.Append(CPPDEFINES=[
  ('LAST_BUILD_TIME', '\\"%s\\"' % ts.strftime("%Y-%m-%d %Hh%Mm")),
  ('GIT_REV', '\\"%s/%s\\"' % (branch, revision))
])

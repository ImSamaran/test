# source the users bashrc if it exists
if [ -f "${HOME}/.bashrc" ] ; then
  source "${HOME}/.bashrc"
fi

export PATH=$PATH:/usr/x86_64-w64-mingw32/sys-root/mingw/bin
export EDITOR=vi
export CMAKE_LEGACY_CYGWIN_WIN32=0

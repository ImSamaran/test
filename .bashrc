
# If not running interactively, don't do anything
[[ "$-" != *i* ]] && return

export PS1='[\u@\h \w]\$ '
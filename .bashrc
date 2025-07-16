#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# BEGIN MOSTRAR FASTFECH AL ABRIR TERMINAL (BASH)
# Solo en shell interactivo, y dentro de Kitty
if [[ $- == *i* ]] && [[ -n "$KITTY_WINDOW_ID" ]]; then
  fastfetch --config ~/.config/fastfetch/config.jsonc
fi
# END MOSTRAR FASTFECH AL ABRIR TERMINAL (BASH)

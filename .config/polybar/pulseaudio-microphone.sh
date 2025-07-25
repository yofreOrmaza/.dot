#!/bin/sh

status() {
  MUTED=$(pacmd list-sources | awk '/\*/,EOF {print}' | awk '/muted/ {print $2; exit}')

  if [ "$MUTED" = "yes" ]; then
    echo "MIC%{F#FF0B30}OFF%{F-}"
  else
    VOLUME=$(pacmd list-sources | grep "\* index:" -A 7 | grep volume | awk -F/ '{print $2}' | tr -d ' ')
    echo "MIC%{F#00FFAB}$VOLUME%{F-}"
  fi
}

listen() {
    status

    LANG=EN; pactl subscribe | while read -r event; do
        if echo "$event" | grep -q "source" || echo "$event" | grep -q "server"; then
            status
        fi
    done
}

toggle() {
  MUTED=$(pacmd list-sources | awk '/\*/,EOF {print}' | awk '/muted/ {print $2; exit}')

  if [ "$MUTED" = "yes" ]; then
      pactl set-source-mute @DEFAULT_SOURCE@ 0
  else
      pactl set-source-mute @DEFAULT_SOURCE@ 1
  fi
}

increase() {
  pactl set-source-volume @DEFAULT_SOURCE@ +5%
}

decrease() {
  pactl set-source-volume @DEFAULT_SOURCE@ -5%
}

case "$1" in
    --toggle)
        toggle
        ;;
    --increase)
        increase
        ;;
    --decrease)
        decrease
        ;;
    *)
        listen
        ;;
esac

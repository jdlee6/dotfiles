# Disable KWin and use i3gaps as WM
export KDEWM=/usr/bin/i3
# Compositor (Animations, Shadows, Transparency)
# xcompmgr -C
# If you use compton then comment above and uncomment below
compton -cCFb --backend glx --vsync opengl

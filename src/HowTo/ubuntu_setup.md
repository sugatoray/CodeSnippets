# Ubuntu Setup Information

## Display Brightness Manipulation

The commands were found in this stackoverflow post: [Changing the screen brightness of the external screen
][#monitor-brightness-management]

Enlist the existing displays using
```bash
xrandr -q | grep " connected"
```
And then use the following command to set brightness.
```bash
xrandr --output DP-1 --brightness 0.5
xrandr --output HDMI-2 --brightness 0.5
```
Here is a complete output:  

```bash
sugatoray@UbuntuX:~$ xrandr -q | grep " connected"
eDP-1 connected primary 3840x2160+3840+0 (normal left inverted right x axis y axis) 344mm x 194mm
DP-1 connected 3840x2160+0+0 (normal left inverted right x axis y axis) 527mm x 296mm
HDMI-2 connected 3840x2160+7680+0 (normal left inverted right x axis y axis) 527mm x 296mm
sugatoray@UbuntuX:~$ xrandr --output DP-1 --brightness 0.5
sugatoray@UbuntuX:~$ xrandr --output HDMI-2 --brightness 0.5
```

<!--- Ref --->

[#monitor-brightness-management]: https://askubuntu.com/questions/894465/changing-the-screen-brightness-of-the-external-screen#


## References:

1. [Changing the screen brightness of the external screen
][#monitor-brightness-management]

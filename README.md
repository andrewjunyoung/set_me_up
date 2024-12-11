# Setmy

This project automatically sets up your computer to be exactly like AJY's.

# Prerequisites
1. Log into the App Store.
1. Install git through xcode utils, and run the output commands (required in new versions of mac). You can do this by running these scripts:
```
```

# Mandatory setup steps
1. Run `git clone https://github.com/andrewjunyoung/setmy && cd setmy` to clone this repo and enter it.
1. Run `make all` to run all the setup scripts automatically.
1. Complete the following manual setup steps in any order:
 1. [MANUAL] Set up Google Japanese Input using the files in mozc_resources/
 1. [MANUAL] Import your iTerm settings from file.
 1. [MANUAL] Open neovim and run `:Plug install`

CHECK: Set up ZSH
CHECK: Can use settings to set up dock?
CHECK: Set up your keyboards in system settings to use Google Japanese Input; JDvorak; Shuangpin input (default keybindings).
CHECK: Delete default US keyboard using `make force_remove_us_keyboard` and restart

# Optional setup steps

- Rename your computer

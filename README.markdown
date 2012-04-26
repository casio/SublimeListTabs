# List Tabs 

Shows a quick panel with all of the open tabs. 

I personally don't like showing the sidebar or  tabs so I use this to
navigate open files or get a quick overview of what I have open on-
demand when I need it.

To install it simply 

    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    git clone https://mads379@github.com/mads379/SublimeListTabs.git

Now add a key-binding

    { "keys": ["super+t"], "command": "list_tabs"},

# TODO

- The default view should be the most recent one. This makes it easy
  to toggle between two files.
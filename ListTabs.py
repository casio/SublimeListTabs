import sublime, sublime_plugin, os

class ListTabsCommand(sublime_plugin.WindowCommand):
  """
    Shows a quick panel with all of the open tabs. 

    I personally don't like showing the sidebar or 
    tabs so I use this to navigate open files or get
    a quick overview of what I have open on-demand when
    I need it.

    Open the sublime console and write the following
    to try it out. 
      
      window.run_command("list_tabs")

    /Mads
  """

  # Keeps a stack of the most recent visited views for each window
  # i.e. it's a Map from Windows to a Stack of views.
  stack_map = {}

  def description():
    "Navigate to open tabs."

  def run(self):
    # The views that are open in this group
    views = self.window.views_in_group(self.window.active_group())    

    # Re-arrange them such that the most recent one is on top.
    if len(self.stack_for_window()) > 0:
      recent = self.stack_for_window().pop()
      f = lambda x: self.name_for_view(x) != self.name_for_view(recent)
      views = [recent] + filter(f, views)


    def callback(index):
      if index != -1:
        self.stack_for_window().append(self.window.active_view())
        self.window.focus_view(views[index])

    def itm(v):
      if v.file_name() == None:
        return [self.name_for_view(v), "Unsaved document"]
      else: 
        return [self.name_for_view(v), v.file_name()]

    open_files = [ itm(v) for v in views]

    self.window.show_quick_panel(open_files, callback)

  def name_for_view(self, v): 
    """Given a view, create a string used as display name for
       that view. """
    if v.file_name() == None:
      return "untitled-" + str(v.id())
    else: 
      return os.path.split(v.file_name())[1]

  def stack_for_window(self):
    """Returns the stack of views for the current window."""
    stack = ListTabsCommand.stack_map.get(self.window)
    if stack == None:
      stack = []
      ListTabsCommand.stack_map.setdefault(self.window, stack)
    return stack
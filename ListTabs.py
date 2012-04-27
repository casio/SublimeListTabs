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

  # Keeps the views that have most recently been visited.
  stack = []

  def description():
    "Navigate to open tabs."

  def run(self):

    views = self.window.views_in_group(self.window.active_group())    

    def callback(index):
      if index != -1:
        ListTabsCommand.stack.append(self.window.active_view())
        self.window.focus_view(views[index])

    def itm(v):
      if v.file_name() == None:
        return ["untitled-" + str(v.id()), "Unsaved document"]
      else: 
        return [os.path.split(v.file_name())[1], v.file_name()]

    open_files = [ itm(v) for v in views]

    self.window.show_quick_panel(open_files, callback)


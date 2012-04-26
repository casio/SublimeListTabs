import sublime, sublime_plugin

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

  def description():
    "Navigate to open tabs."

  def run(self):

    views = self.window.views_in_group(self.window.active_group())    

    def callback(index):
      if index != -1:
        self.window.focus_view(views[index])

    
    open_files = [ [v.file_name().split("/").pop(), v.file_name()] for v in views]

    self.window.show_quick_panel(open_files, callback)



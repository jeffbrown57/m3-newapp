from ._anvil_designer import AboutTemplate
from anvil import *
import anvil.server
from ..Contact import Contact

class About(AboutTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def menu_item_about_click(self, **event_args):
        """This method is called when the component is clicked"""
        form = Contact()
        open_form(form)
     

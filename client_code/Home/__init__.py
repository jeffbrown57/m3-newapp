from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
from ..About import About
from ..Contact import Contact


class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        # label and button added dynamically
        lp = LinearPanel(background="lightgreen")
        lp.add_component(Label(text="Hello"))
        lp.add_component(Button(text="Click me"))
        self.layout.add_component(lp)
        

    def navigation_link_about_click(self, **event_args):
        """This method is called when the component is clicked"""
        form = About()
        open_form(form)
        pass

from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
#from ..About import About
#from ..Contact import Contact

class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        # label and button added dynamically

        
        #lp = LinearPanel(background="lightgreen")
        #lp.add_component(Label(text="Hello"))
        #lp.add_component(btn_on)
        #self.layout.add_component(lp)
        

    def navigation_link_about_click(self, **event_args):
        """This method is called when the component is clicked"""
        form = About()
        open_form(form)
        pass

    def button_submit_click(self, **event_args):
        """This method is called when the component is clicked."""
        #name = self.text_box_name.text
        #email = self.text_box_email.text
        Notification(f"Name: {self.text_box_name.text}\nEmail: {self.text_box_email.text}")
        pass

   
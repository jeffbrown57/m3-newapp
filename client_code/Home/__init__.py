from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
from ..About import About
from ..Contact import Contact
from anvil.js.window import document

#document.addEventListener("click", btn_int_click)

class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        # label and button added dynamically

        btn_on = Button(text="Click Me")
        lp = LinearPanel(background="lightgreen")
        lp.add_component(Label(text="Hello"))
        lp.add_component(btn_on)
        self.layout.add_component(lp)
        
       

    def btn_on_click(self, **event_args):
        """ dynamic button ???"""  
        self.xname = self.text_box_name.text
        self.xemail = self.text_box_email.text
        self.position = self.text_box_position.text
        Notification(f"Name: {self.xname}\nEmail: {self.xemail}").show()
        
    document.addEventListener("click", btn_on_click)

    def navigation_link_about_click(self, **event_args):
        """This method is called when the component is clicked"""
        form = About()
        open_form(form)
        pass

   
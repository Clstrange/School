from breezypythongui import EasyFrame, EasyDialog
from Bookrecommendations import friends, recommend, report
  
#   x = []

class Recommendations(EasyFrame):

    """Application window for the tax calculator."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Book Recommendations")
        self.setBackground("powder blue")
  

        # The command buttons
        self.addButton(
                text = "Report", 
                row = 5, 
                column = 4,
                command = self.report
                )

        self.addButton(
                text = "Recomendations", 
                row = 5, 
                column = 3,
                command = self.recommend_recieved
                )

        self.addButton(
                text = "Friends", 
                row = 5, 
                column = 1,
                command = self.friend_recieved
                )
    # The message boxes
    def friend_recieved(self):
        BookDialog(self, 'friends')

    def recommend_recieved(self):
        BookDialog(self, 'recommend')

    def report(self):

        self.messageBox(
            title = "Report",
            message=  report(),
            width = 70,
            height = 50,
        )

class BookDialog(EasyDialog):

    def __init__(self, parent, title):
        """Creates dialog box as child to BookGui"""

        EasyDialog.__init__(self, parent, title)

    def body(self, parent):
        self.addLabel(parent, text="Reader:", row=0, column=0, sticky="W")
        self.readerField = self.addTextField(parent, text="", row=0, column=1, sticky="W")

    def apply(self):
        reader = self.readerField.getText().capitalize()

        if self.title() == 'friends':
            friendList = ""
            for name in friends(reader):
                friendList += f"{name}\n"
            self.messageBox(title=f"Friends of {reader}", width=30, height=50, message=friendList)

        else:
            bookList = ""
            for (author, book) in recommend(reader):
                bookList += f"{author}, {book}\n"
            self.messageBox(title=f"Recommendations for {reader}", width=53, height=len(bookList.split("\n")),
                            message=bookList)




        
  
 
#Instantiate and pop up the window.
Recommendations().mainloop()


"""This is the main file of Magistrado's Rental Management Application. 


Description:
    When you run this python file, it will show you a hero page that has a clickable START button. Upon clicking the START button, the background or canvas will change and will show you the dashboard page. You can click the navigation menu such as utilities, payments, and receipt. This application will ease the work of the caretaker of the apartment.

How to run the Program:
    1. Click START Button.
    2. Read the data in the dashboard page. If there is any vacancy, post an advertisement on your social media about the apartment. The profit card will show you the total income you have for the current month in which you can confirm if it reflects on the bank account.
    3. If you click the utilities in the navigation bar, you will see entry boxes where you can input the total bill for the apartment, and their previous and present consumption. The application will automatically compute the rate for each unit and will show their total bill.
    4. If you click the payments in the navigation bar, you will see checkboxes. Check a box if the tenant made a payment for the rent.
    5. You can click the receipt in the navigation bar for the summary of the bills that are needed to be paid by tenants.

Defined Function(s):
    start_btn_clicked()
"""

__author__ = "Reuel Magistrado"
__date__ = "July 16, 2022"
__version__ = "1.0.1"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"
__status__ = "Development"
# ---------------------------------


from tkinter import *
from helper_functions.navigation import view_home


window = Tk()
window.geometry("1024x768")


def start_btn_clicked():
    """Upon clicking the START button in the hero page, it will redirect you to the dashboard page of the program. It calls the view_home function and deletes the start button in the hero page so it won't appear in the background.

    Parameters: None
    Return: None
    """

    view_home(
        window=window,
        canvas=canvas,
        canvas_container=background,
        images_list=images,
    )

    start_btn.destroy()  # Destroy start button widget


# Create PhotoImage objects
# and save each of them into a variable
welcome_bg_img = PhotoImage(file=f"final_project/images/welcomebg.png")
start_btn_img = PhotoImage(file=f"final_project/images/startbtn.png")
dashboard_bg_img = PhotoImage(file=f"final_project/images/dashboardbg.png")
home_btn_img = PhotoImage(file=f"final_project/images/homebtn.png")
utilities_btn_img = PhotoImage(file=f"final_project/images/utilitiesbtn.png")
payments_btn_img = PhotoImage(file=f"final_project/images/paymentsbtn.png")
receipt_btn_img = PhotoImage(file=f"final_project/images/receiptbtn.png")
utilities_bg_img = PhotoImage(file=f"final_project/images/utilitiesbg.png")
payments_bg_img = PhotoImage(file=f"final_project/images/paymentsbg.png")
receipts_bg_img = PhotoImage(file=f"final_project/images/receiptsbg.png")


# Store the images into a list for readability purposes
# when passed as an argument
images = [
    home_btn_img,
    utilities_btn_img,
    payments_btn_img,
    receipt_btn_img,
    dashboard_bg_img,
    utilities_bg_img,
    payments_bg_img,
    receipts_bg_img,
]

# Create a canvas where the other widgets will be placed into.
# Save into a variable to be passed as an argument of view_home function
canvas = Canvas(
    window,
    bg="#ffffff",
    height=768,
    width=1024,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
canvas.place(x=0, y=0)

# Create a canvas container
# and store into a variable
# to be passed as an argument
background = canvas.create_image(512.0, 384.0, image=welcome_bg_img)


# Create START BUTTON
start_btn = Button(
    image=start_btn_img,
    borderwidth=0,
    highlightthickness=0,
    command=start_btn_clicked,
    relief="flat",
)
# Place START button in a specified location
start_btn.place(x=429, y=510, width=165, height=71)


# Disable resizing
window.resizable(False, False)
window.mainloop()

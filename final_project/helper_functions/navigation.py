from tkinter import *
from constants import *


#----------------------#
#----------------------#
#----DASHBOARD PAGE----#
#----------------------#
#----------------------#
def view_home(canvas, canvas_container, images_list):
    # Function headers comments that describe the purpose of the function. Don’t restate the name of the function. Describe the scope (range and domain) of inputs and outputs.2
    """It shows the dashboard page of the Rental Management Application. It doesn't have a domain, but its ranges are showing how many vacancies are there and how much profit you gained for the current month. The ranges automatically updates depending on the other data like payments.

    Parameters
        canvas: the area where the background will be placed
        canvas_container: background of the page
        images_list: list of images for the whole application

    Return: None
    """

    # Access the images in the images_list 
    # and save them each into a variable
    dashboard_bg = images_list[DASHBOARD_BG_IMG_INDEX]
    home_btn_img = images_list[HOME_BTN_IMG_INDEX]
    utilities_btn_img = images_list[UTILITIES_BTN_IMG_INDEX]
    payments_btn_img = images_list[PAYMENTS_BTN_IMG_INDEX]
    receipt_btn_img = images_list[RECEIPT_BTN_IMG_INDEX]


    def utilities_btn_clicked():

        view_utilities(
            canvas, canvas_container, images_list
        )
        canvas.delete(profit)
        canvas.delete(vacancy)

    def payments_btn_clicked():
        print("payments_btn_clicked")

    def receipt_btn_clicked():
        print("receipt_btn_clicked")

    canvas.itemconfig(canvas_container, image=dashboard_bg)
    profit = canvas.create_text(
        646.0, 365.5, text="1", fill="#fff", font=("Poppins-Bold", int(96.0))
    )

    vacancy = canvas.create_text(
        152.0, 365.5, text="1", fill="#fff", font=("Poppins-Bold", int(96.0))
    )

    home_btn = Button(
        image=home_btn_img,
        borderwidth=0,
        highlightthickness=0,
        # command=home_btn_clicked,
        relief="flat",
    )

    home_btn.place(x=0, y=-3, width=475, height=68)

    utilities_btn = Button(
        image=utilities_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=utilities_btn_clicked,
        relief="flat",
    )

    utilities_btn.place(x=493, y=0, width=157, height=52)

    payments_btn = Button(
        image=payments_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=payments_btn_clicked,
        relief="flat",
    )

    payments_btn.place(x=667, y=0, width=157, height=52)

    receipt_btn = Button(
        image=receipt_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=receipt_btn_clicked,
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)



#----------------------#
#----------------------#
#----UTILITIES PAGE----#
#----------------------#
#----------------------#
def view_utilities(
    canvas, canvas_container, images_list
):

    utilities_bg = images_list[UTILITIES_BG_IMG_INDEX]
    home_btn_img = images_list[HOME_BTN_IMG_INDEX]
    utilities_btn_img = images_list[UTILITIES_BTN_IMG_INDEX]
    payments_btn_img = images_list[PAYMENTS_BTN_IMG_INDEX]
    receipt_btn_img = images_list[RECEIPT_BTN_IMG_INDEX]

    def home_btn_clicked():
        view_home(
            canvas, canvas_container, images_list
        )
        for entry_box in entry_boxes:
            entry_box.destroy()

        for text in canvas_texts:
            canvas.delete(text)
    

    def btn_clicked():
        print("Button Clicked")

    canvas.itemconfig(canvas_container, image=utilities_bg)

    home_btn = Button(
        image=home_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=home_btn_clicked,
        relief="flat",
    )

    home_btn.place(x=0, y=-3, width=475, height=68)

    utilities_btn = Button(
        image=utilities_btn_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
    )

    utilities_btn.place(x=493, y=0, width=157, height=52)

    payments_btn = Button(
        image=payments_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    payments_btn.place(x=667, y=0, width=157, height=52)

    receipt_btn = Button(
        image=receipt_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)

    unit_a_elecbill = canvas.create_text(
        450.0, 357.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_a_waterbill = canvas.create_text(
        949.0, 357.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_b_elecbill = canvas.create_text(
        450.0, 413.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_b_waterbill = canvas.create_text(
        949.0, 413.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_c_elecbill = canvas.create_text(
        450.0, 469.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_c_waterbill = canvas.create_text(
        949.0, 469.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_d_elecbill = canvas.create_text(
        450.0, 525.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_d_waterbill = canvas.create_text(
        949.0, 525.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_e_elecbill = canvas.create_text(
        450.0, 581.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_e_waterbill = canvas.create_text(
        949.0, 581.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_f_elecbill = canvas.create_text(
        450.0, 637.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_f_waterbill = canvas.create_text(
        949.0, 637.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    unit_a_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_prev_elec.place(x=174, y=342, width=93, height=29)

    unit_a_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_prev_water.place(x=673, y=342, width=93, height=29)

    total_bill_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    total_bill_elec.place(x=174, y=152, width=215, height=29)

    total_bill_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    total_bill_water.place(x=673, y=152, width=215, height=29)

    unit_b_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_prev_elec.place(x=174, y=398, width=93, height=29)

    unit_b_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_prev_water.place(x=673, y=398, width=93, height=29)

    unit_c_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_prev_elec.place(x=174, y=454, width=93, height=29)

    unit_c_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_prev_water.place(x=673, y=454, width=93, height=29)

    unit_d_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_prev_elec.place(x=174, y=510, width=93, height=29)

    unit_d_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_prev_water.place(x=673, y=510, width=93, height=29)

    unit_e_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_prev_elec.place(x=174, y=566, width=93, height=29)

    unit_e_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_prev_water.place(x=673, y=566, width=93, height=29)

    unit_f_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_prev_elec.place(x=174, y=622, width=93, height=29)

    unit_f_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_prev_water.place(x=673, y=622, width=93, height=29)

    unit_a_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_present_elec.place(x=296, y=342, width=93, height=29)

    unit_a_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_present_water.place(x=795, y=342, width=93, height=29)

    unit_b_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_present_elec.place(x=296, y=398, width=93, height=29)

    unit_b_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_present_water.place(x=795, y=398, width=93, height=29)

    unit_c_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_present_elec.place(x=296, y=454, width=93, height=29)

    unit_c_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_present_water.place(x=795, y=454, width=93, height=29)

    unit_d_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_present_elec.place(x=296, y=510, width=93, height=29)

    unit_d_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_present_water.place(x=795, y=510, width=93, height=29)

    unit_e_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_present_elec.place(x=296, y=566, width=93, height=29)

    unit_e_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_present_water.place(x=795, y=566, width=93, height=29)

    unit_f_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_present_elec.place(x=296, y=622, width=93, height=29)

    unit_f_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_present_water.place(x=795, y=622, width=93, height=29)

    meralco_rate = canvas.create_text(
        281.5, 217.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    maynilad_rate = canvas.create_text(
        780.5, 217.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    entry_boxes = [
        total_bill_elec,
        total_bill_water,
        unit_a_prev_elec,
        unit_a_prev_water,
        unit_b_prev_elec,
        unit_b_prev_water,
        unit_c_prev_elec,
        unit_c_prev_water,
        unit_d_prev_elec,
        unit_d_prev_water,
        unit_e_prev_elec,
        unit_e_prev_water,
        unit_f_prev_elec,
        unit_f_prev_water,
        unit_a_present_elec,
        unit_a_present_water,
        unit_b_present_elec,
        unit_b_present_water,
        unit_c_present_elec,
        unit_c_present_water,
        unit_d_present_elec,
        unit_d_present_water,
        unit_e_present_elec,
        unit_e_present_water,
        unit_f_present_elec,
        unit_f_present_water,
    ]

    canvas_texts = [
        meralco_rate,
        maynilad_rate,
        unit_a_elecbill,
        unit_a_waterbill,
        unit_b_elecbill,
        unit_b_waterbill,
        unit_c_elecbill,
        unit_c_waterbill,
        unit_d_elecbill,
        unit_d_waterbill,
        unit_e_elecbill,
        unit_e_waterbill,
        unit_f_elecbill,
        unit_f_waterbill,
    ]

from cgitb import text
from tkinter import *
from constants import *
import tkinter.font as font
from helper_functions.calc import *


# ----------------------#
# ----DASHBOARD PAGE----#
# ----------------------#
def view_home(window, canvas, canvas_container, images_list):
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

        view_utilities(window, canvas, canvas_container, images_list)
        canvas.delete(profit)
        canvas.delete(vacancy)

    def payments_btn_clicked():
        view_payments(window, canvas, canvas_container, images_list)
        canvas.delete(profit)
        canvas.delete(vacancy)

    def receipts_btn_clicked():
        view_receipts(window, canvas, canvas_container, images_list)
        canvas.delete(profit)
        canvas.delete(vacancy)

    canvas.itemconfig(canvas_container, image=dashboard_bg)
    profit = canvas.create_text(
        646.0, 365.5, text="0", fill="#fff", font=("Poppins-Bold", int(96.0))
    )

    vacancy = canvas.create_text(
        152.0, 365.5, text="0", fill="#fff", font=("Poppins-Bold", int(96.0))
    )

    home_btn = Button(
        image=home_btn_img,
        borderwidth=0,
        highlightthickness=0,
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
        command=receipts_btn_clicked,
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)


# ----------------------#
# ----UTILITIES PAGE----#
# ----------------------#
def view_utilities(window, canvas, canvas_container, images_list):

    utilities_bg = images_list[UTILITIES_BG_IMG_INDEX]
    home_btn_img = images_list[HOME_BTN_IMG_INDEX]
    utilities_btn_img = images_list[UTILITIES_BTN_IMG_INDEX]
    payments_btn_img = images_list[PAYMENTS_BTN_IMG_INDEX]
    receipt_btn_img = images_list[RECEIPT_BTN_IMG_INDEX]

    def home_btn_clicked():
        view_home(window, canvas, canvas_container, images_list)
        for entry_box in entry_boxes:
            entry_box.destroy()

        for text in canvas_texts:
            canvas.delete(text)

    def payments_btn_clicked():
        view_payments(window, canvas, canvas_container, images_list)
        for entry_box in entry_boxes:
            entry_box.destroy()

        for text in canvas_texts:
            canvas.delete(text)

    def receipts_btn_clicked():
        view_receipts(window, canvas, canvas_container, images_list)
        for entry_box in entry_boxes:
            entry_box.destroy()

        for text in canvas_texts:
            canvas.delete(text)

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
        command=payments_btn_clicked,
        relief="flat",
    )

    payments_btn.place(x=667, y=0, width=157, height=52)

    receipt_btn = Button(
        image=receipt_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=receipts_btn_clicked,
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)

    unit_a_elecbill = canvas.create_text(
        450.0, 357.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_b_elecbill = canvas.create_text(
        450.0, 413.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_c_elecbill = canvas.create_text(
        450.0, 469.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_d_elecbill = canvas.create_text(
        450.0, 525.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_e_elecbill = canvas.create_text(
        450.0, 581.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_f_elecbill = canvas.create_text(
        450.0, 637.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )


    unit_a_waterbill = canvas.create_text(
        949.0, 357.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_b_waterbill = canvas.create_text(
        949.0, 413.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_c_waterbill = canvas.create_text(
        949.0, 469.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_d_waterbill = canvas.create_text(
        949.0, 525.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_e_waterbill = canvas.create_text(
        949.0, 581.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )
    unit_f_waterbill = canvas.create_text(
        949.0, 637.5, text="0", fill="#000000", font=("Poppins-Regular", int(16.0))
    )

    # Electricity Bill Entry Boxes

    total_bill_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    total_bill_elec.place(x=174, y=152, width=215, height=29)

    # Previous Electricity Consumption
    unit_a_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_prev_elec.place(x=174, y=342, width=93, height=29)
    
    # Present Electricity Consumption
    unit_a_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_present_elec.place(x=296, y=342, width=93, height=29)

    # Previous Electricity Consumption
    unit_b_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_prev_elec.place(x=174, y=398, width=93, height=29)

    # Present Electricity Consumption
    unit_b_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_present_elec.place(x=296, y=398, width=93, height=29)

    # Previous Electricity Consumption
    unit_c_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_prev_elec.place(x=174, y=454, width=93, height=29)

    # Present Electricity Consumption
    unit_c_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_present_elec.place(x=296, y=454, width=93, height=29)
    
    # Previous Electricity Consumption
    unit_d_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_prev_elec.place(x=174, y=510, width=93, height=29)
    
    # Present Electricity Consumption
    unit_d_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_present_elec.place(x=296, y=510, width=93, height=29)

    # Previous Electricity Consumption
    unit_e_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_prev_elec.place(x=174, y=566, width=93, height=29)

    # Present Electricity Consumption
    unit_e_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_present_elec.place(x=296, y=566, width=93, height=29)

    # Previous Electricity Consumption
    unit_f_prev_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_prev_elec.place(x=174, y=622, width=93, height=29)

    # Present Electricity Consumption
    unit_f_present_elec = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_present_elec.place(x=296, y=622, width=93, height=29)


    # Water Bill Entry Boxes

    total_bill_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    total_bill_water.place(x=673, y=152, width=215, height=29)

    # Previous Water Consumption
    unit_a_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_prev_water.place(x=673, y=342, width=93, height=29)

    # Present Water Consumption
    unit_a_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_a_present_water.place(x=795, y=342, width=93, height=29)

    # Previous Water Consumption
    unit_b_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_prev_water.place(x=673, y=398, width=93, height=29)

    # Present Water Consumption
    unit_b_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_b_present_water.place(x=795, y=398, width=93, height=29)

    # Previous Water Consumption
    unit_c_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_prev_water.place(x=673, y=454, width=93, height=29)

    # Present Water Consumption
    unit_c_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_c_present_water.place(x=795, y=454, width=93, height=29)

    # Previous Water Consumption
    unit_d_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_prev_water.place(x=673, y=510, width=93, height=29)

    # Present Water Consumption
    unit_d_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_d_present_water.place(x=795, y=510, width=93, height=29)

    # Previous Water Consumption
    unit_e_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_prev_water.place(x=673, y=566, width=93, height=29)

    # Present Water Consumption
    unit_e_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_e_present_water.place(x=795, y=566, width=93, height=29)

    # Previous Water Consumption
    unit_f_prev_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_prev_water.place(x=673, y=622, width=93, height=29)

    # Present Water Consumption
    unit_f_present_water = Entry(bd=0, bg="#fff", highlightthickness=0)
    unit_f_present_water.place(x=795, y=622, width=93, height=29)


    # Font Format for Buttons in Utilities page
    btn_font = font.Font(family="Poppins-Bold", size=12, weight="bold")
    
    compute_elecbill_btn = Button(
        text="COMPUTE",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: compute_elec_bill(
            canvas,
            total_bill_elec,
            unit_a_prev_elec,
            unit_b_prev_elec,
            unit_c_prev_elec,
            unit_d_prev_elec,
            unit_e_prev_elec,
            unit_f_prev_elec,
            unit_a_present_elec,
            unit_b_present_elec,
            unit_c_present_elec,
            unit_d_present_elec,
            unit_e_present_elec,
            unit_f_present_elec,
            unit_a_elecbill,
            unit_b_elecbill,
            unit_c_elecbill,
            unit_d_elecbill,
            unit_e_elecbill,
            unit_f_elecbill,
            meralco_rate,
        ),
        relief="flat",
    )
    compute_elecbill_btn["font"] = btn_font
    compute_elecbill_btn.place(x=174, y=678, width=93, height=52)

    save_elecbill_btn = Button(
        text="SAVE",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        # command=utilities_btn_clicked,
        relief="flat",
    )
    save_elecbill_btn["font"] = btn_font
    save_elecbill_btn.place(x=296, y=678, width=93, height=52)

    compute_waterbill_btn = Button(
        text="COMPUTE",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        # command=utilities_btn_clicked,
        relief="flat",
    )
    compute_waterbill_btn["font"] = btn_font
    compute_waterbill_btn.place(x=673, y=678, width=93, height=52)

    save_waterbill_btn = Button(
        text="SAVE",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        # command=utilities_btn_clicked,
        relief="flat",
    )
    save_waterbill_btn["font"] = btn_font
    save_waterbill_btn.place(x=795, y=678, width=93, height=52)

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
        compute_elecbill_btn,
        compute_waterbill_btn,
        save_elecbill_btn,
        save_waterbill_btn,
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


# ----------------------#
# -----PAYMENTS PAGE----#
# ----------------------#
def view_payments(window, canvas, canvas_container, images_list):
    home_btn_img = images_list[HOME_BTN_IMG_INDEX]
    utilities_btn_img = images_list[UTILITIES_BTN_IMG_INDEX]
    payments_btn_img = images_list[PAYMENTS_BTN_IMG_INDEX]
    receipt_btn_img = images_list[RECEIPT_BTN_IMG_INDEX]
    payments_bg = images_list[PAYMENTS_BG_IMG_INDEX]

    def home_btn_clicked():
        view_home(window, canvas, canvas_container, images_list)
        for checkbutton in checkbuttons:
            checkbutton.destroy()

    def utilities_btn_clicked():
        view_utilities(window, canvas, canvas_container, images_list)
        for checkbutton in checkbuttons:
            checkbutton.destroy()

    def receipts_btn_clicked():
        view_receipts(window, canvas, canvas_container, images_list)
        for checkbutton in checkbuttons:
            checkbutton.destroy()

    canvas.itemconfig(canvas_container, image=payments_bg)

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
        command=utilities_btn_clicked,
        relief="flat",
    )

    utilities_btn.place(x=493, y=0, width=157, height=52)

    payments_btn = Button(
        image=payments_btn_img,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
    )

    payments_btn.place(x=667, y=0, width=157, height=52)

    receipt_btn = Button(
        image=receipt_btn_img,
        borderwidth=0,
        highlightthickness=0,
        command=receipts_btn_clicked,
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)

    var1 = IntVar()
    unita_paid_btn = Checkbutton(
        window,
        variable=var1,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unita_paid_btn.place(x=471, y=202, width=32, height=30)

    var2 = IntVar()
    unita_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var2,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unita_vacant_btn.place(x=696, y=202, width=40, height=30)

    var3 = IntVar()
    unitb_paid_btn = Checkbutton(
        window,
        variable=var3,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitb_paid_btn.place(x=471, y=270, width=32, height=30)


    var4 = IntVar()
    unitb_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var4,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitb_vacant_btn.place(x=696, y=270, width=40, height=30)



    var5 = IntVar()
    unitc_paid_btn = Checkbutton(
        window,
        variable=var5,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitc_paid_btn.place(x=471, y=338, width=32, height=30)

    var6 = IntVar()
    unitc_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var6,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitc_vacant_btn.place(x=696, y=338, width=40, height=30)

    var7 = IntVar()
    unitd_paid_btn = Checkbutton(
        window,
        variable=var7,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitd_paid_btn.place(x=471, y=407, width=32, height=30)

    var8 = IntVar()
    unitd_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var8,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitd_vacant_btn.place(x=696, y=407, width=40, height=30)

    var9 = IntVar()
    unite_paid_btn = Checkbutton(
        window,
        variable=var9,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unite_paid_btn.place(x=471, y=475, width=32, height=30)


    var10 = IntVar()
    unite_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var10,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unite_vacant_btn.place(x=696, y=475, width=40, height=30)


    var11 = IntVar()
    unitf_paid_btn = Checkbutton(
        window,
        variable=var11,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitf_paid_btn.place(x=471, y=543, width=32, height=30)

    var12 = IntVar()
    unitf_vacant_btn = Checkbutton(
        window,
        text="Yes",
        variable=var12,
        onvalue=1,
        offvalue=0,
        bg="#E1E1E1",
        activebackground="#E1E1E1",
    )
    unitf_vacant_btn.place(x=696, y=543, width=40, height=30)

    checkbuttons = [
        unita_paid_btn,
        unitb_paid_btn,
        unitc_paid_btn,
        unitd_paid_btn,
        unite_paid_btn,
        unitf_paid_btn,
        unita_vacant_btn,
        unitb_vacant_btn,
        unitc_vacant_btn,
        unitd_vacant_btn,
        unite_vacant_btn,
        unitf_vacant_btn
    ]



# ----------------------#
# -----RECEIPTS PAGE----#
# ----------------------#
def view_receipts(window, canvas, canvas_container, images_list):
    home_btn_img = images_list[HOME_BTN_IMG_INDEX]
    utilities_btn_img = images_list[UTILITIES_BTN_IMG_INDEX]
    payments_btn_img = images_list[PAYMENTS_BTN_IMG_INDEX]
    receipt_btn_img = images_list[RECEIPT_BTN_IMG_INDEX]
    receipts_bg = images_list[RECEIPTS_BG_IMG_INDEX]

    def home_btn_clicked():
        view_home(window, canvas, canvas_container, images_list)
        for button in buttons:
            button.destroy()

    def utilities_btn_clicked():
        view_utilities(window, canvas, canvas_container, images_list)
        for button in buttons:
            button.destroy()

    def payments_btn_clicked():
        view_payments(window, canvas, canvas_container, images_list)
        for button in buttons:
            button.destroy()

    def btn_clicked():
        print("Button Clicked")

    canvas.itemconfig(canvas_container, image=receipts_bg)

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
        relief="flat",
    )

    receipt_btn.place(x=841, y=0, width=157, height=52)

    btn_font = font.Font(family="Poppins-Bold", size=20, weight="bold")

    btn_a = Button(
        text="Unit A",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_a["font"] = btn_font
    btn_a.place(x=219, y=202, width=150, height=67)

    btn_b = Button(
        text="Unit B",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_b["font"] = btn_font
    btn_b.place(x=667, y=202, width=150, height=67)

    btn_c = Button(
        text="Unit C",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_c["font"] = btn_font
    btn_c.place(x=219, y=350, width=150, height=67)

    btn_d = Button(
        text="Unit D",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_d["font"] = btn_font
    btn_d.place(x=667, y=350, width=150, height=67)

    btn_e = Button(
        text="Unit E",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_e["font"] = btn_font
    btn_e.place(x=219, y=498, width=150, height=67)

    btn_f = Button(
        text="Unit F",
        bg="#FFE600",
        activebackground="#000",
        activeforeground="#FFE600",
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat",
    )

    btn_f["font"] = btn_font
    btn_f.place(x=667, y=498, width=150, height=67)

    buttons = [btn_a, btn_b, btn_c, btn_d, btn_e, btn_f]

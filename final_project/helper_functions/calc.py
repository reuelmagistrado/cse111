from cgitb import text


def compute_unita_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_unitb_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_unitc_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_unitd_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_unite_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_unitf_electricity(canvas, prev, present, bill):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption
    # canvas.itemconfig(bill, text=total_consumption)

    return total_consumption


def compute_meralco_rate():
    pass


def compute_elec_bill(
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
):
    unita_elec_consumption = compute_unita_electricity(
        canvas, unit_a_prev_elec, unit_a_present_elec, unit_a_elecbill
    )

    unitb_elec_consumption = compute_unitb_electricity(
        canvas, unit_b_prev_elec, unit_b_present_elec, unit_b_elecbill
    )

    unitc_elec_consumption = compute_unitc_electricity(
        canvas, unit_c_prev_elec, unit_c_present_elec, unit_c_elecbill
    )

    unitd_elec_consumption = compute_unitd_electricity(
        canvas, unit_d_prev_elec, unit_d_present_elec, unit_d_elecbill
    )

    unite_elec_consumption = compute_unite_electricity(
        canvas, unit_e_prev_elec, unit_e_present_elec, unit_e_elecbill
    )

    unitf_elec_consumption = compute_unitf_electricity(
        canvas, unit_f_prev_elec, unit_f_present_elec, unit_f_elecbill
    )

    total_consumption = (
        unita_elec_consumption
        + unitb_elec_consumption
        + unitc_elec_consumption
        + unitd_elec_consumption
        + unite_elec_consumption
        + unitf_elec_consumption
    )

    bill = total_bill_elec.get()

    electricity_rate = float(bill) / total_consumption

    canvas.itemconfig(meralco_rate, text=f"{electricity_rate:.2f}")

    unita_elec = unita_elec_consumption * electricity_rate
    canvas.itemconfig(unit_a_elecbill,text=f"{unita_elec:.2f}")

    unitb_elec = unitb_elec_consumption * electricity_rate
    canvas.itemconfig(unit_b_elecbill,text=f"{unitb_elec:.2f}")

    unitc_elec = unitc_elec_consumption * electricity_rate
    canvas.itemconfig(unit_c_elecbill,text=f"{unitc_elec:.2f}")

    unitd_elec = unitd_elec_consumption * electricity_rate
    canvas.itemconfig(unit_d_elecbill,text=f"{unitd_elec:.2f}")

    unite_elec = unite_elec_consumption * electricity_rate
    canvas.itemconfig(unit_e_elecbill,text=f"{unite_elec:.2f}")

    unitf_elec = unitf_elec_consumption * electricity_rate
    canvas.itemconfig(unit_f_elecbill,text=f"{unitf_elec:.2f}")


def compute_unita_water():
    pass


def compute_unitb_water():
    pass


def compute_unitc_water():
    pass


def compute_unitd_water():
    pass


def compute_unite_water():
    pass


def compute_unitf_water():
    pass


# def compute_total_water(canvas, meralco_rate, total_bill_elec):
#     value = total_bill_elec.get()
#     electricity_bill = float(value) / 6
#     canvas.itemconfig(meralco_rate, text=electricity_bill)

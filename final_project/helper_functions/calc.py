def compute_unita_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitb_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitc_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitd_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unite_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitf_electricity(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_meralco_rate(canvas, meralco_rate, electricity_rate):
    canvas.itemconfig(meralco_rate, text=f"{round(electricity_rate, 2)}")


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
        unit_a_prev_elec, unit_a_present_elec
    )

    unitb_elec_consumption = compute_unitb_electricity(
        unit_b_prev_elec, unit_b_present_elec
    )

    unitc_elec_consumption = compute_unitc_electricity(
        unit_c_prev_elec, unit_c_present_elec
    )

    unitd_elec_consumption = compute_unitd_electricity(
        unit_d_prev_elec, unit_d_present_elec
    )

    unite_elec_consumption = compute_unite_electricity(
        unit_e_prev_elec, unit_e_present_elec
    )

    unitf_elec_consumption = compute_unitf_electricity(
        unit_f_prev_elec, unit_f_present_elec
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

    compute_meralco_rate(canvas, meralco_rate, electricity_rate)

    unita_elec = unita_elec_consumption * electricity_rate
    canvas.itemconfig(unit_a_elecbill, text=f"{round(unita_elec, 2)}")

    unitb_elec = unitb_elec_consumption * electricity_rate
    canvas.itemconfig(unit_b_elecbill, text=f"{round(unitb_elec, 2)}")

    unitc_elec = unitc_elec_consumption * electricity_rate
    canvas.itemconfig(unit_c_elecbill, text=f"{round(unitc_elec, 2)}")

    unitd_elec = unitd_elec_consumption * electricity_rate
    canvas.itemconfig(unit_d_elecbill, text=f"{round(unitd_elec, 2)}")

    unite_elec = unite_elec_consumption * electricity_rate
    canvas.itemconfig(unit_e_elecbill, text=f"{round(unite_elec, 2)}")

    unitf_elec = unitf_elec_consumption * electricity_rate
    canvas.itemconfig(unit_f_elecbill, text=f"{round(unitf_elec, 2)}")





def compute_unita_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitb_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitc_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitd_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unite_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_unitf_water(prev, present):
    prev_consumption = float(prev.get())
    present_consumption = float(present.get())
    total_consumption = present_consumption - prev_consumption

    return total_consumption


def compute_maynilad_rate(canvas, maynilad_rate, electricity_rate):
    canvas.itemconfig(maynilad_rate, text=f"{round(electricity_rate, 2)}")


def compute_water_bill(
    canvas,
    total_bill_water,
    unit_a_prev_water,
    unit_b_prev_water,
    unit_c_prev_water,
    unit_d_prev_water,
    unit_e_prev_water,
    unit_f_prev_water,
    unit_a_present_water,
    unit_b_present_water,
    unit_c_present_water,
    unit_d_present_water,
    unit_e_present_water,
    unit_f_present_water,
    unit_a_waterbill,
    unit_b_waterbill,
    unit_c_waterbill,
    unit_d_waterbill,
    unit_e_waterbill,
    unit_f_waterbill,
    maynilad_rate,
):
    unita_water_consumption = compute_unita_water(
        unit_a_prev_water, unit_a_present_water
    )

    unitb_water_consumption = compute_unitb_water(
        unit_b_prev_water, unit_b_present_water
    )

    unitc_water_consumption = compute_unitc_water(
        unit_c_prev_water, unit_c_present_water
    )

    unitd_water_consumption = compute_unitd_water(
        unit_d_prev_water, unit_d_present_water
    )

    unite_water_consumption = compute_unite_water(
        unit_e_prev_water, unit_e_present_water
    )

    unitf_water_consumption = compute_unitf_water(
        unit_f_prev_water, unit_f_present_water
    )

    total_consumption = (
        unita_water_consumption
        + unitb_water_consumption
        + unitc_water_consumption
        + unitd_water_consumption
        + unite_water_consumption
        + unitf_water_consumption
    )

    bill = total_bill_water.get()

    water_rate = float(bill) / total_consumption

    compute_maynilad_rate(canvas, maynilad_rate, water_rate)

    unita_water = unita_water_consumption * water_rate
    canvas.itemconfig(unit_a_waterbill, text=f"{round(unita_water, 2)}")

    unitb_water = unitb_water_consumption * water_rate
    canvas.itemconfig(unit_b_waterbill, text=f"{round(unitb_water, 2)}")

    unitc_water = unitc_water_consumption * water_rate
    canvas.itemconfig(unit_c_waterbill, text=f"{round(unitc_water, 2)}")

    unitd_water = unitd_water_consumption * water_rate
    canvas.itemconfig(unit_d_waterbill, text=f"{round(unitd_water, 2)}")

    unite_water = unite_water_consumption * water_rate
    canvas.itemconfig(unit_e_waterbill, text=f"{round(unite_water, 2)}")

    unitf_water = unitf_water_consumption * water_rate
    canvas.itemconfig(unit_f_waterbill, text=f"{round(unitf_water, 2)}")
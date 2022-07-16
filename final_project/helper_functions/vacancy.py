from tkinter import *

def unita_vacancy_changed(unita_paid_btn, var2):      
        if var2.get() == 1:
            unita_paid_btn.config(state=DISABLED)
        elif var2.get() == 0:
            unita_paid_btn.config(state=NORMAL)

def unitb_vacancy_changed(unitb_paid_btn, var4):      
        if var4.get() == 1:
            unitb_paid_btn.config(state=DISABLED)
        elif var4.get() == 0:
            unitb_paid_btn.config(state=NORMAL)

def unitc_vacancy_changed(unitc_paid_btn, var6):      
        if var6.get() == 1:
            unitc_paid_btn.config(state=DISABLED)
        elif var6.get() == 0:
            unitc_paid_btn.config(state=NORMAL)

def unitd_vacancy_changed(unitd_paid_btn, var8):      
        if var8.get() == 1:
            unitd_paid_btn.config(state=DISABLED)
        elif var8.get() == 0:
            unitd_paid_btn.config(state=NORMAL)

def unite_vacancy_changed(unite_paid_btn, var10):      
        if var10.get() == 1:
            unite_paid_btn.config(state=DISABLED)
        elif var10.get() == 0:
            unite_paid_btn.config(state=NORMAL)

def unitf_vacancy_changed(unitf_paid_btn, var12):      
        if var12.get() == 1:
            unitf_paid_btn.config(state=DISABLED)
        elif var12.get() == 0:
            unitf_paid_btn.config(state=NORMAL)
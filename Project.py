from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

m = Tk()
m.geometry('900x820')
m.title('VIRTUAL DOCTOR')
m.config(bg="#629187")

var1 = StringVar()
var2 = StringVar()
var3 = IntVar()
var4 = StringVar()
var5 = StringVar()
var6 = IntVar()


def med():
    global img

    f2 = Frame(m, )
    f2.place(x=0, y=0, height=1000, width=1000)
    f2.config(bg="#629187")
    img = ImageTk.PhotoImage(Image.open(r'C:\Users\MALIK\Desktop\vd6.PNG'))
    pict = Label(f2, image=img)
    pict.place(x=-40, y=-65, relwidth=1, relheight=1)

    l9 = Label(f2, text='VIRTUAL DOCTOR          ', font='Aerial 22 bold', bg='#629187', fg='white', height=1, width=1)
    l9.pack(side=TOP, fill=X)
    n = var1.get()
    g = var3.get()
    gf = var6.get()
    if g == 1:
        l2 = Label(f2, text="Mr." + n, bg='#FFFFFF', fg='black', width=15, font='Century 16 bold')
        l2.place(x=195, y=240)
    elif gf == 1:
        l2 = Label(f2, text="Ms." + n, bg='#FFFFFF', fg='black', width=9, font='Century 16 bold')
        l2.place(x=222, y=240)

    pp = var5.get()
    ss = var4.get()
    # Head
    if pp == "Head" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF', font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Headache\Migraine", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF', font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Paracetamol\Aspirin\Ibuprofen", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Head" and ss == "Fever":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF', font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Cold\Flu\Sinus Infection ", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="(Note:Other Conditions may also lead to fever.)", fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=350)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF', font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen\Aspirin\Ibuprofen", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Head" and ss == "Chills/Shivering":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Cold\Flu", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Ibuprofen", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Head" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text=" Severe Headache\Migraine", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Paracetamol\Aspirin\Ibuprofen", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician Immediately.)", fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    elif pp == "Head" and ss == "Dizziness":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Vertigo\Ear infection\Anemia\Hypoglycemia\BP drop ", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Betahistine\Meclizine\Amoxicillin\Iron Supplement\Dextrose\n\Glucagon", fg='black',
                   bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)

    # Neck
    elif pp == "Neck" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Nerve Compression\Muscle Spasm\Injury\Rheumatoid Arthritis", fg='black', bg='#FFFFFF',
                   font='Candara 15  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen\Ibuprofen\Acetaminophen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Massage may also help relieve pain.)", fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    elif pp == "Neck" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Nerve Compression\Muscle Spasm\Injury\Rheumatoid Arthritis", fg='black', bg='#FFFFFF',
                   font='Candara 15  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen\Ibuprofen\Acetaminophen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note: If Pain persist, please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    # Arm
    elif pp == "Arm" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Sprain\Tendonitis\Injury\Rheumatoid Arthritis", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Arm" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Sprain\Tendonitis\Injury\Rheumatoid Arthritis\Fracture", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    # Leg
    elif pp == "Leg" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Sprain\Muscle Cramp\Injury\Arthritis\PAD\DVT", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Ibuprofen\Methotrexate\Clopidogrel\Warfarin", fg='black', bg='#FFFFFF',
                   font='Candara 15  italic')
        l2.place(x=195, y=420)

    elif pp == "Leg" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Sprain\Tendonitis\Fracture\Arthritis\PAD\DVT", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Ibuprofen\Methotrexate\Clopidogrel\Warfarin", fg='black', bg='#FFFFFF',
                   font='Candara 15  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician Immediately.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    elif pp == "Leg" and ss == "Cramping":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Sciatica", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Ibuprofen\Cyclobenzaprine", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)

    # Hand
    elif pp == "Hand" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Tendonitis\Injury\Carpal Tunnel Syndrome\Arthritis", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Hand" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Tendonitis\Injury\Carpal Tunnel Syndrome\Arthritis\Fracture", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    # Foot
    elif pp == "Foot" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Tendonitis\Injury\Metatarsalgia\Plantar Fasciitis\Arthritis", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)

    elif pp == "Foot" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Tendonitis\Injury\Metatarsalgia\Plantar Fasciitis\Arthritis\n\Fracture", fg='black',
                   bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Naproxen Sodium\Acetaminophen\Ibuprofen\Methotrexate", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    # Chest
    elif pp == "Chest" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="CAD\Mitral Valve Prolapse\Chest Infection\Pneumonia\COPD\nPneumothorax ", fg='black',
                   bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Bisoprolol\Aspirin\Propranolol\Erythromycin\Azithromycin\n\Salbutamol\Ketamine",
                   fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician for better Assistance.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    elif pp == "Chest" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2,
                   text="CAD\Mitral Valve Prolapse\Chest Infection\Pneumonia\COPD\nPneumothorax\Myocardial Infarction(Heart Attack) ",
                   fg='black',
                   bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Bisoprolol\Aspirin\Propranolol\Erythromycin\Azithromycin\n\Salbutamol\Ketamine",
                   fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',
                   font='Candara 12  italic')
        l2.place(x=195, y=450)

    elif pp == "Chest" and ss == "Difficulty Breathing":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Asthma\Emphysema\Pneumonia\Allergies\Lung Infection\n\Heart Disease\Covid-19 ", fg='black',
                   bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Ipatropium Bromide\Benztropine Mesylate\Amoxicillin\n\Warfarin", fg='black', bg='#FFFFFF',
                   font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Chest" and ss == "Cough":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Asthma\Allergies\Virus", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Dextromethorphan\Pholcodine", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)

    #EYE

    elif pp == "Eye" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Allergies\Infection\Conjunctivitis\Stye", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Loratidine\Vibramycin\Moxifloxacin\Erythromycin", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Eye" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Uveitis\Scleritis\Glaucoma", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Azathioprine\Ibuprofen\Brimonidine", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
        l2 = Label(f2, text="(Note:Please visit Your Nearst Physician as soon as possible.)",
                   fg='black', bg='#FFFFFF',font='Candara 12  italic')
        l2.place(x=195, y=450)
        #MOUTH
    elif pp == "Mouth" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Canker Sores\Toothache\Infection ", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Doxycycline\Acetaminophen\Valacyclovir", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Mouth" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Dental Infection\Jaw infection ", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Amoxicillin\Clindamycin", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Mouth" and ss == "Vomiting":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Indigestion\Food Poisoning\Gastroenteritis", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Simethicone\Loperamide link\Pepto-Bismol", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Mouth" and ss == "Cough":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Asthma\Allergies\Virus", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Dextromethorphan\Pholcodine", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
#Back
    elif pp == "Back" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Spinal Infection\Scoliosis\Arthritis\Sciatica", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Vancomycin plus\Acetaminophen\Feldene\Ibuprofen", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Back" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Spinal Stenosis\Myofacial Pain Syndrome\Disc Problem", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Acetaminophen\Cyclobenzaprine\Amitriptyline\Amitriptyline", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    #Upper Abdomen
    elif pp == "Upper Abdomen" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Appendicitis\Gallstones", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Piperacillin\Ampicillin", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Upper Abdomen" and ss == "Severe Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Gastritis ", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Omeprazole", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Upper Abdomen" and ss == "Nausea":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Gastroenteritis\Dyspepsia", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Kaopectate\Simethicone", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    #Lower Abdomen
    elif pp == "Lower Abdomen" and ss == "Pain" and gf==1:
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Constipation\Colitis\Ovulation", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Bisacodyl\Infliximab\Clomiphene citrate", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)
    elif pp == "Lower Abdomen" and ss == "Pain":
        l2 = Label(f2, text="Possible Medical Condition:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=285)
        l2 = Label(f2, text="Constipation\Colitis\Diverticular Disease", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=320)
        l2 = Label(f2, text="Recommended Medication:", fg='black', bg='#FFFFFF',
                   font='Cambria 16  bold underline')
        l2.place(x=195, y=385)
        l2 = Label(f2, text="Bisacodyl\Infliximab\Metronidazole", fg='black', bg='#FFFFFF', font='Candara 16  italic')
        l2.place(x=195, y=420)

    else:
        l2 = Label(f2, text="SORRY!\nWe are Working on it!", fg='black', bg='#FFFFFF',
                   font='Cambria 20  bold italic')
        l2.place(x=320, y=300)


f1 = Frame(m, )
f1.place(x=0, y=0, height=1000, width=1000)
f1.config(bg="#629187")

img = PhotoImage(file=r'C:\Users\MALIK\Desktop\vd5.PNG')
lim = Label(f1, image=img)
lim.place(x=-40, y=-65, relwidth=1, relheight=1)

l1 = Label(f1, text='VIRTUAL DOCTOR          ', font='Aerial 22 bold', bg='#629187', fg='white', height=1, width=1)
l1.pack(side=TOP, fill=X)

l2 = Label(f1, text="Full Name", bg='#D9D9D9', fg='black', font='Cambria 16 bold')
l2.place(x=222, y=240)

l2 = Label(f1, text="Gender", fg='black', bg='#D9D9D9', font='Cambria 16  bold')
l2.place(x=222, y=284)

c = Checkbutton(f1, text="Male", font='Candara 12 italic bold', variable=var3)
c.place(x=470, y=283)
f = Checkbutton(f1, text="Female", font='Candara 12 italic bold', variable=var6)
f.place(x=570, y=283)

l2 = Label(f1, text="Part/Area of\nSymptom    ", fg='black', bg='#D9D9D9', font='Cambria 15 bold')
l2.place(x=222, y=330)

l2 = Label(f1, text="Symptom", fg='black', bg='#D9D9D9', font='Cambria 16 bold')
l2.place(x=222, y=394)

l2 = Label(f1, text="Any Chronic          \nDisease(Optional)", fg='black', bg='#D9D9D9', font='Cambria 12 bold')
l2.place(x=222, y=440)

var5.set("Click to Select")
p = OptionMenu(f1, var5, "Head", "Neck", "Arm", "Upper Abdomen",
               "Lower Abdomen", "Back", "Leg", "Hand", "Foot", "Chest", "Eye", "Mouth")
p.config(font="Candara 10 bold")
p.place(x=470, y=340)

var4.set("Click to Select")
s = OptionMenu(f1, var4, "Pain", "Fever", "Difficulty Breathing", "Severe Pain", "Nausea", "Vomiting", "Cough",
               "Chills/Shivering", "Dizziness", "Cramping")
s.config(font="Candara 10 bold")
s.place(x=470, y=390)

e1 = Entry(f1, font='Candara 16 italic', textvariable=var1)
e1.place(x=470, y=240)

e2 = Entry(f1, font='Candara 16 italic', textvariable=var2)
e2.place(x=470, y=440)

btn = Button(f1, text='Confirm', fg='black', bg='grey', command=med,
             font='Aerial 16 italic')
btn.place(x=650, y=670)

m.mainloop()
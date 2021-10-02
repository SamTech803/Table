"""#╔ ═ ╗ ║ ╚ ╝
#│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
def make_table(rows,labels=None,centered=False):
    mainString=""
    maxlist=[]
    for i in range(0,len(rows[0])):
        if labels!=None:
            m=len(str(labels[i]))
        else:
            m=0
        for a in rows:
            if len(str(a[i]))>m:
                m=len(str(a[i]))
        maxlist.append(m+1)

    f="┌"
    for i in range(len(maxlist)):
        if i is not len(maxlist)-1:
            f=f+("─"*(maxlist[i]+1))+"┬"
        else:
            f=f+("─"*(maxlist[i]+1))+"┐"
    mainString=mainString+f+"\n"

    f="├"
    n=0
    if labels!=None:
        if centered==False:
            main="│ "
            for i in range(0,len(labels)):
                b=" "*(maxlist[i]-len(str(labels[i]))-i+n)
                if i is not len(labels)-1:
                    main=main+str(labels[i])+str(b)+"│ "
                else:
                    main=main+str(labels[i])+str(b)+"│"
                if i<len(maxlist)-1:
                    f=f+(("─")*(maxlist[i]+1))+"┼"
                else:
                    f=f+(("─")*(maxlist[i]+1))+"┤"
                n=n+1
            mainString=mainString+main+"\n"
            mainString=mainString+f+"\n"
        else:
            main="│ "
            for i in range(0,len(labels)):
                bs=maxlist[i]-len(str(labels[i]))+1
                if bs%2==0:
                    b1=bs/2-1
                    b2=bs/2
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if i is not len(labels)-1:
                        main=main+str(b11)+str(labels[i])+str(b22)+"│ "
                    else:
                        main=main+str(b11)+str(labels[i])+str(b22)+"│"
                    if i<len(maxlist)-1:
                        f=f+(("─")*(maxlist[i]+1))+"┼"
                    else:
                        f=f+(("─")*(maxlist[i]+1))+"┤"
                    n=n+1
                else:
                    b1=(bs/2)-0.5-1
                    b2=(bs/2)-0.5+1
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if i is not len(labels)-1:
                        main=main+str(b11)+str(labels[i])+str(b22)+"│ "
                    else:
                        main=main+str(b11)+str(labels[i])+str(b22)+"│"
                    if i<len(maxlist)-1:
                        f=f+(("─")*(maxlist[i]+1))+"┼"
                    else:
                        f=f+(("─")*(maxlist[i]+1))+"┤"
                    n=n+1
                
            mainString=mainString+main+"\n"
            mainString=mainString+f+"\n"

    for i in range(0,len(rows)):
        if centered==False:
            main="│ "
            for j in range(0,len(rows[i])):
                b=" "*(maxlist[j]-len(str(rows[i][j])))
                if j is not len(rows[i])-1:
                    main=main+str(rows[i][j])+str(b)+"│ "
                else:
                    main=main+str(rows[i][j])+str(b)+"│"
            mainString=mainString+main+"\n"
        else:
            main="│ "
            for j in range(0,len(rows[i])):
                bs=maxlist[j]-len(str(rows[i][j]))+1
                if bs%2==0:
                    b1=bs/2-1
                    b2=bs/2
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if j is not len(rows[i])-1:
                        main=main+str(b11)+str(rows[i][j])+str(b22)+"│ "
                    else:
                        main=main+str(b11)+str(rows[i][j])+str(b22)+"│"
                else:
                    b1=(bs/2)-0.5+1
                    b2=(bs/2)-0.5-1
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if j is not len(rows[i])-1:
                        main=main+str(b22)+str(rows[i][j])+str(b11)+"│ "
                    else:
                        main=main+str(b22)+str(rows[i][j])+str(b11)+"│"

            mainString=mainString+main+"\n"
            
    f="└"
    for i in range(len(maxlist)):
        if i is not len(maxlist)-1:
            f=f+("─"*(maxlist[i]+1))+"┴"
        else:
            f=f+("─"*(maxlist[i]+1))+"┘"
    mainString=mainString+f+"\n"

    return mainString

t=make_table(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=True
            )
#print(t)

t=make_table(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=False
            )
#print(t)

t=make_table(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=True
            )
#print(t)

t=make_table(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=False
            )

#print(t)

t=make_table(
                rows=[(1, '2021-01-01', 'Baba', 'Bank of Baroda', 'Credit', 2860.23, 'Opening Balance'), (2, '2021-01-02', 'Bank of Baroda', 'Personal Expenses', 'Debit', -50, 'Terpent Oil'), (3, '2021-01-11', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, '8208419540'), (4, '2021-01-12', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, '9373594879'), (5, '2021-01-12', 'Bank of Baroda', 'Stationery', 'Debit', -60, 'Lamination'), (6, '2021-01-12', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (7, '2021-01-14', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (8, '2021-01-15', 'Baba', 'Cash', 'Credit', 910, 'For the College Exam Fee.'), (9, '2021-01-16', 'Cash', 'Travelling', 'Debit', -60, 'To college for Exam Form'), (10, '2021-01-16', 'Cash', 'College Stuff', 'Debit', -400, 'Exam Form Semester 3'), (11, '2021-01-16', 'Bank of Baroda', 'Food', 'Debit', -25, 'Kuka'), (12, '2021-01-16', 'Cash', 'Baba', 'Debit', -200, 'Gave Back Extra Money'), (13, '2021-01-17', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (14, '2021-01-17', 'Aai', 'Cash', 'Credit', 5, 'Tp'), (15, '2021-01-18', 'Bank of Baroda', 'Stationery', 'Debit', -60, 'A4 size book for Practials'), (16, '2021-02-01', 'Bank', 'Bank of Baroda', 'Credit', 17, 'Bank Intrest'), (17, '2021-02-02', 'Bank of Baroda', 'Haircut', 'Debit', -100, 'Haircut'), (18, '2021-02-02', 'Bank of Baroda', 'Personal Expenses', 'Debit', -20, 'Tooth Brush'), (19, '2021-02-04', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'February Month'), (20, '2021-02-04', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (21, '2021-02-04', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'February'), (22, '2021-02-05', 'Cash', 'Personal Expenses', 'Debit', -40, 'Water Heater Repairing'), (23, '2021-02-09', 'Bank of Baroda', 'Food', 'Debit', -35, 'Dahi'), (24, '2021-2-15', 'Bank of Baroda', 'Medicine', 'Debit', -150, 'Enerzal'), (25, '2021-2-15', 'Bank of Baroda', 'Food', 'Debit', -50, 'Banana'), (26, '2021-02-17', 'Bank of Baroda', 'Medicine', 'Debit', -140, 'Boric Powder and Enerzal'), (27, '2021-02-19', 'Bank of Baroda', 'Food', 'Debit', -99, 'Gulab Jamun Mix'), (28, '2021-02-24', 'Maha DBT', 'Bank of Baroda', 'Credit', 200, 'Scholarship 2019-20, 2nd Installment'), (29, '2021-02-27', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (30, '2021-02-27', 'Bank of Baroda', 'Stationery', 'Debit', -10, 'Gel Pen'), (31, '2021-02-27', 'Bank of Baroda', 'Grocery', 'Debit', -45, 'Patanjali Toothpaste'), (32, '2021-03-01', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'March'), (33, '2021-03-01', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'March'), (34, '2021-03-01', 'Bank of Baroda', 'Medicine', 'Debit', -225, 'Jambavasava'), (35, '2021-03-01', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (36, '2021-03-07', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (37, '2021-03-07', 'Bank of Baroda', 'Food', 'Debit', -3, 'Center Fresh'), (38, '2021-03-14', 'Bank of Baroda', 'Bank', 'Debit', -17.7, 'SMS Alert Charges'), (39, '2021-3-17', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (40, '2021-3-17', 'Bank of Baroda', 'Food', 'Debit', -40, '1 kg Carrot'), (41, '2021-3-18', 'Cash', 'Baba', 'Debit', -200, ''), (42, '2021-3-18', 'Bank of Baroda', 'Baba', 'Debit', -10, 'Checking the Speed.'), (43, '2021-03-18', 'Bank of Baroda', 'Personal Expenses', 'Debit', -45, 'Glycerin'), (44, '2021-03-18', 'Bank of Baroda', 'Personal Expenses', 'Debit', -5, 'Choclate'), (45, '2021-3-19', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (46, '2021-3-19', 'Bank of Baroda', 'Food', 'Debit', -10, 'Green Chilly'), (47, '2021-3-20', 'Bank of Baroda', 'Food', 'Debit', -160, '3-Patanjali Noodles, 1-Toast Packet'), (48, '2021-3-20', 'Bank of Baroda', 'Food', 'Debit', -77, 'Quaker Oats'), (49, '2021-3-23', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (50, '2021-3-24', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (51, '2021-3-25', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'March-April'), (52, '2021-3-25', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'March-April'), (53, '2021-3-25', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (54, '2021-3-25', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (55, '2021-3-28', 'Bank of Baroda', 'Stationery', 'Debit', -180, 'A4 size Paper Rim 500 Pages'), (56, '2021-3-28', 'Bank of Baroda', 'Food', 'Debit', -83, 'Milk, Curd'), (57, '2021-3-28', 'Bank of Baroda', 'Personal Expenses', 'Debit', -10, 'Gulal'), (58, '2021-4-2', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (59, '2021-4-2', 'Bank of Baroda', 'Haircut', 'Debit', -100, 'Soldier Cut'), (60, '2021-4-2', 'Bank of Baroda', 'Food', 'Debit', -29, 'Milk'), (61, '2021-4-9', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (62, '2021-4-13', 'MPL', 'Bank of Baroda', 'Credit', 18, 'Fruit Dart - First Play'), (63, '2021-4-13', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Fruit Dart'), (64, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 10, 'MI vs KKR Fantasy Team'), (65, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 10, "Aai's Account - Fruit Dart"), (66, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 16, "Aai's Account - Fruit Dart"), (67, '2021-4-15', 'MPL', 'Bank of Baroda', 'Credit', 15, "Aai's Account - SRH vs RCB Fantasy Team"), (68, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -30, 'Shimla and Green Mirch'), (69, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -35, 'Curd'), (70, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -50, 'Frozen Green Peas'), (71, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -63, 'Cream'), (72, '2021-4-16', 'MPL', 'Bank of Baroda', 'Credit', 4, 'My Account - Speed Chess [2 Tournaments]'), (73, '2021-4-17', 'MPL', 'Bank of Baroda', 'Credit', 6, 'Fruit Chop [2 Tournaments]'), (74, '2021-4-18', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'April - May'), (75, '2021-4-19', 'Bank of Baroda', 'Mobile Recharge Aai VI', 'Debit', -49, 'April - May'), (76, '2021-4-19', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'April - May'), (77, '2021-4-22', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - PK vs SRH'), (78, '2021-4-24', 'MPL', 'Bank of Baroda', 'Credit', 10, 'Gourav My11 - MI vs PK'), (79, '2021-4-29', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - MI vs RR'), (80, '2021-5-1', 'Bank', 'Bank of Baroda', 'Credit', 17, 'Bank Interest'), (81, '2021-5-3', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - SRH vs RR'), (82, '2021-5-10', 'Baba', 'Bank of Baroda', 'Credit', 500, 'For the Google Pay and Paytm'), (83, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -151, 'Google Pay 1st Transaction'), (84, '2021-5-10', 'Google Pay', 'Bank of Baroda', 'Credit', 21, '1st Cashback'), (85, '2021-5-10', 'Bank of Baroda', 'Food', 'Debit', -150, 'Chapati'), (86, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -1, 'Paytm 1st Transaction'), (87, '2021-5-10', 'Paytm', 'Bank of Baroda', 'Credit', 5, '1st Cashback'), (88, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -1, 'By Paytm for reward, got 0'), (89, '2021-5-10', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'May - June'), (90, '2021-5-10', 'Paytm', 'Bank of Baroda', 'Credit', 20, "Cashback On Aai's Recharge"), (91, '2021-5-12', 'Baba', 'Bank of Baroda', 'Credit', 51, 'For D2H payment'), (92, '2021-5-12', 'Bank of Baroda', 'D2H', 'Debit', -200, 'By Google Pay'), (93, '2021-5-12', 'Google Pay', 'Bank of Baroda', 'Credit', 27, 'For D2H payment'), (94, '2021-5-15', 'Baba', 'Paytm Voucher', 'Credit', 100, ''), (95, '2021-6-2', 'Baba', 'Bank of Baroda', 'Credit', 500, ''), (96, '2021-6-2', 'Bank of Baroda', 'Electricity Bill', 'Debit', -240, 'May Electricity Bill'), (97, '2021-6-2', 'Bank of Baroda', 'Paytm Voucher', 'Credit', 1, ''), (98, '2021-6-2', 'Bank of Baroda', 'Paytm Voucher', 'Debit', -1, ''), (99, '2021-6-5', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'June-July'), (100, '2021-6-7', 'Bank of Baroda', 'Bank', 'Debit', -17.7, 'SMS Charges'), (101, '2021-6-7', 'Bank of Baroda', 'Food', 'Debit', -30, 'Potatoes'), (102, '2021-6-7', 'Baba', 'Bank of Baroda', 'Credit', 500, ''), (103, '2021-6-7', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'June-July'), (104, '2021-6-13', 'MPL', 'Bank of Baroda', 'Credit', 3, "Aai's VI Account"), (105, '2021-6-13', 'MPL', 'Bank of Baroda', 'Credit', 19, "Aai's VI Account"), (106, '2021-6-14', 'MPL', 'Bank of Baroda', 'Credit', 6, "Aai's VI Account"), (107, '2021-6-15', 'MPL', 'Bank of Baroda', 'Credit', 6, "Aai's VI Account"), (108, '2021-6-17', 'Bank of Baroda', 'Food', 'Debit', -96, '2 Litre Milk'), (109, '2021-6-20', 'Baba', 'Bank of Baroda', 'Credit', 1000, 'For Exam Fee'), (110, '2021-6-20', 'Bank of Baroda', 'College Stuff', 'Debit', -400, 'Exam Form'), (111, '2021-6-21', 'Bank of Baroda', 'Food', 'Debit', -251, 'Samose'), (112, '2021-6-21', 'Bank of Baroda', 'Electricity Bill', 'Debit', -340, 'May'), (113, '2021-6-21', 'Google Pay', 'Bank of Baroda', 'Credit', 5, 'CashBack'), (114, '2021-6-21', 'Bank of Baroda', 'Food', 'Debit', -96, 'Milk')],
                labels=["Id","Date","From","To","Credit/Debit","Amount","Narration"],
                centered=False
            )
print(t)
"""
#╔ ═ ╗ ║ ╚ ╝ ╦
#│ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
def make_table(rows,labels=None,centered=False):
    mainString=""
    maxlist=[]
    for i in range(0,len(rows[0])):
        if labels!=None:
            m=len(str(labels[i]))
        else:
            m=0
        for a in rows:
            if len(str(a[i]))>m:
                m=len(str(a[i]))
        maxlist.append(m+1)

    f="╔"
    for i in range(len(maxlist)):
        if i is not len(maxlist)-1:
            f=f+("═"*(maxlist[i]+1))+"╦"
        else:
            f=f+("═"*(maxlist[i]+1))+"╗"
    mainString=mainString+f+"\n"

    f="╠"
    n=0
    if labels!=None:
        if centered==False:
            main="║ "
            for i in range(0,len(labels)):
                b=" "*(maxlist[i]-len(str(labels[i]))-i+n)
                if i is not len(labels)-1:
                    main=main+str(labels[i])+str(b)+"║ "
                else:
                    main=main+str(labels[i])+str(b)+"║"
                if i<len(maxlist)-1:
                    f=f+(("═")*(maxlist[i]+1))+"╬"
                else:
                    f=f+(("═")*(maxlist[i]+1))+"╣"
                n=n+1
            mainString=mainString+main+"\n"
            mainString=mainString+f+"\n"
        else:
            main="║ "
            for i in range(0,len(labels)):
                bs=maxlist[i]-len(str(labels[i]))+1
                if bs%2==0:
                    b1=bs/2-1
                    b2=bs/2
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if i is not len(labels)-1:
                        main=main+str(b11)+str(labels[i])+str(b22)+"║ "
                    else:
                        main=main+str(b11)+str(labels[i])+str(b22)+"║"
                    if i<len(maxlist)-1:
                        f=f+(("═")*(maxlist[i]+1))+"╬"
                    else:
                        f=f+(("═")*(maxlist[i]+1))+"╣"
                    n=n+1
                else:
                    b1=(bs/2)-0.5-1
                    b2=(bs/2)-0.5+1
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if i is not len(labels)-1:
                        main=main+str(b11)+str(labels[i])+str(b22)+"║ "
                    else:
                        main=main+str(b11)+str(labels[i])+str(b22)+"║"
                    if i<len(maxlist)-1:
                        f=f+(("═")*(maxlist[i]+1))+"╬"
                    else:
                        f=f+(("═")*(maxlist[i]+1))+"╣"
                    n=n+1
                
            mainString=mainString+main+"\n"
            mainString=mainString+f+"\n"

    for i in range(0,len(rows)):
        if centered==False:
            main="║ "
            for j in range(0,len(rows[i])):
                b=" "*(maxlist[j]-len(str(rows[i][j])))
                if j is not len(rows[i])-1:
                    main=main+str(rows[i][j])+str(b)+"║ "
                else:
                    main=main+str(rows[i][j])+str(b)+"║"
            mainString=mainString+main+"\n"
        else:
            main="║ "
            for j in range(0,len(rows[i])):
                bs=maxlist[j]-len(str(rows[i][j]))+1
                if bs%2==0:
                    b1=bs/2-1
                    b2=bs/2
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if j is not len(rows[i])-1:
                        main=main+str(b11)+str(rows[i][j])+str(b22)+"║ "
                    else:
                        main=main+str(b11)+str(rows[i][j])+str(b22)+"║"
                else:
                    b1=(bs/2)-0.5+1
                    b2=(bs/2)-0.5-1
                    b11=" "*int(b1)
                    b22=" "*int(b2)
                    if j is not len(rows[i])-1:
                        main=main+str(b22)+str(rows[i][j])+str(b11)+"║ "
                    else:
                        main=main+str(b22)+str(rows[i][j])+str(b11)+"║"

            mainString=mainString+main+"\n"
            
    f="╚"
    for i in range(len(maxlist)):
        if i is not len(maxlist)-1:
            f=f+("═"*(maxlist[i]+1))+"╩"
        else:
            f=f+("═"*(maxlist[i]+1))+"╝"
    mainString=mainString+f+"\n"

    return mainString

t=make_table(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=True
            )
print(t)

t=make_table(
                rows=[
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"],
                    ["Hippopotomonstrosesquippedaliophobia"],
                    ["Supercalifragilisticexpialidocious"],
                    ["Pseudopseudohypoparathyroidism"],
                    ["Floccinaucinihilipilification"],
                    ["Antidisestablishmentarianism"],
                    ["."]
                ],
                labels=["My Favourite Long Words"],
                centered=False
            )
print(t)

t=make_table(
                rows=[
                    ["A"],
                    ["B"],
                    ["C"],
                    ["D"],
                    ["E"],
                    ["F"],
                    ["Pneumonoultramicroscopicsilicovolcanoconiosis"]
                ],
                labels=["Alphabet"],
                centered=True
            )
print(t)

table = make_table(
    rows=[
        ["Lemon", 18_3285, "Owner"],
        ["Sebastiaan", 18_3285.1, "Owner"],
        ["KutieKatj", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"]
    ],
    labels=["User", "Messages", "Role"]
)
print(table)

t=make_table(
                rows=[(1, '2021-01-01', 'Baba', 'Bank of Baroda', 'Credit', 2860.23, 'Opening Balance'), (2, '2021-01-02', 'Bank of Baroda', 'Personal Expenses', 'Debit', -50, 'Terpent Oil'), (3, '2021-01-11', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, '8208419540'), (4, '2021-01-12', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, '9373594879'), (5, '2021-01-12', 'Bank of Baroda', 'Stationery', 'Debit', -60, 'Lamination'), (6, '2021-01-12', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (7, '2021-01-14', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (8, '2021-01-15', 'Baba', 'Cash', 'Credit', 910, 'For the College Exam Fee.'), (9, '2021-01-16', 'Cash', 'Travelling', 'Debit', -60, 'To college for Exam Form'), (10, '2021-01-16', 'Cash', 'College Stuff', 'Debit', -400, 'Exam Form Semester 3'), (11, '2021-01-16', 'Bank of Baroda', 'Food', 'Debit', -25, 'Kuka'), (12, '2021-01-16', 'Cash', 'Baba', 'Debit', -200, 'Gave Back Extra Money'), (13, '2021-01-17', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (14, '2021-01-17', 'Aai', 'Cash', 'Credit', 5, 'Tp'), (15, '2021-01-18', 'Bank of Baroda', 'Stationery', 'Debit', -60, 'A4 size book for Practials'), (16, '2021-02-01', 'Bank', 'Bank of Baroda', 'Credit', 17, 'Bank Intrest'), (17, '2021-02-02', 'Bank of Baroda', 'Haircut', 'Debit', -100, 'Haircut'), (18, '2021-02-02', 'Bank of Baroda', 'Personal Expenses', 'Debit', -20, 'Tooth Brush'), (19, '2021-02-04', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'February Month'), (20, '2021-02-04', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (21, '2021-02-04', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'February'), (22, '2021-02-05', 'Cash', 'Personal Expenses', 'Debit', -40, 'Water Heater Repairing'), (23, '2021-02-09', 'Bank of Baroda', 'Food', 'Debit', -35, 'Dahi'), (24, '2021-2-15', 'Bank of Baroda', 'Medicine', 'Debit', -150, 'Enerzal'), (25, '2021-2-15', 'Bank of Baroda', 'Food', 'Debit', -50, 'Banana'), (26, '2021-02-17', 'Bank of Baroda', 'Medicine', 'Debit', -140, 'Boric Powder and Enerzal'), (27, '2021-02-19', 'Bank of Baroda', 'Food', 'Debit', -99, 'Gulab Jamun Mix'), (28, '2021-02-24', 'Maha DBT', 'Bank of Baroda', 'Credit', 200, 'Scholarship 2019-20, 2nd Installment'), (29, '2021-02-27', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (30, '2021-02-27', 'Bank of Baroda', 'Stationery', 'Debit', -10, 'Gel Pen'), (31, '2021-02-27', 'Bank of Baroda', 'Grocery', 'Debit', -45, 'Patanjali Toothpaste'), (32, '2021-03-01', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'March'), (33, '2021-03-01', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'March'), (34, '2021-03-01', 'Bank of Baroda', 'Medicine', 'Debit', -225, 'Jambavasava'), (35, '2021-03-01', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (36, '2021-03-07', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (37, '2021-03-07', 'Bank of Baroda', 'Food', 'Debit', -3, 'Center Fresh'), (38, '2021-03-14', 'Bank of Baroda', 'Bank', 'Debit', -17.7, 'SMS Alert Charges'), (39, '2021-3-17', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (40, '2021-3-17', 'Bank of Baroda', 'Food', 'Debit', -40, '1 kg Carrot'), (41, '2021-3-18', 'Cash', 'Baba', 'Debit', -200, ''), (42, '2021-3-18', 'Bank of Baroda', 'Baba', 'Debit', -10, 'Checking the Speed.'), (43, '2021-03-18', 'Bank of Baroda', 'Personal Expenses', 'Debit', -45, 'Glycerin'), (44, '2021-03-18', 'Bank of Baroda', 'Personal Expenses', 'Debit', -5, 'Choclate'), (45, '2021-3-19', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (46, '2021-3-19', 'Bank of Baroda', 'Food', 'Debit', -10, 'Green Chilly'), (47, '2021-3-20', 'Bank of Baroda', 'Food', 'Debit', -160, '3-Patanjali Noodles, 1-Toast Packet'), (48, '2021-3-20', 'Bank of Baroda', 'Food', 'Debit', -77, 'Quaker Oats'), (49, '2021-3-23', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (50, '2021-3-24', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (51, '2021-3-25', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'March-April'), (52, '2021-3-25', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'March-April'), (53, '2021-3-25', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (54, '2021-3-25', 'Baba', 'Bank of Baroda', 'Credit', 1000, ''), (55, '2021-3-28', 'Bank of Baroda', 'Stationery', 'Debit', -180, 'A4 size Paper Rim 500 Pages'), (56, '2021-3-28', 'Bank of Baroda', 'Food', 'Debit', -83, 'Milk, Curd'), (57, '2021-3-28', 'Bank of Baroda', 'Personal Expenses', 'Debit', -10, 'Gulal'), (58, '2021-4-2', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (59, '2021-4-2', 'Bank of Baroda', 'Haircut', 'Debit', -100, 'Soldier Cut'), (60, '2021-4-2', 'Bank of Baroda', 'Food', 'Debit', -29, 'Milk'), (61, '2021-4-9', 'Bank of Baroda', 'Food', 'Debit', -48, 'Milk'), (62, '2021-4-13', 'MPL', 'Bank of Baroda', 'Credit', 18, 'Fruit Dart - First Play'), (63, '2021-4-13', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Fruit Dart'), (64, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 10, 'MI vs KKR Fantasy Team'), (65, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 10, "Aai's Account - Fruit Dart"), (66, '2021-4-14', 'MPL', 'Bank of Baroda', 'Credit', 16, "Aai's Account - Fruit Dart"), (67, '2021-4-15', 'MPL', 'Bank of Baroda', 'Credit', 15, "Aai's Account - SRH vs RCB Fantasy Team"), (68, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -30, 'Shimla and Green Mirch'), (69, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -35, 'Curd'), (70, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -50, 'Frozen Green Peas'), (71, '2021-4-15', 'Bank of Baroda', 'Food', 'Debit', -63, 'Cream'), (72, '2021-4-16', 'MPL', 'Bank of Baroda', 'Credit', 4, 'My Account - Speed Chess [2 Tournaments]'), (73, '2021-4-17', 'MPL', 'Bank of Baroda', 'Credit', 6, 'Fruit Chop [2 Tournaments]'), (74, '2021-4-18', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'April - May'), (75, '2021-4-19', 'Bank of Baroda', 'Mobile Recharge Aai VI', 'Debit', -49, 'April - May'), (76, '2021-4-19', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'April - May'), (77, '2021-4-22', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - PK vs SRH'), (78, '2021-4-24', 'MPL', 'Bank of Baroda', 'Credit', 10, 'Gourav My11 - MI vs PK'), (79, '2021-4-29', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - MI vs RR'), (80, '2021-5-1', 'Bank', 'Bank of Baroda', 'Credit', 17, 'Bank Interest'), (81, '2021-5-3', 'MPL', 'Bank of Baroda', 'Credit', 5, 'Gourav My11 - SRH vs RR'), (82, '2021-5-10', 'Baba', 'Bank of Baroda', 'Credit', 500, 'For the Google Pay and Paytm'), (83, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -151, 'Google Pay 1st Transaction'), (84, '2021-5-10', 'Google Pay', 'Bank of Baroda', 'Credit', 21, '1st Cashback'), (85, '2021-5-10', 'Bank of Baroda', 'Food', 'Debit', -150, 'Chapati'), (86, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -1, 'Paytm 1st Transaction'), (87, '2021-5-10', 'Paytm', 'Bank of Baroda', 'Credit', 5, '1st Cashback'), (88, '2021-5-10', 'Bank of Baroda', 'Baba', 'Debit', -1, 'By Paytm for reward, got 0'), (89, '2021-5-10', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'May - June'), (90, '2021-5-10', 'Paytm', 'Bank of Baroda', 'Credit', 20, "Cashback On Aai's Recharge"), (91, '2021-5-12', 'Baba', 'Bank of Baroda', 'Credit', 51, 'For D2H payment'), (92, '2021-5-12', 'Bank of Baroda', 'D2H', 'Debit', -200, 'By Google Pay'), (93, '2021-5-12', 'Google Pay', 'Bank of Baroda', 'Credit', 27, 'For D2H payment'), (94, '2021-5-15', 'Baba', 'Paytm Voucher', 'Credit', 100, ''), (95, '2021-6-2', 'Baba', 'Bank of Baroda', 'Credit', 500, ''), (96, '2021-6-2', 'Bank of Baroda', 'Electricity Bill', 'Debit', -240, 'May Electricity Bill'), (97, '2021-6-2', 'Bank of Baroda', 'Paytm Voucher', 'Credit', 1, ''), (98, '2021-6-2', 'Bank of Baroda', 'Paytm Voucher', 'Debit', -1, ''), (99, '2021-6-5', 'Bank of Baroda', 'Mobile Recharge Aai Jio', 'Debit', -149, 'June-July'), (100, '2021-6-7', 'Bank of Baroda', 'Bank', 'Debit', -17.7, 'SMS Charges'), (101, '2021-6-7', 'Bank of Baroda', 'Food', 'Debit', -30, 'Potatoes'), (102, '2021-6-7', 'Baba', 'Bank of Baroda', 'Credit', 500, ''), (103, '2021-6-7', 'Bank of Baroda', 'Mobile Recharge My Jio', 'Debit', -149, 'June-July'), (104, '2021-6-13', 'MPL', 'Bank of Baroda', 'Credit', 3, "Aai's VI Account"), (105, '2021-6-13', 'MPL', 'Bank of Baroda', 'Credit', 19, "Aai's VI Account"), (106, '2021-6-14', 'MPL', 'Bank of Baroda', 'Credit', 6, "Aai's VI Account"), (107, '2021-6-15', 'MPL', 'Bank of Baroda', 'Credit', 6, "Aai's VI Account"), (108, '2021-6-17', 'Bank of Baroda', 'Food', 'Debit', -96, '2 Litre Milk'), (109, '2021-6-20', 'Baba', 'Bank of Baroda', 'Credit', 1000, 'For Exam Fee'), (110, '2021-6-20', 'Bank of Baroda', 'College Stuff', 'Debit', -400, 'Exam Form'), (111, '2021-6-21', 'Bank of Baroda', 'Food', 'Debit', -251, 'Samose'), (112, '2021-6-21', 'Bank of Baroda', 'Electricity Bill', 'Debit', -340, 'May'), (113, '2021-6-21', 'Google Pay', 'Bank of Baroda', 'Credit', 5, 'CashBack'), (114, '2021-6-21', 'Bank of Baroda', 'Food', 'Debit', -96, 'Milk')],
                labels=["Id","Date","From","To","Credit/Debit","Amount","Narration"],
                centered=False
            )
#print(t)

# Computer Science Project By :-
# Kartavya Singh XII-B Roll No.- 11
# Saketh Anand   XII-B Roll No.- 20

import pickle
from os import remove, rename

def getlen():
    frobj=open('ITEM1.DAT', 'rb')
    count=0
    try:
        while True:
            item=pickle.load(frobj)
            count+=1
    except:
        frobj.close()
    return count

def additem(n):
    fobj=open('ITEM1.DAT', 'ab')
    code=getlen()
    for i in range (0, n):
        ICode+=1
        Item_Particular=input('Item ? ')
        Rate=float(input('Rate ? '))
        while True:
            if Rate<=0:
                Rate=float(input('Enter valid Rate (> 0) ! '))
            else:
                break
        Quantity=int(input('Quantity ? '))
        while True:
            if Quantity<=0:
                Quantity=int(input('Enter valid Quantity (> 0) ! '))
            else:
                break
        item={'icode':ICode, 'name':Item_Particular.upper(), 'rate':Rate, 'quantity':Quantity}
        pickle.dump(item, fobj)
    fobj.close()

def showitem():
    frobj=open('ITEM1.DAT', 'rb')
    icode='ICode'
    name='ItemParticular'
    rate='Rate'
    quan='Quantity'
    print('%-6s %-15s %-5s %9s' %(icode, name, rate, quan))
    try:
        while True:
            item=pickle.load(frobj)
            print('%-6i %-15s %-14f %-1i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        frobj.close()

def search_icode():
    code=int(input('Enter the code to be searched ? '))
    fobj=open('ITEM1.DAT', 'rb')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
                found=1
    except:
        fobj.close()
    if found==0:
        print('\nNo item with the code %i was found in the list ' %(code))

def search_iname():
    na=input('Enter the item particular (name) to be searched ? ')
    fobj=open('ITEM1.DAT', 'rb')
    found=0
    name=na.upper()
    try:
        while True:
            item=pickle.load(fobj)
            if name==item['name']:
                print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
                found=1
    except:
        fobj.close()
    if found==0:
        print('\nNo item with the name %s was found in the list ' %(name))
        
def modify_iname():
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()
    fobj=open('ITEM1.DAT', 'rb')
    code=int(input('Enter code of the item to modify name ? '))
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                na=input('New Item name ?')
                name=na.upper()
                icode=item['icode']
                iquan=item['quantity']
                irate=item['rate']
                new_item={'icode':icode, 'name':name, 'rate':irate, 'quantity':iquan}
                pickle.dump(new_item, ftobj)
                found=1
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    if found==0:
        print('\nNo item with the code %i is present ' %(code))
    showitem()
    
def modify_irate():
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()
    fobj=open('ITEM1.DAT', 'rb')
    code=int(input('Enter code of the item to modify rate ? '))
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                rate=float(input('New Rate ?'))
                while True:
                    if rate<=0:
                        rate=float(input('Enter valid Rate (> 0) ! '))
                    else:
                        break
                icode=item['icode']
                iquan=item['quantity']
                iname=item['name']
                new_item={'icode':icode, 'name':iname, 'rate':rate, 'quantity':iquan}
                pickle.dump(new_item, ftobj)
                found=1
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    if found==0:
        print('\nNo item with the code %i is present ' %(code))
    showitem()
    
def modify_iquantity():
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()
    fobj=open('ITEM1.DAT', 'rb')
    code=int(input('Enter code of the item to modify quantity ? '))
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                quantity=int(input('New Quantity ?'))
                while True:
                    if quantity<=0:
                        quantity=int(input('Enter valid Quantity (> 0) ! '))
                    else:
                        break
                icode=item['icode']
                iname=item['name']
                irate=item['rate']
                new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':quantity}
                pickle.dump(new_item, ftobj)
                found=1
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    if found==0:
        print('\nNo item with the code %i is present ' %(code))
    showitem()
    
def search_menu():
    while True:
        print('\nSearch items using -\n 1) ICode\n 2) ItemParticular\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            search_icode()
        elif ch==2:
            search_iname()
        elif ch==0:
            break
        else:
            continue
            
def modify_menu():
    while True:
        print('\nModify items -\n 1) ItemParticular\n 2) Rate\n 3) Quantity\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            modify_iname()
        elif ch==2:
            modify_irate()
        elif ch==3:
            modify_iquantity()
        elif ch==0:
            break
        else:
            continue

def search_modify_menu():
    while True:
        print('\n1) Search items\n2) Modify items\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            search_menu()
        elif ch==2:
            modify_menu()
        elif ch==0:
            break
        else:
            continue
            
def del_code():
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    fdobj=open('DEL.DAT', 'wb')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()
    fobj=open('ITEM1.DAT', 'rb')
    code=int(input('Enter code of the item to delete ? '))
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                pickle.dump(item, fdobj)
                found=1
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    fdobj.close()
    remove('DEL.DAT')
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    if found==0:
        print('\nNo item with the code %i is present ' %(code))
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    item=pickle.load(fobj)
    new_code=1
    if item['icode']!=1:
        quantity=item['quantity']
        icode=1
        iname=item['name']
        irate=item['rate']
        new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':quantity}
        pickle.dump(new_item, ftobj)
    else:
        pickle.dump(item, ftobj)
    try:
        while True:
            item=pickle.load(fobj)
            diff=item['icode'] - new_code
            if diff!=1:
                quantity=item['quantity']
                icode=item['icode'] - 1
                iname=item['name']
                irate=item['rate']
                new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':quantity}
                pickle.dump(new_item, ftobj)
                new_code=icode
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    showitem()        
    
def del_name():
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    fdobj=open('DEL.DAT', 'wb')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            print('%-6i %-15s %5f %9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()
    fobj=open('ITEM1.DAT', 'rb')
    na=input('Enter name of the item to delete ? ')
    name=na.upper()
    try:
        while True:
            item=pickle.load(fobj)
            if name==item['name']:
                pickle.dump(item, fdobj)
                found=1
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    fdobj.close()
    remove('DEL.DAT')
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    if found==0:
        print('\nNo item with the code %i is present ' %(code))
    fobj=open('ITEM1.DAT', 'rb')
    ftobj=open('TEMP.DAT', 'ab')
    item=pickle.load(fobj)
    new_code=1
    if item['icode']!=1:
        quantity=item['quantity']
        icode=1
        iname=item['name']
        irate=item['rate']
        new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':quantity}
        pickle.dump(new_item, ftobj)
    else:
        pickle.dump(item, ftobj)
    try:
        while True:
            item=pickle.load(fobj)
            diff=item['icode'] - new_code
            if diff > 1:
                quantity=item['quantity']
                icode=item['icode'] - 1
                iname=item['name']
                irate=item['rate']
                new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':quantity}
                pickle.dump(new_item, ftobj)
                new_code=icode
            else:
                pickle.dump(item, ftobj)
    except:
        fobj.close()
    ftobj.close()
    remove('ITEM1.DAT')
    rename('TEMP.DAT', 'ITEM1.DAT')
    showitem()  
    
def delete_menu():
    while True:
        print('\nDelete using - \n 1) Name\n 2) Code')
        ch=int(input('Enter choice ? '))
        if ch==1:
            del_name()
        elif ch==2:
            del_code()
        elif ch==0:
            break
        else:
            continue

def less_than():
    fobj=open('ITEM1.DAT', 'rb')
    icode='ICode'
    name='ItemParticular'
    rate='Rate'
    quan='Quantity'
    print('%-6s %-15s %-5s %-9s' %(icode, name, rate, quan))
    try:
        while True:
            item=pickle.load(fobj)
            if item['quantity'] < 20:
                print('%-6i %-15s %-5f %-9i' %(item['icode'], item['name'], item['rate'], item['quantity']))
    except:
        fobj.close()

def getno():
    frobj=open('SALES.DAT', 'rb')
    count=0
    try:
        while True:
            item=pickle.load(frobj)
            count=count+1
    except:
        frobj.close()
    return count

def validate_day(dd, mm, yyyy):
    valid=0
    if yyyy%400==0 or yyyy%4==0 and yyyy%100!=0:
        if mm in (1, 3, 5, 7, 8, 10, 12):
            if dd<=31 and dd>=1:
                valid=1
            else: 
                valid=0
        elif mm in (4, 6, 9, 11):
            if dd<=30 and dd>=1:
                valid=1
            else:
                valid=0
        elif mm==2:
            if dd<=29 and dd>=1:
                valid=1
            else:
                valid=0
    else:
        if mm in (1, 3, 5, 7, 8, 10, 12):
            if dd<=31 and dd>=1:
                valid=1
            else: 
                valid=0
        elif mm in (4, 6, 9, 11):
            if dd<=30 and dd>=1:
                valid=1
            else:
                valid=0
        elif mm==2:
            if dd<=28 and dd>=1:
                valid=1
            else:
                valid=0
    return valid

def validate_month(mm):
    valid_m=0
    if mm>=1 and mm<=12:
        valid_m=1
    else:
        valid_m=0
    return valid_m

def validate_year(yyyy):
    valid_y=0
    if yyyy>=1:
        valid_y=1
    else:
        valid_y=0
    return valid_y

def searchcode(code):
    fobj=open('ITEM1.DAT', 'rb')
    found=0
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                found=1
    except:
        fobj.close()
    return found

def get_item_quantity(code):
    fobj=open('ITEM1.DAT', 'rb')
    quantity=0
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                quantity=item['quantity']
    except:
        fobj.close()
    return quantity

def get_item_rate(code):
    fobj=open('ITEM1.DAT', 'rb')
    rate=0
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                rate=item['rate']
    except:
        fobj.close()
    return rate

def get_item_name(code):
    fobj=open('ITEM1.DAT', 'rb')
    name=[]
    try:
        while True:
            item=pickle.load(fobj)
            if code==item['icode']:
                name.append(item['name'])
    except:
        fobj.close()
    return name

def cash_memo_init():
    fmobj=open('SALES.DAT', 'ab')
    memo_no=getno()
    memo_no=memo_no+1
    dd=int(input('Enter day(dd) ? '))
    mm=int(input('Enter month(mm) ? '))
    yyyy=int(input('Enter year(yyyy) ? '))
    while True:
        valid=validate_day(dd, mm, yyyy)
        valid_m=validate_month(mm)
        valid_y=validate_year(yyyy)
        if valid==1 and valid_m==1 and valid_y==1:
            break
        elif valid==0 or valid_m==0 or valid_y==0:
            print('Invalid date ! ')
            dd=int(input('Enter day(dd) ? '))
            mm=int(input('Enter month(mm) ? '))
            yyyy=int(input('Enter year(yyyy) ? '))
    items_in_list=getlen()
    no_items=int(input('Number of different items purchased'))
    while True:
        if no_items<=items_in_list and no_items >=1:
            break
        else:
            no_items=int(input('Enter valid number of items ! '))
    grand_total=0
    item_codes={}
    items_bought=[]
    for i in range (0, no_items):
        showitem()
        frobj=open('ITEM1.DAT', 'rb')
        ftobj=open('TEMP.DAT', 'ab')
        code=int(input('Enter code of item ? '))
        valid_q=0
        while True:
            found=searchcode(code)
            if found==1:
                break
            else:
                code=int(input('Enter present code ! '))
        items_bought.append(code)
        quantity=int(input('Enter quantity of the corresponding item ? '))
        quan=get_item_quantity(code)
        while True:
            if quantity<=quan:
                break
            else:
                quantity=int(input('Enter valid quantity ! '))
        item_codes.update({code:quantity})
        rate=0
        try:
            while True:
                item=pickle.load(frobj)
                if code==item['icode']:
                    new_quantity=item['quantity'] - quantity
                    icode=item['icode']
                    iname=item['name']
                    irate=item['rate']
                    rate=irate
                    new_item={'icode':icode, 'name':iname, 'rate':irate, 'quantity':new_quantity}
                    pickle.dump(new_item, ftobj)
                else:
                    pickle.dump(item, ftobj)
        except:
            frobj.close()
        ftobj.close()
        remove('ITEM1.DAT')
        rename('TEMP.DAT', 'ITEM1.DAT')
        gt=quantity * rate
        grand_total=grand_total+gt
    memos={'memo_no':memo_no, 'day':dd, 'month':mm, 'year':yyyy, 'no_items':no_items, 'grand_total':grand_total, 'items_bought(code)':items_bought}
    pickle.dump(memos, fmobj)
    fmobj.close()
    products_sold={'memo_no':memo_no, 'day':dd, 'month':mm, 'year':yyyy}
    prod_sold={}
    for key in item_codes.keys():
        prod_sold.update({key:item_codes[key]})
    products_sold.update(prod_sold)
    fkobj=open('PRSALES.DAT', 'ab')
    pickle.dump(products_sold, fkobj)
    fkobj.close()
    return memo_no

def clear_sales_file():
    fobj=open('SALES.DAT','rb')
    ftobj=open('TEMP.DAT', 'ab')
    fobj.close()
    ftobj.close()
    remove('SALES.DAT')
    rename('TEMP.DAT', 'SALES.DAT')
    
def showmemo():
    fobj=open('SALES.DAT', 'rb')
    try:
        while True:
            memos=pickle.load(fobj)
            print(memos)
    except:
        fobj.close()

def cashmemo():
    fobj=open('SALES.DAT', 'rb')
    mno=int(input('Enter memo number ? '))
    found=0
    print('\n\n')
    try:
        while True:
            memo=pickle.load(fobj)
            if mno==memo['memo_no']:
                fsobj=open('PRSALES.DAT', 'rb')
                try:
                    while True:
                        prsales=pickle.load(fsobj)
                        if mno==prsales['memo_no']:
                            daystr=str(prsales['day'])
                            monthstr=str(prsales['month'])
                            yearstr=str(prsales['year'])
                            datestr='Date : '+daystr+'/'+monthstr+'/'+yearstr
                            mnostr=str(mno)
                            memo_str='Cash Memo Number : '+mnostr
                            print('%-20s %50s' %(datestr, memo_str))
                            sno='Sno'
                            it_code='ItemCode'
                            particular='Particular'
                            ra='Rate'
                            quan='Quantity'
                            amo='Amount'
                            print('%-10s %-10s %-20s %-10s %-10s %-10s' %(sno, it_code, particular, ra, quan, amo))
                            prod_list=memo['items_bought(code)'] 
                            length=len(prod_list)
                            for i in range (0, length):
                                code=prod_list[i]
                                s_no=i+1
                                name_lis=get_item_name(code)
                                name=name_lis[0]
                                rate=get_item_rate(code)
                                quantity=prsales[code]
                                amount=rate * quantity
                                print('%-10i %-10i %-20s %-10f %-10i %-10f' %(s_no, code, name, rate, quantity, amount))
                            grand_t='Grand Total'
                            gt=memo['grand_total']
                            print('%-20s %54f' %(grand_t, gt))
                except:
                    fsobj.close()
    except:
        fobj.close()

def cash_memo(mno):
    fobj=open('SALES.DAT', 'rb')
    found=0
    print('\n\n')
    try:
        while True:
            memo=pickle.load(fobj)
            if mno==memo['memo_no']:
                fsobj=open('PRSALES.DAT', 'rb')
                try:
                    while True:
                        prsales=pickle.load(fsobj)
                        if mno==prsales['memo_no']:
                            daystr=str(prsales['day'])
                            monthstr=str(prsales['month'])
                            yearstr=str(prsales['year'])
                            datestr='Date : '+daystr+'/'+monthstr+'/'+yearstr
                            mnostr=str(mno)
                            memo_str='Cash Memo Number : '+mnostr
                            print('%-20s %50s' %(datestr, memo_str))
                            sno='Sno'
                            it_code='ItemCode'
                            particular='Particular'
                            ra='Rate'
                            quan='Quantity'
                            amo='Amount'
                            print('%-10s %-10s %-20s %-10s %-10s %-10s' %(sno, it_code, particular, ra, quan, amo))
                            prod_list=memo['items_bought(code)'] 
                            length=len(prod_list)
                            for i in range (0, length):
                                code=prod_list[i]
                                s_no=i+1
                                name_lis=get_item_name(code)
                                name=name_lis[0]
                                rate=get_item_rate(code)
                                quantity=prsales[code]
                                amount=rate * quantity
                                print('%-10i %-10i %-20s %-10f %-10i %-10f' %(s_no, code, name, rate, quantity, amount))
                            grand_t='Grand Total'
                            gt=memo['grand_total']
                            print('%-20s %54f' %(grand_t, gt))
                except:
                    fsobj.close()
    except:
        fobj.close()

def day_report(dd, mm, yyyy):
    fobj=open('SALES.DAT', 'rb')
    total=0
    try:
        while True:
            memo=pickle.load(fobj)
            if mm==memo['month'] and yyyy==memo['year'] and dd==memo['day']:
                total=total+memo['grand_total']
    except:
        fobj.close()
    return total

def daily_report():
    dd=int(input('Enter day ? '))
    mm=int(input('Enter month ? '))
    yyyy=int(input('Enter year ? '))
    total=day_report(dd, mm, yyyy)
    dstr=str(dd)
    tstr=str(total)
    mstr=str(mm)
    ystr=str(yyyy)
    datestr='Date : '+dstr+'/'+mstr+'/'+ystr
    gt='Total Sale : '+tstr
    print('%-30s %20s' %(datestr, gt))
        
def get_month_report(mm, yyyy):
    fobj=open('SALES.DAT', 'rb')
    total=0
    try:
        while True:
            memo=pickle.load(fobj)
            if mm==memo['month'] and yyyy==memo['year']:
                total=total+memo['grand_total']
    except:
        fobj.close()
    return total

def monthly_report():
    months={1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
              7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December',}
    yyyy=int(input('Enter a year to get Monthly reports ? '))
    for i in range (1, 13):
        total=get_month_report(i, yyyy)
        month=months[i]
        gt=str(total)
        mon='Month : '+month
        tot='Total Sale : '+gt
        print('%-30s %20s' %(mon, tot))

def year_report(yyyy):
    y_total=0
    for i in range (1, 13):
        total=get_month_report(i, yyyy)
        y_total=y_total+total
    return y_total
                
def yearly_report():
    yyyy=int(input('Enter the year to get its yearly report ? '))
    y_total=year_report(yyyy)
    ystr=str(yyyy)
    year='Year : '+ystr
    ytstr=str(y_total)
    yt='Total Sale : '+ytstr
    print('%-20s %20s' %(year, yt))

def item_wise_report():
    dic={}
    codes=[]
    vals=[]
    fobj=open('ITEM1.DAT', 'rb')
    tot=0
    try:
        while True:
            item=pickle.load(fobj)
            dic.update({item['icode']:tot})
    except:
        fobj.close()
    for key in dic.keys():
        codes.append(key)
    dd=int(input('Enter day ? '))
    mm=int(input('Enter month ? '))
    yyyy=int(input('Enter year ? '))
    ftobj=open('PRSALES.DAT', 'rb')
    try:
        while True:
            memo=pickle.load(ftobj)
            if mm==memo['month'] and yyyy==memo['year'] and dd==memo['day']:
                for code in codes:
                    sums=dic[code]
                    if code in memo.keys():
                        sums=sums+memo[code]
                    dic[code]=sums
    except:
        ftobj.close()
    dstr=str(dd)
    mstr=str(mm)
    ystr=str(yyyy)
    datestr='Date : '+dstr+'/'+mstr+'/'+ystr
    print(datestr)
    dic1={}
    for key in dic.keys():
        fobj=open('ITEM1.DAT', 'rb')
        try:
            while True:
                item=pickle.load(fobj)
                if key==item['icode']:
                    dic1.update({item['name']:dic[key]})
        except:
            fobj.close()
    for key in dic1.keys():
        print('%-20s %5i' %(key, dic1[key]))

def search_menu():
    while True:
        print('\nSearch items using -\n 1) ICode\n 2) ItemParticular\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            search_icode()
        elif ch==2:
            search_iname()
        elif ch==0:
            break
        else:
            continue
            
def modify_menu():
    while True:
        print('\nModify items -\n 1) ItemParticular\n 2) Rate\n 3) Quantity\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            modify_iname()
        elif ch==2:
            modify_irate()
        elif ch==3:
            modify_iquantity()
        elif ch==0:
            break
        else:
            continue

def search_modify_menu():
    while True:
        print('\n1) Search items\n2) Modify items\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            search_menu()
        elif ch==2:
            modify_menu()
        elif ch==0:
            break
        else:
            continue
            
def delete_menu():
    while True:
        print('\nDelete using - \n 1) Name\n 2) Code\n 0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            del_name()
        elif ch==2:
            del_code()
        elif ch==0:
            break
        else:
            continue
            
def itemfiles():
    while True:
        print('\n1) Add records \n2) Show records\n3) Search and Modify menu\n4) Delete Items\n5) List of low stocked items\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            n=int(input('Enter number of records to add'))
            additem(n)
        elif ch==2:
            showitem()
        elif ch==3:
            search_modify_menu()
        elif ch==4:
            delete_menu()
        elif ch==5:
            less_than()
        elif ch==0:
            break
        else:
            continue

def sales_report():
    while True:
        print('\n1) Daily Reports\n2) Monthly Reports\n3) Yearly Report\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            daily_report()
        elif ch==2:
            monthly_report()
        elif ch==3:
            yearly_report()
        elif ch==0:
            break
        else:
            continue
            
def report_menu():
    while True:
        print('\n1) Sales Report\n2) Item-wise Report\n 0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            sales_report()
        elif ch==2:
            item_wise_report()
        elif ch==0:
            break
        else:
            continue 

def sales_files_s():
    while True:
        print('\n1) View all bills\n2) View a cash memo\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            showmemo()
        elif ch==2:
            cashmemo()
        elif ch==0:
            break
        else:
            continue
        
def staff():
    while True:
        print('\n1) Items file\n2) Sales reports\n3) Sales file\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            itemfiles()
        elif ch==2:
            report_menu()
        elif ch==3:
            sales_files_s()
        elif ch==0:
            break
        else:
            continue
            
def customer():
    while True:
        print('\n1) View Products\n2) Make Purchase and view bill\n0) Previous Menu\n')
        ch=int(input('Enter choice ? '))
        if ch==1:
            showitem()
        elif ch==2:
            memo_no=cash_memo_init()
            cash_memo(memo_no)
        elif ch==0:
            break
        else:
            continue
            
def main_menu():
    while True:
        print('\nSales Management System\n')
        print('\n1) Staff\n2) Customer')
        print('0) EXIT')
        ch=int(input('Enter choice ? '))
        if ch==1:
            staff()
        elif ch==2:
            customer()
        elif ch==0:
            break
        else:
            continue

main_menu()

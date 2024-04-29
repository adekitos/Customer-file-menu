#Import csv and os
import csv
import os
from shutil import copyfile

#Global constants
CSVFILE = 'customers.csv'

CSVFILE_BKUP = 'customers_BKUP.csv'
TEMPFILE = 'customer-temp.csv'
INDENT1 = ' '*3
INDENT2 = ' '*2


def main():
##    found = False
##    #Open file for READING
##    infile = open(CSVFILE,'r', newline='')
##    outfile = open(TEMPFILE, 'w', newline='')
##    outfile1 = open(CSVFILE, 'a', newline='')
##    
##    #Create reader & writer objects
##    reader = csv.reader(infile)
##    writer = csv.writer(outfile)
##    writer1 = csv.writer(outfile1)
##    
##    #Read & write field names
##    fields = next(reader) # from infile
##    writer.writerow(fields) # to outfile
##    
    #header
    print('*'*60)
    header = "Victorino Insurance - Customer Data"
    print(f'{header:^60}')
    print()
    print(INDENT1, "1 - View customer list")
    print(INDENT1, "2 - Lookup customer")
    print(INDENT1, "3 - Enter new customer")
    print(INDENT1, "4 - Update customer")
    print(INDENT1, "5 - Delete customer", "\n")
    print(INDENT1, "7 - Restore customer data - for testing only")
    print(INDENT2, "99 - Exit")
    print('*'*60, '\n')
    
    
    y = False
    while y == False:
        option = input('  Enter a menu option: ')
        if option == '1':
            view_cust_list(CSVFILE, TEMPFILE)
        elif option == '2':
            lookup_cust(CSVFILE, TEMPFILE)
        elif option == '3':
            Enter_new_cust(CSVFILE, TEMPFILE)
        elif option == '4':
            update_cust(CSVFILE, TEMPFILE)
        elif option == '5':
            del_cust(CSVFILE, TEMPFILE)
        elif option == '7':
            restore_cust_data(CSVFILE, CSVFILE_BKUP)
        elif option == '99':
            exit()
            y = True
        else:
            print("  Input invalid. Kindly Enter a valid menu option ", '\n')

#option 1
def view_cust_list(CSVFILE, TEMPFILE):
    found = False
    #Open file for READING
    infile = open(CSVFILE,'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
    outfile1 = open(CSVFILE, 'a', newline='')
    
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer1 = csv.writer(outfile1)
    
    #Read & write field names
    fields = next(reader) # from infile
    writer.writerow(fields) # to outfile

    print(f'    {fields[0]:7} {fields[1]:10} {fields[2]:10}')
    print(' '*3, '-'*7,'-'*10,'-'*10)
    #Loop through reader
    count = 0
    for row in reader:
        
        #Extract values from row
        cust_id = row[0]
        cust_lst_nm = row[1]
        cust_fst_nm = row[2]
        count += 1
        #Display row
        
        print(f'    {cust_id:7} {cust_lst_nm:10} {cust_fst_nm:10}')

    print()

    print('    >>> Total customers: ', count,'\n')

        

    
#option 2
def lookup_cust(CSVFILE, TEMPFILE):
    found = False
    #Open file for READING
    infile = open(CSVFILE,'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
    outfile1 = open(CSVFILE, 'a', newline='')
    
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer1 = csv.writer(outfile1)
    
    #Read & write field names
    fields = next(reader) # from infile
    writer.writerow(fields) # to outfile


    print('-'*45, '\n')
    print(' '*6, '*** Lookup Customer ***')  

    search_id = input('\n    Enter a Customer ID: ')
    
##    print(len(search_id))
    while not search_id.isdigit() or len(search_id) != 3:
        search_id = input('\n    Invalid input. Kindly enter an integer. \n    Enter a Customer ID: ')

    print()
    
    #Loop through customer ID
    for row in reader:
        cust_id = row[0]
        lst_nm = row[1]
        fst_nm = row[2]
        if cust_id == search_id:
            found = True
            print(' '*3, 'Customer record found')
            print(' '*3,'-'*30)
            print(' '*3, 'Customer ID: ', cust_id)
            print(' '*3, 'Last Name:   ', lst_nm)
            print(' '*3, 'First Name:  ', fst_nm, '\n')
            break
        
    if not found:
        print('   Customer ID not found', '\n')    
        
    

#option 3
def Enter_new_cust(CSVFILE, TEMPFILE):

    found = False
    #Open file for READING
    infile = open(CSVFILE,'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
    outfile1 = open(CSVFILE, 'a', newline='')
    
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer1 = csv.writer(outfile1)
    
    #Read & write field names
    fields = next(reader) # from infile
    writer.writerow(fields) # to outfile
    
    
    print('-'*45, '\n')
    print(' '*4, '*** Enter New Customer ***','\n')    


    cust_id = input('    Enter Customer ID: ')    
    while not cust_id.isdigit() or len(cust_id) != 3:
        cust_id = input('\n   Invalid input. Kindly enter an integer. \n   Enter Customer ID: ')
    cust_id = int(cust_id)
        
    lst_nm = input('    Enter Last Name:   ')
    while not lst_nm.isalpha():
        lst_nm = input('\n   Invalid input. Kindly enter an alphabet. \n   Enter Last Name: ')
    lst_nm = str(lst_nm)
        
    fst_nm = input('    Enter First Name:  ')
    while not lst_nm.isalpha():
        fst_nm = input('\n   Invalid input. Kindly enter an alphabet. \n   Enter First Name: ')
    fst_nm = str(fst_nm)

    valid = True
    for row in reader:
        cust_ids_in_list = int(row[0])
        if cust_ids_in_list == cust_id:
            valid = False
            break
        
    if valid == True:
        new_row = [cust_id, lst_nm, fst_nm]
        writer1.writerow(new_row)
        print()
        print(' '*3,'STATUS: Customer ', cust_id, 'saved!', '\n')
    else:
        print('  The Customer ID is already used.', '\n')
    
    outfile1.close()

#option 4
def update_cust(CSVFILE, TEMPFILE):

    found = False
    #Open file for READING
    infile = open(CSVFILE,'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
    outfile1 = open(CSVFILE, 'a', newline='')
    
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer1 = csv.writer(outfile1)
    
    #Read & write field names
    fields = next(reader) # from infile
    writer.writerow(fields) # to outfile
    
    
    print('-'*45, '\n')
    print(' '*6, '*** update Customer ***','\n')   

    search_id = input('    Enter Customer ID: ')    
    while not search_id.isdigit() or len(search_id) != 3:
        search_id = input('\n   Invalid input. Kindly enter an integer. \n   Enter Customer ID: ')


    print('\n')  
    
    for row in reader:
        cust = row[0]
        last = row[1]
        first = row[2]
        if cust == search_id:
            found = True
            count = 1
            print(' '*3,'Enter new values (or press enter to skip)')
            print(' '*3, '-'*45)
    
            
            valid = False
            while valid == False:
                cust_id = input('      Enter new customer id: ')
                if cust_id.isdigit() or cust_id == '' or len(cust_id)!=3:
                    valid = True
                    cust_id = search_id
                else:
                    print('      Invalid input. Kindly enter an integer')
                    
            valid1 = False    
            while valid1 == False:
                lst_nm = input('      Enter new last name:   ')
                if lst_nm.isalpha() or lst_nm == '':
                    valid1 = True
                    if lst_nm == '':
                        lst_nm = last
                        
                else:
                    print('\n      Invalid input. Kindly enter an alphabet')
                    

            valid2 = False    
            while valid2 == False:
                fst_nm = input('      Enter new first name:  ')
                if fst_nm.isalpha() or fst_nm == '':
                    valid2 = True
                    if fst_nm ==  '':
                        fst_nm = first
                        
                else:
                    print('\n      Invalid input. Kindly enter an alphabet')
                             
            
            new_row = [cust_id, lst_nm, fst_nm]
            writer.writerow(new_row)
           
        else:
            writer.writerow(row)
        
    if found:
        print('\n',' '*3, 'STATUS: Customer ', cust_id, ' updated!','\n')
        #close files
        infile.close()
        outfile.close()
        outfile1.close()
    
        #Replace original file w/the new file
        os.remove(CSVFILE)
        os.rename(TEMPFILE,CSVFILE)
    else:
        print(' '*3, 'Customer ID ', search_id,' not found', '\n')
        
    
                    

# option 5
def del_cust(CSVFILE, TEMPFILE):

    found = False
    #Open file for READING
    infile = open(CSVFILE,'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
    outfile1 = open(CSVFILE, 'a', newline='')
    
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer1 = csv.writer(outfile1)
    
    #Read & write field names
    fields = next(reader) # from infile
    writer.writerow(fields) # to outfile
    
    
    print(' ', '-'*45, '\n')
    print(' '*6, '*** Delete Customer ***')
    
    search_id = input('\n    Enter a customer ID: ')
    search_id_len = len(search_id)
    #Validate input
    while not search_id.isdigit() or search_id_len != 3:
        search_id = input('   Invalid input. Please enter an integer. \n   Enter a customer ID: ')
    
    print()
    #Loop through reader
    for row in reader:
        #Extract values
        cust_id = row[0]
        cust_lst_nm = row[1]
        cust_fst_nm = row[2]
        if cust_id == search_id:
            found = True
            cust_id_found = cust_id
            cust_lst_nm_found = cust_lst_nm
            cust_fst_nm_found = cust_fst_nm
        else:
            writer.writerow(row)
                
    if found:
        print(' '*3,'Customer record found')
        print(' '*3, '-'*30)
        print(' '*5, 'customer ID: ', cust_id_found)
        print(' '*5, 'Last name:   ', cust_lst_nm_found)
        print(' '*5, 'First name:  ', cust_fst_nm_found)
        print()
            
        del_conf = input('    Are you sure you want to delete (y/n)? ').lower()
    else:
        print(' '*3, 'Customer ID not found')
        del_conf == 'n'

    #Close file        
    infile.close()
    outfile.close()
    outfile1.close()
            
        
    if del_conf == 'y':
        os.remove(CSVFILE)
        os.rename(TEMPFILE, CSVFILE)
        print('\n',' '*2, 'STATUS: Customer', cust_id_found, 'deleted!' )
    elif del_conf == 'n':
        print('  >>> No record was deleted', '\n')
    else:
        print('   >>>Invalid input!!. Nothing was done as the input was invalid.')
          
 
            
def restore_cust_data(CSVFILE, CSVFILE_BKUP):
    print(' ', '-'*45, '\n')
    print(' '*6, '*** Restore Customer Backup ***')
    
    copyfile(CSVFILE_BKUP,CSVFILE)
    print('\n','     Backup Restored!','\n')



main()

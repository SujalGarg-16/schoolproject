import functions
while True:
    print("\t\t---------------School Management System----------------\n")
    print("1. Student data insert\n2. Student data Search\n3. Student data Update\n4. Student data Delete\n5. Create file")
    print("6. Exit")
    choice=int(input("----Enter Option---"))
    if choice==1:
        try:
            
            functions.insert_record()
        except:
            print("----- Error Comes----Data not Saved----")
    elif choice==2:
        try:
            functions.search_record()
        except:
            break
    elif choice==3:
        try:
            functions.update_record()
        except:
            break
    elif choice==4:
        try:
            functions.delete_record()
        except:
            break
    elif choice==5:
        try:
            functions.csvfile_record()
        except:
            break
    elif choice==6:
        break
    else:
        print("----Invalid Option Selected----")
print("\n\t\t------Thank You for Using Our Software------")
        

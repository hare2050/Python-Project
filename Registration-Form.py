from tkinter import *  #registrationdb
import mysql.connector

def getvals():
    # Replace these placeholders with your actual database information
    db_host = "localhost"      # Your MySQL server host
    db_user = "root"  # Your MySQL username
    db_password = ""  # Your MySQL password
    db_name = "registrationdb"  # Your MySQL database name

    try:
        # Create a connection to the database
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        # Check if the connection was successful
        if connection.is_connected():
            print("Connected to the database")

        # Create a cursor object for executing SQL queries
        cursor = connection.cursor()
        # print(emergency1.get())

        # Define the CREATE TABLE query with correct syntax (IF NOT EXISTS)
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS formdata (
            Name VARCHAR(255),
            Phone VARCHAR(10),
            Gender VARCHAR(255),
            Emergency VARCHAR(255),
            Payment VARCHAR(255)
        )
        '''
        cursor.execute(create_table_query)

        # Define the INSERT INTO query with placeholders and values
        insert_data_query = '''
        INSERT INTO formdata (Name, Phone, Gender, Emergency, Payment) 
        VALUES (%s, %s, %s, %s, %s)
        '''

        # Replace these placeholders with your actual data
        name = name1.get();
        phone = phone1.get();
        gender = gender1.get()
        emergency = emergency1.get()
        paymentmode = paymentmode1.get()

        # Execute the INSERT INTO query with the data
        cursor.execute(insert_data_query, (name, phone, gender, emergency, paymentmode))

        # Commit the changes to the database
        connection.commit()

        print("Data inserted successfully")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection in the finally block
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
        print("accepted")



root = Tk()
root.geometry("500x300")

Label(
    root,
    text="Python Registration Form",
    font="arial 15 bold",
).grid(row=0, column=3)

# Field names
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Payment Mode")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# variable for storing data
name1 = StringVar()
phone1 = StringVar()
gender1 = StringVar()
emergency1 = StringVar()
paymentmode1 = StringVar()
checkval = IntVar



# Creating Entry Fields
nameentry = Entry(root, textvariable=name1)
phoneentry = Entry(root, textvariable=phone1)
genderentry = Entry(root, textvariable=gender1)
emergencyentry = Entry(root, textvariable=emergency1)
paymententry = Entry(root, textvariable=paymentmode1)


# packing Entry Fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# creating checkbox
checkbtn = Checkbutton(text="Remember me?", variable=checkval)
checkbtn.grid(row=6, column=3)
# submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop()




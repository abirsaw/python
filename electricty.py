print("Electricity  Bill Calculator")

amt=0
nu=float(input("Enter the number of electric units\n"))
if nu<=100:
    amt=0
    if nu>100 and nu<=200:
     amt=(nu-100)*5
     if nu>200:
        amt=500(nu-200)*10
        print(f"Amount to be paid!!{amt}")


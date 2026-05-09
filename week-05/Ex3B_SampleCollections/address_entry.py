


print("contact_info")

#mm = {"name":"amanda keke"\n"address":"4930 oakland dr"\n"city":"brooklyn"\n"state":"ny",\n"zipcode":"34905"}
mm = {"name amanda keke\n address:4930 oakland dr\n city:brooklyn\nstate:ny,\nzipcode:34905"}
contactinfo = mm

print(mm)

full_name = {"firstname":"amanda", "lastname":"keke"}

print(full_name)

full_name.update({"middlename":"lisa"})
full_name.update({"honorific":"ms."})
print(full_name)



contactinfo.update(full_name)
print(contactinfo)
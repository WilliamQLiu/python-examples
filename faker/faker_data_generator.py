""" Requires pip install fake-factory """
# pylint: disable=I0011,C0103,W0142,E1101,C0304

# http://docs.python.org/2/library/xml.etree.elementtree.html
# https://pypi.python.org/pypi/fake-factory

import xml.etree.ElementTree as ET

from faker import Factory

if __name__ == '__main__':

    faker = Factory.create()  # Create and instantiate a Faker generator

    # Setup Element Tree
    root = ET.Element("root")  # root
    calls = ET.SubElement(root, "Calls")  # Calls
    call = ET.SubElement(calls, "Call")  # Call
    reportversion = ET.SubElement(call, "ReportVersion")
    calldateandtimestart = ET.SubElement(call, "CallDateAndTimeStart")
    calldateandtimeend = ET.SubElement(call, "CallDateAndTimeEnd")
    phoneworker = ET.SubElement(call, "PhoneWorker")
    pfirstname = ET.SubElement(phoneworker, "FirstName")  # Phone Work First Name
    plastname = ET.SubElement(phoneworker, "LastName")  # Phone Work Last Name
    caller = ET.SubElement(call, "Caller")
    callername = ET.SubElement(caller, "CallerName")
    cfirstname = ET.SubElement(callername, "FirstName")  # Caller First Name
    cmiddlename = ET.SubElement(callername, "MiddleName")  # Caller Middle Name
    clastname = ET.SubElement(callername, "LastName")  # Caller Last Name
    callerlocation = ET.SubElement(caller, "CallerLocation")
    ccountry = ET.SubElement(callerlocation, "Country")
    cstateprovince = ET.SubElement(callerlocation, "StateProvince")
    ccounty = ET.SubElement(callerlocation, "County")
    ccity = ET.SubElement(callerlocation, "City")
    cpostalcode = ET.SubElement(callerlocation, "PostalCode")
    caddress = ET.SubElement(callerlocation, "Address")
    callerphonenumber = ET.SubElement(caller, "CallerPhoneNumber")
    callnotes = ET.SubElement(call, "CallNotes")


    # Put in Fake values
    call.set("ID", str(faker.random_number(digits=9)))
    reportversion.set("ID", str(faker.random_number(digits=4)))
    reportversion.text = str(faker.random_element(\
        array=('H2H', 'DDH', 'OASAS')))
    calldateandtimestart.set("TimeZone", str(faker.timezone()))
    calldateandtimestart.text = str(faker.date_time_this_year())
    calldateandtimeend.set("TimeZone", str(faker.timezone()))
    calldateandtimeend.text = str(faker.date_time_this_year())
    phoneworker.set("ID", str(faker.random_number(digits=5)))
    pfirstname.text = str(faker.first_name())  # Phone Worker First Name
    plastname.text = str(faker.last_name())  # Phone Worker Last Name
    caller.set("ID", str(faker.random_number(digits=6)))
    cfirstname.text = str(faker.first_name())  # Caller  First Name
    cmiddlename.text = str(faker.first_name())  # Caller Last Name
    clastname.text = str(faker.last_name())  # Caller Last Name
    ccountry.text = str(faker.country())
    cstateprovince.text = str(faker.state_abbr())
    ccounty.text = str(faker.city())  # Nothing for counties
    cpostalcode.text = str(faker.postcode())
    caddress.text = str(faker.street_address())
    callerphonenumber.text = str(faker.phone_number())
    callnotes.text = str(faker.paragraphs(nb=3))

    # Write entire tree to xml
    tree = ET.ElementTree(root)
    tree.write("fakedata.xml")

"""
<?xml version="1.0" encoding="utf-8"?>
<root>
  <Calls>
    <Call ID="15784825">
      <ReportVersion ID="333">H2H</ReportVersion>
      <CallDateAndTimeStart TimeZone="UTC-8">2013-10-01 00:44</CallDateAndTimeStart>
      <CallDateAndTimeEnd TimeZone="UTC-8">2013-10-01 01:27</CallDateAndTimeEnd>
      <CallLength>43</CallLength>
      <PhoneWorker ID="30591">
         <FirstName>Susan</FirstName>
         <LastName>Stevens</LastName>
      </PhoneWorker>
      <Caller ID="989898">
         <CallerName>
            <FirstName>Bob</FirstName>
            <MiddleName>Scott</MiddleName>
            <LastName>Jones></LastName>
         </CallerName>
         <CallerLocation>
            <Country>US</Country>
            <StateProvince>CA</StateProvince>
            <County>Alameda</County>
            <City>Oakland</City>
            <PostalCode>94444</PostalCode>
            <Address>133 Elm Street</Address>
         </CallerLocation>
         <CallerPhoneNumber>510-555-1212</CallerPhoneNumber>
      </Caller>
      <CallNotes>This is my note!  My notes can be very long.</CallNotes>
      <CustomFields>
            <Field ID="1234" FieldName="Gender">
                <Value ID="9876">Male</Value>
            </Field>
            <Field ID="1235" FieldName="Age Group">
                <Value ID="9875">25-29</Value>
            </Field>
            <Field ID="1236" FieldName="Mental Status Assessment - Functional">
                <Value ID="9874">Sleep disturbance</Value>
                <Value ID="9873">Fatigued</Value>
                <Value ID="9872">Depressed</Value>
            </Field>
      </CustomFields>
    </Call>
  </Calls>
</root>
"""
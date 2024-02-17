from tkinter import *
from tkinter import messagebox
import requests
import json
import csv
from tkinter import ttk


api_key = "ebbbdc38671df2fd123b07496a7dd98c"
root =Tk()
root.title('Air Quality Application')
root.iconbitmap("logo1.ico")
root.geometry("1024x650")

country_data = [
        '', 'Afghanistan-AF', 'Aland Islands-AX', 'Albania-AL', 'Algeria-DZ', 'American Samoa-AS',
        'Andorra-AD', 'Angola-AO', 'Anguilla-AI', 'Antarctica-AQ', 'Antigua and Barbuda-AG', 
        'Argentina-AR', 'Armenia-AM', 'Aruba-AW', 'Australia-AU', 'Austria-AT', 'Azerbaijan-AZ',
        'Bahamas-BS', 'Bahrain-BH', 'Bangladesh-BD', 'Barbados-BB', 'Belarus-BY', 'Belgium-BE', 
        'Belize-BZ', 'Benin-BJ', 'Bermuda-BM', 'Bhutan-BT', 'Bolivia-BO', 'Bonaire-BQ', 
        'Bosnia and Herzegovina-BA', 'Botswana-BW', 'Bouvet Island-BV', 'Brazil-BR', 
        'British Indian Ocean Territory-IO', 'Brunei Darussalam-BN', 'Bulgaria-BG', 'Burkina Faso-BF', 
        'Burundi-BI', 'Cambodia-KH', 'Cameroon-CM', 'Canada-CA', 'Cape Verde-CV', 'Cayman Islands-KY', 
        'Central African Republic-CF', 'Chad-TD', 'Chile-CL', 'China-CN', 'Christmas Island-CX', 
        'Cocos (Keeling) Islands-CC', 'Colombia-CO', 'Comoros-KM', 'Congo-CG', 'Congo-CD', 'Cook Islands-CK', 
        'Costa Rica-CR', "Cote d'Ivoire-CI", 'Croatia-HR', 'Cuba-CU', 'CuraÃ§ao-CW', 'Cyprus-CY', 'Czechia-CZ', 
        'Denmark-DK', 'Djibouti-DJ', 'Dominica-DM', 'Dominican Republic-DO', 'Ecuador-EC', 'Egypt-EG', 'El Salvador-SV',
        'Equatorial Guinea-GQ', 'Eritrea-ER', 'Estonia-EE', 'Ethiopia-ET', 'Falkland Islands (Malvinas)-FK', 'Faroe Islands-FO',
        'Fiji-FJ', 'Finland-FI', 'France-FR', 'French Guiana-GF', 'French Polynesia-PF', 'French Southern Territories-TF',
        'Gabon-GA', 'Gambia-GM', 'Georgia-GE', 'Germany-DE', 'Ghana-GH', 'Gibraltar-GI', 'Greece-GR', 'Greenland-GL', 'Grenada-GD', 
        'Guadeloupe-GP', 'Guam-GU', 'Guatemala-GT', 'Guernsey-GG', 'Guinea-GN', 'Guinea-Bissau-GW', 'Guyana-GY', 'Haiti-HT', 
        'Heard and Mc Donald Islands-HM', 'Holy See (Vatican City State)-VA', 'Honduras-HN', 'Hong Kong-HK', 'Hungary-HU', 
        'Iceland-IS', 'India-IN', 'Indonesia-ID', 'Iran-IR', 'Iraq-IQ', 'Ireland-IE', 'Isle of Man-IM', 'Israel-IL', 
        'Italy-IT', 'Jamaica-JM', 'Japan-JP', 'Jersey-JE', 'Jordan-JO', 'Kazakstan-KZ', 'Kenya-KE', 'Kiribati-KI', 
        'Korea-KP', 'Korea-KR', 'Kosovo (temporary code)-XK', 'Kuwait-KW', 'Kyrgyzstan-KG', 'Lao-LA', 'Latvia-LV', 
        'Lebanon-LB', 'Lesotho-LS', 'Liberia-LR', 'Libyan Arab Jamahiriya-LY', 'Liechtenstein-LI', 'Lithuania-LT', 
        'Luxembourg-LU', 'Macao-MO', 'Macedonia-MK', 'Madagascar-MG', 'Malawi-MW', 'Malaysia-MY', 'Maldives-MV', 
        'Mali-ML', 'Malta-MT', 'Marshall Islands-MH', 'Martinique-MQ', 'Mauritania-MR', 'Mauritius-MU', 'Mayotte-YT', 
        'Mexico-MX', 'Micronesia-FM', 'Moldova-MD', 'Monaco-MC', 'Mongolia-MN', 'Montenegro-ME', 'Montserrat-MS', 
        'Morocco-MA', 'Mozambique-MZ', 'Myanmar-MM', 'Namibia-nan', 'Nauru-NR', 'Nepal-NP', 'Netherlands-NL', 
        'Netherlands Antilles-AN', 'New Caledonia-NC', 'New Zealand-NZ', 'Nicaragua-NI', 'Niger-NE', 'Nigeria-NG', 
        'Niue-NU', 'Norfolk Island-NF', 'Northern Mariana Islands-MP', 'Norway-NO', 'Oman-OM', 'Pakistan-PK', 
        'Palau-PW', 'Palestinian Territory-PS', 'Panama-PA', 'Papua New Guinea-PG', 'Paraguay-PY', 'Peru-PE', 
        'Philippines-PH', 'Pitcairn-PN', 'Poland-PL', 'Portugal-PT', 'Puerto Rico-PR', 'Qatar-QA', 'Republic of Serbia-RS', 
        'Reunion-RE', 'Romania-RO', 'Russia Federation-RU', 'Rwanda-RW', 'Saint BarthÃ©lemy-BL', 'Saint Helena-SH', 
        'Saint Kitts & Nevis-KN', 'Saint Lucia-LC', 'Saint Martin-MF', 'Saint Pierre and Miquelon-PM', 'Saint Vincent and the Grenadines-VC',
        'Samoa-WS', 'San Marino-SM', 'Sao Tome and Principe-ST', 'Saudi Arabia-SA', 'Senegal-SN', 'Serbia and Montenegro-CS', 
        'Seychelles-SC', 'Sierra Leone-SL', 'Singapore-SG', 'Sint Maarten-SX', 'Slovakia-SK', 'Slovenia-SI', 'Solomon Islands-SB', 
        'Somalia-SO', 'South Africa-ZA', 'South Georgia & The South Sandwich Islands-GS', 'South Sudan-SS', 'Spain-ES', 'Sri Lanka-LK', 
        'Sudan-SD', 'Suriname-SR', 'Svalbard and Jan Mayen-SJ', 'Swaziland-SZ', 'Sweden-SE', 'Switzerland-CH', 'Syrian Arab Republic-SY', 
        'Taiwan-TW', 'Tajikistan-TJ', 'Tanzania-TZ', 'Thailand-TH', 'Timor-Leste-TL', 'Togo-TG', 'Tokelau-TK', 'Tonga-TO', 
        'Trinidad and Tobago-TT', 'Tunisia-TN', 'Turkey-TR', 'Turkish Rep N Cyprus (temporary code)-XT', 'Turkmenistan-TM', 
        'Turks and Caicos Islands-TC', 'Tuvalu-TV', 'Uganda-UG', 'Ukraine-UA', 'United Arab Emirates-AE', 'United Kingdom-GB', 
        'United States-US', 'United States Minor Outlying Islands-UM', 'Uruguay-UY', 'Uzbekistan-UZ', 'Vanuatu-VU', 'Venezuela-VE', 
        'Vietnam-VN', 'Virgin Islands-VG', 'Virgin Islands-VI', 'Wallis and Futuna-WF', 'Western Sahara-EH', 'Yemen-YE', 
        'Zambia-ZM', 'Zimbabwe-ZW'
    ]

title = Label(root,text="AIR QUALITY INDEX",anchor=CENTER,font=("Rockwell",20,"bold","italic"),fg="white",bg='skyblue',bd=25,relief=RIDGE,)
title.pack(side=TOP,fill=X)

instruction = Label(root,text="1: Select Option(zipcode-country/lon-lat/city-country)    2: Fill Following Information   3: Click On Submit Button",font=("Rockwell",13,"bold","italic"),fg="red",pady=10)
instruction.pack()

m = StringVar()
m.set('lonLan')
country_value = ''

#--------------------------MAIN FRAME--------------------------#

mainFrame = LabelFrame(root,bd=20,relief=RIDGE)
mainFrame.place(x=0,y=130,width=1024,height=500)


#----------------------------RIGHT FRAME--------------------------------------------#
rightFrame = LabelFrame(mainFrame,text="Air Quality Info",bd=5,relief=RIDGE,padx=10,font=("Rockwell",12,"bold","italic"))
rightFrame.place(x=480,y=5,width=500,height=450)

#------------------------------------x---------------------------------#
#EXCECUTE FUNCTION
def execute():

    global api_request
    global country_display, lat, lon, city_display
    display_clear()
    option_get = m.get()    
    if option_get == 'zipcode':
        try:

            if zipcode_entry.get().isdigit() and len(country_value) !=0 :
                zip= zipcode_entry.get()
                country_code = country_value.split('-')[1]
                country_display = country_value.split('-')[0]
                api_request = requests.get("http://api.openweathermap.org/geo/1.0/zip?zip={0},{1}&appid={2}".format(zip, country_code, api_key))
                api_data = json.loads(api_request.content)
                lat = api_data['lat']
                lon = api_data['lon']
                city_display = api_data['name']
                display(lat, lon) 
            else:
                error = messagebox.showerror(title="Error", message="Please check zipcode or country!")
        except Exception as e:
            error = messagebox.showerror(title="Error", message=e)       
        
    elif option_get == 'lonLan':
            
        try:
            lon = long_entry.get()
            lat = lat_entry.get()
            if len(lon) !=0 or len(lat) !=0:
                lon = float(lon)
                lat = float(lat)

                if isinstance(lon,float) and isinstance(lat,float):
                    print(lon,lat)
                    api_request = requests.get("http://api.openweathermap.org/geo/1.0/reverse?lat={0}&lon={1}&limit={2}&appid={3}".format(lat, lon, 1, api_key))
                    api_data = json.loads(api_request.content)
                    city_display = api_data[0]['name']
                    country_code = api_data[0]['country']
                    for i in country_data:
                        if country_code in i:
                            country_display = str(i).split('-')[0]            
                    display(lat, lon)
            else:
                error = messagebox.showerror(title="Error", message="Please check Lat and Lan again!")
        except Exception as e:
            error = messagebox.showerror(title="Error", message="Please check Lat and Lan again!")  
        
    elif option_get == 'city':
        try:
            state = ''
            if len(city_entry.get()) !=0 and len(country_value) !=0:
                city_display = city_entry.get()
                country_code = country_value.split('-')[1]
                country_display = country_value.split('-')[0]
                api_request = requests.get("http://api.openweathermap.org/geo/1.0/direct?q={0},{1},{2}&limit={3}&appid={4}".format(city_display, state, country_code, 1, api_key)) 
                api_data = json.loads(api_request.content)
                lat = api_data[0]['lat']
                lon = api_data[0]['lon']
                display(lat, lon)
            else:
                error = messagebox.showerror(title="Error", message="Please check city or country!")
        except Exception as e:
            error = messagebox.showerror(title="Error", message=e)

#---------------------------------------------------X-----------------------------------------------------------------------------#
#Display Function
def display(lat, lon):

    try:
        AIR_API = requests.get("http://api.openweathermap.org/data/2.5/air_pollution?lat={0}&lon={1}&appid={2}".format(lat, lon, api_key))
        #print(AIR_API)
        api = json.loads(AIR_API.content)
        
        quality = api['list'][0]['main']['aqi']
        print("Quality:", quality)
        '''       '''               
        if quality == 1:
            category = "Good"
        elif quality == 2:
            category = "Fair"
        elif quality == 3:
            category = "Unhealthy for Sensitive Groups"
        elif quality == 4:
            category = "Unhealthy"
        elif quality == 5:
            category = "Hazardous"
                    
        
        if category == "Good":
            color = "#00E400"
        elif category == "Fair":
            color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            color = "#ff7e00"
        elif category == "Unhealthy":
            color = "#ff0000"
        elif category == "Hazardous":
            color = "#7e0023"

        city_name_label = Label(rightFrame,text="City",font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        city_name_label.grid(row=0,column=0,sticky=W)
        city_name = Label(rightFrame,text=city_display,font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        city_name.grid(row=0,column=1)

        air_quality_label = Label(rightFrame,text="Air Quality",font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        air_quality_label.grid(row=1,column=0,sticky=W)
        air_quality = Label(rightFrame,text=quality,font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        air_quality.grid(row=1,column=1)
    
        category_label = Label(rightFrame,text="Category",font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        category_label.grid(row=2,column=0,sticky=W)
        category_air = Label(rightFrame,text=category,font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        category_air.grid(row=2,column=1)

        country_name_label = Label(rightFrame,text="Country",font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        country_name_label.grid(row=3,column=0,sticky=W)
        country_name = Label(rightFrame,text=country_display,font=("Rockwell",15,"bold"),padx=2,pady=13,background=color)
        country_name.grid(row=3,column=1)
        rightFrame.configure(background=color)    
    except Exception as e:
        api = error = messagebox.showerror("Error","Please Enter Valid Zipcode or Co-ordinates or City and Country.. ")           

        

#----------------------------------x-------------------------------------#
#Clear Display
def display_clear():
       
    for w in rightFrame.winfo_children():
        w.destroy()

#-----------------------------------x-----------------------------------------#
#Get ComboBox Value (country_entry)
def onChange(event):
    global country_value
    country_value = None
    try:
        country_value = country_entry.get()
        if len(country_value) == 0 or country_value == '':
            error = messagebox.showerror("Error","Please Enter Valid Data..")
    except Exception as e:
        error = messagebox.showerror(title="Error", message="Please select the country!")

#-------------------------------------------x----------------------------#
#Clear All Fields
def clear_field():
    
    display_clear()
    zipcode_entry.delete(0,END)
    long_entry.delete(0,END)
    lat_entry.delete(0,END)
    city_entry.delete(0,END)
    country_entry.current(0)
    rightFrame.configure(background="SystemButtonFace")

#----------------------x----------------------------------------------------#
#----------------------------LEFT FRAME---------------------------------------#
leftFrame = LabelFrame(mainFrame,text="Fill Info",bd=5,relief=RIDGE,padx=10,font=("Rockwell",12,"bold","italic"))
leftFrame.place(x=0,y=5,width=470,height=450)

#----------------------------------------x------------------------------------#
#Check Option
def Check(val):
    rightFrame.configure(background="SystemButtonFace")
    #my_label.destroy()
    clear_field()
    if val == 'zipcode':
        zipcode_entry.configure(state=NORMAL)
        country_entry['state'] = 'readonly'
    else:
        zipcode_entry.delete(0,END)
        zipcode_entry.configure(state=DISABLED)
        country_entry['state'] = DISABLED

    if val == 'lonLan':
        long_entry.configure(state=NORMAL)
        lat_entry.configure(state=NORMAL)
    else:
        long_entry.delete(0,END)
        lat_entry.delete(0,END)
        long_entry.configure(state=DISABLED)
        lat_entry.configure(state=DISABLED)
    
    if val == 'city':
        city_entry.configure(state=NORMAL)
        country_entry['state'] = 'readonly'
    else:
        city_entry.delete(0,END)
        country_entry.delete(0,END)
        city_entry.configure(state=DISABLED)
        #country_entry['state'] = DISABLED
    
#------------------------------------------x-----------------------------------------#
#Create Options For Input
option1 = Radiobutton(leftFrame,text="Zipcode and Country",variable=m,value="zipcode",font=("Rockwell",12,"bold"),padx=2,pady=6,command=lambda: Check(m.get()))
option1.grid(row=0,column=0,sticky=W)

option2 = Radiobutton(leftFrame,text="Longitude and Latitude",variable=m,value="lonLan",font=("Rockwell",12,"bold"),padx=2,pady=6,command=lambda: Check(m.get()))
option2.grid(row=1,column=0,sticky=W)

option3 = Radiobutton(leftFrame,text="City and Country",variable=m,value="city",font=("Rockwell",12,"bold"),padx=2,pady=6,command=lambda: Check(m.get()))
option3.grid(row=2,column=0,sticky=W)

#----------------------------------------------x-------------------------------------#
#Create Labels and Entry Boxes
#For Zipcode
zipcode_label = Label(leftFrame, text="Enter Zipcode",font=("Rockwell",12,"bold"),padx=2,pady=10)
zipcode_label.grid(row=3,column=0,sticky=W)
zipcode_entry = Entry(leftFrame,width=20,font=("Rockwell",12,"bold"),state=DISABLED)
zipcode_entry.grid(row=3,column=1)
#------------------x---------------------------------------------#
#For City And Country
city_label = Label(leftFrame, text="Enter City",font=("Rockwell",12,"bold"),padx=2,pady=10)
city_label.grid(row=4,column=0,sticky=W)
city_entry = Entry(leftFrame,width=20,font=("Rockwell",12,"bold"),state=DISABLED)
city_entry.grid(row=4,column=1)

country_label = Label(leftFrame, text="Enter Country",font=("Rockwell",12,"bold"),padx=2,pady=10)
country_label.grid(row=5,column=0,sticky=W)

text_font = ("Rockwell",12,"bold")
country_entry = ttk.Combobox(leftFrame,value=country_data, width=18,state=DISABLED,font=text_font)
country_entry.current(0)
country_entry.bind("<<ComboboxSelected>>",onChange)
country_entry.grid(row=5,column=1)

#----------------------------x-----------------------------------#
# For Longitude and Latitude
lat_label = Label(leftFrame, text="Enter Latitude",font=("Rockwell",12,"bold"),padx=2,pady=10)
lat_label.grid(row=6,column=0,sticky=W)
lat_entry = Entry(leftFrame,width=20,font=("Rockwell",12,"bold"))
lat_entry.grid(row=6,column=1)

long_label = Label(leftFrame, text="Enter Longitude",font=("Rockwell",12,"bold"),padx=2,pady=10)
long_label.grid(row=7,column=0,sticky=W)
long_entry = Entry(leftFrame,width=20,font=("Rockwell",12,"bold"))
long_entry.grid(row=7,column=1)
#----------------------------------------------x---------------------------------#

#Create Buttons
submit_btn = Button(leftFrame,text="Submit",font=("Rockwell",12,"bold"),padx=50,pady=10,command=execute)
submit_btn.grid(row=8,column=0,sticky=W)

clear_field_btn = Button(leftFrame,text="Clear Fields",font=("Rockwell",12,"bold"),padx=50,pady=10,command=clear_field)
clear_field_btn.grid(row=8,column=1,sticky=W)
#-----------------------------------------------------x------------------------------#
root.mainloop()

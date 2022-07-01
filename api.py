from __future__ import division
import flask, time
from flask import request, jsonify

######
##### NEW PANCHANGA CODE FROM SCRATCH

# importing pandas as pd
import pandas as pd

# From Panchanga.py

from math import ceil
from collections import namedtuple as struct
import swisseph as swe
from datetime import datetime
import math

from flask import Flask, jsonify, request
#from pancha2 import *
from datetime import datetime, timedelta
import sys
import numpy
import numpy as np
import pytz
import json
from flask_cors import CORS
import pandas as pd

app = flask.Flask(__name__)
#app.config["DEBUG"] = True


star_list = ["Ashwini","Bharani","Krittika","Rohini","Mrigashirsha","Ardra","Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta","Chitra","Svati","Visakha","Anuradha","Jyeshtha","Mula","Purva ashadha","Uttara ashada","Sravana","Dhanistha","Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"]
rashi_list = ["Mesha - Aries", "Vrishabha - Taurus", "Mithuna - Gemini", "Karkataka - Cancer", "Simha - Leo", "Kanya - Virgo", "Tula - Libra", "Vrishchika - Scorpio", "Dhanus - Sagittarius", "Makara - Capricorn", "Kumbha - Aquarius", "Meena - Pisces"]
planetary_list = ["Surya", "Chandra", "Kuja", "Mangala", "Budha", "Guru", "Sukra", "Sani", "Rahu", "Ketu", "Uranus", "Neptune"]
star_list = ["Ashwini","Bharani","Krittika","Rohini","Mrigashirsha","Ardra","Punarvasu","Pushya","Ashlesha","Magha","Purva Phalguni","Uttara Phalguni","Hasta","Chitra","Svati","Visakha","Anuradha","Jyeshtha","Mula","Purva ashadha","Uttara ashada","Sravana","Dhanistha","Shatabhisha","Purva Bhadrapada","Uttara Bhadrapada","Revati"]
tithi_list = ["Padyami","Vidiya","Thadiya","Chaturthi","Panchami","Shashthi","Saptami","Ashtami","Navami","Dasami","Ekadasi","Dvadasi","Trayodasi","Chaturdashi","Amavasya","Padyami","Vidiya","Thadiya","Chaturthi","Panchami","Shashthi","Saptami","Ashtami","Navami","Dasami","Ekadasi","Dvadasi","Trayodasi","Chaturdashi","Pournami"]
panchaka = ["0-Good","1-Mrityu Panchaka(Donate Gems)","2-Agni Panchaka(Donate Sandal Paste)", "3-Good","4-Raja Panchaka(Donate Lemon)","5-Good","6-Chora Panchaka(Donate Lamp)","7-Good","8-Roga Pachaka(Donate Food Grains)"]
masa_list = ["Chaitra","Vaisakha","Jyeshta","Ashada","Shravana","Bhadrapada","Aswayuja","Kartika","Margasira","Pushya","Magha","Phalguna"]
vaara_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
yoga_list = ["Vishkumbha","Priti","Ayushman","Saubhagya","Shobhana","Atiganda","Sukarma","Dhriti","Shoola","Ganda","Vriddhi","Dhruva","Vyaghata","Harshana","Vajra","Siddhi","Vyatipata","Variyana","Parigha","Shiva","Siddha","Sadhya","Shubha","Shukla","Brahma","Indra","Vaidhriti"]
karna_list = ["Kintughna","Bava","Baalava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Gara","Taitila","Kaulava","Vanija","Vishti",\
"Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Bava","Balava","Kaulava","Taitila","Gara","Vanija","Vishti","Shakuni","Chatushpada","Naga"]
ritu_list = ["Vasant - Spring","Grishma - Summer","Varsha - Monsoon","Sharad - Autumn","Hemant - Pre-winter","Shishir - Winter"]
rashi_list = ["Mesha - Aries", "Vrishabha - Taurus", "Mithuna - Gemini", "Karkataka - Cancer", "Simha - Leo", "Kanya - Virgo", "Tula - Libra", "Vrishchika - Scorpio", "Dhanus - Sagittarius", "Makara - Capricorn", "Kumbha - Aquarius", "Meena "]
star_start_time = [16.8,19.2,21.6,20.8,15.2,14,21.6,17.6,22.4,21.6,17.6,16.8,18,17.6,15.2,15.2,13.6,15.2,17.6,19.2,17.6,13.6,13.6,16.8,16,19.2,21.6]
varjam_start_time = [20,9.6,12,16,5.6,8.4,12,8,12.8,12,8,12.8,12,8,7.2,8.4,8,5.6,5.6,4,5.6,[8,22.4],9.6,8,4,4,7.2,6.4,9.6,12]
hora_list = ["Sun","Venus","Mercury","Moon","Saturn","Jupiter","Mars"]
vaara_lord = ["Sun","Moon","Mars","Mercury","Jupiter","Venus","Saturn"]
day_muhurtha = ["Rudra","Ahi","Mitra","Pitra","Vasu","Udaka","Vishwedeva","Vidhatri","Brhama","Indra","Indragini","Niriti","Toyapa","Aryama","Bhaga"]
night_muhurtha = ["Isha","Ajapada","Ahirbudhanya","Pusha","Ashwani","Yama","Vahni","Dhatri","Chandra","Aditi","Ijya(Tijya)","Vishnu","Arka","Twashtri","Vaayu"]

# Variables for Rahu, Yama, Gulika and durmuhurtha calculations
rahu_kala_cal = [0.875,0.125,0.75,0.5,0.625,0.375,0.25]
yama_kala_cal = [0.5,0.375,0.25,0.125,1,0.75,0.625]
gulika_kala_cal = [0.75,0.625,0.5,0.375,0.25,0.125,1]
durmu_cal = [0.14,[6.4,8.8],[2.4,4.8],5.6,[4,8.8],[2.4,6.4],1.6]

panchanga = [{   "panchanga": {
    "vaara": {      "current": "current",      "upcoming": "upcmng"    },
    "maasa": {      "amanta": "amantha",      "puriamanta": "puamanta"    },
    "samvat": {      "current": "year",      "Saka": "sakayr",      "Samvat": "samvatyr"    },
    "nakshatra:": {      "Current": "star&pada",      "at_sunrise": "staratsunrise&pada",      "upcoming": "nextstarpada",      "Yogi": "ystar",      "Avayogi": "avstar"    },
    "tithi": {      "paksha": "tithipaksha",     "current": "currentpaksha",      "at_sunrise": "pakshatsunrise",      "next": "nexttithi"    },
    "karana": {      "current": "karana",      "at_sunrise": "karana",      "next": "karananext"    },
    "yoga": {      "current": "yogacurrent",      "at_sunrise": "yogasunrise",      "next": "yoganext"    },
    "Sun": {      "Sunrise": "rise",      "sunset": "set",      "sunrise_tomorrow": "tomorow",      "Sun_Rashi": "rashi"    },
    "Moon": {      "MoonRise": "rise",      "MoonSet": "set",      "Moon_Rashi": "rashi"    },
    "Rashi": {      "Lagna": "rashi",      "Daghdha": "rashis",      "Ghatak": "rashis"    },
    "Muhurtha": {      "Brahma": "brahma",      "Abhijjit": "muhurtha",      "Rahu_Kaal": "kaal",      "Gulika_Kaal": "kaal",      "Yama_Ganda": "ganda",      "Divisions": "divisions"    },
    "Chogadhiya": {      "Day_Chogadhiya": "daygc",      "Night_Chogadhiya": "nightgc"    },
    "Hora": {      "Current": "CurrentHora",      "Upcoming": "NextHora"    },
    "Pakshi": {      "Current_Pakshi": "pakshicurr",      "Upcoming_Pakshi": "upcoming"    },
    "Duration": {      "Duration_day": "dayDuration",      "Duration_night": "nightduration"    },
    "Ayana": "ayana",  "Ritu": "Ritu",  "positions": "positions"},
  }]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Astrology API</h1><p>This site is a prototype API for Panchanga.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/panchanga', methods=['GET'])
def api_all():
    date = request.args.get('date')
    loc_lat = request.args.get('lat')
    loc_lng = request.args.get('lng')
    time=request.args.get('time')
    tz=request.args.get('tz')
    val = pancha(date, loc_lat, loc_lng, time, tz)
#    print(val)


    if date==None or loc_lat == None or loc_lng == None or tz == None:
        return "Provide Proper Details"
    else :
        return jsonify(val)


@app.route('/api/v1/panchapakshi', methods=['GET'])
def pakshi():
    date = request.args.get('date')
    loc_lat = request.args.get('lat')
    loc_lng = request.args.get('lng')
    time=request.args.get('time')
    tz=request.args.get('tz')
    val = pancha(date, loc_lat, loc_lng, time, tz)
#    print(val)


#    if date==null or loc_lat == null or loc_lng == null or time == null:
#        return "Provide Proper Details"
#    else :
    return jsonify(val)


def pancha(date, loc_lat, loc_lng, time, tz):
    print(date)
    print(type(date))
#    date = datetime.strptime(str(date), '%Y-%m-%d')
#    print(date)
#    print(type(date))
#    jd2 = date.to_julian_date()
#    print(jd2)
#    ts = pd.Timestamp(year = 2021,  month = 10, day = 17, hour = 20, minute = 57, second = 49, tz = 'Asia/Kolkata')
    td = pd.Timestamp.now()
    print(td)
# Print the Timestamp object
#    print(ts)
#    print(ts.to_julian_date())
#    print(td)
    print(td.to_julian_date())
#    jd = td.to_julian_date()
#    date = pd.Timestamp.now() #'2021-10-19 11:54:00'
#    now = datetime.now()

#    date = '2021-11-2  13:30:00'
#    date = now.strftime("%Y-%m-%d %H:%M:%S")
#    print(date)

    #date = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')

    try:
        date = datetime.strptime(date,'%Y-%m-%d')
    #        print(date)
    #        date = date.datet()
    #        print(date)
    except IndexError:
        date = datetime.now()

    #    tb = time.split('.')
    #    hr = int(tb[0])
    #    mn = int(tb[1])
    d_1 = date - timedelta(days=1)
    d1 = date + timedelta(days=1)
    #print("****d1****")
    #print(d1)

    # Julian Day number as on (year, month, day) at 00:00 UTC
    gregorian_to_jd_detail = lambda date: swe.julday(date.year, date.month, date.day, date.hour)
    gregorian_to_jd = lambda date: swe.julday(date.year, date.month, date.day, 0.0)
    jd_to_gregorian = lambda jd: swe.revjul(jd, swe.GREG_CAL)

    date_detail = gregorian_to_jd_detail(datetime(date.year, date.month, date.day, date.hour, date.minute))

    date = gregorian_to_jd(datetime(date.year, date.month, date.day))
    #print(date)
    d1 =  gregorian_to_jd(datetime(d1.year, d1.month, d1.day))
   # print(d1)
    d_1 =  gregorian_to_jd(datetime(d_1.year, d_1.month, d_1.day))
    #print(d_1)
#    date = td.to_julian_date()
#    print("Julian date")
#    print(date)
#    print(date)
        #date = gregorian_to_jd(Date(2019, 4, 11))

    ##data = {
    #    'Given Location':loc,
    #    'Given Date':date
    #}
        #print loc
        #print date

    #with open("newcities.json") as fp:
    #    cities = json.load(fp)
    #    #only_cities = cities.keys()
    #    if loc not in cities:
    #        return jsonify({'Error':'City Not found'})
    lat = float(loc_lat)
    lon = float(loc_lng)
#    print(lat)
#    print(lon)

    #lat = float(cities[loc]["latitude"])
    #lon = float(cities[loc]["longitude"])
    #tz = cities[loc]["timezone"]
#    lat = 17.38405
#    lon = 78.45636
#    tz = 'Asia/Kolkata'

    #print(tz)
    #timez = pytz.timezone(tz)

    #dt = datetime.utcnow()
    #offset_seconds = timez.utcoffset(dt).seconds
    #offset_hours = offset_seconds / 3600.0
    #tz = "{:+d}:{:02d}".format(int(offset_hours), int((offset_hours % 1) * 60))
    #tz = int(tz)
    def delta_to_dec(timedel):
        hours, remainder = divmod(timedel.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        m = int(minutes) * 1/60
        s = int(seconds) * 1/3600
        h = int(hours)
        dura = h + m + s
        return dura, hours, minutes, seconds

    def get_night_duration(MR, MS):
        MRT = timedelta(hours=MR1[0],minutes=MR1[1],seconds=MR1[2])
        MST = timedelta(hours=MS1[0],minutes=MS1[1],seconds=MS1[2])

        night_diff = MST-MRT
        night_dura, hours, minutes, seconds = delta_to_dec(night_diff)

        night_dura_formated = "{0}:{1}:{2}".format(hours,minutes,seconds)
        #night_dura = timedelta(hours=hours,minutes=minutes,seconds=seconds)
        return night_dura, night_dura_formated


    dt = datetime.now()
    #print (dt)
    tz_now = pytz.timezone(tz)
    print(tz_now)
    tz = tz_now.utcoffset(dt).total_seconds()/60/60
    print(tz)
    location = Place(lat, lon, tz)
#    print(location)
    Vaara = vaara(date)
    Masa = masa(date, location)
#    Samvat
###### Nakshatra - Details
    Pr_Nakshatra = nakshatra(d_1,location)
    Su_Nakshatra = nakshatra(date,location)
    Ne_Nakshatra = nakshatra(d1,location)
    Cu_Nakshatra = nakshatra(date,location)
#    Yogi_Nakshatra = nakshatra(date_detail,location)
#    AvaYogi_Nakshatra = nakshatra(date_detail,location)

#### Tithi Details
#   paksha
#   Tithi
    Curr_Tithi = tithi(date_detail, location)
    Next_Tithi = tithi(date_detail, location)
    sunrise_Tithi = tithi(date_detail, location)

    Curr_Karna = karana(date_detail, location)
    Next_Karna = karana(date_detail, location)
    Sunrise_Karna = karana(date_detail, location)
    MR = moonrise(date, location)
    MR1 = moonrise(date, location)
    MR = "{0}:{1}:{2}".format(MR[0],MR[1],MR[2])
    MS = moonset(date, location)
    MS1 = moonset(date, location)
    MS = "{0}:{1}:{2}".format(MS[0],MS[1],MS[2])

    SRA = sunrise(date, location)[1]
    SRAN = sunrise(d1, location)[1]
    print(SRA)
    #SR1 = sunrise(date, location)[0]
    #SRO = timedelta(hours=SRA[0],minutes=SRA[1],seconds=SRA[2])
    SR = "{0}:{1}:{2}".format(SRA[0],SRA[1],SRA[2])
    SRN = "{0}:{1}:{2}".format(SRAN[0],SRAN[1],SRAN[2])

    SSA = sunset(date, location)[1]
    #SS1 = sunset(date, location)[0]
    SS = "{0}:{1}:{2}".format(SSA[0],SSA[1],SSA[2])
    
    Karna = karana(date_detail, location)
    Tithi = tithi(date_detail, location)
#    Nakshatra = nakshatra(date_detail,location)
    Pada = nakshatra_pada(lon)
    Yoga = yoga(date,location)
    Paksha = pakshaname(date)
    Ritu = ritu(Masa[0])

    ##########################################
    Lagna = ascendant(date,location)
    Sun = sun_position(date,location)
    Moon = moon_position(date,location)
    Hora = hora(date, location)
    
    ## print(dt)
    #Rashi = raasi(date)
    planet_pos = planetary_positions(date,location)
#    lunar_phase = lunar_phase(date)
    GC = gauri_chogadiya(date, location)
    Muhurthas = muhurthas(date,location)
#    AM = abhijit_muhurta(date,location)

    #Day Duration for Rahu, Yamganda kalas
    day_dura = day_duration(date, location)
    day_dura_formated = "{0}:{1}:{2}".format(day_dura[1][0],day_dura[1][1],day_dura[1][2])
    if Karna is not None:
        karna = karna_list[Karna[0]-1]
    else:
        karna = ''
    if Vaara is not None:
        day_name = vaara_list[Vaara]
    else:
        day_name = ''

    #Tithi Conversion
    Tithi1 = tithi_list[Tithi[0]-1]
    tithiVal = tithi_list.index(Tithi1)
    # print(tithiVal)
    # print(Tithi1)
    Tithi1_time = timedelta(hours=Tithi[1][0],minutes=Tithi[1][1], seconds=Tithi[1][2])
    Tithi1_time = str(Tithi1_time)
    if '1 day' in Tithi1_time:
        Tithi1_time = Tithi1_time.replace('1 day', 'Next day')
    Thithi = "{0} till {1}".format(Tithi1, Tithi1_time)

    if len(Tithi)>2:
        Tithi2 = tithi_list[Tithi[2]-1]
        tithiVal = tithi_list.index(Tithi2)
        # print(tithiVal)
        # print(Tithi2 )
        Tithi2_time = Tithi[3]
        Tithi2_time = timedelta(hours=Tithi[3][0],minutes=Tithi[3][1], seconds=Tithi[3][2])
        Tithi2_time = str(Tithi2_time)
        if '1 day' in str(Tithi2_time):
            Tithi2_time = Tithi2_time.replace('1 day', 'Next day')
            Thithi = "{0} till {1}, Tithi {2} till {3}".format(Tithi1, Tithi1_time, Tithi2, Tithi2_time)

        # Rashi Calculation
    #    if Rashi:
    #        rashival = rashi_list.index[Rashi]
    #        # print(rashival)
    #        # print(Rashi)

        #Nakshatra Calcuation
#    if Nakshatra:
#        star = star_list[Nakshatra[0]-1]
#        NaksVal = star_list.index(star)
#        # print(NaksVal)
#        # print(star )
#        star_time1 = timedelta(hours=Nakshatra[1][0],minutes=Nakshatra[1][1], seconds=Nakshatra[1][2])
#        star_time = str(star_time1)

#    if '1 day' in star_time:
#        star_time = star_time.replace('1 day', 'Next day')
#    ## print("Nakshatra :{0} , Till {1}".format(star,star_time))
#    Nakshatram = "{0} , Till {1}".format(star,star_time)

    if Cu_Nakshatra:
        star = star_list[Cu_Nakshatra[0]-1]
        NaksVal = star_list.index(star)
#        print(NaksVal)
#        print(star )
#        print(Cu_Nakshatra[0])
#        print(Cu_Nakshatra[1])
        star_time1 = timedelta(hours=Cu_Nakshatra[1][0],minutes=Cu_Nakshatra[1][1], seconds=Cu_Nakshatra[1][2])
#        print("star time")
#        print(star_time1)
        star_time = str(star_time1)
#        print(date)
        ddate = jd_to_gregorian(date)
#        yrs = str(ddate[0])
#        mnths = str(ddate[1])
#        dys = str(ddate[2])
        ddaat = str(ddate[0])+"-"+str(ddate[1])+"-"+str(ddate[2])
        date_str =  datetime.strptime(ddaat, '%Y-%m-%d')
#        print (date_str)
#        print(star_time1)
#        print(type(date_str))
#        print(type(star_time1))
        new_time = date_str + star_time1
#        valhours = star_time1.hours
#        print(valhours)
#        print(new_time)
        val = new_time.strftime("%m/%d/%Y %H:%M:%S")
#        print(val)
        dtobj = datetime.strptime(val, '%m/%d/%Y %H:%M:%S')
#        dtobj = datetime.fromisoformat(val)
#        print(dtobj)
        val_detail = gregorian_to_jd_detail(datetime(dtobj.year, dtobj.month, dtobj.day, dtobj.hour, dtobj.minute, dtobj.second))       
        print(val_detail)

    if '1 day' in star_time: 
        star_time = star_time.replace('1 day', 'Next day')
    ## print("Nakshatra :{0} , Till {1}".format(star,star_time))
#    Cu_Nakshatram = "{0} , Till {1}, {2}".format(star,star_time,val_detail)
#    Cu_Nakshatram = "{0} : {1}".format(star,val_detail)
    Cu_Nakshatram = "{0} , till {1}".format(star,star_time)
#    print(Cu_Nakshatram)
#    print(type(Cu_Nakshatram))

    if Ne_Nakshatra:
        star = star_list[Ne_Nakshatra[0]-1]
        NaksVal = star_list.index(star)
        # print(NaksVal)
        # print(star )
        star_time1 = timedelta(hours=Ne_Nakshatra[1][0],minutes=Ne_Nakshatra[1][1], seconds=Ne_Nakshatra[1][2])
#        print("next star time")
#        print(star_time1)
        star_time = str(star_time1)

    if '1 day' in star_time:
        star_time = star_time.replace('1 day', 'Next day')
    ## print("Nakshatra :{0} , Till {1}".format(star,star_time))
    Ne_Nakshatram = "{0} , till {1}".format(star,star_time)

    if Pr_Nakshatra:
        star = star_list[Pr_Nakshatra[0]-1]
        NaksVal = star_list.index(star)
        # print(NaksVal)
        # print(star )
        star_time1 = timedelta(hours=Pr_Nakshatra[1][0],minutes=Pr_Nakshatra[1][1], seconds=Pr_Nakshatra[1][2])
 #       print("next star time")
 #       print(star_time1)
        star_time = str(star_time1)

    if '1 day' in star_time:
        star_time = star_time.replace('1 day', 'Next day')
    ## print("Nakshatra :{0} , Till {1}".format(star,star_time))
    Pr_Nakshatram = "{0} , Till {1}".format(star,star_time)

    if Su_Nakshatra:
        star = star_list[Su_Nakshatra[0]-1]
        NaksVal = star_list.index(star)
        # print(NaksVal)
        # print(star )
        star_time1 = timedelta(hours=Su_Nakshatra[1][0],minutes=Su_Nakshatra[1][1], seconds=Su_Nakshatra[1][2])
        star_time = str(star_time1)

    CuNaks = cal_current_naks(Cu_Nakshatram,Ne_Nakshatra)

    if '1 day' in star_time:
        star_time = star_time.replace('1 day', 'Next day')
    ## print("Nakshatra :{0} , Till {1}".format(star,star_time))
    Su_Nakshatram = "{0} , Till {1}".format(star,star_time)


    #Yogam
    #Add pros and cons of Yogas
    if Yoga:
        yogam = yoga_list[Yoga[0]-1]
        yogaVal = yoga_list.index(yogam)
        # print(yogaVal)
        # print(yogam)
        yoga_time = timedelta(hours=Yoga[1][0],minutes=Yoga[1][1], seconds=Yoga[1][2])
        yoga_time = str(yoga_time)
        if '1 day' in yoga_time:
            yoga_time = yoga_time.replace('1 day', 'Next day')
            Yoga = "{0} , Till {1}".format(yogam,yoga_time)


        #Masa Calcuation
    if Masa:
        masam = masa_list[Masa[0]-1]
        if Masa[1]:
            masam = "Adhika "+masam

    if Ritu is not None:
        Ritu = ritu_list[Ritu]

    def to_dt(decimal_time):
        m = int((decimal_time * 60) % 60)
        s = int((decimal_time * 3600) % 60)
        h = int(decimal_time)
        formated_time = "{0}:{1}:{2}".format(h,m,s)
        return (formated_time)

    def decimal_SR(SRA):
        m = int(SRA[1]) * 1/60
        s = int(SRA[2]) * 1/3600
        h = int(SRA[0])
        decimal_SR = h + m + s
        return decimal_SR

    def rahu_kalam(Vaara,day_dura,rahu_kala_cal,SRA):
        rahu_kal_start = decimal_SR(SRA)+day_dura[0]*rahu_kala_cal[Vaara]
        rahu_kal_end = rahu_kal_start+day_dura[0]*0.125

        rahu_kal_start = to_dt(rahu_kal_start)
        rahu_kal_end = to_dt(rahu_kal_end)

        return ("Start: {0} , End: {1}".format(rahu_kal_start, rahu_kal_end))

    def yamaganda_kalam(Vaara,day_dura,yama_kala_cal,SRA):
        yama_kal_start = decimal_SR(SRA)+day_dura[0]*yama_kala_cal[Vaara]
        yama_kal_end = yama_kal_start+day_dura[0]*0.125

        yama_kal_start = to_dt(yama_kal_start)
        yama_kal_end = to_dt(yama_kal_end)

        return ("Start: {0} , End: {1}".format(yama_kal_start, yama_kal_end))

    def gulika(Vaara,day_dura,gulika_kala_cal,SRA):
        gulika_kal_start = decimal_SR(SRA)+day_dura[0]*gulika_kala_cal[Vaara]
        gulika_kal_end = gulika_kal_start+day_dura[0]*0.125

        gulika_kal_start = to_dt(gulika_kal_start)
        gulika_kal_end = to_dt(gulika_kal_end)

        return ("Start: {0} , End: {1}".format(gulika_kal_start, gulika_kal_end))

    night_dura, night_dura_formated = get_night_duration(MR, MS)

    def durmuhurtham(Vaara,day_dura,SRA,SSA,durmu_cal,night_dura):
        if Vaara in [1,2,4,5]:
            if Vaara == 2:
                durmu1 = decimal_SR(SRA)+day_dura[0]*(durmu_cal[Vaara][0]/12)
                durmu2 = decimal_SR(SSA)+night_dura*(durmu_cal[Vaara][1]/12)
                return durmu1, durmu2, day_dura[0]*(0.8/12)
            else:
                durmu1 = decimal_SR(SRA)+day_dura[0]*(durmu_cal[Vaara][0]/12)
                durmu2 = decimal_SR(SRA)+day_dura[0]*(durmu_cal[Vaara][1]/12)
                return durmu1, durmu2, day_dura[0]*(0.8/12)
        elif Vaara in [0,3,6]:
                durmu1 = decimal_SR(SRA)+day_dura[0]*(durmu_cal[Vaara]/12)
                return durmu1, None, day_dura[0]*(0.8/12)

    rahu_kalam = rahu_kalam(Vaara,day_dura,rahu_kala_cal,SRA)
    yama_kalam = yamaganda_kalam(Vaara,day_dura,yama_kala_cal,SRA)
    gulika_kalam = gulika(Vaara,day_dura,gulika_kala_cal,SRA)
    durmu1, durmu2, day_durat = durmuhurtham(Vaara,day_dura,SRA,SSA,durmu_cal,night_dura)

    if durmu2==None:
        till = durmu1+day_durat
        durmu_today = "{0} till {1}".format(to_dt(durmu1), to_dt(till))
        #print (durmu_today)
    else:
        till1 = durmu1+day_durat
        till2 = durmu2+day_durat
        durmu_today = "{0} till {1}, and again from {2} till {3}".format(to_dt(durmu1), to_dt(till1), to_dt(durmu2), to_dt(till2))
        #print (durmu_today)

    def amrita_gadiyas(star_time1, Cu_Nakshatra, star_start_time):
        #amrita starts after x hours of starting time of nakshatra
        #stime of amrita/varj = start time of Nakshatra * x/24(duration of nakshatra)
        stime_of_star = delta_to_dec(star_time1)
        ## print(star_time)
        ## print(stime_of_star)
        #print (star_start_time[Nakshatra[0]-1])

            #duration of amrita/varj = duration of nakshatra * 1.6/24
        return True



    def varjam():
        return True

    amrita_gadiyas(star_time1, Cu_Nakshatra, star_start_time)

    data2 = {
            'MoonRise': MR,
            'MoonSet': MS,
            'SunRise': SR,
            'SunSet': SS,
            'SunRise_Next' : SRN,
            'Vaaram': day_name,
            'Karna': karna,
            'Tithi': Thithi,
            'Maasa': masam,
            'Ritu': Ritu,
#            'Hora':Hora,
            'Current_Nakshatra': Cu_Nakshatram,
#            'Next_Nakshatra': Ne_Nakshatram,
#            'Sunrise_Nakshatra': Su_Nakshatram,
#            'Pada' : Pada,
    #        'Rashi': Rashi,
    #        'Planets': planet_pos,
            'Day Duration': day_dura_formated,
            'Night Duration': night_dura_formated,
            'Rahu Kalam': rahu_kalam,
            'Yama Kalam': yama_kalam,
            'Gulika Kalam': gulika_kalam,
            'Durmuhurtam': durmu_today,
#            'Cu_Naks': CuNaks,
#            'Yoga':Yogaa,
#            'Lagna' : Lagna,
#            'Sun' : Sun,
#            'Moon': Moon,
#            'Abhijit' : AM,
            'Paksha' : Paksha
#            'Gouri' : GC,
#            'Day_Muhurthas': Muhurthas
    }
    print(data2)
    return (data2)

Date = struct('Date', ['year', 'month', 'day'])
Place = struct('Place', ['latitude', 'longitude', 'timezone'])

sidereal_year = 365.256360417   # From WolframAlpha


# Hindu sunrise/sunset is calculated w.r.t middle of the sun's disk
# They are geomretic, i.e. "true sunrise/set", so refraction is not considered
_rise_flags = swe.BIT_DISC_CENTER + swe.BIT_NO_REFRACTION

# namah suryaya chandraya mangalaya ... rahuve ketuve namah
swe.KETU = swe.PLUTO  # I've mapped Pluto to Ketu
planet_list = [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER,swe.VENUS, swe.SATURN, swe.MEAN_NODE, # Rahu = MEAN_NODE
               swe.KETU, swe.URANUS, swe.NEPTUNE ]

revati_359_50 = lambda: swe.set_sid_mode(swe.SIDM_USER, 1926892.343164331, 0)
galc_cent_mid_mula = lambda: swe.set_sid_mode(swe.SIDM_USER, 1922011.128853056, 0)

set_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_LAHIRI)
reset_ayanamsa_mode = lambda: swe.set_sid_mode(swe.SIDM_FAGAN_BRADLEY)

# Temporary function
def get_planet_name(planet):
  names = { swe.SURYA: 'Surya', swe.CHANDRA: 'Candra', swe.KUJA: 'Mangala',
            swe.BUDHA: 'Budha', swe.GURU: 'Guru', swe.SUKRA: 'Sukra',
            swe.SANI: 'Sani', swe.MEAN_NODE: 'Rahu', swe.KETU: 'Ketu', swe.PLUTO: 'Ketu'}
  return names[planet]

# Convert 23d 30' 30" to 23.508333 degrees
from_dms = lambda degs, mins, secs: degs + mins/60 + secs/3600

# the inverse
def to_dms_prec(deg):
  d = int(deg)
  mins = (deg - d) * 60
  m = int(mins)
  s = round((mins - m) * 60, 6)
  return [d, m, s]

def to_dms(deg):
  d, m, s = to_dms_prec(deg)
  return [d, m, int(s)]

def unwrap_angles(angles):
  """Add 360 to those elements in the input list so that
     all elements are sorted in ascending order."""
  result = angles
  for i in range(1, len(angles)):
    if result[i] < result[i-1]: result[i] += 360

  assert(result == sorted(result))
  return result

# Make angle lie between [-180, 180) instead of [0, 360)
norm180 = lambda angle: (angle - 360) if angle >= 180 else angle

# Make angle lie between [0, 360)
norm360 = lambda angle: angle[0] % 360

# Ketu is always 180° after Rahu, so same coordinates but different constellations
# i.e if Rahu is in Pisces, Ketu is in Virgo etc
ketu = lambda rahu: (rahu + 180) % 360

def function(point):
    swe.set_sid_mode(swe.SIDM_USER, point, 0.0)
    #swe.set_sid_mode(swe.SIDM_LAHIRI)
    # Place Revati at 359°50'
    #fval = norm180(swe.fixstar_ut("Revati", point, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0]) - ((359 + 49/60 + 59/3600) - 360)
    # Place Revati at 0°0'0"
    #fval = norm180(swe.fixstar_ut("Revati", point, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0])
    # Place Citra at 180°
    fval = swe.fixstar_ut("Citra", point, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0] - (180)
    # Place Pushya (delta Cancri) at 106°
    # fval = swe.fixstar_ut(",deCnc", point, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)[0] - (106)
    return fval

def bisection_search(func, start, stop):
  left = start
  right = stop
  epsilon = 5E-10   # Anything better than this puts the loop below infinite

  while True:
    middle = (left + right) / 2
    midval =  func(middle)
    rtval = func(right)
    if midval * rtval >= 0:
      right = middle
    else:
      left = middle

    if (right - left) <= epsilon: break

  return (right + left) / 2

def inverse_lagrange(x, y, ya):
  """Given two lists x and y, find the value of x = xa when y = ya, i.e., f(xa) = ya"""
  assert(len(x) == len(y))
  total = 0
  for i in range(len(x)):
    numer = 1
    denom = 1
    for j in range(len(x)):
      if j != i:
        numer *= (ya - y[j])
        denom *= (y[i] - y[j])

    total += numer * x[i] / denom

  return total

  # returns (y, m, d, h, min, s)

def local_time_to_jdut1(year, month, day, hour = 0, minutes = 0, seconds = 0, timezone = 0.0):
  """Converts local time to JD(UT1)"""
  y, m, d, h, mnt, s = swe.utc_time_zone(year, month, day, hour, minutes, seconds, timezone)
  # BUG in pyswisseph: replace 0 by s
  jd_et, jd_ut1 = swe.utc_to_jd(y, m, d, h, mnt, 0, flag = swe.GREG_CAL)
#  print("jd_utl")
#  print(jd_utl)
  return jd_ut1

def nakshatra_pada(longitude):
  """Gives nakshatra (1..27) and paada (1..4) in which given longitude lies"""
  # 27 nakshatras span 360°
  one_star = (360 / 27)  # = 13°20'
  # Each nakshatra has 4 padas, so 27 x 4 = 108 padas in 360°
  one_pada = (360 / 108) # = 3°20'
  quotient = int(longitude / one_star)
  reminder = (longitude - quotient * one_star)
  pada = int(reminder / one_pada)
  # convert 0..26 to 1..27 and 0..3 to 1..4
  star_val = quotient
#  pada_val = 1 + pada
  nakstra = star_list[star_val]
  return [nakstra, 1 + pada]

def sidereal_longitude(jd, planet):
  """Computes nirayana (sidereal) longitude of given planet on jd"""
  set_ayanamsa_mode()
  longi = swe.calc_ut(jd, planet, flag = swe.FLG_SWIEPH | swe.FLG_SIDEREAL)
  reset_ayanamsa_mode()
  return norm360(longi[0]) # degrees

solar_longitude = lambda jd: sidereal_longitude(jd, swe.SUN)
lunar_longitude = lambda jd: sidereal_longitude(jd, swe.MOON)

def sunrise(jd, place):
  """Sunrise when centre of disc is at horizon for given date and place"""
  lat, lon, tz = place
#  print('sunrise')
#  print(jd)
#  jd = 2459507.15
  result = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = 0 + swe.CALC_RISE)
#  print(result)
  rise = result[1][0]  # julian-day number
#  print("sunrise")
  # Convert to local time
#  print([rise + tz/24., to_dms((rise - jd) * 24 + tz)])
  return [rise + tz/24., to_dms((rise - jd) * 24 + tz)]

def sunset(jd, place):
  """Sunset when centre of disc is at horizon for given date and place"""
  lat, lon, tz = place
  result = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)
  setting = result[1][0]  # julian-day number
  # Convert to local time
  return [setting + tz/24., to_dms((setting - jd) * 24 + tz)]

def moonrise(jd, place):
  """Moonrise when centre of disc is at horizon for given date and place"""
  lat, lon, tz = place
  result = swe.rise_trans(jd - tz/24, swe.MOON, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)
  rise = result[1][0]  # julian-day number
  
  # Convert to local time
  return to_dms((rise - jd) * 24 + tz)
  

def hora(jd, place):
  """Moonrise when centre of disc is at horizon for given date and place"""
  horalist = []
  tz = place.timezone
  jd1 = jd +1
  SR1 = sunrise(jd, place)
  SR2 = sunrise(jd1, place)
#  print(SR1[1])
#  print(SR1[0])
  jd_to_gregorian = lambda jd: swe.revjul(jd, swe.GREG_CAL)
  d1 = jd_to_gregorian(SR1[0])
  d2 = jd_to_gregorian(SR2[0])
  t1 = SR1[1]
  t2 = SR2[1]
  #    SRA = sunrise(date, location)[1]
  #  print(SRA)
    #SR1 = sunrise(date, location)[0]
    #SRO = timedelta(hours=SRA[0],minutes=SRA[1],seconds=SRA[2])
#  print(d1)
  val = vaara(jd)
  hl = vaara_lord[val]
#  print(hl)
  v2 = hora_list.index(hl)
#  print(v2)
#  print(hora_list[v2])
  date1 = "{0}-{1}-{2}".format(d1[0],d1[1],d1[2])
  time1 = "{0}:{1}:{2}".format(t1[0],t1[1],t1[2])
  date2 = "{0}-{1}-{2}".format(d2[0],d2[1],d2[2])
  time2 = "{0}:{1}:{2}".format(t2[0],t2[1],t2[2])

  datetime1 = date1 +" "+time1
  datetime2 = date2 +" "+time2
  ts1 = pd.Timestamp(datetime1).timestamp()
  ts2 = pd.Timestamp(datetime2).timestamp()
#  print(ts1)
#  print(ts2)
  n = 24
  x = (ts2-ts1)/n
  for i in range(24):
     t4 = ts1+x*i
     t3 = ts1+x*(i+1)
     pdt4 = pd.Timestamp(t4, unit='s')
     pdt3 = pd.Timestamp(t3, unit='s')
     pdtf4 = pd. to_datetime(pdt4, format='%H:%M:%S')
     pdtf3 = pd. to_datetime(pdt3, format='%H:%M:%S')
     horalist.append(hora_list[v2]+':  From : '+str(pdtf4)+' To : '+str(pdtf3))
     
#     if t4 < tn < t3:
#         Current_Hora = plantlist[val]+' From : '+str(t4)+' To : '+str(t3)
         #print(plantlist[val]+' From : '+str(t4)+' To : '+str(t3))

     v2 = v2+1
     if v2 == len(hora_list):
         v2 = 0

#  print(horalist)
#    print(Current_Hora)
  # 1. Find time of sunrise
#  rise = sunrise(jd, place)[0] - tz / 24
  rise = sunrise(jd, place)[0]
#  print(rise)
#  print([rise + tz/24., to_dms((rise - jd) * 24 + tz)])
#  val = [rise + tz/24., to_dms((rise - jd) * 24 + tz)]
  
  return horalist

def moonset(jd, place):
  """Moonset when centre of disc is at horizon for given date and place"""
  lat, lon, tz = place
  result = swe.rise_trans(jd - tz/24, swe.MOON, lon, lat, rsmi = _rise_flags + swe.CALC_SET)
  setting = result[1][0]  # julian-day number
  # Convert to local time
  return to_dms((setting - jd) * 24 + tz)

# Tithi doesn't depend on Ayanamsa
def tithi(jd, place):
  """Tithi at sunrise for given date and place. Also returns tithi's end time."""
  tz = place.timezone
  # 1. Find time of sunrise
#  rise = sunrise(jd, place)[0] - tz / 24
  rise = sunrise(jd, place)[0]

  # 2. Find tithi at this JDN
  moon_phase = lunar_phase(rise)
  today = ceil(moon_phase / 12)
  degrees_left = today * 12 - moon_phase

  # 3. Compute longitudinal differences at intervals of 0.25 days from sunrise
  offsets = [0.25, 0.5, 0.75, 1.0]
  lunar_long_diff = [ (lunar_longitude(rise + t) - lunar_longitude(rise)) % 360 for t in offsets ]
  solar_long_diff = [ (solar_longitude(rise + t) - solar_longitude(rise)) % 360 for t in offsets ]
  relative_motion = [ moon - sun for (moon, sun) in zip(lunar_long_diff, solar_long_diff) ]

  # 4. Find end time by 4-point inverse Lagrange interpolation
  y = relative_motion
  x = offsets
  # compute fraction of day (after sunrise) needed to traverse 'degrees_left'
  approx_end = inverse_lagrange(x, y, degrees_left)
  ends = (rise + approx_end -jd) * 24 + tz
  answer = [int(today), to_dms(ends)]

  # 5. Check for skipped tithi
  moon_phase_tmrw = lunar_phase(rise + 1)
  tomorrow = ceil(moon_phase_tmrw / 12)
  isSkipped = (tomorrow - today) % 30 > 1
  if isSkipped:
    # interpolate again with same (x,y)
    leap_tithi = today + 1
    degrees_left = leap_tithi * 12 - moon_phase
    approx_end = inverse_lagrange(x, y, degrees_left)
    ends = (rise + approx_end -jd) * 24 + place.timezone
    leap_tithi = 1 if today == 30 else leap_tithi
    answer += [int(leap_tithi), to_dms(ends)]

  return answer


def nakshatra(jd, place):
  """Current nakshatra as of julian day (jd)
     1 = Asvini, 2 = Bharani, ..., 27 = Revati
  """
  # 1. Find time of sunrise
#  print(jd)
  lat, lon, tz = place
  rise = sunrise(jd, place)[0] - tz / 24.  # Sunrise at UT 00:00

  offsets = [0.0, 0.25, 0.5, 0.75, 1.0]
  longitudes = [ lunar_longitude(rise + t) for t in offsets]

  # 2. Today's nakshatra is when offset = 0
  # There are 27 Nakshatras spanning 360 degrees
  nak = ceil(longitudes[0] * 27 / 360)
  # 3. Find end time by 5-point inverse Lagrange interpolation
  y = unwrap_angles(longitudes)
  x = offsets
  approx_end = inverse_lagrange(x, y, nak * 360 / 27)
  ends = (rise - jd + approx_end) * 24 + tz
#  print('Naks values')
#  print(nak)
#  print(to_dms(ends))
  answer = [int(nak), to_dms(ends)]
#  print(answer)

  # 4. Check for skipped nakshatra
  nak_tmrw = ceil(longitudes[-1] * 27 / 360)
#  print("nak_tmrw")
#  print(nak_tmrw)
  isSkipped = (nak_tmrw - nak) % 27 > 1
  if isSkipped:
    leap_nak = nak + 1
    approx_end = inverse_lagrange(offsets, longitudes, leap_nak * 360 / 27)
    ends = (rise - jd + approx_end) * 24 + tz
#    print('ends --- leap_nak')
    leap_nak = 1 if nak == 27 else leap_nak
#    print(leap_nak)
#    print(ends)
    answer += [int(leap_nak), to_dms(ends)]
  
#  print(' Nakshatra Answer')
#  print(answer)
#  print(type(answer))
  return answer


def yoga(jd, place):
  """Yoga at given jd and place.
     1 = Vishkambha, 2 = Priti, ..., 27 = Vaidhrti
  """
  # 1. Find time of sunrise
  lat, lon, tz = place
  rise = sunrise(jd, place)[0] - tz / 24.  # Sunrise at UT 00:00

  swe.set_sid_mode(swe.SIDM_LAHIRI)
  # 2. Find the Nirayana longitudes and add them
  lunar_long = lunar_longitude(rise)
  solar_long = solar_longitude(rise)
  total = (lunar_long + solar_long) % 360
  # There are 27 Yogas spanning 360 degrees
  yog = ceil(total * 27 / 360)

  # 3. Find how many longitudes is there left to be swept
  degrees_left = yog * (360 / 27) - total

  # 3. Compute longitudinal sums at intervals of 0.25 days from sunrise
  offsets = [0.25, 0.5, 0.75, 1.0]
  lunar_long_diff = [ (lunar_longitude(rise + t) - lunar_longitude(rise)) % 360 for t in offsets ]
  solar_long_diff = [ (solar_longitude(rise + t) - solar_longitude(rise)) % 360 for t in offsets ]
  total_motion = [ moon + sun for (moon, sun) in zip(lunar_long_diff, solar_long_diff) ]

  # 4. Find end time by 4-point inverse Lagrange interpolation
  y = total_motion
  x = offsets
  # compute fraction of day (after sunrise) needed to traverse 'degrees_left'
  approx_end = inverse_lagrange(x, y, degrees_left)
  ends = (rise + approx_end - jd) * 24 + tz
  answer = [int(yog), to_dms(ends)]

  # 5. Check for skipped yoga
  lunar_long_tmrw = lunar_longitude(rise + 1)
  solar_long_tmrw = solar_longitude(rise + 1)
  total_tmrw = (lunar_long_tmrw + solar_long_tmrw) % 360
  tomorrow = ceil(total_tmrw * 27 / 360)
  isSkipped = (tomorrow - yog) % 27 > 1
  if isSkipped:
    # interpolate again with same (x,y)
    leap_yog = yog + 1
    degrees_left = leap_yog * (360 / 27) - total
    approx_end = inverse_lagrange(x, y, degrees_left)
    ends = (rise + approx_end - jd) * 24 + tz
    leap_yog = 1 if yog == 27 else leap_yog
    answer += [int(leap_yog), to_dms(ends)]

  return answer


def karana(jd, place):
  """Returns the karana and their ending times. (from 1 to 60)"""
  # 1. Find time of sunrise
  rise = sunrise(jd, place)[0]
  
  swe.set_sid_mode(swe.SIDM_LAHIRI)

  # 2. Find karana at this JDN
  solar_long = solar_longitude(rise)
  lunar_long = lunar_longitude(rise)
  moon_phase = (lunar_long - solar_long) % 360
  today = ceil(moon_phase / 6)
#  print("karana")
#  print(moon_phase)
  degrees_left = today * 6 - moon_phase

  return [int(today)]

def vaara(jd):
  """Weekday for given Julian day. 0 = Sunday, 1 = Monday,..., 6 = Saturday"""
  return int(ceil(jd + 1) % 7)

def masa(jd, place):
  """Returns lunar month and if it is adhika or not.
     1 = Chaitra, 2 = Vaisakha, ..., 12 = Phalguna"""
  ti = tithi(jd, place)[0]
  critical = sunrise(jd, place)[0]  # - tz/24 ?
  last_new_moon = new_moon(critical, ti, -1)
  next_new_moon = new_moon(critical, ti, +1)
  this_solar_month = raasi(last_new_moon)
  next_solar_month = raasi(next_new_moon)
  is_leap_month = (this_solar_month == next_solar_month)
  maasa = this_solar_month + 1
  if maasa > 12: maasa = (maasa % 12)
  val = samvatsara(jd, maasa)
  print(val)
  return [int(maasa), is_leap_month]

# epoch-midnight to given midnight
# Days elapsed since beginning of Kali Yuga
ahargana = lambda jd: jd - 588465.5

def elapsed_year(jd, maasa_num):
  ahar = ahargana(jd)  # or (jd + sunrise(jd, place)[0])
  kali = int((ahar + (4 - maasa_num) * 30) / sidereal_year)
  saka = kali - 3179
#  print(saka)
  vikrama = saka + 135
#  print(kali)
#  print(vikrama)
  return kali, saka

# New moon day: sun and moon have same longitude (0 degrees = 360 degrees difference)
# Full moon day: sun and moon are 180 deg apart
def new_moon(jd, tithi_, opt = -1):
  """Returns JDN, where
     opt = -1:  JDN < jd such that lunar_phase(JDN) = 360 degrees
     opt = +1:  JDN >= jd such that lunar_phase(JDN) = 360 degrees
  """
  if opt == -1:  start = jd - tithi_         # previous new moon
  if opt == +1:  start = jd + (30 - tithi_)  # next new moon
  # Search within a span of (start +- 2) days
  x = [ -2 + offset/4 for offset in range(17) ]
  y = [lunar_phase(start + i) for i in x]
  y = unwrap_angles(y)
  y0 = inverse_lagrange(x, y, 360)
  return start + y0

def raasi(jd):
  """Zodiac of given jd. 1 = Mesha, ... 12 = Meena"""
#  print("Raasi Date : ")

#  print(jd)
  s = solar_longitude(jd)
  solar_nirayana = solar_longitude(jd)
  # 12 rasis occupy 360 degrees, so each one is 30 degrees
#  print(ceil(solar_nirayana / 30.))
  return ceil(solar_nirayana / 30.)

def lunar_phase(jd):
  thithi = ["0","Shukla Paksha Prathama", "Shukla Paksha Dwitiya", "Shukla Paksha Tritiya", "Shukla Paksha Chaturthi", "Shukla Paksha Panchami", "Shukla Paksha Shashthi", "Shukla Paksha Saptami", "Shukla Paksha Ashtami", "Shukla Paksha Navami", "Shukla Paksha Dashami", "Shukla Paksha Ekadashi", "Shukla Paksha Dwadashi","Shukla Paksha Thrayodashi","Shukla Paksha Chaturdashi","Purnima","Krishna Paksha Prathama", "Krishna Paksha Dwitiya", "Krishna Paksha Tritiya", "Krishna Paksha Chaturthi", "Krishna Paksha Panchami", "Krishna Paksha Shashthi", "Krishna Paksha Saptami", "Krishna Paksha Ashtami", "Krishna Paksha Navami", "Krishna Paksha Dashami", "Krishna Paksha Ekadashi", "Krishna Paksha Dwadashi","Krishna Paksha Thrayodashi","Krishna Paksha Chaturdashi","Amavasya"]
  solar_long = solar_longitude(jd)
  lunar_long = lunar_longitude(jd)
  moon_phase = (lunar_long - solar_long) % 360
#  print(moon_phase)
#  print(type(moon_phase))

#  if moon_phase < 0:
#      thitinumber = math.ceil((moon_phase + 360) / 12)
#  else:
#      thitinumber = math.ceil((moon_phase) / 12)

#  print(thithi[thitinumber])
#  print('lunar phase')
#  print(moon_phase)
  return moon_phase
  
def pakshaname(jd):
  thithi = ["0","Shukla Paksha Prathama", "Shukla Paksha Dwitiya", "Shukla Paksha Tritiya", "Shukla Paksha Chaturthi", "Shukla Paksha Panchami", "Shukla Paksha Shashthi", "Shukla Paksha Saptami", "Shukla Paksha Ashtami", "Shukla Paksha Navami", "Shukla Paksha Dashami", "Shukla Paksha Ekadashi", "Shukla Paksha Dwadashi","Shukla Paksha Thrayodashi","Shukla Paksha Chaturdashi","Purnima","Krishna Paksha Prathama", "Krishna Paksha Dwitiya", "Krishna Paksha Tritiya", "Krishna Paksha Chaturthi", "Krishna Paksha Panchami", "Krishna Paksha Shashthi", "Krishna Paksha Saptami", "Krishna Paksha Ashtami", "Krishna Paksha Navami", "Krishna Paksha Dashami", "Krishna Paksha Ekadashi", "Krishna Paksha Dwadashi","Krishna Paksha Thrayodashi","Krishna Paksha Chaturdashi","Amavasya"]
  solar_long = solar_longitude(jd)
  lunar_long = lunar_longitude(jd)
  moon_phase = (lunar_long - solar_long) % 360
  print(moon_phase)
  print(type(moon_phase))

  if moon_phase < 0:
      thitinumber = math.ceil((moon_phase + 360) / 12)
  else:
      thitinumber = math.ceil((moon_phase) / 12)

  print(thithi[thitinumber])
  return thithi[thitinumber]
#  print('lunar phase')
#  print(moon_phase)
#  return moon_phase

def cal_current_naks(Cu_Nakshatram, Ne_Nakshatra ):
   print('****************************')
   print(Cu_Nakshatram)
   print(Ne_Nakshatra)
   return True

def samvatsara(jd, maasa_num):
  kali = elapsed_year(jd, maasa_num)[0]
  # Change 14 to 0 for North Indian tradition
  # See the function "get_Jovian_Year_name_south" in pancanga.pl
  if kali >= 4009:    kali = (kali - 14) % 60
  samvat = (kali + 27 + int((kali * 211 - 108) / 18000)) % 60
  print(samvat)
  return samvat

def ritu(masa_num):
  """0 = Vasanta,...,5 = Shishira"""
  return (masa_num - 1) // 2

def day_duration(jd, place):
  srise = sunrise(jd, place)[0]  # julian day num
  sset = sunset(jd, place)[0]    # julian day num
  diff = (sset - srise) * 24     # In hours
  return [diff, to_dms(diff)]

# The day duration is divided into 8 parts
# Similarly night duration
def gauri_chogadiya(jd, place):
  lat, lon, tz = place
  tz = place.timezone
  srise = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  sset = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)[1][0]
  day_dur = (sset - srise)

  end_times = []
  for i in range(1, 9):
    end_times.append(to_dms((srise + (i * day_dur) / 8 - jd) * 24 + tz))

  # Night duration = time from today's sunset to tomorrow's sunrise
  srise = swe.rise_trans((jd + 1) - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  night_dur = (srise - sset)
  for i in range(1, 9):
    end_times.append(to_dms((sset + (i * night_dur) / 8 - jd) * 24 + tz))

  return end_times

def trikalam(jd, place, option='rahu'):
  lat, lon, tz = place
  tz = place.timezone
  srise = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  sset = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)[1][0]
  day_dur = (sset - srise)
  weekday = vaara(jd)

  # value in each array is for given weekday (0 = sunday, etc.)
  offsets = { 'rahu': [0.875, 0.125, 0.75, 0.5, 0.625, 0.375, 0.25],
              'gulika': [0.75, 0.625, 0.5, 0.375, 0.25, 0.125, 0.0],
              'yamaganda': [0.5, 0.375, 0.25, 0.125, 0.0, 0.75, 0.625] }

  start_time = srise + day_dur * offsets[option][weekday]
  end_time = start_time + 0.125 * day_dur

  # to local timezone
  start_time = (start_time - jd) * 24 + tz
  end_time = (end_time - jd) * 24 + tz
  return [to_dms(start_time), to_dms(end_time)] # decimal hours to H:M:S

rahu_kalam = lambda jd, place: trikalam(jd, place, 'rahu')
yamaganda_kalam = lambda jd, place: trikalam(jd, place, 'yamaganda')
gulika_kalam = lambda jd, place: trikalam(jd, place, 'gulika')

def durmuhurtam(jd, place):
  lat, lon, tz = place
  tz = place.timezone

  # Night = today's sunset to tomorrow's sunrise
  sset = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)[1][0]
  srise = swe.rise_trans((jd + 1) - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  night_dur = (srise - sset)

  # Day = today's sunrise to today's sunset
  srise = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  day_dur = (sset - srise)

  weekday = vaara(jd)

  # There is one durmuhurtam on Sun, Wed, Sat; the rest have two
  offsets = [[10.4, 0.0],  # Sunday
             [6.4, 8.8],   # Monday
             [2.4, 4.8],   # Tuesday, [day_duration , night_duration]
             [5.6, 0.0],   # Wednesday
             [4.0, 8.8],   # Thursday
             [2.4, 6.4],   # Friday
             [1.6, 0.0]]   # Saturday

  # second durmuhurtam of tuesday uses night_duration instead of day_duration
  dur = [day_dur, day_dur]
  base = [srise, srise]
  if weekday == 2:  dur[1] = night_dur; base[1] = sset

  # compute start and end timings
  start_times = [0, 0]
  end_times = [0, 0]
  for i in range(0, 2):
    offset = offsets[weekday][i]
    if offset != 0.0:
      start_times[i] = base[i] + dur[i] * offsets[weekday][i] / 12
      end_times[i] = start_times[i] + day_dur * 0.8 / 12

      # convert to local time
      start_times[i] = (start_times[i] - jd) * 24 + tz
      end_times[i] = (end_times[i] - jd) * 24 + tz
 # print(start_times, end_times)
  return [start_times, end_times]  # in decimal hours

def abhijit_muhurta(jd, place):
  """Abhijit muhurta is the 8th muhurta (middle one) of the 15 muhurtas   during the day_duration (~12 hours)"""
  lat, lon, tz = place
  tz = place.timezone
  srise = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  sset = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)[1][0]
  day_dur = (sset - srise)
  print(day_dur)
  muhurt = day_dur/15
  print(muhurt)
  start = srise - 2*muhurt
  end = srise - muhurt
  bstart  = to_dms((start - jd)*24+tz)
  bend = to_dms((end - jd)*24+tz)
  print(bstart)
  print(bend)
  start_time = srise + 7 / 15 * day_dur
  end_time = srise + 8 / 15 * day_dur

  # to local time
 # print([(start_time - jd) * 24 + tz, (end_time - jd) * 24 + tz])
  return [to_dms((start_time - jd) * 24 + tz), to_dms((end_time - jd) * 24 + tz)]


def muhurthas(jd, place):
  """Abhijit muhurta is the 8th muhurta (middle one) of the 15 muhurtas   during the day_duration (~12 hours)"""
  lat, lon, tz = place
  tz = place.timezone
  srise = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  srise2 = swe.rise_trans(jd+1 - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_RISE)[1][0]
  sset = swe.rise_trans(jd - tz/24, swe.SUN, lon, lat, rsmi = _rise_flags + swe.CALC_SET)[1][0]
  day_dur = (sset - srise)
  night_dur = (srise2 -sset)
  day_muhurtha_list = []
  night_muhurtha_list = []
  muhurtha_dur = day_dur/15
  muhurtha_nigh = night_dur/15
  x = 0
  y = 0
  for i in range(15):
      mstart = srise + muhurtha_dur*(i-1)
      muh_start = (mstart -jd)*24+tz
      mend = srise +  muhurtha_dur*(i)
      muh_end = (mend -jd)*24+tz
      day_muhurtha_list.append(day_muhurtha[x]+' From : '+str(to_dms(muh_start))+' To : '+str(to_dms(muh_end)))
      x = x+1

  for i in range(15):
      nmstart = sset + muhurtha_nigh*(i-1)
      nmuh_start = (nmstart -jd)*24+tz
      nmend = sset +  muhurtha_nigh*(i)
      nmuh_end = (nmend -jd)*24+tz
      night_muhurtha_list.append(night_muhurtha[y]+' From : '+str(to_dms(nmuh_start))+' To : '+str(to_dms(nmuh_end)))
      y = y+1

#  print(day_muhurtha_list)
#  start_time = srise + 7 / 15 * day_dur
#  end_time = srise + 8 / 15 * day_dur

  # to local time
 # print([(start_time - jd) * 24 + tz, (end_time - jd) * 24 + tz])
  return [day_muhurtha_list, night_muhurtha_list]


# 'jd' can be any time: ex, 2015-09-19 14:20 UTC
# today = swe.julday(2015, 9, 19, 14 + 20./60)
def planetary_positions(jd, place):
  """Computes instantaneous planetary positions
     (i.e., which celestial object lies in which constellation)

     Also gives the nakshatra-pada division
   """
  jd_ut = jd - place.timezone / 24.
#  print(jd_ut)
#  jd_ut = 2459481.35112

  positions = []
  plan_positions = []
  for planet in planet_list:
    if planet != swe.KETU:
      nirayana_long = sidereal_longitude(jd_ut, planet)
    else: # Ketu
      nirayana_long = ketu(sidereal_longitude(jd_ut, swe.MEAN_NODE))

    # 12 zodiac signs span 360°, so each one takes 30°
    # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
    constellation = int(nirayana_long / 30)
    rashi = rashi_list[constellation]
#    print(planet)
    plant = planetary_list[planet]
#    print(plant)
    coordinates = to_dms(nirayana_long % 30)
    positions.append([planet, constellation, coordinates, nakshatra_pada(nirayana_long)])
    plan_positions.append([plant, rashi, coordinates, nakshatra_pada(nirayana_long)])
#    print(plan_positions)
  return plan_positions

def sun_position(jd, place):
  """Computes instantaneous planetary positions
     (i.e., which celestial object lies in which constellation)

     Also gives the nakshatra-pada division
   """
  #jd_ut = jd - place.timezone / 24.
#  print(jd_ut)
#  jd_ut = 2459481.35112

#  positions = []
  sun_position = []
#  for planet in planet_list:
 #   if planet != swe.KETU:
  nirayana_long = sidereal_longitude(jd, 0)
 #   else: # Ketu
 #     nirayana_long = ketu(sidereal_longitude(jd_ut, swe.MEAN_NODE))

    # 12 zodiac signs span 360°, so each one takes 30°
    # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
  constellation = int(nirayana_long / 30)
  rashi = rashi_list[constellation]
#    print(planet)
  plant = planetary_list[0]
#    print(plant)
  coordinates = to_dms(nirayana_long % 30)
#    positions.append([planet, constellation, coordinates, nakshatra_pada(nirayana_long)])
  sun_position.append([plant, rashi, coordinates, nakshatra_pada(nirayana_long)])
#    print(plan_positions)
  return sun_position


def moon_position(jd, place):
  """Computes instantaneous planetary positions
     (i.e., which celestial object lies in which constellation)

     Also gives the nakshatra-pada division
   """
  #jd_ut = jd - place.timezone / 24.
#  print(jd_ut)
#  jd_ut = 2459481.35112

#  positions = []
  sun_position = []
#  for planet in planet_list:
 #   if planet != swe.KETU:
  nirayana_long = sidereal_longitude(jd, 1)
 #   else: # Ketu
 #     nirayana_long = ketu(sidereal_longitude(jd_ut, swe.MEAN_NODE))

    # 12 zodiac signs span 360°, so each one takes 30°
    # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
  constellation = int(nirayana_long / 30)
  rashi = rashi_list[constellation]
#    print(planet)
  plant = planetary_list[1]
#    print(plant)
  coordinates = to_dms(nirayana_long % 30)
#    positions.append([planet, constellation, coordinates, nakshatra_pada(nirayana_long)])
  sun_position.append([plant, rashi, coordinates, nakshatra_pada(nirayana_long)])
#    print(plan_positions)
  return sun_position



def ascendant(jd, place):
  """Lagna (=ascendant) calculation at any given time & place"""
  lat, lon, tz = place
#  print("**********************")
#  print(lat)
#  print(lon)
#  print(tz)
#  print(jd)
  jd_utc = jd - (tz / 24.)
#  jd_utc = 2459505.415
#  jd_utc = 2459492.1187500
  set_ayanamsa_mode() # needed for swe.houses_ex()
#  print(jd_utc)
  # returns two arrays, cusps and ascmc, where ascmc[0] = Ascendant
  nirayana_lagna = swe.houses_ex(jd_utc, lat, lon, flag = swe.FLG_SIDEREAL)[1][0]
#  print(nirayana_lagna)
  # 12 zodiac signs span 360°, so each one takes 30°
  # 0 = Mesha, 1 = Vrishabha, ..., 11 = Meena
  constellation = int(nirayana_lagna / 30)
#  rashiindex = constellation+1
  rashi = rashi_list[constellation]
#  print(rashi)
  coordinates = to_dms(nirayana_lagna % 30)

  reset_ayanamsa_mode()
#  print ([rashi, coordinates, nakshatra_pada(nirayana_lagna)])
  return [rashi, coordinates, nakshatra_pada(nirayana_lagna)]

# http://www.oocities.org/talk2astrologer/LearnAstrology/Details/Navamsa.html
# Useful for making D9 divisional chart
def navamsa_from_long(longitude):
  """Calculates the navamsa-sign in which given longitude falls
  0 = Aries, 1 = Taurus, ..., 11 = Pisces
  """
  one_pada = (360 / (12 * 9))  # There are also 108 navamsas
  one_sign = 12 * one_pada    # = 40 degrees exactly
  signs_elapsed = longitude / one_sign
  fraction_left = signs_elapsed % 1
  return int(fraction_left * 12)

def navamsa(jd, place):
  """Calculates navamsa of all planets"""
  jd_utc = jd - place.timezone / 24.

  positions = []
  for planet in planet_list:
    if planet != swe.KETU:
      nirayana_long = sidereal_longitude(jd_utc, planet)
    else: # Ketu
      nirayana_long = ketu(sidereal_longitude(jd_utc, swe.MEAN_NODE))

    positions.append([planet, navamsa_from_long(nirayana_long)])

  return positions





#app.run()

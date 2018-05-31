#!/usr/bin/env python

from linkedin import linkedin

API_KEY = '78tsqie02v4wm8'
API_SECRET = 'VyZuUkUHEQkbeZTK'
RETURN_URL = 'http://localhost:8080'

# authentication = linkedin.LinkedInAuthentication(
#     API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
# # Optionally one can send custom "state" value that will be returned from OAuth server
# # It can be used to track your user state or something else (it's up to you)
# # Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
# #authorization.state = 'your_encoded_message'
# print authentication.authorization_url  # open this url on your browser
# application = linkedin.LinkedInApplication(authentication)
# authentication.authorization_code = 'AQSWhBRUvB2FkargS0rK8Osv8PCB48cnaDlsPyS79-3iitRUe6Rq5HJmm8j2YE8O-ex0MlCr9xVXZAG2AJgr3soeCOOZAm-jr3bpIn9ys_VL4WAPcbRnUg7xPkDvP6NJe7mmyMSe4AIO2Kp5m9STXNioenxsbg'
# print(authentication.get_access_token())
#
token=('AQXafh8-xJlEHszFPWXa8hFFPAy6KPmVVJeh-G4Y1tffPslPyauYG2s2etW7x8a_'
       'NpiPBNMKrxXPKBkH_JWUbG_KlrPSI_oasTzo4_WPe-gA1uvCiSBnQpb_A9jiw00qtd-E1S'
       'e6Wkh1ExvMXseJRa8HC4SfFU6sL4VLrdMSokMOsr2Zqw3Q4ksUjkxfG7k6mZMet-LXXU3o'
       '0Ngd4FALxU0UsGH1VmBQirlQNRbF3p8oq0KoW85DBPjLw4VVTp4ohJdWBbDJ512_2_OSxo'
       '4LXbtd5lb-tal586wxD71FZz_sXdR-7QZ1L19s45Q4EMMcqr97Ekz5hagS0Js8-'
       'tb1XJBHHoNs0Q')

application = linkedin.LinkedInApplication(token=token)
p = application.get_profile(selectors=['positions:(company,title,summary,startDate,endDate,isCurrent)'], member_url='https://www.linkedin.com/in/oleg-shn/')
print p['positions']

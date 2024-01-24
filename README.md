# Get a notification email when Class is no longer closed
## Introduction
<h5>Tired about checking the course search and enroll? Let's go with a simple web scraper!</h5>
<h5>Get an email notification when class is not longer closed (best for classes without waitlist)</h5>
ex: I am using for genetics 133 in this case.

## Process
* Using https://public.enroll.wisc.edu/search, the website is for General Public to search UW-Madison courses – Public Course Search & Enroll application. There is no login required.
* Using gmail as the platform to send email. Reference to https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp.
* The check is happened every hour. Using schedule to do work every hour. Reference: https://schedule.readthedocs.io/en/stable/examples.html

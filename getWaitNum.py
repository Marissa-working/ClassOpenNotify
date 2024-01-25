import requests

def check_waitlist_num():
    url = "https://public.enroll.wisc.edu/api/search/v1/enrollmentPackages/1244/600/011667"
    response = requests.get(url)

    if response.status_code == 200:
        #section number-1 in []
        data = dict(response.json()[1])
        size = data.get("enrollmentStatus", {}).get("waitlistCurrentSize")
        print("Current waitlist size: " + str(size) )
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Run the check_waitlist_num function
check_waitlist_num()

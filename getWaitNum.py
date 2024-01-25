import requests

def check_waitlist_num(classNumber):
    url = "https://public.enroll.wisc.edu/api/search/v1/enrollmentPackages/1244/600/011667"
    response = requests.get(url)

    if response.status_code == 200:
        for section in response.json():
            info = section.get("enrollmentStatus", {})
            #print(info.get("classUniqueId",{}).get("classNumber"))
            if info.get("classUniqueId",{}).get("classNumber") == classNumber:
                size = info.get("waitlistCurrentSize")
                print("Current waitlist size: " + str(size) )
                return
        print("The class number is not found")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Run the check_waitlist_num function by the desired class number
check_waitlist_num(classNumber = 53823)

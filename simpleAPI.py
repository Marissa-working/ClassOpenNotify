!pip install requests
import requests

def check_class_status():
    url = "https://public.enroll.wisc.edu/api/search/v1/enrollmentPackages/1244/412/008122"
    response = requests.get(url)

    if response.status_code == 200:
        data = dict(response.json()[0])
        #print(dict(data[0]))
        status = data.get("packageEnrollmentStatus", {}).get("status")

        if status == "CLOSED":
            notify_user("Class is closed!")
        else:
            print("Class is still open.")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def notify_user(message):
    print(f"Notification: {message}")

# Run the check_class_status function
check_class_status()

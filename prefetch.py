import webbrowser
import time

# List of links to open
links = [
    "https://youtube.com",
    "https://github.com"
]

# Time interval between opening links (in seconds)
interval = 0  # Adjust as needed

# Loop to open links repeatedly
while True:
    for link in links:
        webbrowser.open(link)  # Opens the link in the default browser
        print(f"Opened: {link}")
        time.sleep(interval)  # Wait before opening the next link
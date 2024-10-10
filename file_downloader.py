import requests


def download_file(url, file_name):
    # Send a GET request to the provided URL
    file_name=f"{file_name}.{url.split(".")[-1].lower()}"#to generate extension from url
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")
    print(f"Content Length: {len(response.content)}")
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")#Example usage


with open("test.txt", "w") as f:
    f.write("This is a test file.")

if __name__ == "__main__":
	url = 'https://www.python.org/static/img/python-logo@2x.png'
	file_name = 'file'
	download_file(url, file_name)

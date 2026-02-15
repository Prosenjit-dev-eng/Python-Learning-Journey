import json
# 🧩 What is JSON?

# JSON stands for JavaScript Object Notation.
# It’s a text-based format for storing and exchanging data —
# easy for humans to read and computers to parse.
# Think of it as a lightweight way to represent structured data (like Python dictionaries).

# The under is a json data 
# {
#   "name": "Alice",
#   "age": 25,
#   "isStudent": false,
#   "skills": ["Python", "C++", "HTML"],
#   "address": {
#     "city": "Paris",
#     "country": "France"
#   }
# }

def load_data():
    # just like give values in array
    # try: best for database
    try:
        with open('youtube.txt', 'r') as file:

            test = json.load(file)# go to the file, as alias it is here, then convert its data into json
            # print(type(test))#json list
            return test
    except FileNotFoundError:# There are too much case for error handling
            return []
    
def save_data_helper(videos):
# bcz we don't not return anything in except case here
# so we don't use try
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)# what & where are the parameters of dumb


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

#  Why pass exists
# It’s mostly used as a placeholder when:
# You’re designing your program structure.
# You want to avoid syntax errors temporarily.
# You’ll fill in the code later.

def main():
    # let, videos = [] -> list
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("\n 1. List all youtube videos ")
        print("\n 2. Add a youtube video ")
        print("\n 3. Update a youtube video detail ")
        print("\n 4. Delete a youtube video ")
        print("\n 5. Exit the app ")
        choice = input("Enter your choice: ")

        # like switch here match
        match choice:
            case '1':
                #1 is not aan integer , it's a string mind it
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos) 
            case '5':
                break;
            case _:
                #   Here '_' means default, meanwhile all values except 1 to 5
                print("Invalid Choices")
                        
if __name__ == "__main__":
    main()#'__'=> It's called dunder to fetch the __name__ function
            
        

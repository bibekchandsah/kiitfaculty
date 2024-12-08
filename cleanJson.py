import json

# Load and clean JSON data from a file with multiple objects (if necessary)
try:
    with open('facultyDetail.json', 'r') as file:
        data = file.read().strip()
        
        # Check if the file contains multiple JSON objects (not inside an array)
        if '}{' in data:
            # If multiple JSON objects exist, we need to fix them by adding a wrapping array
            data = f"[{data.replace('}{', '},{')}]"
        
        json_data = json.loads(data)
        
    # Now proceed with removing keys and saving back
    keys_to_remove = ["likesId", "dislikesId", "reviews", "semesterSectionId", "subjectId"]
    for key in keys_to_remove:
        for obj in json_data:
            if key in obj:
                del obj[key]
    
    # Save the updated JSON data back to the file
    with open('facultyDetail.json', 'w') as file:
        json.dump(json_data, file, indent=4)

    print("Data updated successfully!")

except json.JSONDecodeError as e:
    print(f"Error reading JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

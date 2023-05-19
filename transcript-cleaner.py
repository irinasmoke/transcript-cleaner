import os

# Set the folder path~
input_folder_path = "input"
output_folder_path = "output"

# Create a dictionary to store the mapping between old names and new names
# If the script comes across names that are NOT found in the list below, you will be prompted to enter a name for them in the command line
 #NOTE: Names must match what is in the transcript EXACTLY. For example, if the name in the transcript is "Irina Smoke (guest)", then the name in the dictionary must be "Irina Smoke (guest)" and not "Irina" or "Irina Smoke"

name_mapping = {
    
    #Replace names below with the names of speakers in your transcripts assign them an anonymous name instead, such as Interviewer 01 or P01

    #Interviewers
    "Irina Smoke": "Interviewer 01",
    "Al Tsang": "Interviewer 02",
    "Marie Hagman": "Interviewer 03",

    #Customers
    "Alice (guest)":"P01",
    "Bob (guest)":"P02",
    "Sally":"P03",
    "Vignesh M (External)":"P04",
    "David Liang":"P05",
}



# Loop through each file in the folder and replace names to anonymize
for filename in os.listdir(input_folder_path):

    # Check if the file is a text file
    if filename.endswith('.txt'):

        # Construct the full file path
        file_path = os.path.join(input_folder_path, filename)

        # Open the input file
        with open(file_path, 'r') as input_file:

            # Read the contents of the input file
            contents = input_file.read()

            # Loop through the contents of the file and replace all instances of old names with new names
            while True:
                # Find the next instance of a name
                start_index = contents.find('<v ')
                if start_index == -1:
                    break
                end_index = contents.find('>', start_index)
                name = contents[start_index+3:end_index]

                # If the name has not been seen before, ask the user for a new name
                if name not in name_mapping:
                    new_name = input(f"What would you like to replace '{name}' with? ")
                    name_mapping[name] = new_name

                # Replace the old name with the new name
                new_name = name_mapping[name]
                contents = contents[:start_index] + f"< {new_name} > \n" + contents[end_index+1:]

        # Remove the specified string from the contents of the file
        contents = contents.replace("</v>", '')
        contents = contents.replace("WEBVTT", '')
        

        # Construct the output file path
        output_file_path = os.path.join(output_folder_path, filename)

        # Open the output file
        with open(output_file_path, 'w') as output_file:

            # Write the reformatted contents to the output file
            output_file.write(contents)
        
        # Close the input and output files
        input_file.close()
        output_file.close()



# Loop through each file in the folder
for filename in os.listdir(output_folder_path):

    # Check if the file is a text file
    if filename.endswith('.txt'):

        
        # Construct the full file path
        output_file_path = os.path.join(output_folder_path, filename)

        

        # Open the output file
        with open(output_file_path, 'r+') as output_file:

            # Read the contents of the input file
            contents02 = output_file.readlines()

            # Filter out lines that begin with a number
            filtered_contents = [line for line in contents02 if not line.lstrip().startswith(tuple(str(i) for i in range(10)))]
            

        #Write the new contents to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(filtered_contents)

        # Close the output files
        output_file.close()




    
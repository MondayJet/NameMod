"""Earth - Our Solar System - #3.txt
Jupiter - Our Solar System - #5.txt
Mars - Our Solar System - #1.txt
Mercury - Our Solar System - #4.txt
Neptune - Our Solar System - #10.txt
Saturn - Our Solar System - #7.txt
Uranus - Our Solar System - #6.txt
Venus - Our Solar System - #2.txt """

#Given the above file format. this file converts it to the output seen below


import os

# Set the working directory to the location of the files
os.chdir("C:\\Users\\JohnMonday\\Desktop\\Templates\\file1")

# Print the current working directory to confirm
print(os.getcwd())

# Loop through each file in the directory
for f in os.listdir():
    # Split the filename from its extension
    fname, fext = os.path.splitext(f)
    
    # Split the filename by "-"
    mod_fname = fname.split("-")
    
    # Unpack the split filename into individual values
    value1, value2, value3 = mod_fname
    
    # Remove white spaces from the values
    value1 = value1.strip()
    value2 = value2.strip()
    
    # Remove white spaces, specify starting point, and pad value3 to have two digits
    value3 = value3.strip()[1:].zfill(2) #Same result can be achieved wutg value3 = value3.strip()[1:.02]
    
    # Format the desired output filename
    desired = f"{value3} {value1}{fext}"
    
    # Print the desired output filename
    print(desired)
    
    # Rename the file to the desired output filename
    os.rename(f, desired)


"""THE FILE OPERATED UPON IS THE ABOVE THE RESULT IS GIVE BELOW
01 Mars.txt
02 Venus.txt
03 Earth.txt
04 Mercury.txt
05 Jupiter.txt
06 Uranus.txt
07 Saturn.txt
10 Neptune.txt
    """
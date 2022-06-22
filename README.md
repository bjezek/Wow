
# Overview of the project 
creating an application that runs a customers income and debt information along with there credit
score to determine if they qualify for the loan they request and then asking them if they want to save it.

# Technology used is python 3.10 and Fire.Fire



# Wow

#Application used to save file path and ask user if they want to say loans to csvfile
if not exit application. 


#updated csv file path 
#updated path for qualifying loan applications to save to csvfile.

# @TODO: Complete the usability dialog for savings the CSV Files.
    
    if not qualifying_loans:
        sys.exit("Sorry, there are no qualifying loans!")

    saveFile = questionary.confirm("Would you like to save the qualifying loans?").ask()

    if saveFile:
        csvpath = questionary.text(
            "Please enter a filepath for the saved data: (qualifying_loans.csv)"
        ).ask()
        save_csv(Path(csvpath), qualifying_loans)
        
# saves rows into csv file with data that user qualifies for and imports it row by row allowing the user to read the loan data clearly. 
              for row in csvreader:
            data.append(row)
    return data
def save_csv(csvpath, data, header =None):
    """Save csv file and implement data to file, import list of list
    from csvpath to qualify loan"""
    with open(csvpath, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=" ,")
        if header:
            csvwriter.writerow(header)
        csvwriter.writerows(data)
        
        """Path to rund save loan data function""
        
    

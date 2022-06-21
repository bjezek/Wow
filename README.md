# Wow

#Application used to save file path and ask user if they want to say loans to csvfile
if not exit application. 


#updated csv file path 
#updated path for qualifying loan applications to save to csvfile.

# @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    if not qualifying_loans:
        sys.exit("Sorry, there are no qualifying loans!")

    saveFile = questionary.confirm("Would you like to save the qualifying loans?").ask()

    if saveFile:
        csvpath = questionary.text(
            "Please enter a filepath for the saved data: (qualifying_loans.csv)"
        ).ask()
        save_csv(Path(csvpath), qualifying_loans)
        
        
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

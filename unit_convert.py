#Unit Converter

def main():
    #Takes in which category will be used
    conversionCategories = [
        "Length", "Temp", "Area", "Volume", "Weight", "Time"
        ]
    print("Conversion Categories: ")
    for index, value in enumerate(conversionCategories):
        print(f"{index} : {value}")
    choice = int((input("\nSelect One: \n")))
    
    #Dictionary for running the function related to the conversion that was chosen
    conversion_options = {
        0: Length_Converter_Menu, 
        1: Temp_Converter,
        2: Area_Converter,
        3: Volume_Converter,
        4: Weight_Converter,
        5: Time_Converter,
    }
    
    if choice in conversion_options:
        conversion_options[choice]()
    else:
        print("Invalid Choice")
        
        
#Will take in conversions related to Length
def Length_Converter_Menu():
    #sets the base units for each factor
    #list of units to create the numbered list
    units = [
    "Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", 
    "Nanometer", "Mile", "Yard", "Foot", "Inch"
    ]
    for index, unit in enumerate(units):
        print(f"{index}. {unit}")
    
    from_choice = int(input("Select the unit you want to convert from (0-9)"))
    if from_choice < 0 or from_choice >= len(units):
        print("Invalid choice for 'from' unit. Please select a valid option.")
        return 
    to_choice = int(input("Select the unit you want to convert to (0-9)"))
    if to_choice < 0 or from_choice >= len(units):
        print("Invalid choice for 'from' unit. Please select a valid option.")
        return 
    value = int(input("Enter the value you want to convert"))
    
    from_unit = units[from_choice]
    to_unit = units[to_choice]
    result = Length_Converter(value, from_unit, to_unit)
    
    print(f"{value} {from_unit} is {result} {to_unit}")
    
def Length_Converter(value, from_unit, to_unit):
    length_conversion_factors = {
        "Meter" : 1, #base unit
        "Kilometer" : 0.001,
        "Centimeter" : 100,
        "Millimeter" : 1000,
        "Micrometer" : 1e6, 
        "Nanometer" : 1e9,
        "Mile" : 0.0006621371,
        "Yard" : 1.09361,
        "Foot" : 3.28084,
        "Inch" : 39.3701,
    }
    
    #make sure inputs are correct
    if from_unit not in length_conversion_factors or to_unit not in length_conversion_factors:
        return "Error"
    
    #conversion formula    ex. converting 1cm to meters would output 0.01, 1*(meter / centimeter) = 1 divided by 100 = 0.01 * 1 = "0.01"
    return value * (length_conversion_factors[to_unit] / length_conversion_factors[from_unit])
    
    

#Will take in conversions related to Temp    
def Temp_Converter():
    print("1")  
#Will take in conversions related to Area    
def Area_Converter():
    print("1")  
#Will take in conversions related to Volume
def Volume_Converter():
    print("1")   
#Will take in conversions related to Weight    
def Weight_Converter():
    print("1")   
#Will take in conversions related to Time    
def Time_Converter():
    print("1")    
main()
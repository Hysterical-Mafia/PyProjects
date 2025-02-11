#Unit Converter

def main():
    #Takes in which category will be used
    conversionCategories = [
        "Length", "Temp", "Area", "Volume", "Weight", "Time"
        ]
    print("Conversion Categories: ")
    for index, value in enumerate(conversionCategories):
        print(f"{index} : {value}")
    choice = int((input("\nSelect One: ")))
    
    #Dictionary for running the function related to the conversion that was chosen
    conversion_options = {
        0: Length_Converter_Menu, 
        1: Temp_Converter_Menu,
        2: Area_Converter_Menu,
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
        print("Invalid choice for 'to' unit. Please select a valid option.")
        return 
    value = float(input("Enter the value you want to convert"))
    
    from_unit = units[from_choice]
    to_unit = units[to_choice]
    result = Length_Converter(value, from_unit, to_unit)
    
    print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    
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
def Temp_Converter_Menu():
    temp_conversion_formula = {
    ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32,
    ("Celsius", "Kelvin"): lambda c: c + 273.15,
    ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
    ("Fahrenheit", "Kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
    ("Kelvin", "Celsius"): lambda k: k - 273.15,
    ("Kelvin", "Fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32,
    }
    
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    for index, unit in enumerate(units):
        print(f"{index}: {unit}")
    
    try:
        from_choice = int(input("Select the temperatures you want to convert from (0-2): "))
        to_choice = int(input("Select the unit you want to convert to (0-2): "))
        
        if from_choice not in range(len(units)) or to_choice not in range(len(units)):
            print("Invalid choice for conversions. Please select a valid option.")
            return 
    
        value = float(input("Enter the value you want to convert: "))
    
        from_unit = units[from_choice]
        to_unit = units[to_choice]
        
        result = Temp_Converter(value, from_unit, to_unit, temp_conversion_formula)
        #.2f rounds it 2 decimal places instead of it being a long decimal ex. 25.6789 to 25.68
        print(f"\n{value} {from_unit} is {result:.2f} {to_unit}")

    except ValueError:
        print("Invalid input")
    
def Temp_Converter(value, from_unit, to_unit, temp_conversion_formula):
    if from_unit == to_unit:  
        return value 

    if (from_unit, to_unit) in temp_conversion_formula:
        return temp_conversion_formula[(from_unit, to_unit)](value)

    raise ValueError("Invalid conversion type")
     
#Will take in conversions related to Area    
def Area_Converter_Menu():
    #sets the base units for each factor
    #list of units to create the numbered list
    units = [
        "Square Meter(m²)",
        "Square Kilometer(km²)",
        "Square Centimeter(cm²)",
        "Square Millimeter(mm²)",
        "Square Micrometer(µm²)", 
        "Hectare(ha)",
        "Square Mile(mi²)",
        "Square Yard(yd²)",
        "Square Foot(ft²)",
        "Square Inch(in²)",
        "Acre(ac)",
    ]
    for index, unit in enumerate(units):
        print(f"{index}. {unit}")
    
    try:
        from_choice = int(input("Select the units you want to convert from (0-10): "))
        to_choice = int(input("Select the unit you want to convert to (0-10): "))
        
        if from_choice not in range(len(units)) or to_choice not in range(len(units)):
            print("Invalid choice for conversions. Please select a valid option.")
            return  
        value = float(input("Enter the value you want to convert"))
    
        from_unit = units[from_choice]
        to_unit = units[to_choice]
        result = Area_Converter(value, from_unit, to_unit)
    
        print(f"\n{value} {from_unit} is {result:} {to_unit}")

    except ValueError:
        print("Invalid input")
    
def Area_Converter(value, from_unit, to_unit):
    area_conversion_factors = {
        "Square Meter(m²)" : 1, #base unit
        "Square Kilometer(km²)" : 0.000001,
        "Square Centimeter(cm²)" : 10000,
        "Square Millimeter(mm²)" : 1e6,
        "Square Micrometer(µm²)" : 1e12, 
        "Hectare(ha)" : 0.0001,
        "Square Mile(mi²)" : 3.861018768E-7,
        "Square Yard(yd²)" : 1.1959900463,
        "Square Foot(ft²)" : 10.763910417,
        "Square Inch(in²)" : 1550.0031,
        "Acre(ac)" : 0.0002471054,
    }
    
    #make sure inputs are correct
    if from_unit not in area_conversion_factors or to_unit not in area_conversion_factors:
        return "Error"
    
    return value * (area_conversion_factors[to_unit] / area_conversion_factors[from_unit])


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
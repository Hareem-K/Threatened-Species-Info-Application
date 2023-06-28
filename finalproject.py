# Final Project
# Hareem Khan, ENDG 233 F21
# ID# 30140959
# Group number L03-21
# A terminal based application to process and plot threatened species data based on provided csv files and given user input


import numpy as np
import matplotlib.pyplot as plt
import math


class Country:

    """ A class used to create a country object.

        Attributes:
        name (str): String that represents the country's name
        pop (int): Integer that represents the country's current population
        un_region (str): String that represents the UN Region of the country
        un_subregion (str): String that represents the UN Sub-region of the country

    """

    def __init__(self, name, pop, un_region, un_subregion):
        self.name = name
        self.pop = pop
        self.un_region = un_region
        self.un_subregion = un_subregion


    def print_country_stats(self):
        """A function that prints the name, population, region and sub-region of the country instance.

        Parameters: None
        Return: None

        """

        print(", Country: {0}\n, Region: {3}\n, Sub-Region: {1}\n, Current Population: {2}\n".format(self.name, self.un_region, self.un_subregion, self.pop))                                                                                           #Printing out country info using Country class to output
        print()

def print_main_message(user_input1,countries_list,user_input2, valid_list):
    """A function that prints the welcome message to the user when valid input is provided (for both inputs).

    Parameters:
    user_input1 (str): country that is inputted
    countries_list (list): list of all countries
    user_input2 (str): option of 1, 2, or 3 that is inputted
    valid_list (list[str]): list of 1, 2, and 3 used for if statement

    Return: None
    
    """
    if user_input1 in countries_list and user_input2 in valid_list: 
        print('ENDG 233 Threatened Species Database')                                                                                                                                                                                                   #Printing out welcome message to output

def print_end_message(user_input1,countries_list,user_input2, valid_list):
    """A function that prints the end message to the user when valid input is provided (for both inputs).

    Parameters:
    user_input1 (str): country that is inputted
    countries_list (list): list of all countries
    user_input2 (str): option of 1, 2, or 3 that is inputted
    valid_list (list[str]): list of 1, 2, and 3 used for if statement

    Return: None
    
    """
    if user_input1 in countries_list and user_input2 in valid_list:
        print('Thank You For Using The ENDG 233 Threatened Species Database')                                                                                                                                                                           #Printing out end message to output

def main():

    #array data from csv files

    country_data = np.genfromtxt('Country_Data.csv', delimiter = ',', encoding = None, dtype = None)                                                                                                                                                    #Array from the 'country data' csv file

    population_data = np.genfromtxt('Population_Data.csv', delimiter = ',', encoding = None, dtype = None)                                                                                                                                              #Array from the 'population data' csv file

    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter = ',', encoding = None)                                                                                                                                                      #Array from the 'threatened species' csv file


    #lists with country names and current (2020) population
    
    
    countries_list = list(country_data[:,0])                                                                                                                                                                                                            #List of all countries created from the country data array
 


  
    valid_list = ['1','2','3']                                                                                                                                                                                                                          #List of all valid options for the second input to ensure only valid options are inputted
    
    
    #user input while loops
    user_input1 = input('Please enter a Country Name: ')                                                                                                                                                                                                #User prompted to input a counntry
    while user_input1 not  in countries_list:                                                                                                                                                                                                           #While loop to ensure a valid country is inputted. If not the user is prompted to re-enter their country
        print('Please enter a valid country.')
        user_input1 = input('Please enter a Country Name: ')   


    user_input2 = input('Enter 1 for average threatened species, 2 for the density of current population/threatened species, or 3 for the total threatened species and max and min threatened species:  ')                                              #User prompted to input an option of 1, 2 or 3 depending on what they want to output about their inutted country
    while user_input2 not in valid_list:                                                                                                                                                                                                                #While loop to ensure a valid option is inputted. If not the user is prompted to re-enter their option
        print('Please enter a valid option.')
        user_input2 = input('Enter 1 for average threatened species, 2 for the density of current population/threatened species, or 3 for the total threatened species and max and min threatened species:  ')


    
    country_index = countries_list.index(user_input1)                                                                                                                                                                                                   #Index of country based on list of countries and user input (used to search through arrays)


    pop_2017 = int(population_data[country_index,18])                                                                                                                                                                                                   #Population of inputted country in 2017 (used in plot)
    pop_2018 = int(population_data[country_index,19])                                                                                                                                                                                                   #Population of inputted country in 2018 (used in plot)
    pop_2019 = int(population_data[country_index,20])                                                                                                                                                                                                   #Population of inputted country in 2019 (used in plot)
    pop_2020 = int(population_data[country_index,21])                                                                                                                                                                                                   #Population of inputted country in 2020 (used in plot)
    
    print_main_message(user_input1,countries_list,user_input2, valid_list)                                                                                                                                                                              #Welcome message is printed to user once valid input is provided
    

    #printing country, region, sub-region and current population using country class 
    if user_input1 in countries_list and user_input2 in valid_list:                                                                                                                                                                                     #If both user inputs are valid, the country class is called to print out country info such as name, region, sub-rgion and current population
        user_region = country_data[country_index,1]
        user_subregion = country_data[country_index,2]
        user_country = Country(user_input1, user_region, user_subregion, pop_2020)

    user_country.print_country_stats()                                                                                                                                                                                                                  #Calling print country stats function in the Country class

    #second user_input options
    if user_input2 == '1':                                                                                                                                                                                                                              #If the user inputs '1' for the second input, they are returned with the average amount of threatened species in their desired country, and the number of each threatened species
        average_threatened_sp = int((threatened_species[country_index,1] + threatened_species[country_index,2] + threatened_species[country_index,3] + threatened_species[country_index,4])/4)                                                          #Calculating average threatened species (adding amount of each species from threatened species array and dividing by 4)
        print('Average threatened species in', user_input1, 'is:', average_threatened_sp)                                                                                                                                                               #Printing average threatened species to output
        print()
        print('This includes:')                                                                                                                                                                                                                         #Printing out the number of each threatened species to output from threatened species array
        print(math.floor(threatened_species[country_index,1]), 'threatened plants')
        print(math.floor(threatened_species[country_index,2]), 'threatened fish')
        print(math.floor(threatened_species[country_index,3]), 'threatened birds')
        print(math.floor(threatened_species[country_index,4]), 'threatened mammals')
        print()

    elif user_input2 == '2':                                                                                                                                                                                                                            #If the user inputs '2' for the second input, they are returned with the population change form 2017-2020, the current population density of their desired country and the total threatened species density to compare
        input_area = int(country_data[country_index,3])                                                                                                                                                                                                 #Area of inputted country from country data array
        current_pop_density = pop_2020 / input_area                                                                                                                                                                                                     #Calculating current population density by dividing current pop and area (people per square km)
        format_current_pop_density = "{:.6f}".format(current_pop_density)
        change_pop_percent = (((pop_2020 - pop_2017)/pop_2017)*100)                                                                                                                                                                                     #Calculating percent change in population of the desired country from 2017 to 2020
        format_change_pop_percent = str("{:.2f}".format(change_pop_percent))
        print(f'The change in population from 2017 to 2020 in', user_input1, 'is', format_change_pop_percent + '%')                                                                                                                                     #Printing percent change in population of desired country to output
        
        print('The current population density in', user_input1, 'is',format_current_pop_density,'people per square kilometer')                                                                                                                          #Printing current population density to output

        input_total_species = math.floor(threatened_species[country_index,1] + threatened_species[country_index,2] + threatened_species[country_index,3] + threatened_species[country_index,4])                                                         #Adding together all of the threatened species to get total threatened species
        total_species_density = input_total_species / input_area                                                                                                                                                                                        #Calculating total threatened species density by dividing total species and area of country (threatened species per square km)
        format_total_species_density = "{:.8f}".format(total_species_density)
        print('The total amount of threatened species in', user_input1,'is', format_total_species_density,'species per square kilometer')                                                                                                               #Printing total threatened species density to output

        print()


    elif user_input2 == '3':                                                                                                                                                                                                                            #If the user inputs '3' for the second input, they are returned with the total amount of threatened species, and also the max and min threatened species for their desired country

        max_species = math.floor(np.nanmax(threatened_species[country_index]))                                                                                                                                                                          #Calculating max threatened species using numpy method nanmax (to ignore any nans) using the threatened species array
        if max_species == threatened_species[country_index,1]:                                                                                                                                                                                          #If max in column 1, the species name is plants
            species_1 = 'Plants'
        elif max_species == threatened_species[country_index,2]:                                                                                                                                                                                        #If max in column 2, the species name is fish
            species_1 = 'Fish'
        elif max_species == threatened_species[country_index,3]:                                                                                                                                                                                        #If max in column 3, the species name is birds
            species_1 = 'Birds'
        elif max_species == threatened_species[country_index,4]:                                                                                                                                                                                        #If max in column 4, the species name is mammals
            species_1 = 'Mammals'


        min_species = math.floor(np.nanmin(threatened_species[country_index]))                                                                                                                                                                          #Calculating min threatened species using numpy method nanmin (to ignore any nans) using the threatened species array
        if min_species == threatened_species[country_index,1]:                                                                                                                                                                                          #If min in column 1, the species name is plants
            species_2 = 'Plants'
        elif min_species == threatened_species[country_index,2]:                                                                                                                                                                                        #If min in column 2, the species name is fish
            species_2 = 'Fish'
        elif min_species == threatened_species[country_index,3]:                                                                                                                                                                                        #If min in column 3, the species name is birds
            species_2 = 'Birds'
        elif min_species == threatened_species[country_index,4]:                                                                                                                                                                                        #If min in column 4, the species name is mammals
            species_2 = 'Mammals'
        
      
        input_total_species = math.floor(threatened_species[country_index,1] + threatened_species[country_index,2] + threatened_species[country_index,3] + threatened_species[country_index,4])                                                         #Calculating total threatened species by adding them all together from threatened species array
        print('In', user_input1, 'there are a total of', input_total_species, 'threatened species.')                                                                                                                                                    #Print total threatened species to output
        print('This includes a maximum threatened species of', max_species, species_1, 'and a minimum threatened species of', min_species, species_2)                                                                                                   #Print max and min threatened species to output
        print()


    #matplotlib plots

    #density of each threatened species 
    input_area = int(country_data[country_index,3])                                                                                                                                                                                                                                      #Area of inputted country from country data array
    x_axis1 = ['Plants', 'Fish', 'Birds', 'Mammals']                                                                                                                                                                                                                                     #Plot 1 has an x axis of each threatened species
    plt.bar(x_axis1,[((threatened_species[country_index,1])/input_area), ((threatened_species[country_index,2])/input_area), ((threatened_species[country_index,3])/input_area), ((threatened_species[country_index,4])/input_area)], color = ['blue'], label = user_input1)             #bar plot of density of each threatened species. blue bars labeled with the desired country
    plt.xlabel('Threatened Species')                                                                                                                                                                                                                                                     #The label of the x axis is 'Threatened Species'
    plt.ylabel('Density (species per sq km)')                                                                                                                                                                                                                                            #The label of the y axis is 'Density (species per sq km)'
    plt.title('Density of Each Threatened Species')                                                                                                                                                                                                                                      #The title of the plot is 'Density of Each Threatened Species'
    plt.legend(shadow=True, loc="upper right")                                                                                                                                                                                                                                            #The legend of this plot is in the upper right corner
    plt.show()                                                                                                                                                                                                                                                                           #Showing the plot of density of each threatened species to output

  

    #population density over that last 4 years 
    x_axis2 = [2017, 2018, 2019, 2020]                                                                                                                                                                                                                                                   #Plot 2 has an x axis of the past 4 years, 2017, 2018, 2019, and 2020                                  
    plt.plot(x_axis2, [(pop_2017/input_area), (pop_2018/input_area), (pop_2019/input_area), (pop_2020/input_area)], 'r-', label = user_input1)                                                                                                                                           #Plot of density of the population of the desired country in each set year, red solid line, labelled the users desired country
    plt.xlabel('Past Four Years')                                                                                                                                                                                                                                                        #The label of the x axis is 'Past Four Years'
    plt.ylabel('Density (people per sq km)')                                                                                                                                                                                                                                             #The label of the y axis is 'Density (people per sq km)'
    plt.title('Population Density in the Last Four Years')                                                                                                                                                                                                                               #The title of the plot is 'Population Density in the Last Four Years'            
    plt.xticks(np.arange(2017,2021,1))                                                                                                                                                                                                                                                   #This ensures the x axis of this subplot shows only the years 2017 to 2020, (with a jump of 1) and no extra decimal values in between
    plt.legend(shadow=True, loc="upper left")                                                                                                                                                                                                                                            #The legend of this plot is in the upper left corner
    plt.show()                                                                                                                                                                                                                                                                           #Showing the plot of population density for the past 4 years to output

    print_end_message(user_input1,countries_list,user_input2, valid_list)                                                                                                                                                                               #Once the plots are shown, the end message function is called to print the end message to the output
    


if __name__ == '__main__':                                                                                                                                                     
    main()                                                                                                                                                                                                                                              #The main function is called to begin the program

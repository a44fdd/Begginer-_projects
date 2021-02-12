import matplotlib.pyplot as plt

'''Temperature graphics'''
# nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
# nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
# nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
# months = range(1,13)

# plt.title("Temprature NYC")
# plt.xlabel("months")
# plt.ylabel("Temperature")
# plt.plot(months,nyc_temp_2000,months,nyc_temp_2006,months,nyc_temp_2012)
# plt.legend([2000,2006,2012])
# plt.axis(ymin = 30)
# plt.axis(xmin = 1)
# plt.show()

'''Graphic'''
# def create_graph():
#     x_numbers = [1,2,3]
#     y_numbers = [2,4,6]
#     plt.plot(x_numbers, y_numbers)
#     plt.show()
# if __name__ == "__main__":
#     create_graph()

'''Newton Universal Gravitation Law'''
def draw_graph(x,y):
    plt.plot(x,y,marker="o")
    plt.xlabel("Distance in meters")
    plt.ylabel("Gravitational force in newtons")
    plt.title("Gravitational force and distance")
    plt.show()

# def generate_F_r():
    #Range r
    # r = range(100,1001,50)
    #List that save the values of F
    # F = []

    '''Constants and values'''
    '''Gravity constant'''
    # G = 6.674 * (10**-11)

    '''Mass'''
    # m1 = 0.5
    # m2 = 1.5

    '''Calculate with the formula and add tho the list'''
    # for distance in r:
        # N = (G*m1*m2)/(distance**2) 
        # F.append(N)
    
    # draw_graph(r,F)
# if __name__ == "__main__":
    # generate_F_r()
        

'''Use the data to create two lists in your program and to create a
graph with the time of day on the x-axis and the corresponding temperature
on the y-axis. The graph should tell you how the temperature varies
with the time of day. Try a different city and see how the two cities compare
by plotting both lines on the same graph
'''
#Values

hours = range(10,23,3)# x-axis is determined by the next 12 hours, the will creatde at 11:00 a.m
toluca_tempt = [18,21,21,13,9]
querétaro_tempt = [22,26,27,22,17]

# #Graph
plt.title('Temperature in Toluca and Queretaro')
plt.xlabel('Hours since 11 am')
plt.ylabel('Temperature')
plt.axis(xmin=11)
plt.axis(xmax=23)
plt.axis(ymin=4)
plt.axis(ymax=30)
plt.plot(hours,toluca_tempt,hours,querétaro_tempt)
plt.legend(['Toluca','Queretaro'])
plt.show()

'''
You’ll write a program that creates a bar chart for
easy comparison of weekly expenditures. The program should first ask for
the number of categories for the expenditures and the weekly total expenditure
in each category, and then it should create the bar chart showing
these expenditures.
'''
'''Categories'''

# num_categories =  int(input('How categories you want to create?'))
# categories_list = []
# expenditure_list = []
# for i in range(num_categories):
#     name_categorie = input('Enter category:')
#     categories_list += [name_categorie]
#     expenditure = int(input('Expenditure:'))
#     expenditure_list += [expenditure]


# plt.title('Expenditure in a month')
# plt.xlabel('Category')
# plt.ylabel('Expend')
# plt.bar(categories_list,expenditure_list)
# plt.show()

'''
Finding the median 
'''
# def calculate_median(numbers):
#     N = len(numbers)
#     numbers.sort()
#     # Find the median
#     if N % 2 == 0:
#         # if N is even
#         m1 = N/2
#         m2 = (N/2) + 1
#         # Convert to integer, match position
#         m1 = int(m1) - 1
#         m2 = int(m2) - 1
#         median = (numbers[m1] + numbers[m2])/2
#     else:
#         m = (N+1)/2
#         # Convert to integer, match position
#         m = int(m) - 1
#         median = numbers[m]
#         return median
# if __name__ == '__main__':
#     donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
#     median = calculate_median(donations)
#     N = len(donations)
#     print('Median donation over the last {0} days is {1}'.format(N, median))


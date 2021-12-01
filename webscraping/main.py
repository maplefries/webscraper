from bs4 import BeautifulSoup

with open('webscraping/home.html', 'r') as html_file: #opening the scraper as a file
        content = html_file.read() 
        

        soup = BeautifulSoup(content, 'lxml') # a way for formatting the content 

        course_cards = soup.find_all('div',class_= 'card' )
        for course in course_cards:
                course_name = course.h5.text
                course_price = course.a.text.split()[-1]

                print(f'{course_name} costs {course_price}')
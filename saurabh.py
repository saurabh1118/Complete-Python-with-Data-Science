print('''This modle is created by Saurabh Chaudhary
For more updates : Follow >>🔎 www.saurabh-chaudhary.com''')


# Function 1
def say_hello():
    print('Hello world!!')

# Function 2
def greet(name):
    import random
    all_msg = ['hello','Hii','Welcome','Hey!','WhatsUp']

    start = random.choice(all_msg)
    final_msg = f'{start} {name}, How are You ?'
    return final_msg

# Function 3
def greet_person(name):
    import random
    all_msg = ['hello','Hii','Welcome','Hey!','WhatsUp']

    first_msg= random.choice(all_msg) 

    # print(first_msg)
    last_all_msg =  [
    "How's it going?",
    "How are you doing?",
    "What's up?",
    "How are things?",
    "How have you been?",
    "How's everything?",
    "How's life treating you?",
    "What's good?",
    "How's your day going?",
    "How are things with you?"]

    last_msg = random.choice(last_all_msg)

    final_msg =f'{first_msg} {name} , {last_msg}'
    
    return final_msg

# Function 4
def check_prime(number):
    '''This is a check prime fuction , return True If number is Prime otherwise return False
    eg.
    check_prime(22)>>False
    check_prime(23)>>True'''
    for i in range(2,number):
        if number % i == 0:
            return False
            break
        else:
            return True

# Function 5
def fibbonacci(number):
    fibo=[0,1]
    for i in range(number-2):
        last_element=fibo[-1]
        second_last_element=fibo[-2]
        next_element = last_element+second_last_element
        fibo.append(next_element)

    return fibo

# Function 6
def check_anagram(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    
    word1_dict = {}
    word2_dict = {}
    for i in word1:
        word1_dict[i]=word1.count(i)

    for i in word2:
        word2_dict[i]=word2.count(i)

    if word1_dict == word2_dict:
        print('Anagram')
    else:
        print('NOt Anagram')

# Function 7
def check_year(year):
    if (year % 4 ==0 and year % 100 !=0 )or( year%400 ==0):
        return True
    else:
        return False

#Function 8
def chatbot():

    customer_query_database = {'Name':[],'Ticket ID':[], 'Customer_concerns':[],'Query':[],'Ticket_date':[]} 
    import random 
    import time

    customer_name = input('Enter name : ')
    customer_query_database['Name'].append(customer_name)
    print(greet_person(customer_name))
    time.sleep(2)

    print('Connecting with our customer care wait!!',end='')
    for i in range(5):
        print('.',end='')
        time.sleep(1)

    customer_care_names = ["Aarav Kumar","Priya Sharma","Vikram Singh","Ananya Gupta","Rajesh Reddy","Neha Patel","Kunal Verma","Sneha Iyer"]

    active_customer = random.choice(customer_care_names)

    greetings_message = [
    "Hello! How can I assist you today?",
    "Good day! How can we help you?",
    "Hi there! Thank you for reaching out. How may I assist you?",
    "Welcome! How can I make your experience better today?",
    "Greetings! How can I assist you with your concerns?",
    "Good morning/afternoon/evening! How can I help you today?",
    "Thank you for contacting us! What can we do for you?",
    "Hello and welcome! How may I assist you with your query?",
    "Hi! Let me know how I can assist you today.",
    "Welcome! How can I be of service to you today?"
    ]
    customer_care_msg = random.choice(greetings_message)

    print(f"\nHello I'm {active_customer} ", end='')
    for i in range(3):
        print('.',end='')
        time.sleep(1)

    print('\n'+customer_care_msg)

    customer_concerns = {
                        "Technical Issues": [
                            "Difficulty logging in to the platform",
                            "Issues with video playback or audio quality",
                            "Inability to access certain course materials",
                            "App crashes or freezes during use",
                            "Problems with content loading or buffering"
                        ],
                        
                        "Account & Billing": [
                            "Issues with subscription or payment processing",
                            "Questions regarding refund policy",
                            "Billing discrepancies or overcharging",
                            "Difficulty updating payment information",
                            "Account suspension or deactivation issues"
                        ],
                        
                        "Course Content & Quality": [
                            "Requests for more detailed or advanced course material",
                            "Issues with the course layout or design",
                            "Desire for more interactive learning methods",
                            "Confusion about course prerequisites or requirements",
                            "Complaints about outdated or inaccurate content"
                        ],
                        
                        "Customer Support & Service": [
                            "Delayed responses from customer support",
                            "Difficulty reaching a representative or live chat issue",
                            "Lack of personalized assistance or guidance",
                            "Unresolved inquiries or support tickets",
                            "Negative experience with a support representative"
                        ],
                        
                        "Platform Usability & Features": [
                            "Difficulty navigating the platform interface",
                            "Missing or non-functional features (e.g., bookmarking, progress tracking)",
                            "Suggestions for new features or improvements",
                            "Mobile app usability concerns",
                            "Requests for language or accessibility options"
                        ]
                    }

    print('select your concern: ')
    for index , key in enumerate(customer_concerns):
        print(f'{index+1}. {key}')

    concern_input = int(input('Enter value here : '))
    time.sleep(2)
    if 1<=concern_input<=5:
        concern_topic = list(customer_concerns)[concern_input-1]
        customer_query_database['Customer_concerns'].append(concern_topic)

        for ix,msg in enumerate(customer_concerns[concern_topic]):
            print(f' {ix+1}.{msg}')

        query_input = int(input('Select value here: '))
        query_msg = customer_concerns[concern_topic][query_input-1]
        customer_query_database['Query'].append(query_msg)

        if 1<=query_input<=5:
            all_closing_msg = [
                 "Thank you for reaching out! Let us know if you need further help.",
                "We’re happy to assist you! Feel free to contact us anytime.",
                "Thanks for your time! We’re here if you need anything else.",
                "Your satisfaction matters! Don’t hesitate to reach out again.",
                "It was a pleasure helping you! Have a great day ahead!"
            ]
    
            final_closing_msg = random.choice(all_closing_msg)
            time.sleep(2)
            print("😊"+final_closing_msg+"😊")
            ticket_id = 'G'+str(random.randint(11111111,99999999))+'T'
    
            print(f'''Save this ticket ID for ref : 
            ticket_id : {ticket_id}''')
    
            customer_query_database['Ticket ID'].append(ticket_id)
            customer_query_database['Ticket_date'].append(time.asctime())
        else:
            print('Invalid Input')

    else:
        print('Invalid Input')
    display(clear = True)    
        
# Function 9
def star_print(n,star_type=None):
    if star_type == None:
        print('Pass Star type')
    else:
        if star_type.lower() == 'left':
            space =''
        elif star_type.lower() == 'mid':
            space = ' '
        elif star_type.lower() == 'right':
            space = '  '
        else:
            space = ' '
        for i in range(1,n+1):
            #for spaces
            for j in range(n-i):
                print(space,end ='')
                #for * print
            for k in range(1,i+1):
                print('*',end=' ')
            print()
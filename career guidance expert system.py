#Rule Based Algorithm
def get_yes_no(question):
    ans = input(question + " (yes/no): ").strip().lower()
    return ans == "yes"


def career_guidance():
    print("*********************************************")
    print("         Career Guidance Expert System       ")
    print("*********************************************\n")

    enjoys_math = get_yes_no("Do you enjoy solving math problems?")
    loves_technology = get_yes_no("Are you interested in technology or computers?")
    enjoys_helping = get_yes_no("Do you enjoy helping people?")
    creative_thinker = get_yes_no("Do you consider yourself creative?")
    likes_business = get_yes_no("Are you interested in business or marketing?")
    loves_outdoors = get_yes_no("Do you enjoy working outdoors?")
    good_communication = get_yes_no("Do you have good communication skills?")
    detail_oriented = get_yes_no("Do you pay close attention to details?")

   
    if enjoys_math and loves_technology and detail_oriented:
        print("\n Recommended Career: Software Engineer or Data Analyst")
    elif enjoys_helping and good_communication:
        print("\n Recommended Career: Teacher, Nurse, or Counselor")
    elif creative_thinker and likes_business:
        print("\n Recommended Career: Marketing Manager or Entrepreneur")
    elif loves_outdoors and not loves_technology:
        print("\n Recommended Career: Environmental Scientist or Agriculture Expert")
    elif enjoys_math and likes_business:
        print("\n Recommended Career: Accountant or Financial Analyst")
    elif creative_thinker and not enjoys_math:
        print("\n Recommended Career: Graphic Designer or Writer")
    elif loves_technology and not enjoys_math:
        print("\n Recommended Career: IT Support Specialist or Web Designer")
    else:
        print("\n You have a diverse skill set! Explore different fields through internships or courses.")

    print("\n*********************************************")
    print(" Thank you for using the Career Guidance System!")
    print("*********************************************")


if __name__ == "__main__":
    career_guidance()

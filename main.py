def main():
    ans = input("What can I help you with today? :)\n")
    
    help = "help"
    prereq = "prerequisites"
    courses = "courses"
    stat = "stat"
    advisor = "advisor"
    appointment = "appointment"
    work = "work"
    job = "job"
    nothing = "nothing"
    nothing2 = "Nothing"
    true = 0
    
    while true == 0:
    
        if courses in ans:
            from coursesAvail import coursesAvail
            coursesAvail()
        #elif work in ans or job in ans:
            #job funtion
        #elif stat in ans:
            #stat func
        #elif advisor in ans or appointment in ans:
            #apointmet func
        #elif prereq in ans:
            #prereq func
        else:
            from getHelp import get_help
            get_help()
            
        ans = input("What else can I help you with?\n")
        if nothing in ans or nothing2 in ans:
            print("Thank you for talking with me, I hope this was helpful!")
            true = 1

    

main()


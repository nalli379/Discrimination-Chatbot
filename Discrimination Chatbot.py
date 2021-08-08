import webbrowser
import pathlib as p

#how to make caps not important global
#can you reuse a question format 'yes no not sure...' with new inputs each time?

#question user if it discrimination?
def is_it_discrim():

    while True:
        question_discrim = input("Do you think you're experiencing discrimination at work? yes/no/not sure ").lower()
        if question_discrim not in ("y", "yes", "n", "no", "not sure", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if question_discrim == "y" or question_discrim == "yes":
        person = "personal"
        with open("statement.txt", "a") as statement_handler:
            statement_handler.write("Personal Summary")
            statement_handler.write("\n\n")
            statement_handler.close()
        direct_discrim(person)
        what_is_discrim(person)
                  
    elif question_discrim == "n" or question_discrim == "no":
        question_witness()

    elif question_discrim == "not sure":
        need_help_discrim()

    elif question_discrim == "q":
        q()
    

#question if the user needs more information
def need_help_discrim():
    while True:
        need_help = input(f"Do you want to read more about what discrimination is or talk to someone? read/talk ").lower()
        if need_help not in("read", "r", "talk", "t", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break

    if need_help == "read" or need_help == "r":
        person = "learner"
        what_is_discrim(person)

    elif need_help == "talk" or need_help == "t":
        help_page()

    elif need_help == "q":
        q()

#info page opens two functions 1. organisations websites 2. access url
def help_page():

    organisations_dict = organisations_dict_funct()
    organisations_dict_url(organisations_dict)

#function creates dictionary
def organisations_dict_funct():
    organisations_dict = {}
    organisations_dict["1"] = "https://www.acas.org.uk/contact"
    organisations_dict["2"] = "http://www.equalityadvisoryservice.com/"
    organisations_dict["3"] = "https://www.citizensadvice.org.uk/about-us/contact-us/contact-us/contact-us/"

    print("You can contact any of these organisations for advice and information on discrimination and equality rights and responsibilities.\n 1. ACAS \n 2. Equality Advisory Support Service\n 3. Citizens Advice Bureau")
    
    return organisations_dict

#open organisations web page
def organisations_dict_url(organisations_dict):

    while True:
        select_organisation = input("Select either 1, 2 or 3 to open the organisation's website. ")
        if select_organisation not in("1", "2", "3", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if select_organisation == "q":
        q()
    
    else:
        organisation_url = organisations_dict.get(select_organisation)
        webpage = webbrowser.open_new(f"{organisation_url}")
        help_page_repeat(organisations_dict)


#loop help page to open multiple urls to organisations
def help_page_repeat(organisations_dict):
    while True:
        repeat = input("Do you want to open another organisation's website? yes/no ").lower()
        if repeat not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if repeat == "y" or repeat == "yes":
        organisations_dict_url(organisations_dict)

    elif repeat == "n" or repeat == "no":
        q()

    elif repeat == "q":
        q()  

#question if the user is witness to discrimination
def question_witness():
    while True:
        question_witness = input("Are you talking about a friend, relative or colleague who you think is experiencing discrimination or harassment at work? yes/no ").lower()
        if question_witness not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    if question_witness == "y" or question_witness == "yes":
        person = "witness"
        with open("statement.txt", "a") as statement_handler:
            statement_handler.write("Witness Summary")
            statement_handler.write("\n\n")
            statement_handler.close()
        what_is_discrim(person)

    elif question_witness == "n" or question_witness == "no":
        help_page()

    elif question_witness == "q":
        q()

#describe discrimination in equality law based on protected characteristics
#work on this statement!!
def what_is_discrim(person):
    print("Discrimination is when someone is treated unfairly because of who they are.\n\nThe Equality Act 2010 protects anyone who is treated unfairly by a broad range of businesses, services and public bodies including an employer.\n\nThe Act also protects anyone who is discriminated against for being associated (such as a relative or a friend) with someone who has a protected characteristic.\n\nThe nine characteristics protected by law are:\n\n1. age\n2. disability\n3. gender reassignment\n4. marriage or civil partnership\n5. pregnancy and maternity\n6. race\n7. religion or belief\n8. sex\n9. sexual orientation\n")
    print("")
    is_it_protected_charac(person)

#establish if discrim is against protected characteristics
def is_it_protected_charac(person):

    #adapt question based on if user is talking about personal situation, witness for someone else or a learner
    if person == "personal":
        person_pc_input = "you are experiencing"
        pc_space  = " "

    elif person == "witness":
        person_pc_input = "you are witnessing"
        pc_space = " "
    
    elif person == "learner":
        person_pc_input = "this"
        pc_space = " is "
    
    while True:
        #are you experiencing discrim on personal charac, depending on whether witness, personal, learner then need to switch person questions
        protected_charac = input(f"Do you think {person_pc_input} discrimination{pc_space}against one or more of the protected characteristics? yes/no/not sure ").lower()
        
        if protected_charac not in ("y", "yes", "n", "no", "not sure", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if protected_charac == "y" or protected_charac == "yes":
        which_protected_characs(person)
                  
    elif protected_charac == "n" or protected_charac == "no":
        need_help_protected_charac(person)

    elif protected_charac == "not sure":
        need_help_protected_charac(person)

    elif protected_charac == "q":
        q()


#need more info on discrimination against protected characteristics?
def need_help_protected_charac(person):
    while True:
        need_help_protected_charac_input = input("Do you want to read more about what the protected characteristics, talk to someone or move on? read/talk/move on ").lower()
        if need_help_protected_charac_input not in ("read", "r", "talk", "t", "move on", "m", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if need_help_protected_charac_input == "read" or need_help_protected_charac_input == "r":
        protected_charac_info_page(person)
            
    elif need_help_protected_charac_input == "talk" or need_help_protected_charac_input == "t":
        help_page()
    
    elif need_help_protected_charac_input == "move on" or need_help_protected_charac_input == "m":
        what_is_direct_indirect(person)

    elif need_help_protected_charac_input == "q":
        q()

#info page opens two functions 1. protected characteristics dictionary with url 2. opens urls on each characteristic/eq law
def protected_charac_info_page(person):

    protected_charac_dict = protected_charac_dict_funct()
    protected_charac_url(protected_charac_dict, person)

#creates protected characteristics dictionary using number and urls to characteristics info page and EQ law
def protected_charac_dict_funct():
    protected_charac_dict = {}
    protected_charac_dict["1"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/age-discrimination/"
    protected_charac_dict["2"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/what-counts-as-disability/"
    protected_charac_dict["3"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/gender-reassignment-discrimination/"
    protected_charac_dict["4"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/marriage-and-civil-partnership-discrimination/"
    protected_charac_dict["5"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/what-are-the-different-types-of-discrimination/pregnancy-and-maternity-discrimination/"
    protected_charac_dict["6"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/race-discrimination/"
    protected_charac_dict["7"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/religion-or-belief-discrimination/"
    protected_charac_dict["8"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/sex-discrimination/"
    protected_charac_dict["9"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/protected-characteristics/sexual-orientation-discrimination/"
    
    return protected_charac_dict
    
#opens urls to protected characteristics and EQ law, can be repeated
def protected_charac_url(protected_charac_dict, person):
        
    while True:
        select_protected_charac = input("Enter a number 1 - 9 to open a web page about that protected characteristic. ")
        if select_protected_charac not in("1", "2", "3", "4", "5", "6", "7", "8", "9", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if select_protected_charac == "q":
        q()
    
    else:       
        protected_charac_url = protected_charac_dict.get(select_protected_charac)
        webpage = webbrowser.open_new(f"{protected_charac_url}")
        protected_charac_info_page_repeat(protected_charac_dict, person)

#loop help page to open multiple urls about protected characteristics
def protected_charac_info_page_repeat(protected_charac_dict, person):
    while True:
        repeat = input("Do you want to open another web page? yes/no ").lower()
        if repeat not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if repeat == "y" or repeat == "yes":
        protected_charac_url(protected_charac_dict, person)

    elif repeat == "n" or repeat == "no":
        which_protected_characs(person)

    elif repeat == "q":
        q()


#which protected characteristics experiencing discrimination function
def which_protected_characs(person):

    #if user is learner skip statement, if user is talking about personal situation or witness, go to statement
    if person == "learner":
        what_is_direct_indirect(person)

    elif person == "personal" or person == "witness":

        #adapt question based on if user is talking about personal situation, witness for someone else or a learner
        if person == "personal":
            which_pc_input = "are you experiencing"
            space = " "

        elif person == "witness":
            which_pc_input = "you are witnessing"
            space = " "
    
        elif person == "learner":
            which_pc_input = "this"
            space = " is "
    
        #will user share information about which pc is being discriminated against?
        while True:
            which_protected_characs_input = input(f"Can you tell me which protected characteristics {which_pc_input} discrimination{space}against? yes/no/not sure ")
            if which_protected_characs_input not in ("y", "yes", "no", "n", "not sure", "q"):
                print("Sorry I didn't understand your answer.")
                continue
            else:
                break
        
        if which_protected_characs_input == "y" or which_protected_characs_input == "yes":
            list_protected_characs(person)

        elif which_protected_characs_input == "n" or which_protected_characs_input == "no":
            print("Discrimination against one or more of the nine protected characteristics is unlawful under the Equalities Act 2010.\n\nWe all have some of these characteristics such as age and sex, so the law protects everyone.")
            need_help_protected_charac(person)

        elif which_protected_characs_input == "not sure":
            protected_charac_info_page(person)

        elif which_protected_characs_input == "q":
            q()


#function to capture 
def list_protected_characs(person):

    #list to capture protected characteristics
    list_protected_characs = []

    #multiple inputs for protected characteristics
    while True:
        list_protected_characs_item = input("List each protected characteristic and press enter, when you're done enter 'd'. ").lower()
        list_protected_characs.append(list_protected_characs_item)
        if list_protected_characs_item in ("d", "done", "q"):
            break

    #remove 'd' or 'done' from list of protected characteristics
    if list_protected_characs_item == "d" or list_protected_characs_item == "done":
        list_protected_characs.remove(list_protected_characs_item)

        #if no entry, loop to check if want to repeat
        if len(list_protected_characs) == 0:
            print("Sorry, I didn't understand your answer.")
            which_protected_characs(person)
        
            
        #if entries made, saves to statement text file
        else:
            with open("statement.txt", "a") as statement_handler:
                statement_handler.write("Protected Characteristics: ")
                for item in list_protected_characs:
                    statement_handler.write("%s, " % item)
                statement_handler.write("\n\n")
                statement_handler.close()

            what_is_direct_indirect(person)
    
    elif list_protected_characs_item == "q":
        q()

#describe direct/indirect discrimination
def what_is_direct_indirect(person):

    print("When someone is treated differently or worse than someone else because of who they are it is direct discrimination.\n\nWhen there are rules or arrangements which apply to everyone but it has a different or worse effect on someone because of who they are, it is indirect discrimination. The arrangements can be formal or informal, it can be a practice, a policy and even a one-off decision.")
    print("")
    is_it_direct_indirect(person)

#establish if discrim is against protected characteristics
def is_it_direct_indirect(person):

    #adapt question based on if user is talking about personal situation, witness for someone else or a learner
    if person == "personal":
        person_d_input = "you are experiencing"

    elif person == "witness":
        person_d_input = "you are witnessing"
    
    elif person == "learner":
        person_d_input = "this is"
    
    while True:
        #are you experiencing discrim on personal charac, depending on whether witness, personal, learner then need to switch person questions
        direct_or_indirect_input = input(f"Do you think {person_d_input} direct or indirect discrimination? direct/indirect/not sure ").lower()
        
        if direct_or_indirect_input not in ("direct", "d", "indirect", "i", "not sure", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if direct_or_indirect_input == "direct" or direct_or_indirect_input == "d":
        with open("statement.txt", "a") as statement_handler:
            statement_handler.write("Type of Discrimination: Direct")
            statement_handler.write("\n\n")
            statement_handler.close()
        direct_discrim(person)
                  
    elif direct_or_indirect_input == "indirect" or direct_or_indirect_input == "i":
        with open("statement.txt", "a") as statement_handler:
            statement_handler.write("Type of Discrimination: Indirect")
            statement_handler.write("\n\n")
            statement_handler.close()
        indirect_discrim(person)

    elif direct_or_indirect_input == "not sure":
        need_help_direct_indirect(person)

    elif direct_or_indirect_input == "q":
        q()

#need more info on direct/indirect discrimination?
def need_help_direct_indirect(person):
    while True:
        need_help_direct_indirect_input = input("Do you want to read more about direct and indirect discrimination, talk to someone or move on? read/talk/move on ").lower()
        if need_help_direct_indirect_input not in ("read", "r", "talk", "t", "move on", "m", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if need_help_direct_indirect_input == "read" or need_help_direct_indirect_input == "r":
        direct_indirect_info_page(person)
        
    elif need_help_direct_indirect_input == "talk" or need_help_direct_indirect_input == "t":
        help_page()

    elif need_help_direct_indirect_input == "move on" or need_help_direct_indirect_input == "m":
        what_is_evidence(person)

    elif need_help_direct_indirect_input == "q":
        q()

#info page opens two functions 1. protected characteristics dictionary with url 2. opens urls on each characteristic/eq law
def direct_indirect_info_page(person):
    direct_indirect_dict = direct_indirect_dict_funct()
    direct_indirect_url(direct_indirect_dict, person)

#creates protected characteristics dictionary using number and urls to characteristics info page and EQ law
def direct_indirect_dict_funct():
    direct_indirect_dict = {}
    direct_indirect_dict["1"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/what-are-the-different-types-of-discrimination/direct-discrimination/"
    direct_indirect_dict["2"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/what-are-the-different-types-of-discrimination/indirect-discrimination/"
   
    print("1. Direct discrimination\n2. Indirect discrimination")
    return direct_indirect_dict
    
#opens urls to protected characteristics and EQ law, can be repeated
def direct_indirect_url(direct_indirect_dict, person):
        
    while True:
        direct_indirect_input = input("Enter a number 1 - 2 to open a web page about direct or indirect discrimination. ")
        if direct_indirect_input not in("1", "2", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if direct_indirect_input == "q":
        q()
    
    else:       
        direct_indirect_url = direct_indirect_dict.get(direct_indirect_input)
        webpage = webbrowser.open_new(f"{direct_indirect_url}")
        direct_indirect_info_page_repeat(direct_indirect_dict, person)

#loop help page to open multiple urls about protected characteristics
def direct_indirect_info_page_repeat(direct_indirect_dict, person):
    while True:
        repeat = input("Do you want to open another web page? yes/no ").lower()
        if repeat not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if repeat == "y" or repeat == "yes":
        direct_indirect_url(direct_indirect_dict, person)

    elif repeat == "n" or repeat == "no":
        is_it_direct_indirect(person)

    elif repeat == "q":
        q()

def direct_discrim(person):
    print("It doesn't matter if the person treating someone unfairly didn't know or didn't mean to discriminate against them.\n\nIt is unlawful discrimination if someone is treated differently and worse because of who they are.\n\nHowever, they need to compare their treatment with the treatment of someone else who doesn't have the same protected characteristic to show it is direct discrimination.")
    print("")
    who_direct_discrim(person)


def indirect_discrim(person):
    print("Although the law protects anyone who is treated unfairly because of who they are, if the person applying the rules or arrangements can show a good enough reason for it, it may not be indirect discrimination.\n\nSomeone can only challenge rules or arrangements which they think are indirectly discriminatory when it affects them personally (and other people who share their protected characteristic).\n\nThey will also need to show that other people are not disadvantaged by the same rules or arrangements.")
    print("")
    need_help_direct_indirect(person)

#who are responsible for direct discrimination
def who_direct_discrim(person):
    
    #if user is learner skip statement, if user is talking about personal situation or witness, go to statement, if learner go direct to collecting evidence info
    if person == "learner":
        what_is_evidence(person)

    elif person == "personal" or person == "witness":
        
        if person == "personal":
            direct_discrim_input = "you"
        
        elif person == "witness":
            direct_discrim_input = "someone you know"
        
        #can user list titles of people responsible for discrimination
        while True:
            who_direct_discrim_input = input(f"Can you tell me who is directly discriminating against {direct_discrim_input}? yes/no ").lower()
        
            if who_direct_discrim_input not in ("y", "yes", "no", "n", "q"):
                print("Sorry I didn't understand your answer.")
                continue
            else:
                break

        if who_direct_discrim_input == "y" or who_direct_discrim_input == "yes":
            list_direct_discrim(person)

        elif who_direct_discrim_input == "n" or who_direct_discrim_input == "no":
            what_is_evidence(person)
        
        elif who_direct_discrim_input == "q":
            q()

#function to capture titles if employees responsible for direct discrimination
def list_direct_discrim(person):
    
    #list to capture titles of people responsible for direct discrimination
    list_discrim_titles = []

    #multiple inputs for titles
    while True:
        list_discrim_item = input("List each person's job title and press enter, when you're done enter 'd'. ").lower()
        list_discrim_titles.append(list_discrim_item)
        if list_discrim_item in ("d", "done", "q"):
            break

    #list of titles saved to file
    if list_discrim_item == "d" or list_discrim_item == "done":
        list_discrim_titles.remove(list_discrim_item)

        #if no entry loops to check if want to repeat?
        if len(list_discrim_titles) == 0:
            print("Sorry, I didn't understand what you wrote.")
            who_direct_discrim(person)

        #if entries noted, saves to text.
        else:
            with open("statement.txt", "a") as statement_handler:
                statement_handler.write("Employees Involved: ")
                for item in list_discrim_titles:
                    statement_handler.write("%s, " % item)
                statement_handler.write("\n\n")
                statement_handler.close()
        
            what_is_evidence(person)

    elif list_discrim_item == "q":
        q()

def what_is_evidence(person):
    print("I hope you're feeling more informed about what discrimination at work is. Next, it's all about taking action. First, let's talk about gathering evidence in order to make a claim to an employer.\n\nEvidence can be any type of document such as emails, letters, photos, video, social media, personal notes describing what happened, a witness's version of events...\n\nBasically, anything that helps to describe the situation.\n\nAt this point, it's worth checking if the employer has done everything their supposed to do - have a read through their policy on issues such as bullying and equal opportunities.\n\nRemember, if you want to finish our conversation, press 'q'.")
    print("")

    #adapt direction based on if user is talking about personal, witness or learner
    if person == "personal":
        is_there_evidence(person)

    elif person == "witness":
        is_there_evidence(person)

    elif person == "learner":
        need_help_evidence(person)


#question user is there evidence of discrimination?
def is_there_evidence(person):
    
    #adapt question based on if user is talking about personal, witness or learner
    if person == "personal":
        evidence_input = "Do you have"
        evidence_input_2 = "you are"

    elif person == "witness":
        evidence_input = "Is there"
        evidence_input_2 = "someone you know is"
    
    while True:   
        #question user if there is evidence?
        is_there_evidence_input = input(f"{evidence_input} any evidence to show that {evidence_input_2} being discriminated against? yes/no/not sure ").lower()
        
        if is_there_evidence_input not in ("y", "yes", "n", "no", "not sure", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if is_there_evidence_input == "y" or is_there_evidence_input == "yes":
        share_evidence(person)
                  
    elif is_there_evidence_input == "n" or is_there_evidence_input == "no":
        need_help_evidence(person)

    elif is_there_evidence_input == "not sure":
        need_help_evidence(person)

    elif is_there_evidence_input == "q":
        q()

#does user need more info to understand what is evidence gathering
def need_help_evidence(person):
    while True:
        need_help_evidence_input = input(f"Do you want to read more about how to gather evidence for a discrimination claim, talk to someone or move on? read/talk/move on ").lower()
        if need_help_evidence_input not in("read", "r", "talk", "t", "move on", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break

    if need_help_evidence_input == "read" or need_help_evidence_input == "r":
        evidence_info_page(person)

    elif need_help_evidence_input == "talk" or need_help_evidence_input == "t":
        help_page()
    
    elif need_help_evidence_input == "move on":
        taking_action(person)

    elif need_help_evidence_input == "q":
        q()


#function input what evidence?
def share_evidence(person):

    #if user is talking about personal situation or witness, go to statement
    if person == "personal":
        person_evidence_input = "you have"
        person_evidence_input_2 = "your"

    elif person == "witness":
        person_evidence_input = "someone you know has"
        person_evidence_input_2 = "their"
    
    #will user share information about available evidence
    while True:
        share_evidence_input = input(f"Can you tell me about the evidence {person_evidence_input} that describes {person_evidence_input_2} situation? yes/no/not sure ").lower()
        if share_evidence_input not in ("y", "yes", "no", "n", "q"):

            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
        
    if share_evidence_input == "y" or share_evidence_input == "yes":
        list_evidence(person)
        
    elif share_evidence_input == "n" or share_evidence_input == "no":
        taking_action(person)
        
    elif share_evidence_input == "q":
        q()


#function to capture evidence
def list_evidence(person):

    #list to capture evidence items
    list_types_evidence = []

    #multiple inputs for different evidence types
    while True:
        list_types_evidence_item = input("List each type of evidence there is and press enter, when you're done enter 'd'. ").lower()
        list_types_evidence.append(list_types_evidence_item)
        if list_types_evidence_item in ("d", "done", "q"):
            break
        else:
            continue

    #remove 'd' or 'done' from list of evidence
    if list_types_evidence_item == "d" or list_types_evidence_item == "done":
        list_types_evidence.remove(list_types_evidence_item)

        #if no entry, loop to check if wnat to repeat
        if len(list_types_evidence) == 0:
            print("Sorry I didn't understand your answer.")
            share_evidence(person)

        else:
            with open("statement.txt", "a") as statement_handler:
                statement_handler.write("Types of Evidence: ")
                for item in list_types_evidence:
                    statement_handler.write("%s, " % item)
                statement_handler.write("\n\n")
                statement_handler.close()

                taking_action(person)
    

    elif list_types_evidence_item == "q":
        q()


#what kind of info required for evidence gathering. info page opens two functions 1. sources on gathering evidence with urls 2. opens urls on each page
def evidence_info_page(person):
    evidence_dict = evidence_dict_funct()
    evidence_url(evidence_dict, person)

#function to create dictionary
def evidence_dict_funct():
    evidence_dict = {}
    evidence_dict["1"] = "https://www.citizensadvice.org.uk/work/discrimination-at-work/taking-action/gathering-evidence-about-discrimination-at-work/"
    evidence_dict["2"] = "https://www.equalityhumanrights.com/en/multipage-guide/gathering-evidence-your-complaint"

    print("1. Citizens Advice Bureau\n2. Equality and Human Rights Commission")
    
    return evidence_dict 

#takes dictionary value to open urls to information about evidence gathering 
def evidence_url(evidence_dict, person):

    while True:
        evidence_input = input("Enter a number 1 - 2 to open a web page about gathering evidence from these organisations. ")
        if evidence_input not in("1", "2", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if evidence_input == "q":
        q()
    
    else:
        evidence_url = evidence_dict.get(evidence_input)
        webpage = webbrowser.open_new(f"{evidence_url}")
        evidence_info_page_repeat(evidence_dict, person)

#open another url - refers back to evidence url page or back to evidence help page
def evidence_info_page_repeat(evidence_dict, person):
    while True:
        repeat = input("Do you want to open another web page? yes/no ").lower()
        if repeat not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if repeat == "y" or repeat == "yes":
        evidence_url(evidence_dict, person)
        
    elif repeat == "n" or repeat == "no":
        #if user is talking about personal situation or witness, go to statement, if learner go direct
        if person == "learner":
            need_help_evidence(person)

        elif person == "personal" or person == "witness":
            is_there_evidence(person)

    elif repeat == "q":
        q()


#if the user has input information about their own/someone else's situation this prints the statement or goes to taking action.
def taking_action(person):
    path = p.Path("statement.txt")
    if path.exists() and path.stat().st_size >0:
        retrieve_statement(person)
    else:
        next_steps_action(person)

def retrieve_statement(person):
    print("I've summarised what you've told me in our chat below so that you can refer to it when you need to.\n\n")
    with open("statement.txt") as statement:
        print(statement.read())
    next_steps_action(person)

def next_steps_action(person):
    print("Now it's about deciding on how to take action.\n\nThis can be an informal complaint, a formal complaint (a grievance) or taking legal action.\n\nIt's worth checking the employer's policy on issues such as bullying and harassment to find out the procedure for making a complaint and how it will be managed.\n\nI'd also recommend reading more about taking action and talking to someone about the situation before deciding what to do next...\n\n")
    need_help_action(person)

#what kind of information does the user need to take action - read about it online or talk to someone
def need_help_action(person):
    while True:
        need_help_action_input = input(f"Do you want to read more about taking action, talk to someone or close the app? read/talk/close").lower()
        if need_help_action_input not in("read", "r", "talk", "t", "close", "c", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if need_help_action_input == "read" or need_help_action_input == "r":
        action_info_page(person)
    
    elif need_help_action_input == "talk" or need_help_action_input == "t":
        help_page(person)
    
    elif need_help_action_input == "close" or need_help_action_input == "c":
        q()
    
    elif need_help_action_input == "q":
        q()


#leads to information on taking action. info page opens two functions. 1. sources on different types of action with urls 2. opens urls on each page
def action_info_page(person):
    action_dict = action_dict_funct()
    action_url(action_dict, person)

#function to create dictionary
def action_dict_funct():
    action_dict = {}
    action_dict["1"] = "https://www.citizensadvice.org.uk/work/discrimination-at-work/taking-action/deciding-what-to-do-about-discrimination-at-work/"
    action_dict["2"] = "https://www.citizensadvice.org.uk/work/discrimination-at-work/taking-action/taking-action-about-discrimination-at-work/"
    action_dict["3"] = "https://www.citizensadvice.org.uk/law-and-courts/discrimination/taking-action-about-discrimination/taking-legal-action-about-discrimination/"

    print("1. Deciding what to do\n\n2. Taking action\n\n3. Taking legal action")

    return action_dict

#takes dictionary value to open urls to information about taking action
def action_url(action_dict, person):

    while True:
        action_input = input("Enter a number 1 - 3 to open a web page about taking action. ")
        if action_input not in ("1", "2", "3", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break
    
    if action_input == "q":
        q()
    
    else:
        action_url = action_dict.get(action_input)
        webpage = webbrowser.open_new(f"{action_url}")
        action_info_page_repeat(action_dict, person)


#open another url - refers back to action url page or back to action help page
def action_info_page_repeat(action_dict, person):
    while True:
        repeat = input("Do you want to open another web page? yes/no ").lower()
        if repeat not in ("y", "yes", "n", "no", "q"):
            print("Sorry I didn't understand your answer.")
            continue
        else:
            break

    if repeat == "y" or repeat == "yes":
        action_url(action_dict, person)

    elif repeat == "n" or repeat == "no":
        need_help_action(person)
    
    elif repeat == "q":
        q()
    

#introductory statement
def intro():
    print("Hi, I'm here to talk through with you about what is discrimination at work. I will ask lots of questions and direct you to where you can get information and advice. At any point you want to finish our conversation, press 'q'. Let's start... ")
    print("")
    is_it_discrim()

def q():
    return print("I hope you got the information you need. Thanks for talking with me ")

intro()


def match_people(person, list_people):
    current_match = None

    for people in list_people:
        match_score = 0

        # perffect data
        if people[1].lower() == person[1].lower():
            match_score += 10
        elif people[2].lower() == person[2].lower():
            match_score += 10
        elif people[3].lower() == person[3].lower():
            match_score += 10
        elif people[4].lower() == person[4].lower():
            match_score += 10
        elif people[5].lower() == person[5].lower():
            match_score += 10

        # anomaly

        #### name ####
        people_from_list_names = people[1].split(' ')
        person_names = person[1].split(' ')

        match_score += match_name(person_names, people_from_list_names)

        #### mom name ####
        mom_name_from_list_names = people[2].split(' ')
        mom_name = person[2].split(' ')

        match_score += match_name(mom_name, mom_name_from_list_names)

        #### father name ####
        dad_from_list_names = people[3].split(' ')
        dad_names = person[3].split(' ')

        match_score += match_name(person_names, dad_from_list_names)

        # verify based in score if it is the same people
        if match_score > 30:
            return people

    return None


def match_name(person_names, people_from_list_names):
    match_score = 0
    for name in person_names:
        for to_match_name in people_from_list_names:
            # if it is not an Abbreviation
            if len(name) > 1 and len(to_match_name) > 1:
                if name.lower() == to_match_name.lower():
                    match_score += 5
            elif len(name) == 1:
                # Abbreviation
                if name.lower() == to_match_name[0].lower():
                    match_score += 2
            elif to_match_name.lower() == name[0].lower():
                    match_score += 2

            # Do the match by letter
            letters_name = list(name.lower())
            letter_to_match = list(to_match_name.lower())

            match_letters = list(filter(lambda x : x in letters_name, letter_to_match))
            count = len(match_letters)

            percent = (len(letter_to_match) * 100) / len(letters_name)
            if percent > 75:
                match_score += 5

    return match_score
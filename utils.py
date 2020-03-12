def match_people(person, list_people):
    current_match = None

    for people in list_people:
        match_score = 0
        max_score = 0

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

        max_score += 10

        # anomaly

        #### name ####
        people_from_list_names = people[1].split(' ')
        person_names = person[1].split(' ')

        match_score += match_name(person_names, people_from_list_names)
        max_score = 5 * len(person_names) * len(people_from_list_names)

        #### mom name ####
        mom_name_from_list_names = people[2].split(' ')
        mom_name = person[2].split(' ')

        match_score += match_name(mom_name, mom_name_from_list_names)
        max_score = 5 * len(mom_name) * len(mom_name_from_list_names)

        #### father name ####
        dad_from_list_names = people[3].split(' ')
        dad_names = person[3].split(' ')

        match_score += match_name(dad_names, dad_from_list_names)
        max_score = 5 * len(dad_names) * len(dad_from_list_names)

        import ipdb; ipdb.set_trace()

        # verify based in score if it is the same people
        percent_from_max = (max_score * 86) / 100
        if match_score > percent_from_max:
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
            if percent > 85:
                match_score += 5

    return match_score
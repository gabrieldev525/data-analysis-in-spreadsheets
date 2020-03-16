from constants import WORD_MATCH_SCORE
from constants import ABREVIATION_MATCH_SCORE
from constants import PERCENT_TO_MATCH

def match_people(person, list_people):
    """
        SCORES:
            - For each word match +2 points in the match score
            - For each word with abreviation match +1 point in the match score
    """

    for compare_people in list_people:
        match_score = 0
        max_score = 0

        # perffect data
        # check each name information, name, mother name, father name, genre
        for i in range(1, 4):
            if compare_people[i].lower() == person[i].lower():
                match_score += len(person[1].split(' ')) * WORD_MATCH_SCORE

            max_score += len(person[1].split(' ')) * WORD_MATCH_SCORE

        # anomaly

        # ### name ### #
        people_from_list_names = compare_people[1].split(' ')
        person_names = person[1].split(' ')

        match_result = match_name(person_names, people_from_list_names)
        match_score += match_result[0]
        max_score += match_result[1]

        # ### mom name ### #
        mom_name_from_list_names = compare_people[2].split(' ')
        mom_name = person[2].split(' ')

        match_result = match_name(mom_name, mom_name_from_list_names)
        match_score += match_result[0]
        max_score += match_result[1]

        # ### father name ### #
        dad_from_list_names = compare_people[3].split(' ')
        dad_names = person[3].split(' ')

        match_result = match_name(dad_names, dad_from_list_names)
        match_score += match_result[0]
        max_score += match_result[1]

        # verify based in score if it is the same people
        percent_from_max = (max_score * PERCENT_TO_MATCH) / 100

        if match_score > percent_from_max:
            return compare_people

    return None


def match_name(person_names, people_from_list_names):
    match_score = 0
    max_score = 0

    for name in person_names:
        for to_match_name in people_from_list_names:
            # none is abreviation
            if(len(name) > 1 and len(to_match_name) > 1):
                if name.lower() == to_match_name.lower():
                    match_score += WORD_MATCH_SCORE
                max_score += WORD_MATCH_SCORE

            # the person name is a abreviation
            elif(len(name) == 1 and len(to_match_name) > 1):
                if name.lower() == to_match_name[0].lower():
                    match_score += ABREVIATION_MATCH_SCORE
                max_score += ABREVIATION_MATCH_SCORE

            # the word to compare is a abreviation
            elif(len(name) > 1 and len(to_match_name) == 1):
                if name[0].lower() == to_match_name.lower():
                    match_score += ABREVIATION_MATCH_SCORE
                max_score += ABREVIATION_MATCH_SCORE

            # the words are abreviations
            else:
                if name[0].lower() == to_match_name[0].lower():
                    match_score += ABREVIATION_MATCH_SCORE
                max_score += ABREVIATION_MATCH_SCORE

    return match_score, max_score

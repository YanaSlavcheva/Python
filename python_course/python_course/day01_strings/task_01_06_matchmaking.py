import itertools


people = [
    {
        'name': "Мария",
        'interests': ['пътуване', 'танци', 'плуване', 'кино'],
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': ['мода', 'спортна стрелба', 'четене', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': ['танци', 'покер', 'история', 'софтуер'],
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': ['покер', 'автомобили', 'танци', 'кино'],
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': ['пътуване', 'автомобили', 'плуване', 'баскетбол'],
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': ['плуване', 'покер', 'наука', 'скандинавска поезия'],
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': ['кино', 'лов със соколи', 'пътуване', 'мода'],
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': ['баскетбол', 'автомобили', 'кино', 'наука'],
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': ['автомобили', 'футбол', 'плуване', 'танци'],
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': ['футбол', 'скандинавска поезия', 'история', 'танци'],
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': ['летене', 'баскетбол', 'софтуер', 'наука'],
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': ['футбол', 'лов със соколи', 'автомобили', 'баскетбол'],
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': ['пътуване', 'покер', 'баскетбол', 'лов със соколи'],
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': ['история', 'покер', 'пътуване', 'автомобили'],
        'gender': "male",
    },
]

index_iterator = range(len(people))
list_proper_matches = []


for i,j in itertools.permutations(index_iterator, 2):
    first_person = people[i]
    second_person = people[j]

    if first_person['gender'] != second_person['gender']:
        same_interests = set(first_person['interests']).intersection(second_person['interests'])
        if len(same_interests) > 0:
            pair_indexes_people_that_match = []
            pair_indexes_people_that_match.extend([i, j, same_interests])

            list_proper_matches.append(pair_indexes_people_that_match)

print(list_proper_matches)

for pair in list_proper_matches:
    print(people[pair[0]]['name'] + ' и ' + people[pair[1]]['name'] + ' - общ интерес: ' + ', '.join(pair[2]))

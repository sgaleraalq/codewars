def are_they_acq(dic: dict, prince_id: int, thief_id: int, persons: list, current: int) -> bool:
    for friend in dic[current]:
        if friend == prince_id or friend in persons:
            continue

        if friend in dic[prince_id]:
            continue

        if friend == thief_id:
            return True

        persons.append(friend)
        if are_they_acq(dic, prince_id, thief_id, persons, friend):
            return True
    return False

def find_suspects(data: list, prince_id, thief_id) -> list:
    friends_dict, possible_suspects = {}, []
    for p1, p2 in data:
        friends_dict.setdefault(p1, []).append(p2)
        friends_dict.setdefault(p2, []).append(p1)
    
    if thief_id in friends_dict[prince_id]:
        return sorted(friends_dict[prince_id])
    
    for person in friends_dict[prince_id]:
        if are_they_acq(friends_dict, prince_id, thief_id, [person], person):
            possible_suspects.append(person)
            
    return sorted(possible_suspects)
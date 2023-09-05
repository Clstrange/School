

books_list = []
friends_dict = {}
a = {}

with open('booklist.txt', 'r') as books:
    
    for x in books:
        books_list.append(x.strip())


with open('ratings.txt', 'r') as friends:
    friend = friends.readlines()
    for x in range(0, len(friend), 2):
        friends_dict[friend[x].strip()] = list(map(int, friend[x+1].strip().split(' ')))

        
def friends(user):
    friends_list = list(friends_dict.keys())
    friends_list.remove(user)
    user_value = friends_dict[user]
    affinity = []
    for friend in friends_list:
        dot_product = []
        for i in range(len(friends_dict[friend])):
            dot_product.append(friends_dict[friend][i] * user_value[i])
        affinity.append(sum(dot_product))
    _affinity = affinity[:]
    first_friend = max(_affinity)
    _affinity.remove(first_friend)
    second_friend = max(_affinity)
    friend_one = friends_list[affinity.index(first_friend)]
    friend_two = friends_list[affinity.index(second_friend)]
    return friend_one, friend_two


def recommend(user):
    best_friends = friends(user)
    rec = []
    def sort(rec):
        first_name = rec[0].split(' ')[0]
        last_name = rec[0].split(' ')[-1]
        title = rec[1]
        return last_name, first_name, title
    for i in range(len(friends_dict[best_friends[0]])):
        if friends_dict[best_friends[0]][i] >= 3 and friends_dict[user][i] == 0:
            rec.append(tuple(books_list[i].split(',')))
        if friends_dict[best_friends[1]][i] >= 3 and friends_dict[user][i] == 0:
            rec.append(tuple(books_list[i].split(',')))
    recs = set(rec)
    return sorted(recs, key=sort)


def report():
  lyst = ""
  d = sorted(friends_dict)
  for reader in d:
    friend = friends(reader)
    lyst = '{}\n{}: {}\n'.format(lyst, reader, friend)
    recommendList = recommend(reader)
    for e in recommendList:
      lyst = '{}\t{}\n'.format(lyst, e)
  return lyst


def main():
    reader = input("Enter a reader's name: ")
    if reader in friends_dict:
        print("Recommendations for ", reader, "from ", friends(reader))
        for i in recommend(reader):
            print(i)
    else:
        print("Pleasae try another name...")



if __name__ == "__main__":
    main()


    




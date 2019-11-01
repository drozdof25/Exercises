import math
from collections import Counter
import vk_api
import matplotlib.pyplot as plt
import time
# привести точку данных к номеру интервала
def bucketize(point,bucket_size):
    """ Округлить точку до следующего наименьшего кратного
    размера интервала bucket_size"""
    return bucket_size * math.floor(point/bucket_size)
# подготовить гистограммму
def make_histogram(points,bucket_size):
    """сгрупировать точки и подсчитать количество в интервале"""
    return Counter(bucketize(point,bucket_size) for point in points)
# изобразить гистограмму
def plot_histogram(points,bucket_size,title=""):
    histogram = make_histogram(points,bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width = bucket_size)
    plt.title(title)
    plt.show()

def main():
    login = input('Логин ')
    password = input('Пароль ')
    login, password = login, password
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    i_am = vk.users.get()
    print('Мой id ' + str(i_am[0]['id']))
    friends = vk.friends.get(user_id=i_am[0]['id'])
    print('Количество друзей ' + str(friends['count']))
    friends_data = vk.users.get(user_ids = [index for index in friends['items']],fields = 'bdate')
    years = [2019 - int(friend['bdate'].split('.')[2]) for friend in friends_data
                if 'bdate' in friend.keys()
                if len(friend['bdate'].split('.')) == 3]
    posts_count = []
    for friend in friends_data:
        print(str(100*len(posts_count)/len(years)) + '%')
        if 'bdate' in friend.keys():
            if len(friend['bdate'].split('.')) == 3:
                posts = vk.wall.get(owner_id=friend['id'])
                time.sleep(1/3)
                posts_count.append(posts['count'])
    plot_histogram(years, 1, "Диаграмма возраста друзей")
    plt.scatter(years,posts_count,marker = '.',color = 'green')
    plt.show()
if __name__ == '__main__':
    main()
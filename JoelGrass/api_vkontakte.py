# -*- coding: utf-8 -*-
import vk_api
import time


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
    response = vk.wall.get(count=1)
    last_post_id = 0
    if response['items']:
        last_post_id = response['items'][0]['id']
    # like_last_pos = response.likes.getList
    likers = vk.likes.getList(type = 'post',owner_id = 97091843, item_id = last_post_id)
    for i in range(0,likers['count']):
        print(vk.users.get(user_ids=likers['items'][i]))
if __name__ == '__main__':
    main()
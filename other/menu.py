from modules import vk_friends


def menu(token):
    category = raw_input('Choose category:\n 1 - Friends\n\n')
    if category == "1":
        friends(token)


def friends(token):
    script = raw_input('Choose script:\n 1 - Add all friends\n 2 - Unfollow from all people\n\n')
    if script == "1":
        vk_friends.add_all(token)
    elif script == "2":
        vk_friends.unfollow_all(token)
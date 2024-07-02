from instabot import Bot
bot = Bot()
bot.login(username= "fact fusion", password="fact12fuion@")
bot.follow("aminarana48")
# uploade a photo
bot.upload_photo("C:/Users/Admin/Desktop/Arooj SS/2.png", caption="I LOVE PYTHON")
# unfollow a user
bot.unfollow("aminarana48")
# send msg multiple people
bot.send_message("i love python", ["personal blog", "noorit", "kainat1"])
# geet info of user
follower=bot.get_user_followers("fact fusion")
for follower in follower:
    print(bot.get_user_info(follower))
    # to see following list
    following = bot.get_user_following("fact fusion")
    for Following in following:
        print(bot.get_user_info(following))
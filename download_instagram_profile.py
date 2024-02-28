import instaloader

ig = instaloader.Instaloader()
dp = input("Enter Instagram Username here: ")

ig.download_profile(dp, profile_pic_only=True)

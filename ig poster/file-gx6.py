import time
from instabot import Bot

def login_to_instagram(username, password):
    # Initialize the bot using your Instagram account username and password
    bot = Bot()

    # Attempt to log in
    if bot.login(username=username, password=password, use_cookie=False):
        # Successfully logged in
        print("Logged in successfully.")
        print("User ID:", bot.api.user_id)
        print("Username:", bot.api.username)
        return bot
    else:
        print("Login failed. Check your credentials.")
        return None

def main():
    # Your Instagram account credentials
    username = 'vicwjay'
    password = 'Vitron123'

    # Attempt to log in to Instagram
    bot = login_to_instagram(username, password)

    # Check if login was successful
    if bot:
        # Define the path to the picture and the caption
        picture_path = '/Desktop/ig poster/pics/'
        caption = 'joy 0f kRISMAS.'

        # Define the interval (in seconds) between each posting
        interval = 3600  # 1 hour

        # Define a loop to keep posting pictures
        while True:
            try:
                # Post a picture to your Instagram account
                bot.upload_photo(picture_path, caption=caption)

                # Pause the execution of the code for the specified interval
                time.sleep(interval)

            except Exception as e:
                print(f"Error: {e}")

                # Handle rate limiting by waiting for 5 minutes if a 429 error occurs
                if "429" in str(e):
                    print("Rate limit exceeded. Sleeping for 5 minutes.")
                    time.sleep(300)  # Sleep for 5 minutes to avoid rate limiting

if __name__ == "__main__":
    main()

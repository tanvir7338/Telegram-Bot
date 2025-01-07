# Telegram Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

# Movie and Series Recommendation Function
def get_recommendation(query):
    # Example API for movie info (replace with your source)
    api_url =https://m.ca7i.com/ https://www.mxplayer.in/q={query}"  # Replace with a real API
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        recommendations = [f"{item['title']} ({item['year']})" for item in data['results']]
        return "\n".join(recommendations) or "No recommendations found."
    return "Error fetching recommendations."

# Start Command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! I'm your Movie and Web Series Bot. Send me a movie or series name for recommendations.")

# Recommendation Handler
def recommend(update: Update, context: CallbackContext):
    query = update.message.text
    recommendations = get_recommendation(query)
    update.message.reply_text(recommendations)

def main():
    # Replace 'YOUR_BOT_TOKEN' with the token from BotFather
    updater = Updater( 7987361835:AAGDDKYC97DXLJUARYeldtX4_2ZVjW7108, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, recommend))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

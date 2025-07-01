from telegram import Update
from telegram.ext import Updater, ChatMemberHandler, CallbackContext

TOKEN = "7643190111:AAGvV8Ch0_t2dVk6BfNLRpgTy6KR-UICs1s"
CHANNEL_ID = -1002831436891

def welcome_new_member(update: Update, context: CallbackContext):
    chat_member = update.chat_member
    new_members = chat_member.new_chat_members
    if new_members:
        for member in new_members:
            try:
                context.bot.send_message(
                    chat_id=member.id,
                    text="🎉 Welcome 🤗 to our channel *Estimate Hub*! Enjoy our videos 📷.",
                    parse_mode="Markdown"
                )
                print(f"Welcome sent to {member.username or member.id}")
            except Exception as e:
                print(f"❌ Couldn't message {member.id}: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ChatMemberHandler(welcome_new_member, ChatMemberHandler.CHAT_MEMBER))

    updater.start_polling()
    print("🤖 Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()

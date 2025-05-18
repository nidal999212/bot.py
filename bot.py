from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
TOKEN = '7530759323:AAF7oNowTgos9csp5kgyysQ2FwexkWEIOHs'

# دالة التعامل مع /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("رابط خداع", callback_data="show_facebook")],
        [InlineKeyboardButton("الذهاب إلى بوتي الثاني", url="https://t.me/Hgi6_bot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("اختر أحد الخيارات:", reply_markup=reply_markup)

# دالة التعامل مع الضغط على زر
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "show_facebook":
        await query.message.reply_text("هذا رابط ارسله للضحية وانضر نتيجة حتى تصلك:\nhttps://facebook.com")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(handle_button))

    print("[*] Bot is running...")
    PORT = int(os.environ.get("PORT", 8443))
app.run_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN,
                webhook_url=f"https://YOUR-RAILWAY-APP-NAME.up.railway.app/{TOKEN}")

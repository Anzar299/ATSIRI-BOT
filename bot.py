import os
import random
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ======================
# ENV
# ======================
TOKEN = os.getenv("BOT_TOKEN")

# ======================
# INTENT: TERIMA KASIH
# ======================
THANKS_KEYWORDS = [
    "terima kasih", "terimakasih", "makasih", "makasi",
    "makas", "thanks", "thank you", "trims", "mksh", "tq", "tks", "sami sami"
]

THANKS_RESPONSES = [
    "Baik, terima kasih kembali Aromates 🌿😊",
    "Sama-sama Aromates ✨ Senang bisa membantu 🌸",
    "Dengan senang hati Aromates 🌿 Jika ada yang ingin ditanyakan lagi, silakan yaa 😊",
]

# ======================
# INTENT: EO + KULIT
# ======================
EO_KULIT_KEYWORDS = [
    "essential oil", "eo",
]

KULIT_KEYWORDS = [
    "kulit", "oles", "langsung", "badan", "dipakai", "pakai"
]

EO_KULIT_RESPONSES = [
    (
        "Halo Aromates 🌿\n\n"
        "Essential Oil dari Rumah Atsiri itu 100% *pure* dan sangat terkonsentrasi, "
        "jadi *tidak disarankan digunakan langsung ke kulit* yaa.\n\n"
        "Kalau ingin diaplikasikan ke kulit, "
        "wajib dicampurkan (*diluted*) terlebih dahulu dengan *carrier oil* seperti "
        "jojoba, coconut, atau almond oil 💧✨"
    ),
    (
        "Hai Aromates 😊\n\n"
        "Untuk Essential Oil Rumah Atsiri, karena sifatnya *murni & kuat*, "
        "tidak boleh langsung diaplikasikan ke kulit.\n\n"
        "Solusinya, EO perlu dicampur dulu dengan *carrier oil* agar aman "
        "dan nyaman digunakan 🌿"
    ),
    (
        "Terima kasih sudah bertanya Aromates 🌸\n\n"
        "Essential Oil Rumah Atsiri bersifat *high concentration*, "
        "sehingga tidak bisa digunakan langsung ke kulit.\n\n"
        "Gunakan metode *dilution* dengan carrier oil agar lebih aman yaa ✨"
    ),
]

# ======================
# INTENT: DILUTION
# ======================
DILUTION_KEYWORDS = [
    "DILUTION", "dilution", "diluted",
]

DILUTION_RESPONSES = [
    (
        "Halo Aromates 🌿\n\n"
        "Dilution adalah proses pencampuran minyak Atsiri dengan minyak pembawa atau Carrier Oil"
        "sebelum diaplikasikan ke kulit 💧✨"
    ),
]

# ======================
# INTENT: EO + DIMAKSUD
# ======================
EO_DIMAKSUD_KEYWORDS = [
    "essential oil", "eo",
]

DIMAKSUD_KEYWORDS = [
    "apa yang dimaksud", "itu apa", "apa itu",
]

EO_APAITU_RESPONSES = [
    (
        "Halo Aromates 🌿\n\n"
        "Essential oil atau Minyak atsiri adalah intisari tumbuhan, komponen "
        "kimiawi dengan konsentrasi tinggi dari berbagai bagian tumbuhan. "
        "Setiap minyak atsiri memiliki sifat, manfaat terapi, dan aroma "
        "yang beragam sesuai dengan tanaman aslinya."
    ),
    (
        "Hai Aromates 😊\n\n"
        "Essential oil atau Minyak atsiri adalah intisari tumbuhan, komponen "
        "kimiawi dengan konsentrasi tinggi dari berbagai bagian tumbuhan. "
        "Setiap minyak atsiri memiliki sifat, manfaat terapi, dan aroma "
        "yang beragam sesuai dengan tanaman aslinya."
    ),
    (
        "Terima kasih sudah bertanya Aromates 🌸\n\n"
        "Essential oil atau Minyak atsiri adalah intisari tumbuhan, komponen "
        "kimiawi dengan konsentrasi tinggi dari berbagai bagian tumbuhan. "
        "Setiap minyak atsiri memiliki sifat, manfaat terapi, dan aroma "
        "yang beragam sesuai dengan tanaman aslinya."
    ),
]


# ======================
# COMMAND /start
# ======================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo Aromates 🌿\n"
        "Atmin Rumah Atsiri siap membantu 😊\n\n"
        "Silakan ketik pertanyaan kamu seputar produk ATSIRI yaa ✨"
    )

# ======================
# AUTO REPLY (AI-LIKE)
# ======================
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # ---- INTENT TERIMA KASIH (PRIORITAS) ----
    if any(k in text for k in THANKS_KEYWORDS):
        response = random.choice(THANKS_RESPONSES)
        await update.message.reply_text(response)
        return

    # ---- INTENT EO + KULIT ----
    if (
        any(k in text for k in EO_KULIT_KEYWORDS)
        and any(k in text for k in KULIT_KEYWORDS)
    ):
        response = random.choice(EO_KULIT_RESPONSES)
        await update.message.reply_text(response, parse_mode="Markdown")
        return

         # ---- EO + DIMAKSUD ----
    if (
        any(k in text for k in EO_DIMAKSUD_KEYWORDS)
        and any(k in text for k in DIMAKSUD_KEYWORDS)
    ):
        response = random.choice(EO_APAITU_RESPONSES)
        await update.message.reply_text(response, parse_mode="Markdown")
        return

        # ---- DILUTION ----
    if (
        any(k in text for k in DILUTION_KEYWORDS)
    ):
        response = random.choice(DILUTION_RESPONSES)
        await update.message.reply_text(response, parse_mode="Markdown")
        return
    
    # ---- FALLBACK ----
    await update.message.reply_text(
        "Baik Aromates 🌿\n"
        "Boleh dijelaskan sedikit lagi yaa agar Atmin bisa bantu lebih tepat 😊"
    )

# ======================
# MAIN
# ======================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot ATSIRI AI-like started...")
    app.run_polling()

if __name__ == "__main__":
    main()

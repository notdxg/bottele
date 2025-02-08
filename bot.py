import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Thay YOUR_BOT_TOKEN bằng token bạn nhận từ BotFather
TOKEN = "7270643753:AAEwAgCcOQEMny98_i1-QUzX8IQYJSguNqI"

# Hàm xử lý lệnh /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Chào Bạn! Mình Là Nhân Viên Quản Lý Của CÔNG TY ấn ZALO Cho Đối Tác ✅ Cũng Là Người Phụ Trách Hướng Dẫn CTV Làm Việc ☀️ Các Bạn Hãy Sắp Xếp Thời Gian Làm Việc 1 Cách Hiệu Quả Nhất 🔥 Bạn Có Muốn Làm CTV Bên Mình Không ⚠️\n\nBạn Nạp Vốn 110k Để Vào Nhóm Tiếp Tục Công Việc Nhé, Sau Khi Nạp Bạn Nhận Được Nhiệm Vụ Đầu Có Giá Trị 600k Và Những Ngày Tiếp Làm Nhiệm Vụ Để Nhận Hoa Hồng + Lương.\n- Bạn Hãy Vui Lòng Chuyển Tiền Vào Tài Khoản Do Mình Cung Cấp.\nNgân Hàng MB BANK\nSố Tài Khoản: 99999021099999\nChủ Tài Khoản: NONG TRUNG DUNG \nNội Dung Chuyển Tiền Là Tên Của Bạn.\n⭐ Khi Đã Chuyển Xong Thì Bạn Vui Lòng Chụp Lại Bill Và Gửi Cho Mình Và Gửi Sẵn STK Và Ngân Hàng Của Bạn Luôn Nhé 🔥")
        # Gửi hình ảnh sau khi gửi tin nhắn
    with open(r"c:\Users\Kien Lan\Videos\Captures\9abc6ef5fb55440b1d44.jpg", "rb") as photo:
        await update.message.reply_photo(photo)

# Hàm phản hồi tin nhắn
async def echo(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    await update.message.reply_text(f"Vui lòng hoàn thành nhiệm vụ trên trước để tiếp tục công việc")

# Thiết lập bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Thêm handler cho lệnh /start
    app.add_handler(CommandHandler("start", start))
    # Thêm handler cho tin nhắn
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot đang chạy...")
    app.run_polling()

if __name__ == "__main__":
    main()

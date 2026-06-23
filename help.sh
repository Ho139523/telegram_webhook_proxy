# getMe
curl "https://api.telegram.org/bot<YOUR TELEGRAM BOT TOKEN>/getMe"

# getWebhookInfo
curl "https://api.telegram.org/bot<YOUR TELEGRAM BOT TOKEN>/getWebhookInfo"

# deleteWebhookInfo
curl "https://api.telegram.org/bot<YOUR TELEGRAM BOT TOKEN>/deleteWebhook"

# setWebhook
curl "https://api.telegram.org/bot<YOUR TELEGRAM BOT TOKEN>/setWebhook"   -d '{"url": "https://intellium.ir/telegram"}' -H "Content-Type: application/json"

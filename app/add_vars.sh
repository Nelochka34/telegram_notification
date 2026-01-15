bot_token=$bot_token
netsec_chat=$netsec_chat_id

sed -i "s/add_bot_token/$bot_token/g" ./app/app.py
sed -i "s/add_netsec_chat_id/$netsec_chat/g" ./app/app.py

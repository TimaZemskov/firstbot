#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TOKEN = '1066058140:AAHxkY0lqHt-3yzPMet93MmGA1Ywe9KVxCc'


# In[2]:


from telegram.ext import Updater
updater = Updater(TOKEN, use_context=True) 

# In[ ]:


dispatcher = updater.dispatcher


# In[ ]:


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# In[ ]:


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


# In[ ]:


from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# In[ ]:


updater.start_polling()


# In[ ]:





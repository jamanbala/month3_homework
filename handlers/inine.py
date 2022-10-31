from aiogram import types, Dispatcher

from youtube_search import YoutubeSearch as YT
import hashlib


def finder(text):
    return YT(text, max_results=10).to_dict()




async def inline_google_handlers(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://www.google.com/search?q={text}"
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title="Google: ",
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=f"Держи смотри\n\nhttps://www.google.com/search?q={text}"
        )
    )]
    await query.answer(articles, cache_time=60)



def register_handlers_inline(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_google_handlers)
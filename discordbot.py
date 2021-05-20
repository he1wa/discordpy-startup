from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

#BADWORDS
bad_words = ["綿引", "健太", "エスプール", "spool", "ワタヒキ", "わたひき", "おがわゆうと", "小川悠斗", "清水", "おがわ", "おがゆう", "ゆうと", "ゅうと", "ゅぅと", "ぉがわ", "エスプ"]

#BADWORDSを削除
for bad_word in bad_words:
    if bad_word in message.content:
        await massage.dalete()
        
#実行
loop.start()


bot.run(ODQ0OTI1MzQ5MzA4NTMwNjkx.YKZgDQ.Oc0fxZhfbCWMHA3YspGQlGwCZdI)

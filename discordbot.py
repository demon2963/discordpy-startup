from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#ひらがな五十音のリストを作り、1つランダムに選ぶ
hiraganalist = [chr(i) for i in range(12353, 12436)]
#質問内容になるものをリストにし、1つランダムに選ぶ
wadailist = ["楽しいイベント","丸いもの","怖いもの","名作映画","お金持ちが持っているもの","かわいい生き物","さらりと言えたらかっこいい言葉","彼氏に言われてキュンとくる一言","日本を代表するアイドル","部下に慕われる上司の条件"," 今 流行っているもの","人としてやってはいけない事","日本が世界に誇れるもの","母親がよく言う一言","時代劇でよく聞く言葉","お酒に合うおつまみ","日本の名曲","学校にあるもの","ＯＬが好きな甘い食べ物","デートの後のかっこいい一言","人に言われて傷つく言葉","新婚旅行で行きたい観光スポット","体によさそうなもの","大人が抱えるコンプレックス","芸能人に必要なもの","独身女性が求める結婚相手の条件","中華料理の定番メニュー","心が癒されること","女の子に言われて傷つくこと","主婦の生活必需品","大人の飲み物","モテる女性の条件","日本の名作漫画","子どもが好きなキャラクター","腹立たしい行為","テンションの上がる出来事","人にあげて喜ばれるもの","小学校にあるもの","プロスポーツ選手に必要なもの","相手を不快にさせる行為","メガネが似合う人","焼いて食べると旨いもの","恋人に作って欲しい料理","バレると奥さんに怒られること","冬に飲みたくなる飲み物","テレビ番組に必要なもの","政治家に必要なもの","人気者","子供が喜ぶもの","アメリカ人が好きな食べ物","今使うと恥ずかしい死語","不良がよく言うセリフ","お年寄りが大好きなもの","FPSあるある","日本人の大好きな食べ物","オシャレな男が持っているもの","女性に贈ると喜ばれる物","お弁当に入っていてうれしいおかず","人として最低な行為","小腹が空いた時食べたくなるスイーツ","強い生き物","卒業式で言いたい言葉","人から言われて嬉しい言葉","夏休みの定番行事","滅多に食べられないご馳走","イケてる男の部屋にあるもの","朝の食卓に欠かせない物","売れっ子アイドルの条件","外国人が喜ぶ日本のおみやげ","コンビニでよく買うもの","女子高生のカバンに入っているもの","初老男性の悩み","夏休みに行きたくなる人気スポット","人気アニメ","かっこいい職業","おしゃれなもの","おいしい和食","カラオケで盛り上がる曲","健康に良いこと","綺麗なもの","汚いもの","サラリーマンがよく使う言葉","学校の先生がよく言うこと","頭が良さそうな言葉","毎日すること","懐かしい言葉","やわらかいもの","清楚なイメージのあるキャラクター","強いキャラクター","モテるキャラクターの条件","生きる上で欠かせないもの","無人島にもっていくもの","一生に一度はみてみたいもの","冬の食べ物","お父さんが娘に嫌われること","人を煽る一言","はやいもの","悲しいこと","見るべきもの","疲れること","子供の頃から学ぶべきもの","簡単には出来ないこと","生まれ変わりたいもの","覚えているとかっこいいもの","絶対敵わないもの","キラキラなもの","大切にしたいもの","危ないこと","思わず拍手が起こること","いつかは身に付けたいこと","踏むと痛いもの","温まるもの","意味のないこと","人が集まる場所","自分に足りないもの","赤いもの","根気が必要なもの","薄いもの"]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@bot.command()
async def wadai(ctx):
    #ひらがなと話題をリストからランダムに選ぶ
    hiragana = str(hiraganalist[random.randrange(len(hiraganalist))])
    wadai = str(wadailist[random.randrange(len(wadailist))])
    #ひらがなができなさそうな言葉なら選びなおす
    while hiragana in "ぁ-ぃ-ぅ-ぇ-ぉ-っ-ゃ-ゅ-ょ-ゎ-ゐ-ゑ-を-ん-げ-ず-ぜ-ば-べ-ぼ-ぴ-ぷ-ぺ-ざ":
        hiragana = str(hiraganalist[random.randrange(len(hiraganalist))])
        
    await ctx.send("「" + hiragana +"」から始まる" + wadai + "は？")


bot.run(token)

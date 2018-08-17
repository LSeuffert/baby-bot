def main():
    from babybot import BabyBot
    baby_bot = BabyBot()
    load_cogs(baby_bot)
    baby_bot.run()

def load_cogs(bot):
    bot.load_extension('babybot.cogs.coglord')
    
if __name__ == '__main__':
    main()

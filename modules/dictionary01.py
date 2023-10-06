import discord
import json
from discord.ext import commands

class GameDevDictionary(commands.Cog):
    """The `GameDevDictionary` class"""

    def __init__(self, bot):
        self.bot = bot

        with open('./tutorials.json') as f:
            self.data = json.load(f)

        self.resources = {
            'General': {
                'Game Dev Database': 'https://gamedevelop.io/resources',
                'GDC Vault': 'https://www.gdcvault.com/free',
                'Reddit Game Dev': 'https://www.reddit.com/r/gamedev/',
                'Learn Anything': 'https://learn-anything.xyz',
                'GameDev.net': 'https://www.gamedev.net/',
                'Game Industry Biz': 'https://www.gamesindustry.biz/',
                'Games From Scratch': 'https://gamefromscratch.com/',
            },
            'Unity': {
                'Unity Learn': 'https://learn.unity.com/',
                'Unity Docs': 'https://docs.unity3d.com/Manual/index.html',
                'Unity Forums': 'https://answers.unity.com/index.html',
                'Unity Reddit': 'https://www.reddit.com/r/Unity3D/',
            },
            'Unreal': {
                'Unreal Learn': 'https://www.unrealengine.com/en-US/onlinelearning-courses?sessionInvalidated=true',
                'Unreal Docs': 'https://docs.unrealengine.com/en-US/index.html',
                'Unreal Reddit': 'https://www.reddit.com/r/unrealengine/',
                'Community Wiki': 'https://www.ue4community.wiki/',
                'Raywenderlich Tutorials': 'https://www.raywenderlich.com/unreal-engine',
            },
            'Godot': {
                'Godot Website': 'https://godotengine.org/',
                'Godot Documentation': 'https://docs.godotengine.org/en/stable/index.html',
                'Godot Reddit': 'https://www.reddit.com/r/godot/',
            },
            'Art': {
                'Massive Art Resource Page': 'https://www.notion.so/The-Empire-Command-3a3bf979f8df4ca2a49315bc0dc31f9f',
                'ArtStation Learning': 'https://www.artstation.com/learning',
                '80lv': 'https://80.lv/',
                'Polycount': 'https://polycount.com/',
                'BlenderNation': 'https://www.blendernation.com/',
                'FlippedNormals Tutorials': 'https://flippednormals.com/',
                'Magma Studio': 'https://magmastudio.io/',
            },
            'Programming': {
                'Programming Patterns Book': 'https://shorturl.at/fgrMU',
                'Infallible Code YouTube': 'https://shorturl.at/cgGLQ',
                'Learn Anything General Resources': 'https://shorturl.at/M4679',
                'Learn C# by Building an RPG': 'https://shorturl.at/qrwR2',
                'C# Book': 'https://shorturl.at/oqwM7',
                'Beginning C++ Through Game Programming': 'https://shorturl.at/xABNU',
            },
            'Audio': {
                'Reddit Game Audio Wiki': 'https://www.reddit.com/r/GameAudio/wiki/',
                'Gamasutra Game Audio Design': 'https://www.gamasutra.com/blogs/PavelShylenok/20190506/342095/Designing_Sounds_for_a_Game.php',
                'Game Design Learn Audio Design': 'https://www.gamedesigning.org/learn/video-game-sound/',
            },
            'Shaders': {
                'Book of Shaders Website': 'http://thebookofshaders.com',
                'Shader Resource Archive': 'http://halisavakis.com/archive/',
                'ShaderLab Website': 'http://www.shaderslab.com',
            }
        }

    @commands.command(pass_context=True)
    async def tutorials(self, ctx):
        """Command Description"""
        await ctx.send(f"See how to use this command by running `{ctx.prefix}help tutorials`")

    @commands.command(pass_context=True, name='DictionaryTest')
    async def test(self, ctx):
        await ctx.send(self.data['general'][0]['value'])

    @commands.command(pass_context=True, name='Info')
    async def DInfo(self, ctx):
        channel = ctx.message.channel
        embed = discord.Embed(title="Game Development Dictionary",
                              description="This module allows you to look up terms related to game development and access more information and resources.",
                              color=0xffffff)

        for index, category in enumerate(self.resources, start=1):
            field_value = '\n'.join([f"{index}. !{term}" for index, term in enumerate(self.resources[category], start=1)])
            embed.add_field(name=f"{index}. {category}", value=field_value, inline=False)

        await ctx.send(channel, embed=embed)

    # Define other commands for categories as needed...


def setup(bot):
    """Method that loads this module into the client"""
    bot.add_cog(GameDevDictionary(bot))
    print("GameDevDictionary module loaded.")

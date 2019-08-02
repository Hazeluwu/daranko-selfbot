import os
import sys
import time
import inspect
import discord
import asyncio
import datetime
import threading
import subprocess


client = discord.Client()
void ="" # returns nothing
#decorations file_ just an variable decorator meaning it has no function other than its name

startTime = datetime.datetime.now()

def getUptime():
    return datetime.datetime.now() - startTime
getUptime()

def restart():
     python = sys.executable
     os.execl(python,python, * sys.argv)

def Writer():
    while(True):
        try:
            os.system("free -h | awk '{print $1, $2, $3, $4,  $5, $6, $7, $8}' >> tmp/tmp.txt")
            os.system("ps aux | grep %s | awk '{sum=sum+$6}; END {print sum/1024 }'  >> tmp/tmp2.txt" %(inspect.getfile(inspect.currentframe())))
            os.system("if ps aux | grep apache | grep -vw grep >/dev/null 2>/dev/null; then ps aux | grep apache | awk '{sum=sum+$6}; END {print sum/1024 }' >> tmp/tmp3.txt; else ps aux | grep http | awk '{sum=sum+$6}; END {print sum/1024 }'  >> tmp/tmp3.txt; fi")
            file = open('tmp/tmp.txt', 'r'); file_ = file.read()
            file2 = open('tmp/tmp2.txt', 'r'); file2_ = file2.read()
            file3 = open('tmp/tmp3.txt', 'r'); file3_ = file3.read()
            file_writer = open("/var/www/html/panel/data/bot_data.txt", "w", encoding="utf-8").write("%s %s [BOT] Ram MB %s [HTTP] Ram %s"% (getUptime(), file_ , file2_ , file3_))
            for server in client.servers:
                file_master = open("/var/www/html/panel/data/servers.txt", "a", encoding="utf-8").write("[SYNCED] [%s] - [ID %s] - [Owner %s] - [Members %s]\n" % (server.name, server.id, server.owner, len(server.members)))
                Session["TOTAL_SERVERS"] += 1
            for channel in client.private_channels:
               if(channel.type == discord.ChannelType.group):
                  file_writer = open("/var/www/html/panel/data/dms.txt", "a", encoding="utf-8").write("GROUP - %s - CID %s - CEO %s\n" % (channel, channel.id, channel.owner))
               elif channel.name == None:
                  file_writer = open("/var/www/html/panel/data/dms.txt", "a", encoding="utf-8").write("DM-info - dm with - [%s]-[%s] - cid [%s] - dm user id - [%s]\n" % (channel.user,client.user, channel.id, channel.user.id))
                  Session["TOTAL_DMS"] += 1
               else:
                 void
            file = open("/var/www/html/panel/data/typing.txt", "w", encoding="utf-8").write("%s"% (Session["TYPE"]))
            file2 = open("/var/www/html/panel/data/send.txt", "w", encoding="utf-8").write("%s"% (Session["SEND"]))
            file3 = open("/var/www/html/panel/data/edited.txt", "w", encoding="utf-8").write("%s"% (Session["EDIT"]))
            file4 = open("/var/www/html/panel/data/deleted.txt", "w", encoding="utf-8").write("%d"% (Session["DELETE"]))
            file5 = open("/var/www/html/panel/data/cmds_send.txt", "w", encoding="utf-8").write("%s"% (Session["COMMANDS_SENT"]))
            file6 = open("/var/www/html/panel/data/groups.txt", "w", encoding="utf-8").write("join %s | leave %s"% (Session["GROUP_JOIN"], Session["GROUP_LEAVE"]))
            file7 = open("/var/www/html/panel/data/total_dms.txt", "w", encoding="utf-8").write("%s"% (Session["TOTAL_DMS"]))
            file8 = open("/var/www/html/panel/data/total_servers.txt", "w", encoding="utf-8").write("%s"% (Session["TOTAL_SERVERS"]))
            file9 = open("/var/www/html/panel/data/total_logs.txt", "w", encoding="utf-8").write("%s"% (Session["TOTAL_LOGS"]))
            file10 = open("/var/www/html/panel/data/spam.txt", "w", encoding="utf-8").write("%s"% (Session["SPAM"]))
            file11 = open("/var/www/html/panel/data/saved.txt", "w", encoding="utf-8").write("%s"% (Session["SAVED"]))
            file12 = open("/var/www/html/panel/data/cleared.txt", "w", encoding="utf-8").write("%s"% (Session["CLEARED"]))
            time.sleep(1)
            Session["TOTAL_DMS"] =0
            Session["TOTAL_SERVERS"] =0
            open('/var/www/html/panel/data/dms.txt', 'w').close(); open('/var/www/html/panel/data/servers.txt', 'w').close()
            open('/var/www/html/panel/data/bot_data.txt', 'w').close()
            open('tmp/tmp.txt', 'w').close()
            open('tmp/tmp2.txt', 'w').close()
            open('tmp/tmp3.txt', 'w').close()
        except Exception as c:
               print("[error in pannel writer] %s" %(c))
               time.sleep(5)
               pass





class messages_processor:
    def message_init_dms(self):
        file = open("logs/dms/%s.log"% (self.message_channel_id_1) , "a", encoding="utf-8").write("DM %s %s - %s - %s - %s - %s [] %s\n" % (self.type_1, self.datetime_1, self.message_channel_1, self.message_channel_id_1, self.author_id_1, self.author_1, self.message_1))
    def message_init_groups(self):
        file = open("logs/dms/%s.log"% (self.message_channel_id_2) , "a", encoding="utf-8").write("GROUP %s %s - %s - %s - %s - %s [] %s\n" % (self.type_2, self.datetime_2, self.message_channel_2, self.message_channel_id_2, self.author_id_2, self.author_2, self.message_2))
    def message_init_servers(self):
        file = open("logs/servers/%s.log"% (self.message_server_id_3) , "a", encoding="utf-8").write("SERVER %s %s - %s - %s - %s - %s - %s - %s -[] %s\n" % (self.type_3, self.datetime_3, self.message_server_3, self.message_server_id_3, self.message_channel_3, self.message_channel_id_3, self.author_id_3, self.author_3, self.message_3))

class last_deleted:
    def deleted(self):
        fname = "logs/deleted/last.log"
        num_lines = 0
        with open(fname, 'r') as f:
            for line in f:
             if(len(line.strip()) == 0):
              void
             num_lines += 1
             if(num_lines == 20):
                num_lines += 0
                open('logs/deleted/last.log', 'w').close()
        file = open("logs/deleted/last.log", "a", encoding="utf-8").write("%s DEL %s %s %s \n" % (num_lines, self.date, self.user, self.message))


def token_init():
    while(True):
        for tokens in open("data/tokens.txt", "r").readlines():
            AUTHS["authenticated_ids"].append(tokens.strip())
        time.sleep(1)
        AUTHS["authenticated_ids"] =[]


AUTHS ={
    "authenticated_ids": [],
    "dm_ids": []
    }
Session ={
   "DELETE": 1,
   "TYPE": 1,
   "SEND": 1,
   "EDIT": 1,
   "SAVED": 1,
   "CLEARED": 1,
   "CLIENT_MENTIONS": 1,
   "EVERYONE_MENTIONS": 1,
   "SPAM": 1,
   "GROUP_JOIN": 1,
   "GROUP_LEAVE": 1,
   "COMMANDS_SENT": 1,
   "TOTAL_SERVERS": 0,
   "TOTAL_DMS": 0,
   "TOTAL_LOGS": 90332
   }



@client.event
async def on_ready():
    with open("data/tokens.txt") as f:
       lines = f.readlines();lines
    lines[0] = "%s\n" %(client.user.id);lines
    with open("data/tokens.txt", "w") as f: f.writelines(lines)
    print("\033[33m[\033[0m\033[1;33mSELFBOT\033[0m\033[33m]\033[0m \033[33m[\033[0m\033[1;31mIS READY!!\033[0m\033[33m]\033[0m")
    a = threading.Thread(target = Writer, name = 'console-writer').start()
    await client.change_presence(status=discord.Status.offline)
    print("\033[1;32mclient user:\033[0m \033[4;1;34m%s\033[0m" % (client.user)); print("\033[1;32mclient user id:\033[0m \033[4;1;34m%s\033[0m" % (client.user.id))
    if len(sys.argv) > 1:
       if sys.argv[1] == "sync":
          sys.stdout.write("\033[33m[\033[0m\033[1;33mSELFBOT\033[0m\033[33m]\033[0m \033[33m[\033[0m\033[36mSynchronizing data\033[0m\033[33m]\033[0m\n")
          open('data/friends.info', 'w').close()
          open('data/mas_dm.txt', 'w').close()
          for channel in client.private_channels:
              if(channel.type == discord.ChannelType.group):
                 void
              elif channel.name == None:
                   open("data/friends.info", "a", encoding="utf-8").write("[friends info] %s - uid %s - cid %s\n" % (channel.user, channel.user.id, channel.id))
                   open("data/mas_dm.txt", "a", encoding="utf-8").write("%s\n" % (channel.id))
    for load in open("data/mas_dm.txt", "r").readlines():
            AUTHS["dm_ids"].append(load.strip())



@client.event
async def on_typing(channel, user, when):
    Session["TYPE"] += 1

@client.event
async def on_message_edit(before, after):
  Session["EDIT"] += 1
  await client.wait_until_ready()
  if(before.channel.name == None):
     r1 = messages_processor()
     r1.type_1 = ("EDIT");
     r1.datetime_1 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
     r1.message_channel_1 = (before.channel)
     r1.message_channel_id_1 = (before.channel.id)
     r1.author_id_1 = (before.author.id)
     r1.author_1 = (before.author)
     r1.message_1 = ("%s | %s" % (before.content, after.content))
     r1.message_init_dms()
  elif before.channel.type == discord.ChannelType.group:
       r2 = messages_processor();
       r2.type_2 = ("EDIT")
       r2.datetime_2 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       r2.message_channel_2 = (before.channel)
       r2.message_channel_id_2 = (before.channel.id)
       r2.author_id_2 = (before.author.id)
       r2.author_2 = (before.author)
       r2.message_2 = ("%s | %s" % (before.content, after.content))
       r2.message_init_groups()
  else:
      r3 = messages_processor()
      r3.type_3 = ("EDIT")
      r3.datetime_3 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      r3.message_server_3 = (before.server)
      r3.message_server_id_3 = (before.server.id)
      r3.message_channel_3 = (before.channel)
      r3.message_channel_id_3 = (before.channel.id)
      r3.author_id_3 = (before.author.id)
      r3.author_3 = (before.author)
      r3.message_3 = ("%s | %s" % (before.content, after.content))
      r3.message_init_servers()


@client.event
async def on_message_delete(message):
   Session["DELETE"] += 1
   last = last_deleted()
   last.date = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
   last.user = (message.author)
   last.message = (str(message.content))
   last.deleted()
   if(message.channel.name == None):
      r1 = messages_processor()
      r1.type_1 = ("DELETE")
      r1.datetime_1 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      r1.message_channel_1 = (message.channel)
      r1.message_channel_id_1 = (message.channel.id)
      r1.author_id_1 = (message.author.id)
      r1.author_1 = (message.author)
      r1.message_1 = (str(message.content))
      r1.message_init_dms()
   elif message.channel.type == discord.ChannelType.group:
        r2 = messages_processor()
        r2.type_2 = ("DELETE")
        r2.datetime_2 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        r2.message_channel_2 = (message.channel)
        r2.message_channel_id_2 = (message.channel.id)
        r2.author_id_2 = (message.author.id)
        r2.author_2 = (message.author)
        r2.message_2 = (str(message.content))
        r2.message_init_groups()
   else:
       r3 = messages_processor();
       r3.type_3 = ("DELETE")
       r3.datetime_3 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       r3.message_server_3 = (message.server)
       r3.message_server_id_3 = (message.server.id)
       r3.message_channel_3 = (message.channel)
       r3.message_channel_id_3 = (message.channel.id)
       r3.author_id_3 = (message.author.id)
       r3.author_3 = (message.author)
       r3.message_3 = (str(message.content))
       r3.message_init_servers()


@client.event
async def on_message(message):
   Session["SEND"] += 1
   if(message.channel.name == None):
      r1 = messages_processor()
      r1.type_1 = ("SEND")
      r1.datetime_1 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      r1.message_channel_1 = (message.channel)
      r1.message_channel_id_1 = (message.channel.id)
      r1.author_id_1 = (message.author.id)
      r1.author_1 = (message.author)
      r1.message_1 = (str(message.content))
      r1.message_init_dms()
   elif message.channel.type == discord.ChannelType.group:
        r2 = messages_processor()
        r2.type_2 = ("SEND")
        r2.datetime_2 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        r2.message_channel_2 = (message.channel)
        r2.message_channel_id_2 = (message.channel.id)
        r2.author_id_2 = (message.author.id)
        r2.author_2 = (message.author)
        r2.message_2 = (str(message.content))
        r2.message_init_groups()
   else:
       r3 = messages_processor()
       r3.type_3 = ("SEND")
       r3.datetime_3 = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       r3.message_server_3 = (message.server)
       r3.message_server_id_3 = (message.server.id)
       r3.message_channel_3 = (message.channel)
       r3.message_channel_id_3 = (message.channel.id)
       r3.author_id_3 = (message.author.id)
       r3.author_3 = (message.author)
       r3.message_3 = (str(message.content))
       r3.message_init_servers()


   for userid in AUTHS["authenticated_ids"]:
     if(message.author.id == userid):
        commands = []
        count = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[count:index])
                count = index+1
        commands.append(message.content[count:])



        if commands[0].lower() == "xa":
            Session["COMMANDS_SENT"] += 1
            Session["CLEARED"] = 0
            if len(commands) == 1:
                async for msg in client.logs_from(message.channel,limit=9999):
                   if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                            Session["CLEARED"] += 1
                        except Exception as c:
                            continue

            elif len(commands) == 2:
              async for msg in client.logs_from(message.channel, limit=int(commands[1])):
                    if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                            Session["CLEARED"] += 1
                        except Exception as c:
                            continue

        elif commands[0].lower() == "typing":
            Session["COMMANDS_SENT"] += 1
            for _ in range(int(commands[1])):
                await client.send_typing(message.channel)
                await asyncio.sleep(11)

        elif commands[0].lower() == "add":
           Session["COMMANDS_SENT"] += 1
           AUTHS["authenticated_ids"] =[]
           if(message.author.id == client.user.id):
              file = open("data/tokens.txt", "a", encoding="utf-8").write("%s\n"% (commands[1]))

        elif commands[0].lower() == "remove-token":
             Session["COMMANDS_SENT"] += 1
             if(message.author.id == client.user.id):
              os.system("sed -i '/%s/d' ./data/tokens.txt" %(commands[1]))

        elif commands[0].lower() == "auths":
            Session["COMMANDS_SENT"] += 1
            file= open('data/tokens.txt', 'r')
            file_ = file.read()
            var =  "```json\n%s\n```"% (file_)
            await client.send_message(message.channel, var)

        elif commands[0].lower() == "--remove":
             Session["COMMANDS_SENT"] += 1
             if(message.author.id == client.user.id):
              os.system("rm -rf /var/www/html/panel/data/commands_responses.txt")


        elif commands[0].lower() == "massdm":
           Session["COMMANDS_SENT"] += 1
           if(message.author.id == client.user.id):
              for cid in AUTHS["dm_ids"]:
                if(message.author.id == client.user.id):
                    try:
                      await client.send_message(client.get_channel(cid), (commands[1]))
                    except Exception as x:
                        continue


        elif commands[0].lower() == "massdm_clear":
             if(message.author.id == client.user.id):
              Session["COMMANDS_SENT"] += 1
              for cid in AUTHS["dm_ids"]:
                  print("\033[33m[\033[0m\033[36mMASS CLEANING\033[0m\033[33m]\033[0m \033[33m[\033[0m\033[31m%s\033[0m\033[33m]\033[0m \033[33m[\033[0m\033[1;35;40mCID\033[0m \033[1;33m%s\033[0m\033[33m]\033[0m" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cid))
                  file = open("/var/www/html/panel/data/commands_responses.txt", "a", encoding="utf-8").write("[MASS CLEANING] %s CID %s\n"% (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cid))
                  async for msg in client.logs_from(client.get_channel(cid),limit=9999):
                   if(msg.channel.type == discord.ChannelType.group):
                      void
                   if msg.author == client.user:
                       try:
                          await client.delete_message(msg)
                       except Exception as c:
                           continue

        elif commands[0].lower() == "userid":
             Session["COMMANDS_SENT"] += 1
             var = "[info] %s - %s - UID %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), message.mentions[0], message.mentions[0].id)
             file = open("/var/www/html/panel/data/commands_responses.txt", "a", encoding="utf-8").write("%s\n"% (var))


        elif commands[0].lower() == "search":
            Session["COMMANDS_SENT"] += 1
            await asyncio.sleep(1)
            if(message.channel.name == None):
             info = open("logs/dms/%s.log" % (message.channel.id))
            elif message.channel.type == discord.ChannelType.group:
             info = open("logs/dms/%s.log" % (message.channel.id))
            else:
                info = open("logs/servers/%s.log" % (message.server.id))
            Session["COMMANDS_SENT"] += 1
            os.system("rm -rf logs/searches/%s.log" % (commands[1]))
            storage = []
            for _ in info:
                _ = _.strip()
                if(str(commands[1]) == _ or str(commands[1]) in _):
                    storage.append(_)
            for _ in storage:
                file = open("logs/searches/%s.log" % (commands[1]), "a", encoding="utf-8").write(str(_) + "\n")
            if(message.channel.name == None):
             var =  "[search] %s Returned %d Results! for %s" % (message.channel, len(storage), (commands[1]))
             file = open("/var/www/html/panel/data/commands_responses.txt", "a", encoding="utf-8").write("%s\n"% (var))
            elif message.channel.type == discord.ChannelType.group:
             var2 =  "[search] %s Returned %d Results! for %s" % (message.channel, len(storage), (commands[1]))
             file2 = open("/var/www/html/panel/data/commands_responses.txt", "a", encoding="utf-8").write("%s\n"% (var2))
            else:
             var3 ="[search] %s Returned %d Results! for %s" % (message.server, len(storage), (commands[1]))
             file3 = open("/var/www/html/panel/data/commands_responses.txt", "a", encoding="utf-8").write("%s\n"% (var3))

        elif commands[0].lower() == "upload-search":
            Session["COMMANDS_SENT"] += 1
            area=message.channel
            await client.send_file(area, r"logs/searches/%s.log" % (commands[1]) ,filename="%s.log" % (commands[1]))
            await asyncio.sleep(2)
            await client.delete_message(message)


        elif commands[0].lower() == "save":
           Session["COMMANDS_SENT"] += 1
           Session["SAVED"] = 0
           await asyncio.sleep(2)
           await client.delete_message(message)
           async for msg in client.logs_from(message.channel, limit=int(commands[2])):
            try:
             WriteTxtFile = open("logs/saves/%s.save" % (commands[1]) , "a")
             if(message.channel.name == None):
              WriteTxtFile.write("SAVED DM %s - %s - CID %s - UID %s - %s -[] %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), message.channel, message.channel.id, msg.author.id, msg.author, msg.content))
              Session["SAVED"] += 1
             elif message.channel.type == discord.ChannelType.group:
              WriteTxtFile.write("SAVED GROUP %s - %s - CID %s - UID %s - %s -[] %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), message.channel, message.channel.id, msg.author.id, msg.author, msg.content))
              Session["SAVED"] += 1
             else:
              WriteTxtFile.write("SAVED SERVER %s - %s - SID %s - %s - UID %s - %s  -[] %s\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), message.server, message.server.id, message.channel, msg.author.id, msg.author, msg.content))
              Session["SAVED"] += 1
            except:
              continue

        elif commands[0].lower() == "upload-save":
            Session["COMMANDS_SENT"] += 1
            await asyncio.sleep(2)
            await client.delete_message(message)
            area=message.channel
            await client.send_file(area, r"logs/saves/%s.save" % (commands[1]) ,filename="%s.save" % (commands[2]))


        elif commands[0].lower() == "spam":
            Session["COMMANDS_SENT"] += 1
            if(message.author.id == client.user.id):
             await client.delete_message(message)
             for _ in range(int(commands[1])):
                await client.send_message(message.channel, commands[2])

        elif commands[0].lower() == "upload-log":
            Session["COMMANDS_SENT"] += 1
            area=message.channel
            await client.send_file(area, r"logs/%s.log" % (commands[1]) ,filename="%s_log.json" % (commands[2]))
            await asyncio.sleep(2)
            await client.delete_message(message)

        elif commands[0].lower() =="--leave":
           Session["COMMANDS_SENT"] += 1
           try:
              if(message.author.id == client.user.id):
                 await client.leave_server(message.server)
           except Exception as c:
                print(c)
                continue

        elif commands[0].lower() == "--delete-server":
           Session["COMMANDS_SENT"] += 1
           if(message.author.id == client.user.id):
            await client.delete_server(message.server)

        elif commands[0].lower() == "--info":
            Session["COMMANDS_SENT"] += 1
            os.system("free -h | awk '{print $1, $2, $3, $4,  $5, $6, $7, $8}' >> tmp/void.txt")
            os.system("ps aux | grep sboting | awk '{sum=sum+$6}; END {print sum/1024 }'  >> tmp/void2.txt")
            file = open('tmp/void.txt', 'r')
            file_ = file.read()
            file2 = open('tmp/void2.txt', 'r')
            file2_ = file2.read()
            await client.send_message(message.channel, "```css\n UPTIME %s %s bot usage %s\n```" % (getUptime(), file_ , file2_))
            os.system("rm -rf tmp/void.txt"); os.system("rm -rf tmp/void2.txt")


        elif commands[0].lower() == "--deleted":
             Session["COMMANDS_SENT"] += 1
             file = open('logs/deleted/last.log', 'r')
             file_ = file.read()
             await client.send_message(message.channel, "```css\n%s\n```" %(file_))

        elif commands[0].lower() == "--help":
            Session["COMMANDS_SENT"] += 1
            embed = discord.Embed(name="HELP")
            embed.set_author(name="help")
            embed.add_field(name="add", value="adds a id to [tokens | retards | important] [with name args]", inline=False)
            embed.add_field(name="remove", value="[remove-name] removes a id from [-token | -retard | -important] [with name args]", inline=False)
            embed.add_field(name="masdm", value="mas dms with arg1", inline=False)
            embed.add_field(name="dmc", value="mas clears all messages in all dms", inline=False)
            embed.add_field(name="xa", value="clears messages xa | xa amount", inline=False)
            embed.add_field(name="userid", value="gets user id | userid mention of target", inline=False)
            embed.add_field(name="typing", value="keeps sending typing status | typing amount", inline=False)
            embed.add_field(name="auths", value="shows all ids in the files [tokens | retards | important] [auths name]", inline=False)
            embed.add_field(name="--leave", value="leaves server", inline=False)
            embed.add_field(name="--delete-server", value="deletes server only if your owner", inline=False)
            embed.add_field(name="search", value="searches for arg in logs [search msg channel id]", inline=False)
            embed.add_field(name="spam", value="spams with numbers of times and arg1 as message [spam 900 hi]", inline=False)
            embed.add_field(name="save", value="saves all messages in channel with arguments [save file-name amount]", inline=False)
            embed.add_field(name="upload-save", value="uploads-save | save-to-upload name-to-give-it [upload-save kek keking]", inline=False)
            embed.add_field(name="upload-log", value="uploads-log | folder/log-to-upload name-to-give-it [upload-log servers/id keking]", inline=False)
            embed.add_field(name="--info", value="shows bot info", inline=False)

            await client.send_message(message.channel, embed=embed)

        elif commands[0].lower() == "--reboot":
           if(message.author.id == client.user.id):
            Session["COMMANDS_SENT"] += 1
            await asyncio.sleep(2)
            await client.delete_message(message)
            restart()
        break



print("\033[33m[\033[0m\033[1;33mSELFBOT\033[0m\033[33m]\033[0m \033[33m[\033[0m\033[36mSTARTING THREADS!!!\033[0m\033[33m]\033[0m")
b = threading.Thread(target = token_init, name = 'token').start()
#client.run("NjAxNzAxNDIyODQ4OTMzODg5.XTGIQA.nFRka44qP2y5Qwi7ZzGgw9QobJs", bot=False) #lissa
client.run("token", bot=False) # Viki

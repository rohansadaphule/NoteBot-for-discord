import discord
import os

token = os.environ['NoteBot_token']
client = discord.Client()

assignments_q = {'css':'link'}
assignments_a = {'spcc':'newLink'}
experiments = {'ai':'hello'}
question_bank = {'cc':'not yet'}
question_paper = {'dsip':'hmmm'}

def sending_link(subject, option):
  if option == 'q':
    if subject in assignments_q:
      return assignments_q[subject]
    else:
      return "These notes are currently unavailable. Try entering different subject."
      
  if option == 'a':
    if subject in assignments_a:
      return assignments_a[subject]
    else:
      return "These notes are currently unavailable. Try entering different subject."
      
  if option == 'e':
    if subject in experiments:
      return experiments[subject]
    else:
      return "These notes are currently unavailable. Try entering different subject."
      
  if option == 'qp':
    if subject in question_paper:
      return question_paper[subject]
    else:
      return "These notes are currently unavailable. Try entering different subject."
      
  if option == 'qb':
    if subject in question_bank:
      return question_bank[subject]
    else:
      return "These notes are currently unavailable. Try entering different subject."
      
  else:
    return "Please enter a valid option"
  
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith("$send"):
    if len(msg.split(" ")) < 3:
      await message.channel.send("Enter valid option.")
      return
    subject = msg.split(" ")[1].lower()
    option = msg.split(" ")[2].lower()
    link = sending_link(subject, option)
    await message.channel.send(link)
    
client.run(token)

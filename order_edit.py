import re
import time
from time import sleep
#from telegram.message import Message
#from telegram.update import Update
import sys, traceback
import os
import subprocess
import sys
from datetime import datetime
import glob
import requests
import asyncio
import telethon
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.events import NewMessage
from telethon import events
from metaapi_cloud_sdk import MetaApi
import asyncio
import logging
import math

string= '1BVtsOL0Bu1z9mIzMjjHqfTiuy_R2S00u4849An1BZYhk91hiAYg9rs6qAcHlot2mkUD92HbJDsyANpvz1xyhU_jmpSjfg6F4cx2CznvuHrQUyCUEZ5tXjcxPj2Uz309i6gA84aPCxz8AQmdSRxIScJSUvWian_fXOxLO_FLbxmw0g6d4-YPUBaPBOsdRhEY4qhwZPCSkb5LMVYowRQtV6bwhs-Lo1JOlbGanU5DoaUM-u3zUmB0a-fJ3MUbDG9m70SdexfL9CE-WAb-O0UBVR9bgAohCyhrNTtThNsWlHBYRWK4GLm8BXth69FciZQjbwy6y2dt9zoB7PeXRsq_PYwUuyX7NCow='
client = telethon.TelegramClient(StringSession(string),api_id=3030128, api_hash='cfc3885f5d2cbdbc5f10e6a643de2711')
client.connect()
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmOWI4ZGVlMzljMzVhNDY4ZmNmOGE1ZDlkYTAzNzFiZCIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiZjliOGRlZTM5YzM1YTQ2OGZjZjhhNWQ5ZGEwMzcxYmQiLCJpYXQiOjE2ODkzMzk5MjV9.NsgW8ziS-GvcqoSK1UEOiheJpun1PViBtrWAqqzWbrsEHfgsAdtnRkt0SwPnQCzdr4kyQSiN7JIBy8Ug1x4mX_aW4xAT9oX8PGRunwh2DLYjSsc8yuw1cOiCKUeg1suZVmEGUB9F1omkF0057_Mx2tgkzN-9a-rANohy5jplhmlcEyj4FjVs6924Tyf9CTGl-O-YJ8YT66163JlTngXhzYOqlxFKSPiPPnNT18aMWE6hq46_n4LAC-1Owm4Xm_yp_TH3q09ve_SAP01phIYgSy7YI_n3hJOfIR3MWXyghqMTjm7hWovYaq9w47mhkuqlZ5kmhYDSVtIw0ClW0gp02HDH5-HG0tQQuZZ9eVdcmD-IYRiyldV7SDVNQPGP4YLKjwkVB9bThATtOKzVjfwzgSbkLvp0NcmZ0U7rLacSTCXezJdy4gXOK41fA6b67re-nVxwnNuN7cLfjMHUNtWJtroc6nYDJJpIWxOYgiATDgumonbhCtJvOlkww88lHvEUYZwxhjUHGNmbcw116Jg9Litpiqt-MhwylqcrX0UHjfZhMhK-il-yZF-MdRcoU-pUFI_GiMbDUnn6KwkEOgHz0DJEHJpsV7eS89I6ZzN_XyAHG6PpfSBHK1QkXzhAWqWPyiamlgoB7QQF-yCkiRmQehZY8xvHhg8Dq5xuLVpNeS0"
#ACCOUNT_ID = "2da5bee2-1da0-4ed4-b03b-13714acc8009" #main demo
  #Scalping Account
channel1 = 1963686318
channel2 = 1928900037
#channel_id = -1001981997793  #main
#channel_id = -1001963686318  #trading test
igroup = -990951103

@client.on(events.MessageEdited)
async def my_event_handler(event):
    message = str(event.text)
    
    channel_id = event.message.peer_id.channel_id
    if channel_id == channel1: 
    #send_channel = message.chat.title
        pair = ""
        string = message
        tstring = string.split("\n")
        def remove_empty_datatypes(list_of_strings):
            new_list = []
            for string in list_of_strings:
                if string:
                    new_list.append(string)
            return new_list
        try:
            list_of_strings = tstring
            tstring = remove_empty_datatypes(list_of_strings)
            pao = tstring[0].split(" ")
            pair = pao[0]
            order = pao[1]
            order_check = pao[2].strip(" ").upper()
            print(order)
        except IndexError:
            await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
            return
        if order_check == "NOW":
            sl = str(tstring[1].split(":")[1].strip(" "))
            tp1 = str(tstring[2].split(":")[1].strip(" "))
            tp2 = str(tstring[3].split(":")[1].strip(" "))
            if pair == "GOLD":
                pair = "XAUUSD"
            else:
                pass 
            await client.send_message(igroup, 'Order Edit Detected \n'+'TP1 : '+tp1+'\nTP2 : '+tp2+'\nSL : '+sl)
            #current_price=terminalState.price(symbol='EURUSD')
            #edit_order(sl,tp1,tp2)
            f = open(str(channel1)+".txt", "r")
            ID = f.read()
            f.close()
            f = open(str(channel1)+"_price.txt","r")
            price = float(f.read())
            f.close
            tp1 = price+1.5
            ACCOUNT_ID = "2474c021-d9e2-41d0-84a2-07910e34fdf3"
            api = MetaApi(API_KEY)
            account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']
            if initial_state not in deployed_states:
                await account.deploy()
            await account.wait_connected()
                        # connect to MetaApi API
            connection = account.get_rpc_connection()
            await connection.connect()
            await connection.wait_synchronized()
            account_information = await connection.get_account_information()
            try:
                ID = await connection.modify_position(ID, float(sl), float(tp1))
            except:
                await connection.modify_order(ID, price, float(sl),float(tp1))    
            await client.send_message(igroup, "Order modified ✅")
            ID = str((ID['positionId']))
            f = open(str(channel1)+".txt", "w")
            f.write(str(ID))
            f.close()                    
        else:
            pass

    elif channel_id == channel2:                                              #trading test 2
        message = str(event.text)
        pair = ""
        string = message
        tstring = string.split("\n") 
        def remove_empty_datatypes(list_of_strings):
            new_list = []
            for string in list_of_strings:
                if string:
                    new_list.append(string)
            return new_list
        try:
            list_of_strings = tstring
            tstring = remove_empty_datatypes(list_of_strings)
            pao = tstring[1].split(" ")
            pair = tstring[0].split(" ")[0].strip(" ")
            try:
                price = float(pao[2].strip("@"))
            except ValueError:
                pass    
            order = pao[0].strip(" ")
            order_check = pao[1].strip(" ").upper()
        except IndexError:
            pass
        if order_check == "NOW":
            ACCOUNT_ID = "faad96c8-48b5-4457-a288-75711873eedd"
            account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']
            if initial_state not in deployed_states:
                await account.deploy()
            await account.wait_connected()
            connection = account.get_rpc_connection()
            await connection.connect()
            await connection.wait_synchronized()
            account_information = await connection.get_account_information()           
            sl = str(tstring[5].split(":")[1].strip(" "))
            tp1 = str(tstring[2].split(":")[1].strip(" "))
            tp2 = str(tstring[3].split(":")[1].strip(" "))
            tp3 = str(tstring[4].split(":")[1].strip(" "))
            if pair == "GOLD":
                pair = "XAUUSD"    
            else:
                pass 
            await client.send_message(igroup, 'Order Edit Detected \n'+'TP1 : '+tp1+'\nTP2 : '+tp2+'\nSL : '+sl)
            #current_price=terminalState.price(symbol='EURUSD')
            #edit_order(sl,tp1,tp2)
            f = open(str(channel2)+".txt", "r")
            ID = f.read()
            ID = str(message.text)
            api = MetaApi(API_KEY)
            account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']
            if initial_state not in deployed_states:
                await account.deploy()
                await account.wait_connected()
                        # connect to MetaApi API
                connection = account.get_rpc_connection()
                await connection.connect()
                await connection.wait_synchronized()
                account_information = await connection.get_account_information()
                ID = await connection.modify_position(ID, float(sl), float(tp1))
                await client.send_message(igroup, "Order modified ✅")
                ID = str((ID['positionId']))
                f = open(str(channel2)+".txt", "w")
                f.write(str(ID))
                f.close()                    
        else:
            pass                  

client.start()
client.run_until_disconnected()

import re
import time
import telegram
from telegram.ext import Updater
import telegram.ext
from telegram.ext import CommandHandler
from time import sleep
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
#from telegram.message import Message
#from telegram.update import Update
from telegram.error import RetryAfter
from pyrogram.errors import FloodWait
from pyrogram import Client
from pyrogram import filters
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

string= '1BVtsOMYBu8Xrn1nNQsmv2hen1e3wDVmZEh9-oH2asBbb4Gu6fqCO-_qyfwAxHSaZt5SFli3bYTiMQBfW0YZbe6ts3yHHyJvizSkHFd3XK18CZTrdsS_e5JLbtNSbOZ-9FCwzJ7dN9BET8vsC0hompAw_3WMEgOYW5Cn7Y95PaXjgPHNlU1OhfN88BEHt1gyzrjdKeqGukZ2i8HTqWt8m0Ft7A_QeB6ksL9Nt23OJWFooud8uZ7t9JuZfUQrZXeqbfB9dSMlqQcRdKFDwSu3AHOpsIZFrlRm3cAW21R0fi0Lpq7Y5SAQwuMVABsTGBampj5JcHOmjkMSJGu0R7cRdikiKu1oNAmE='
client = telethon.TelegramClient(StringSession(string),api_id=3030128, api_hash='cfc3885f5d2cbdbc5f10e6a643de2711')
client.connect()
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmOWI4ZGVlMzljMzVhNDY4ZmNmOGE1ZDlkYTAzNzFiZCIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX1dLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiZjliOGRlZTM5YzM1YTQ2OGZjZjhhNWQ5ZGEwMzcxYmQiLCJpYXQiOjE2ODkzMzk5MjV9.NsgW8ziS-GvcqoSK1UEOiheJpun1PViBtrWAqqzWbrsEHfgsAdtnRkt0SwPnQCzdr4kyQSiN7JIBy8Ug1x4mX_aW4xAT9oX8PGRunwh2DLYjSsc8yuw1cOiCKUeg1suZVmEGUB9F1omkF0057_Mx2tgkzN-9a-rANohy5jplhmlcEyj4FjVs6924Tyf9CTGl-O-YJ8YT66163JlTngXhzYOqlxFKSPiPPnNT18aMWE6hq46_n4LAC-1Owm4Xm_yp_TH3q09ve_SAP01phIYgSy7YI_n3hJOfIR3MWXyghqMTjm7hWovYaq9w47mhkuqlZ5kmhYDSVtIw0ClW0gp02HDH5-HG0tQQuZZ9eVdcmD-IYRiyldV7SDVNQPGP4YLKjwkVB9bThATtOKzVjfwzgSbkLvp0NcmZ0U7rLacSTCXezJdy4gXOK41fA6b67re-nVxwnNuN7cLfjMHUNtWJtroc6nYDJJpIWxOYgiATDgumonbhCtJvOlkww88lHvEUYZwxhjUHGNmbcw116Jg9Litpiqt-MhwylqcrX0UHjfZhMhK-il-yZF-MdRcoU-pUFI_GiMbDUnn6KwkEOgHz0DJEHJpsV7eS89I6ZzN_XyAHG6PpfSBHK1QkXzhAWqWPyiamlgoB7QQF-yCkiRmQehZY8xvHhg8Dq5xuLVpNeS0"
#ACCOUNT_ID = "2da5bee2-1da0-4ed4-b03b-13714acc8009" #main demo
  #another demo

channel1 = 1963686318
channel2 = 1928900037

#channel_id = -1001981997793  #main
#channel_id = -1001963686318  #trading test
igroup = -990951103

@client.on(events.NewMessage)
async def my_event_handler(event):
    channel_id = event.message.peer_id.channel_id
    api = MetaApi(API_KEY)
    if channel_id == 1963686318:                                                #trading test
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
            pao = tstring[0].split(" ")
            pair = pao[0]
            order = pao[1]
            try:
                pao = remove_empty_datatypes(pao)
                try:
                    price = float(pao[4].split("-")[0])
                except ValueError:
                    print("it's shown Value error")
                    pass    
            except IndexError:
                price = float(pao[4].strip(" "))
            order_check = pao[2].strip(" ").upper()
        except IndexError:
            await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
            return
        if order_check == "NOW":
            ACCOUNT_ID = "2474c021-d9e2-41d0-84a2-07910e34fdf3"
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
            sl = str(tstring[1].split(":")[1].strip(" "))
            tp1 = str(tstring[2].split(":")[1].strip(" "))
            tp2 = str(tstring[3].split(":")[1].strip(" "))
            if pair == "GOLD":
                pair = "XAUUSD"
            if order == "BUY" and order_check == "NOW":
                await client.send_message(igroup, "BUY NOW ORDER TRIGGERING")
                if tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01)
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    print(c_price)
                    print(price)
                    if price >= c_price:
                        ID = await connection.create_market_buy_order(pair, 0.01)
                    else:
                        #try:
                        ID = await connection.create_limit_buy_order(pair, 0.01, price)
                        #except:
                            #ID = await connection.create_market_buy_order(pair, 0.01) 
                        
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯 Waiting for TP and SL")
                        #current_price = await connection.get_symbol_price(symbol='XAUUSD')
                        f = open(str(channel1)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        print(ID)
                        ID = str((ID['orderId']))
                        f = open(str(channel1)+".txt", "w")
                        f.write(str(ID))
                        f.close()       

                    else:
                        msg = (ID['message'])
                        await client.send_message(igroup, msg)


                elif not tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01,float(sl),float(tp1))
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    if price >= c_price:
                        ID = await connection.create_market_buy_order(pair, 0.01, float(sl),float(tp1))
                    else:
                        ID = await connection.create_limit_buy_order(pair, 0.01, price,float(sl),float(tp1))
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯")
                        f = open(str(channel1)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        ID = str((ID['orderId']))
                        f = open(str(channel1)+".txt", "w")
                        f.write(str(ID))
                        f.close()                  
                else:
                    await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
                        

            if order == "SELL" and order_check == "NOW":
                await client.send_message(igroup, "SELL NOW ORDER TRIGGERING")
                if tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01)
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['ask'])
                    print(c_price)
                    print(price)
                    if price <= c_price:
                        ID = await connection.create_market_sell_order(pair, 0.01)
                    else:
                        #try:
                        ID = await connection.create_limit_sell_order(pair, 0.01, price)
                        #except:
                            #ID = await connection.create_market_buy_order(pair, 0.01) 
                        
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯 Waiting for TP and SL")
                        #current_price = await connection.get_symbol_price(symbol='XAUUSD')
                        f = open(str(channel1)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        print(ID)
                        ID = str((ID['orderId']))
                        f = open(str(channel1)+".txt", "w")
                        f.write(str(ID))
                        f.close()       

                    else:
                        msg = (ID['message'])
                        await client.send_message(igroup, msg)


                elif not tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01,float(sl),float(tp1))
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['ask'])
                    if price <= c_price:
                        ID = await connection.create_market_sell_order(pair, 0.01, float(sl),float(tp1))
                    else:
                        print(price)
                        ID = await connection.create_limit_sell_order(pair, 0.01, price,float(sl),float(tp1))
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯")
                        f = open(str(channel1)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        ID = str((ID['orderId']))
                        f = open(str(channel1)+".txt", "w")
                        f.write(str(ID))
                        f.close()                  
                else:
                    await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
                        

            else:
                pass
                
        elif tstring[1] == 'Let’s close first entry and set BREAKEVEN last layer. Scalpers can close all now ✅':
            ACCOUNT_ID = "7c348b78-2c13-4340-9875-e1d241cb0323"
            account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']
            if initial_state not in deployed_states:
                await account.deploy()
            await account.wait_connected()
            connection = account.get_rpc_connection()
            await connection.connect()
            await connection.wait_synchronized()            
            f = open(str(channel1)+".txt", "r")
            ID = str(f.read())
            try:
                cancel = await connection.close_position(ID)
            except:
                cancel = await connection.cancel_order(ID)
            await client.send_message(igroup, str(cancel))  
        else:
            pass
    
    elif channel_id == 1928900037:                                              #trading test 2
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
            ACCOUNT_ID = "7c348b78-2c13-4340-9875-e1d241cb0323"
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
            if order == "BUY" and order_check == "NOW":
                await client.send_message(igroup, "BUY NOW ORDER TRIGGERING")
                if tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01)
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    if price >= c_price:
                        ID = await connection.create_market_buy_order(pair, 0.01)
                    else:
                        ID = await connection.create_limit_buy_order(pair, 0.01, price)    
                        
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯 Waiting for TP and SL")
                        #current_price = await connection.get_symbol_price(symbol='XAUUSD')
                        f = open(str(channel2)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        ID = str((ID['orderId']))
                        f = open(str(channel2)+".txt", "w")
                        f.write(str(ID))
                        f.close()                        

                    else:
                        msg = (ID['message'])
                        await client.send_message(igroup, msg)


                elif not tp1 == "":
                    #ID = await connection.create_market_buy_order(pair, 0.01,float(sl),float(tp1))
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    if price >= c_price:
                        ID = await connection.create_market_buy_order(pair, 0.01)
                    else:
                        ID = await connection.create_limit_buy_order(pair, 0.01, price)   
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯")
                        f = open(str(channel2)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        ID = str((ID['orderId']))
                        f = open(str(channel2)+".txt", "w")
                        f.write(str(ID))
                        f.close()              
                else:
                    await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))
                        

            elif order == "SELL" and order_check == "NOW":
                if tp1 == "":
                    #ID = await connection.create_market_sell_order(pair, 0.01)
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    if price <= c_price:
                        ID = await connection.create_market_sell_order(pair, 0.01, float(sl),float(tp1))
                    else:
                        ID = await connection.create_limit_sell_order(pair, 0.01, price ,float(sl),float(tp1))
                        
                    if (ID['message']) == "No error returned":
                        await client.send_message(igroup, "Order Placed 🎯 Waiting for TP and SL")
                        current_price = await connection.get_symbol_price(symbol='XAUUSD')
                        f = open(str(channel2)+"_price.txt", "w")
                        f.write(str(price))
                        f.close()
                        ID = str((ID['orderId']))
                        f = open(str(channel)+".txt", "w")
                        f.write(str(ID))
                        f.close()                            
                    else:
                        msg = (ID['message'])
                        await client.send_message(igroup, msg)

                    PID = str((ID['orderId']))
                    f = open(str(channel2)+".txt", "w")
                    await connection.get_symbol_price(symbol='XAUUSD')
                    f.write(str(PID))
                    f.close()      

                elif tp1 == "":
                    #ID=await connection.create_market_sell_order(pair, 0.01,float(sl),float(tp1))
                    c_price = await connection.get_symbol_price(symbol='XAUUSD')
                    c_price = float(c_price['bid'])
                    if price <= c_price:
                        ID = await connection.create_market_sell_order(pair, 0.01, float(sl),float(tp1))
                    else:
                        ID = await connection.create_limit_sell_order(pair, 0.01, price ,float(sl),float(tp1))
                    await client.send_message(igroup, "Order Placed 🎯")   
                    f = open(str(channel2)+"_price.txt", "w")
                    f.write(str(price))
                    f.close()
                    ID = str((ID['orderId']))
                    f = open(str(channel2)+".txt", "w")
                    f.write(str(ID))
                    f.close()       
                else:
                    await client.send_message(igroup, 'Trading Not Placed \n Check this string  \n '+str(tstring))                 
            else:
                pass
                
        elif tstring[1] == 'Scalper can close all if satisfied. Set BE to hold your position.':
            ACCOUNT_ID = "7c348b78-2c13-4340-9875-e1d241cb0323"
            account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
            initial_state = account.state
            deployed_states = ['DEPLOYING', 'DEPLOYED']
            if initial_state not in deployed_states:
                await account.deploy()
            await account.wait_connected()
            connection = account.get_rpc_connection()
            await connection.connect()
            await connection.wait_synchronized()          
            f = open(str(channel2)+".txt", "r")
            ID = str(f.read())
            try:
                cancel = await connection.close_position(ID)
            except:
                cancel = await connection.cancel_order(ID)
            await client.send_message(igroup, str(cancel))  

        else:
            pass
        print(tstring)


client.start()
client.run_until_disconnected()

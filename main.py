# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 06:09:33 2021

@author: Quentin Tedeschi
"""
from maze import create_maze, printMaze
from agent import Agent_1
from agent2 import Agent_2
from agent3 import Agent_3
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

if __name__ == '__main__':
	width = 30
	height = 15
	maze = create_maze(height, width)
	
	agents = list()
	port = int(argv[1])
   
	agent_1 = Agent_1(AID(name='agent_1@localhost:{}'.format(port)))
	agent_1.init_maze(maze)
	agents.append(agent_1)
	port += 1
   
	agent_2 = Agent_2(AID(name='agent_2@localhost:{}'.format(port)))
	agent_2.init_maze(maze)
	agents.append(agent_2)
	port += 1
  
	agent_3 = Agent_3(AID(name='agent_3@localhost:{}'.format(port)))
	agent_3.init_maze(maze)
	agents.append(agent_3)

	start_loop(agents)
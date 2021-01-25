from random import randrange
from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from sys import argv
from pade.acl.filters import Filter
import pickle

class Agent_1(Agent):
    def __init__(self, aid):
        super(Agent_1, self).__init__(aid=aid, debug=False)
        self.pos = [0,0]
        self.back = 0
        self.escaped = 0
    def init_maze(self, maze):
        self.maze = maze
        self.width = len(maze)
        self.height = len(maze[0])
        self.init_pos()
    def init_pos(self):
        while(self.maze[self.pos[0]][self.pos[1]] == '1'):
            self.pos[0] = randrange(self.width)
            self.pos[1] = randrange(self.height)
    def on_start(self):
        super(Agent_1, self).on_start()
        display_message(self.aid.localname, "Recherche de la sortie...")
        self.call_later(10.0, self.escape)
    def sending_pos(self):
        #display_message(self.aid.localname, "Dead end found : sending to agent_2")
        message = ACLMessage(ACLMessage.PROPOSE)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.set_sender(AID('agent_1'))
        message.add_receiver(AID('agent_2'))
        message.set_ontology("deadend")
        pos = {'posx' : self.pos[0], 'posy' : self.pos[1]}
        pos_encp = pickle.dumps(pos)
        message.set_content(pos_encp)
        self.send(message)
        #display_message(self.aid.localname, "Dead end found : sending to agent_3")
        message.add_receiver(AID('agent_3'))
        self.send(message)
    def react(self, message):
        super(Agent_1, self).react(message)
        perPRO="propose"
        ontoPRO="deadend"
        if message.performative==perPRO and message.ontology==ontoPRO:
            pos_encp = message.content
            pos = pickle.loads(pos_encp)
            self.maze[pos['posx']][pos['posy']] = 'X'
    def check_surroundings(self):
        if self.pos[1] != self.height-1:
            north = [[self.pos[0], self.pos[1]+1],self.maze[self.pos[0]][self.pos[1]+1]]
        else:
            north = None
        if self.pos[1] != 0:
            south = [[self.pos[0], self.pos[1]-1],self.maze[self.pos[0]][self.pos[1]-1]]
        else:
            south = None
        if self.pos[0] != 0:
            west = [[self.pos[0]-1,self.pos[1]], self.maze[self.pos[0]-1][self.pos[1]]]
        else:
            west = None
        if self.pos[0] != self.width-1:
            east = [[self.pos[0]+1,self.pos[1]], self.maze[self.pos[0]+1][self.pos[1]]]
        else:
            east = None
        return [north, south, west, east]
    
    def move(self):
        surroundings = self.check_surroundings()
        legal_move = []
        marked_move = []
        for cardinal in surroundings:
            if cardinal is None:
                self.escaped = 1
                return self.pos
            if cardinal[1] == '0':
                legal_move.append(cardinal)
            if cardinal[1] == 'X' :
                marked_move.append(cardinal)
        if len(legal_move) == 1:
            self.maze[self.pos[0]][self.pos[1]] = 'U'
            self.sending_pos()
            self.back = self.pos
            self.pos = legal_move[0][0]
            return self.pos
        if len(legal_move) == 0:
            if len(marked_move) == 1:
                self.maze[self.pos[0]][self.pos[1]] = 'U'
                self.sending_pos()
                self.back = self.pos
                self.pos = marked_move[0][0]
            else:
                for move in marked_move:
                    if move[0] == self.back:
                        marked_move.remove(move)
                self.back = self.pos
                self.pos = marked_move[randrange(len(marked_move))][0]
            return self.pos
        else:
            for move in legal_move:
                if move[0] == self.back:
                    legal_move.remove(move)
            self.back = self.pos
            self.pos = legal_move[randrange(len(legal_move))][0]
            return self.pos
    def escape(self):
        while self.escaped == 0:
            self.move()
        print('Agent 1 escaped!')
        print(self.escaped)
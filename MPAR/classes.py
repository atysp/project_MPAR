from grammaire.gramListener import gramListener

class State:
    def __init__(self, id,gain):
        self.id = id
        self.gain = gain
        
    def __repr__(self):
        return(f"State({self.id})")


class Action:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return(f"Action({self.id})")

class Transition:
    def __init__(self, departure, action, targets, weights):
        self.departure = departure
        self.action = action
        self.targets = targets
        self.weights = weights 
    
    def __repr__(self):
        return (f'Transition({self.departure}, {self.action}, {self.targets}, {self.weights})')

class gramPrintListener(gramListener):
    def __init__(self):
        pass
        
    def enterDefstates(self, ctx):
        print("States: %s" % str([str(x) for x in ctx.ID()]))

    def enterDefactions(self, ctx):
        print("Actions: %s" % str([str(x) for x in ctx.ID()]))

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with action "+ act + " and targets " + str(ids) + " with weights " + str(weights))
        
    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with no action and targets " + str(ids) + " with weights " + str(weights))


class gramDataListener(gramListener):
    def __init__(self):
        self.states = []
        self.actions = []
        self.transitions = []

    def enterStatenoreward(self, ctx):
        for x in ctx.ID():
            self.states.append(State(str(x),""))
            
    def enterStatereward(self, ctx):
        for k in range (len(ctx.ID())):
            self.states.append(State(str(ctx.ID()[k]), (str(ctx.INT()[k])) ))

    def enterDefactions(self, ctx):
        for x in ctx.ID():
            self.actions.append(Action(str(x)))

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        ids = [State(x,"") for x in ids]
        weights = [int(str(x)) for x in ctx.INT()]
        self.transitions.append(Transition(State(dep,""), Action(act), ids, weights))

    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        ids = [State(x,"") for x in ids]
        self.transitions.append(Transition(State(dep,""),Action(""), ids, weights))
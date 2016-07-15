import nuke
import re

def findAllNodes(expression):
    curNodeList = []
    expression = expression.replace("parent.", "")
    nodeKnob = re.compile('[A-Za-z0-9_.]+')
    findedNodes = nodeKnob.findall(expression)
    for findedNode in findedNodes:
        nodeName = findedNode.split('.')
        curNodeList.append(nodeName[0])
    return curNodeList

def openBaseNode(openFloat = True):
    nodeList = []
    nodes = nuke.selectedNodes()
    for sn in nodes:
        for knob in sn.knobs():
            curKnob = sn['%s'%knob]
            if curKnob.hasExpression():
                knobValue = curKnob.getValue()
                knobType = type(knobValue)
                if knobType is float:
                    curFloatExpression = curKnob.animation(0).expression()
                    foundNodesFloat = findAllNodes(curFloatExpression)
                    nodeList.extend(foundNodesFloat)
                if knobType is list:
                    for i in range(0, len(knobValue)):
                        try:
                            curListExpression =  curKnob.animation(i).expression()
                            foundNodesList = findAllNodes(curListExpression)
                            nodeList.extend(foundNodesList)
                        except:
                            pass

    nodeList = list(set(nodeList))
    for node in nodeList:
        n = nuke.toNode('%s'%node)
        nuke.show(n, forceFloat = openFloat)

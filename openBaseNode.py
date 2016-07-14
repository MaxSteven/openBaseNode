import nuke

def openBaseNode(float = True):
    sn = nuke.selectedNode()
    for knob in sn.knobs():
        if sn['%s'%knob].hasExpression():
            expression = sn['%s'%knob].animation(0).expression()
            expression = expression.replace("parent.", "")
            nodeName = expression.split('.')
            n = nuke.toNode('%s'%nodeName[0])
            nuke.show(n, forceFloat = float)
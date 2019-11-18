import sys,statistics

def extractAverages(rawCsv):
    raw=rawCsv.replace('",','%%%').replace('"','')
    lines=[s.split('%%%') for s in raw.split('\\n')]
    head=[h.lower() for h in lines.pop(0)]
    numerical={key: [] for key in head}
    for line in lines:
        for key,val in zip(head,line):
            try:
                numerical[key].append(int(val))
            except:
                pass #Qualitative
    numerical={key:statistics.mean(val) for key,val in numerical.items() if len(val)>0}
    return numerical
if __name__=='__main__':
    filename=sys.argv[1]
    numerical={}
    with open(filename) as f:
        raw=f.read()
        numerical=extractAverages(raw)
    print(numerical)
                                          
                


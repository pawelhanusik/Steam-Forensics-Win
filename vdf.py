def parse(filepath):
    data = {}
    section = []
    sectionDepth = 0

    f = open(filepath)
    line = True
    while line:
        line = f.readline()
        s = line.split('"')
        
        if len(s) == 3:
            subSectionName = s[1]
            while len(section)-1 < sectionDepth:
                section += ['']
            section[sectionDepth] = subSectionName
        elif len(s) == 1:
            if line.find('{') >= 0:
                sectionDepth += 1
            elif line.find('}') >= 0:
                if len(section) > sectionDepth:
                    section[sectionDepth] = ''
                sectionDepth -= 1
        elif len(s) == 5:
            key = s[1]
            value = s[3]

            subData = data
            for subSectionName in section:
                if not subSectionName in subData:
                    subData[subSectionName] = {}
                subData = subData[subSectionName]
            subData[key] = value
            
    f.close()

    return data

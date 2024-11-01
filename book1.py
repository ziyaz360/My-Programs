#def collatz(number):
##    if number%2==0:
##        result=number//2
##    else:
##        result=3*number+1
##    print(result)
##    return result
##
##number=input("Enter an integer:")
##if number==str("k"):
##        continue
##n=int(number)
##while n!=1:
##    number=collatz(number)
##    if number==str("k"):
##        continue
##print("ziya\"s phone")
##print('ziya\'s phone')
##print('ziya\t phone')
##print('ziya\n 360')
##print('ziya\\ 360')
##print('''Dear sana,
##It's ziya i am waiting for you i dont know
##when you are going to accenpt my proposal but
## if you do like me please , i will get placed soon please mary
## me''')
##print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
##"""This is a test python program.
##written by ziya ziyax360@gmail.com
##
##this is designed for py 1 and 2 not 3"""
##def spam():
##    """This is a multiline comment to help
##     explain what  spam() function does."""
##    print("hello" )
##
##spam()
##def Energy(trail):
##    TotalEnergy=0
##    for i in range(len(trail)-1):
##        if trail[i+1]>trail[i]:
##            TotalEnergy=TotalEnergy+(trail[i+1]-trail[i])
##    return TotalEnergy
##trail=[1,3,2,5,4,7]
##result=Energy(trail)
##print(result)

##def CalculateEnergy(panels):
##    TotalEnergy=0.0
##    for panel in panels:
##        panelEnergy=panel["max_capacity"]*panel["efficiency_factor"]
##        TotalEnergy += panelEnergy
##    return round(TotalEnergy, 2)
##panels = [
##    {"max_capacity": 100, "efficiency_factor": 0.8},
##    {"max_capacity": 150, "efficiency_factor": 0.6},
##    {"max_capacity": 200, "efficiency_factor": 0.75}
##]
##Total=CalculateEnergy(panels)
##print(Total)

##def FindCombinations(snacks,target,combination=[]):
##    if target == 0:
##        print("+".join(combination))
##        return 1
##    if target < 0:
##        return 0
##    
##    TotalCombinations=0
##    for snack,spiciness in snacks:
##        TotalCombinations += FindCombinations(snacks,target-spiciness,combination+[snack])
##
##    return TotalCombinations
##snacks = [("Samosa",5),("Ketchup",2),("Chips",3),("Spicy Nuts",4)]
##target_spiciness = 7
##result = FindCombinations(snacks, target_spiciness)
##print(f"Total Combinations: {result}")

##def SignalReach(remote_position,remote_range,tv_position):
##    RemoteX,RemoteY=remote_position
##    TvX,TvY=tv_position
##    if RemoteX==TvX:
##        if abs(TvY-RemoteY)<=remote_range:
##            return True
##    elif RemoteY==TvY:
##        if abs(TvX-RemoteX)<=remote_range:
##            return True
##    return False
##remote_position=(2,3)
##remote_range=4
##tv_position=(2,6)
##result=SignalReach(remote_position,remote_range,tv_position)
##print(result)
##def HorizontalPoints(building_heights):
##    HorizontalPoints=[]
##    MaxHeight=-1
##    for i in range(len(building_heights)):
##        if building_heights[i]> MaxHeight:
##            HorizontalPoints.append(i)
##            MaxHeight=building_heights[i]
##    return HorizontalPoints
##building_heights=[3,1,5,2,6]
##result=HorizontalPoints(building_heights)
##print(result)
##def Path(directions):
##    UD,LR=0,0
##    for direction in directions:
##        if direction=='U':
##            UD+=1
##        elif direction=='D':
##            UD-=1
##        elif direction=='L':
##            LR-=1
##        elif direction=='R':
##            LR+=1
##    return UD==0 and LR==0
##Dir="UDLLRRDDRULU"
##result=Path(Dir)
##print(result)
##def ArrangeTitles(n,titles):
##    ArrangeTitles=sorted(titles)
##    return ArrangeTitles
##n=5
##titles=["Introduction","Conclusion","Appendix","History","Methods"]
##result=ArrangeTitles(n,titles)
##print(result)

##def rearrange_chords(s):
##    freq = {}
##    for chord in s:
##        if chord in freq:
##            freq[chord] += 1
##        else:
##            freq[chord] = 1
##    max_freq = 0
##    max_chord = ''
##    for chord in freq:
##        if freq[chord] > max_freq:
##            max_freq = freq[chord]
##            max_chord = chord
##    if max_freq > (len(s) + 1) // 2:
##        return "Not Possible"
##    result = [""] * len(s)
##    index = 0
##    while freq[max_chord] > 0:
##        result[index] = max_chord
##        index += 2
##        freq[max_chord] -= 1
##    for chord in freq:
##        while freq[chord] > 0:
##            if index >= len(s):
##                index = 1
##            result[index] = chord
##            index += 2
##            freq[chord] -= 1
##    return ''.join(result)
##s1 = "AAABBBCCC"
##s2 = "AAAAA"
####print(rearrange_chords(s1))
####print(rearrange_chords(
##from collections import Counter
##import heapq
##def ArrangeChords(s):
##    Count=Counter(s)
##    MaxCount=[]
##    for chord,count in Count.items():
##        heapq.heappush(MaxCount,(-count,chord))
##    result=[]
##    BeforeCount,BeforeChord=0,''
##    while MaxCount:
##        count,chord= heapq.heappop(MaxCount)
##        result.append(chord)
##        if BeforeCount< 0:
##            heapq.heappush(MaxCount,(BeforeCount,BeforeChord))
##        BeforeCount,BeforeChord=count+1,chord
##    if len(result)==len(s):
##        return ''.join(result)
##    else:
##        return "Not Possible"
##s1 = "AAABBBCCC"
##s2 = "AAAAA"
##print(ArrangeChords(s1))
##print(ArrangeChords(s2))
##def EncryptKeywords(n,keywords,shift_value):
##    EncryptedKeywords=[]
##    
##    for keyword in keywords:
##        EncryptedWord=''
##        for char in keyword:
##            if char.islower():
##                EncryptedWord+=chr((ord(char)-ord('a')+shift_value)%26+ord('a'))
##            elif char.isupper():
##                EncryptedWord+=chr((ord(char)- ord('A')+shift_value)%26+ord('A'))
##            else:
##                EncryptedWord+=char
##        EncryptedKeywords.append(EncryptedWord)
##    return EncryptedKeywords
##n=3
##keywords=["Hello","Journal","Secret"]
##shift_value = 3
##print(EncryptKeywords(n,keywords,shift_value))
##def Destination(distance,fuel):
##    MaximumDistance=24
##    ExtraFuel=30
##    TotalFuel=0
##    while distance>0:
##        if distance<=MaximumDistance:
##            TotalFuel+=1
##            break
##        else:
##            TotalFuel+=1
##            distance-=MaximumDistance
##            MaximumDistance-=1
##    return TotalFuel<= fuel
##distance1=900
##fuel1=90
##distance2=400
##fuel2=17
##print(Destination(distance1,fuel1))
##print(Destination(distance2,fuel2))
##def can_reach_destination(distance, fuel):
##    # Calculate how many litres the car needs to travel the distance
##    initial_efficiency = 24  # Maximum efficiency (24 km per litre)
##    extra_fuel_km = 30  # Every 30 km, the car consumes 1 extra litre
##
##    total_fuel_needed = 0  # Track total fuel consumption
##    while distance > 0:
##        if distance <= initial_efficiency:
##            total_fuel_needed += 1  # If remaining distance is less than max efficiency, use 1 litre
##            break
##        else:
##            # For every 30 km, we need extra fuel
##            total_fuel_needed += 1
##            distance -= initial_efficiency
##            initial_efficiency -= 1  # Efficiency drops by 1 km/l after 30 km
##    
##    return total_fuel_needed <= fuel
##
### Example Input
##distance1 = 900
##fuel1 = 90
##distance2 = 400
##fuel2 = 17
##
### Outputs
##print(can_reach_destination(distance1, fuel1))  # Output: True
##print(can_reach_destination(distance2, fuel2))  # Output: False
##def LongPath(n,m,grid):
##    Direction=[(-1,0),(1,0),(0,-1),(0,1)]
##    def dfs(x,y,path):
##        PathNow=path+[(x,y)]
##        BestPath=PathNow
##        for dx,dy in directions:
##            nx,ny=x+dx,y+dy
##            if 0<=nx<n and 0<=ny<m and grid[nx][ny]>grid[x][y]:
##                NewPath =dfs(nx,ny,PathNow)
##                if len(NewPath)>len(BestPath):
##                    BestPath=NewPath
##                elif len(NewPath)==len(BestPath)and sum(grid[i][j] for i,j in NewPath)>sum(grid[i][j] for i,j in BestPath):
##                    BestPath=NewPath  
##        return BestPath
##    LongestPath=[]
##    for i in range(n):
##        for j in range(m):
##            path= dfs(i,j,[])
##            if len(path) > len(LongestPath):
##                LongestPath=path
##            elif len(path)==len(LongestPath) and sum(grid[x][y] for x, y in path) > sum(grid[x][y] for x, y in longest_path):
##                LongestPath=path
##    return LongestPath
##n=4
##m=5
##grid=[[10, 12, 14, 13, 9],
##      [9, 11, 15, 14, 8],
##      [8, 10, 12, 16, 7],
##      [7, 9, 11, 10, 6]]
##print(LongPath(n,m,grid))
##def LongPath(n,m,grid):
##    Direction=[(-1,0),(1,0),(0,-1),(0,1)]
##    def dfs(x, y, path):
##        PathNow = path + [(x, y)]
##        BestPath = PathNow
##        for dx, dy in Direction:
##            nx, ny = x + dx, y + dy
##            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > grid[x][y]:
##                NewPath = dfs(nx, ny, PathNow)
##                if len(NewPath) > len(BestPath):
##                    BestPath = NewPath
##                elif len(NewPath) == len(BestPath) and sum(grid[i][j] for i, j in NewPath) > sum(grid[i][j] for i, j in BestPath):
##                    BestPath = NewPath  
##        return BestPath
##    LongestPath = []
##    for i in range(n):
##        for j in range(m):
##            path = dfs(i, j, [])
##            if len(path) > len(LongestPath):
##                LongestPath = path
##            elif len(path) == len(LongestPath) and sum(grid[x][y] for x, y in path) > sum(grid[x][y] for x, y in LongestPath):  # Use 'LongestPath'
##                LongestPath = path
##    return LongestPath
##n = 4
##m = 5
##grid = [
##    [10, 12, 14, 13, 9],
##    [9, 11, 15, 14, 8],
##    [8, 10, 12, 16, 7],
##    [7, 9, 11, 10, 6]
##]
##print(LongPath(n, m, grid))
##def LongestWord(words,ch):
##    LongestWord=""
##    for word in words:
##        if word.startswith(ch):
##            if len(word)>len(LongestWord):
##                LongestWord=word
##    return LongestWord
##words1=["explore","adventure","uncharted","endless","expedition"]
##ch1='e'
##print(LongestWord(words1,ch1))
##words2=["quest","voyage","map","horizon"]
##ch2='a'
##print(LongestWord(words2,ch2))
##def RangersNeeded(rhino_counts,max_rhinos_per_ranger):
##    TotalRangers=0
##    for rhinos in rhino_counts:
##        RangersZone=(rhinos+max_rhinos_per_ranger-1)//max_rhinos_per_ranger
##        TotalRangers+=RangersZone
##    return TotalRangers
##rhino_counts =[10,8,15,12]
##max_rhinos_per_ranger=10
##print(RangersNeeded(rhino_counts,max_rhinos_per_ranger))

##def MaxStories(story_durations,total_time):
##    story_durations.sort()
##    StoryCount=0
##    TimeUsed=0
##    for duration in story_durations:
##        if TimeUsed+duration<=total_time:
##            TimeUsed+=duration
##            StoryCount+=1
##        else:
##            break
##    return StoryCount
##story_durations=[10,15,20,5,30]
##total_time=50
##print(MaxStories(story_durations,total_time))

##def countRustySpots(rust_grid,max_allowable_rust):
##    count=0
##    for row in rust_grid:
##        for RustLevel in row:
##            if RustLevel>max_allowable_rust:
##                count+=1
##    return count
##rust_grid = [
##    [1, 3, 5, 2],
##    [4, 6, 8, 3],
##    [7, 2, 1, 5],
##    [3, 4, 6, 2]
##]
##max_allowable_rust=4
##print(countRustySpots(rust_grid,max_allowable_rust))

##def ScareCrows(farm):
##    ScarecrowCount=0
##    i=0
##    while i<len(farm):
##        if farm[i]=='C':
##            if i+1<len(farm) and farm[i+1]=='.':
##                ScarecrowCount+=1
##                i+=3
##            elif i-1>=0 and farm[i-1]=='.':
##                ScarecrowCount+=1
##                i+=2
##            elif i+2<len(farm) and farm[i+2]=='.':
##                ScarecrowCount+=1
##                i+=4
##            else:
##                return -1
##        else:
##            i+=1
##    return ScarecrowCount
##farm_1='C..C.C.C..'
##print(ScareCrows(farm_1))
##farm_2='C.C.#C.CC'
##print(ScareCrows(farm_2))
##def covered(grid):
##    rows,cols=len(grid),len(grid[0])
##    def cover(r,c):
##        covered[r][c]=True
##        directions=[(-1,0),(1,0),(0,-1),(0,1)]
##        for dr,dc in directions:
##            nr,nc=r+dr,c+dc
##            if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]!='X':
##                covered[nr][nc]=True
##    covered=[[False for _ in range(cols)] for _ in range(rows)]
##    for r in range(rows):
##        for c in range(cols):
##            if grid[r][c]=='C':
##                cover(r,c)
##    for r in range(rows):
##        for c in range(cols):
##            if grid[r][c]=='.' and not covered[r][c]:
##                return False
##    return True
##grid = [
##    ['C', '.', '.', '.'],
##    ['X', '.', 'C', '.'],
##    ['.', '.', 'X', 'C']
##]
##print(covered(grid))

##def Makers(road):
##    n=len(road)
##    markers=0
##    i=0
##    while i<n:
##        if road[i]==1:
##            markers+=1
##            i+=3
##        else:
##            i+= 1
##    return markers
##road1=[1,0,1,1,0,1]
##road2=[1,0,0,1,1,0,1]
##print(Makers(road1))
##print(Makers(road2))

##def Compress(words):
##    result=[]
##    for word in words:
##        Target="JUMBO"
##        Index=0        
##        for char in word:
##            if char==Target[Index]:
##                Index+=1
##            if Index==len(Target):
##                result.append("JUMBO")
##                break
##        else:
##            result.append(word)
##    return result
##words=["jumbo","robot","abjuvombo"]
##print(Compress(words))

##def Compress(words):
##    result=[]
##    for word in words:
##        target="JUMBO"
##        index=0        
##        for char in word:
##            if char.upper()==target[index]:
##                index+=1
##            if index==len(target):
##                result.append("JUMBO")
##                break
##        else:
##            result.append(word)
##    return result
##words = ["jumbo", "robot", "abjuvombo"]
##print(Compress(words))

##def Island(grid):
##    rows=len(grid)
##    cols=len(grid[0])    
##    def dfs(x,y):
##        if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]==0:
##            return
##        grid[x][y]=0
##        dfs(x+1,y)
##        dfs(x-1,y)
##        dfs(x,y+1)
##        dfs(x,y-1)
##    NoOfIsland=0
##    for i in range(rows):
##        for j in range(cols):
##            if grid[i][j]==1:
##                dfs(i,j)
##                NoOfIsland+=1
##    return NoOfIsland
##grid1=[
##    [1,1,0,0,0],
##    [1,1,0,0,1],
##    [0,0,0,1,1],
##    [0,0,0,0,0],
##    [1,0,1,0,1]
##]
##print(Island(grid1))

##def balance_bowing_pattern(BowingPattern):
##    DownBows = BowingPattern.count('D')
##    UpBows = BowingPattern.count('U')
##    Difference = abs(DownBows - UpBows)
##    if Difference <= 1:
##        return True, BowingPattern
##    ExcessDown = (DownBows - UpBows) // 2 if DownBows > UpBows else 0
##    ExcessUp = (UpBows - DownBows) // 2 if UpBows > DownBows else 0
##    Modified = list(BowingPattern)
##    Replacements = 0
##    if ExcessDown > 0:
##        for i in range(0, len(Modified), 2):
##            if Modified[i] == 'D' and Replacements < ExcessDown:
##                Modified[i] = 'U'
##                Replacements += 1
##        if Replacements < ExcessDown:
##            return False, BowingPattern
##    Replacements = 0
##    if ExcessUp > 0:
##        for i in range(1, len(Modified), 2):
##            if Modified[i] == 'U' and Replacements < ExcessUp:
##                Modified[i] = 'D'
##                Replacements += 1
##        if Replacements < ExcessUp:
##            return False, BowingPattern
##    return True, ''.join(Modified)
##print(balance_bowing_pattern("DUDUUUUUD"))
##print(balance_bowing_pattern("DUDUUDUD"))

##def TotalDistance(Landmarks):
##    TotalDistance=0.0
##    for i in range(len(Landmarks) - 1):
##        x1,y1=Landmarks[i]
##        x2,y2=Landmarks[i+1]        
##        Distance=((x2-x1)**2+(y2-y1)**2)**0.5
##        TotalDistance+=Distance
##    return round(TotalDistance,2)
##Landmarks=[(1,2),(4,6),(8,10)]
##print(TotalDistance(Landmarks))



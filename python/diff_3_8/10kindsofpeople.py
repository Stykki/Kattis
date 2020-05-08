

class runner:

    def __init__(self, start, end, max_x, max_y, run_map):
        self.binr = 0
        self.pos_x = int(start[0]) -1
        self.pos_y = int(start[1]) -1

        self.end_x = int(end[0]) -1
        self.end_y = int(end[1]) -1
        
        self.max_x = int(max_x) -1
        self.max_y = int(max_y) -1

        self.rum_map = run_map
        self.prev_nodes = []

    def base_run(self):
        binary = self.run(self.pos_x, self.pos_y)
        self.binr = 1
        self.prev_nodes = []
        decimal = self.run(self.pos_x, self.pos_y)
        if not binary and not decimal:
            print('neither')
        if binary:
            print('binary')
        if decimal:
            print("decimal")
            

    def run(self, where_x, where_y):
        #item = self.rum_map[where_x][where_y]
        #self.rum_map[where_x][where_y] = "x"
        #print("new step")
        #for line in self.rum_map:
        #    print(line)
        #self.rum_map[where_x][where_y] = item
        
        if self.binr != int(self.rum_map[where_x][where_y]):
            return False
        if where_x == int(self.end_x) and where_y == int(self.end_y) and int(self.rum_map[where_x][where_y]) == int(self.binr):
            return True
        self.prev_nodes.append((where_x, where_y))
        passed = False
        if (where_x + 1 < self.max_x and (where_x+1, where_y) not in self.prev_nodes): # CREATE [X][Y] AND/OR [Y][X]
            passed = passed or self.run(where_x+1, where_y)

        if (where_y + 1  < self.max_y and (where_x, where_y+1) not in self.prev_nodes):
            passed = passed or self.run(where_x, where_y+1)

        if (where_y - 1  > 0 and (where_x, where_y-1) not in self.prev_nodes):
            passed = passed or self.run(where_x, where_y-1)

        if (where_x - 1  > 0 and ((where_x-1, where_y)) not in self.prev_nodes):
            passed = passed or self.run(where_x-1, where_y )

        return passed

        


       





def main():
    x, y = input().split(" ")
    x, y = int(x), int(y)
    
    map_list = []

    for i in range(0, x):
        map_list.append(list(input()))

    queries = input()
    queries = int(queries)
    queries_list = []

    for i in range(0, int(queries)):
        queries_list.append(input().split(" "))
    
    for i in range(0, int(queries)):
        temp_runner = runner((queries_list[i][0], queries_list[i][1]),(queries_list[i][2],
            queries_list[i][3]), x, y, map_list )
        temp_runner.base_run()
    

main()

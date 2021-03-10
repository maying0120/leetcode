class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food  =  food
        self.food_index = 0
        self.movement = {'U':[-1,0],'L':[0,-1],'R':[0,1],'D':[1,0]}
        self.snake = deque([(0,0)])
        self.snake_set = {(0,0) : 1}
        
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        newhead = (self.snake[0][0] + self.movement[direction][0],
                   self.snake[0][1] + self.movement[direction][1])
        
        #check if the snakes hits the boundary
        bound_1 = newhead[0] < 0 or newhead[0] >= self.height
        bound_2 = newhead[1] < 0 or newhead[1] >= self.width
        
        #check the snake to bites itself,current tail is not the part of the snake body
        bites = newhead in self.snake_set and newhead !=self.snake[-1]
        
        if bound_1 or bound_2 or bites: return -1
        
        next_food_item = self.food[self.food_index] if self.food_index<len(self.food) else None
        
            # If there's an available food item and it is on the cell occupied by the snake after the move, eat it
        if self.food_index < len(self.food) and next_food_item[0]==newhead[0] and next_food_item[1]==newhead[1]: 
            #eat it
            self.food_index += 1 
        else:
            tail = self.snake.pop()
            del self.snake_set[tail]
        
        # A new head always gets added
        self.snake.appendleft(newhead)
        
        self.snake_set[newhead] = 1
            
        return len(self.snake) - 1
            
            
            
        
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
from functools import wraps
from time import time

import numpy
from random import randint

DICE_SIDES              =   4

TOTAL_TURNS             =   (10 ** 7) * 1

MOST_FREQUENT_CELLS     =   3

class Monopoly:
    MONOPOLY_BOARD_CELLS_NUMBER     =   40
    
    COMMUNITY_CHEST_CARDS_NUMBER    =   16
    CHANCE_CARDS_NUMBER             =   16
    
    GO_INDEX                        =   0                     
    JAIL_CELL_INDEX                 =   10
    C1_INDEX                        =   11
    E3_INDEX                        =   24
    H2_INDEX                        =   39
    
    R1_INDEX                        =   5
    R2_INDEX                        =   15
    R3_INDEX                        =   25
    
    U1_INDEX                        =   12
    U2_INDEX                        =   28
    
    CH1_INDEX                       =   7
    CH2_INDEX                       =   22
    CH3_INDEX                       =   36
    
    G2J_INDEXES                     =   [ 30 ]
    CH_INDEXES                      =   [ CH1_INDEX, CH2_INDEX, CH3_INDEX ]
    CC_INDEXES                      =   [ 2, 17, 33 ]
    
    def __init__(self, dice_sides = 6):
        self.current_chance_index           = 0
        self.current_commmunity_chest_index = 0
        self.doubles_go_to_jail_treshold    = 2
        self.dices_number                   = 2
        self.turn_number                    = 0
        self.consecutive_doubles_counter    = 0
        self.dice_sides                     = dice_sides
        self._board_cells_hit_counter       = [0] * Monopoly.MONOPOLY_BOARD_CELLS_NUMBER
        self.current_cell_index             = 0
        self._init_game_logic()
    
    def _init_game_logic(self):
        # Special Cells Handlers
        def chance_handler():
            GO_NEXT_R_CHANCE_CARDS_INDEXES      = [ 6, 7 ]
            GO_NEXT_U_CHANCE_CARDS_INDEXES      = [ 8 ]
            GO_BACK_3_CHANCE_CARDS_INDEXES      = [ 9 ]
            chance_routing_cells                = [ Monopoly.GO_INDEX, Monopoly.JAIL_CELL_INDEX, Monopoly.JAIL_CELL_INDEX, Monopoly.C1_INDEX, Monopoly.E3_INDEX, Monopoly.H2_INDEX, Monopoly.R1_INDEX ]
            self.current_chance_index           = ( 1 + self.current_chance_index ) % Monopoly.CHANCE_CARDS_NUMBER
            # If chance routing
            if len(chance_routing_cells) > self.current_chance_index:
                self.current_cell_index         = chance_routing_cells[self.current_chance_index]
            # Else, if 'Go to next R (railway company)'
            elif self.current_chance_index in GO_NEXT_R_CHANCE_CARDS_INDEXES:
                NEXT_R_CELL_DICTIONARY          = \
                    {
                        Monopoly.CH1_INDEX : Monopoly.R2_INDEX,
                        Monopoly.CH2_INDEX : Monopoly.R3_INDEX,
                        Monopoly.CH3_INDEX : Monopoly.R1_INDEX
                    } 
                self.current_cell_index         = NEXT_R_CELL_DICTIONARY[self.current_cell_index]
            # Else, if 'Go to next U (utility company)'
            elif self.current_chance_index in GO_NEXT_U_CHANCE_CARDS_INDEXES:
                NEXT_U_CELL_DICTIONARY          = \
                    {
                        Monopoly.CH1_INDEX : Monopoly.U1_INDEX,
                        Monopoly.CH2_INDEX : Monopoly.U2_INDEX,
                        Monopoly.CH3_INDEX : Monopoly.U1_INDEX
                    } 
                self.current_cell_index         = NEXT_U_CELL_DICTIONARY[self.current_cell_index]
            # Else, if 'Go back 3 squares'
            elif self.current_chance_index in GO_BACK_3_CHANCE_CARDS_INDEXES:
                self.current_cell_index         -= 3
        def community_chest_handler():
            community_chest_routing_cells       = [ Monopoly.GO_INDEX, Monopoly.JAIL_CELL_INDEX ]
            self.current_commmunity_chest_index = ( 1 + self.current_commmunity_chest_index ) % Monopoly.COMMUNITY_CHEST_CARDS_NUMBER
            if len(community_chest_routing_cells) > self.current_commmunity_chest_index:
                self.current_cell_index         = community_chest_routing_cells[self.current_commmunity_chest_index]
        def go_to_jail_handler():
            self.current_cell_index             = Monopoly.JAIL_CELL_INDEX
        self.go_to_jail_handler = go_to_jail_handler
        # Initialize special cells handlers
        self.special_cells_handlers             = \
            [
                ( Monopoly.CH_INDEXES,  chance_handler),
                ( Monopoly.CC_INDEXES,  community_chest_handler),
                ( Monopoly.G2J_INDEXES, go_to_jail_handler),
            ]
        
    def run_monopoly_turn(self):
        # Functions Section
        def roll_dice():
            return randint(1, self.dice_sides)
        def is_dices_double(dices_results):
            return 1 == len(set(dices_results))
        # Code Section
        # Roll dices
        dices_results = [ roll_dice() for _ in range(self.dices_number) ]
        # Update doubles counter
        self.consecutive_doubles_counter        = 0 if not is_dices_double(dices_results) else ++self.consecutive_doubles_counter
        # If reached doubles threshold
        if self.doubles_go_to_jail_treshold == self.consecutive_doubles_counter:
            self.consecutive_doubles_counter    = 0
            self.go_to_jail_handler()
        # Else, handle dices results sum
        else:
            # Calculate dices results sum
            dices_results_sum                   = sum(dices_results)
            # Update current cell index
            self.current_cell_index             = (self.current_cell_index + dices_results_sum) % Monopoly.MONOPOLY_BOARD_CELLS_NUMBER
            # Handle special cells
            for special_cells_indexes, special_cells_handler in self.special_cells_handlers:
                if self.current_cell_index in special_cells_indexes:
                    special_cells_handler()
        self._board_cells_hit_counter[self.current_cell_index] += 1

    def get_cells_by_frequency(self):
        return [ str(index) if index >= 10 else '0' + str(index) for index in numpy.argsort(self._board_cells_hit_counter)[::-1] ]

def play_monopoly(monopoly, turns_number = TOTAL_TURNS):    
    for _ in range(turns_number):
        monopoly.run_monopoly_turn()

def measure_time_tresholded_decorator(RUNTIME_THRESHOLD=60):
    def measure_time_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start       = time()
            result      = f(*args, **kwargs)
            end         = time()
            time_diff   = end-start
            if 60 < time_diff:
                print(f'Fails {RUNTIME_THRESHOLD} runtime threshold ({time_diff}s)')
            else:
                print(f'Elapsed time: {time_diff}s')        
            return result
        return wrapper
    return measure_time_decorator

# Main
@measure_time_tresholded_decorator()
def main():
    monopoly = Monopoly(dice_sides = DICE_SIDES)
    play_monopoly(monopoly)
    
    # 101524
    print(''.join(monopoly.get_cells_by_frequency()[:MOST_FREQUENT_CELLS]))
    
if __name__ == "__main__":
    main()

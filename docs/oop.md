# Classes
There are two main classes: Game and Player. Below are their attributes, methods and relationship with one another.

``` mermaid
classDiagram
    note "Game is a single object that has many Player objects."
    Game --|> Player
    class Game{
        +int plr_num
        +int maf_num
        +int discussion_time
        +bool include_doc
        +bool include_det
        +bool anonymous_voting
        +bool allow_skip
        +bool execute_if_tie
        +str host_name
        +str host_accent
        +str game_stage
        +int vote_count
        +list mafia_players
        +Player last_player_eliminated
        +Player doctor_player
        +Player detective_player

        +list players
        +list votes
        +list living_players
        +list dead_players
        +int skip_vote
        +int good_team_num
        +int bad_team_num
        +str winning_team

        +get_last_player_eliminated()
        +create_player(plr_name)
        +clear_player_list()
        +get_player(name)
        +set_stage(stage)
        +remove_dead_players(args)
        +reset_votes()
        +execute_voted_player(args)
        +game_is_over()
    }
    class Player{
        +str name
        +str role
        +str team 
        +bool is_alive
        +str audio_file
        +int votes
        
        +die()
        +heal()
        +reveal_team()
        +reveal_role()
        +final_reveal()
        +add_vote()
        +reset_vote()
    }

```

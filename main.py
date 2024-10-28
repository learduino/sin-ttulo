

scene.set_background_color(9)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """),
        SpriteKind.player))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE))
info.player1.set_life(3)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
    sprites.create(img("""
            8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
                8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
        """),
        SpriteKind.player))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO))
info.player2.set_life(3)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
    sprites.create(img("""
            7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 
                7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
        """),
        SpriteKind.player))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.THREE))
info.player3.set_life(3)
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
    sprites.create(img("""
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        """),
        SpriteKind.player))
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.FOUR))
info.player4.set_life(3)
scene.camera_follow_sprite(mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)))

def on_forever():
    effects.confetti.start_screen_effect()
forever(on_forever)

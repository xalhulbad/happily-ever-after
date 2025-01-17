# Contains the code associated with all of the princess monologues for after route endings.

# Default variables
default got_happily_ever_after = False
default got_saved_hero = False
default got_sacrificed_hero = False
default got_sacrificed_princess = False
default got_unfulfilled_love = False
default got_corrupted_hero = False
default got_inherited_throne = False
default got_forest_curse = False
default got_forest_protectors = False
default got_love_beyond_death = False


label happily_ever_after:
    if got_happily_ever_after:
        jump repeat_ending

    $ got_happily_ever_after = True

    stop music
    scene bg actual_blackscreen
    pause 2.5
    
    pt "The world beyond the tower and kingdom was more than I ever imagined. We chose a life together, free from the shadows of our past, a choice made not out of obligation, but out of a genuine desire to be with one another."
    pt "For so long, I believed that my story was one of waiting-to be rescued, to be saved. But I discovered something different. It was about finding my own strength, my courage to make decisions for myself."
    pt "In that moment, standing at the edge of the world, I felt a freedom I never knew existed. It was a choice to step into the unknown, to embrace independence and carve out a life that wasn't dictated by the rules."
    pt "I now know that I can be daring, and that I have the courage to face the world on my terms. That strength was always within me, waiting to be realized. Together, the hero and I forged a path that was uniquely ours."
    pt "Even in this quiet moment of reflection, I know that the decisions we made were ours alone. They were born from a place of love, courage, and the desire to live life authentically. That is the greatest lesson of all."
    
    window hide
    pause 3
    return

label saved_hero:
    if got_saved_hero:
        jump repeat_ending

    $ got_saved_hero = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "I never imagined I'd be the one to save him. The stories always cast me as the one needing rescue, but this time, I was the one who acted." 
    pt "Seeing him vulnerable, knowing that he depended on me... it changed something inside me."
    pt "I made the choice out of loyalty, to protect someone who mattered to me. In that moment, it wasn't about being a princess or a hero; it was about compassion, about the bonds we formed through our journey."
    pt "Strength isn't just about wielding a sword or breaking free from chains."
    pt "It's in the quiet moments, in the choice to put someone's well-being above your own fears. It's in taking initiative, in being the one to lead when the path seems uncertain."
    pt "As I cared for his wounds, I realized that I have the power to change the story, to protect and nurture those I care about."
    pt "Now, as I reflect, I know that this journey has reshaped me. I am not just a damsel in distress; I am capable of taking the lead."
    pt "It's not the end of the story, but a new beginning-one where I can be both protector and protected."
    
    window hide
    pause 3
    return

label sacrificed_hero:
    if got_sacrificed_hero:
        jump repeat_ending

    $ got_sacrificed_hero = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "He gave everything for me. In that final, heartbreaking moment, he chose to protect me, even at the cost of his own life. It's a sacrifice I can hardly fathom, and the weight of it is something I will carry forever."
    pt "The stories always speak of heroes and their noble deeds, but seeing him make that ultimate choice is something else entirely." 
    pt "His bravery, his selflessness... it wasn't just for glory or honor. It was an act of pure love and protection."
    pt "I realized that being a hero isn't about being invincible. It's about the willingness to give everything for a cause, for someone you care about."
    pt "His sacrifice wasn't in vain, but it's a loss that fills me with sorrow and a deep sense of responsibility. It's a reminder that true strength sometimes means enduring the pain of loss and carrying on."
    pt "As I stand in this emptiness, reflecting on what was lost, I know that his sacrifice has changed me. I bear the weight of his final act, the grief and sorrow of losing someone who meant so much." 
    pt "It's a part of my story now, a reminder of the cost of love and bravery."

    window hide
    pause 3
    return

label sacrificed_princess:
    if got_sacrificed_princess:
        jump repeat_ending

    $ got_sacrificed_princess = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "I never thought I would be the one to make such a choice. But when the moment came, it felt right, even if it meant giving up everything."
    pt "To see him safe, to protect what we believed in... it was worth it, even if it meant sacrificing myself."
    pt "The stories always tell of heroes sacrificing themselves for others, but sometimes, the roles reverse. I chose to put his life above my own, not out of duty, but out of love. It was an act of courage, one that came from deep within."
    pt "In that moment, I realized that true courage isn't just about facing danger. It's about being willing to give up everything for your cause."
    pt "There was no regret in my choice, only a deep sense of peace. My sacrifice was a way of ensuring that our story would live on, even if I couldn't be there to see it through."
    pt "Now, as I reflect on what happened, I know that this act of selflessness has defined me. It taught me that there is strength in giving, in putting others before myself."
    pt "It's a legacy of courage and sacrifice, a part of me that will endure beyond this moment."

    window hide
    pause 3
    return

label unfulfilled_love:
    if got_unfulfilled_love:
        jump repeat_ending

    $ got_unfulfilled_love = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "It's hard to accept that our story ended this way. We defied the rules, followed our hearts, and yet, it led to his banishment."
    pt "It feels like a cruel twist of fate, but deep down, I know it was the only choice left to us."
    pt "We tried to carve our own path, to find a place where we could be together despite the kingdom's laws. But in the end, our defiance came at a cost-one that neither of us could bear."
    pt "Our actions were driven by a desire to be together, to reject the roles assigned to us. But sometimes, breaking the rules means facing consequences we can't escape."
    pt "The hero was banished, and with him, a part of my heart. We couldn't stay together, and now, the memories of our time are tinged with sadness and regret." 
    pt "It was a love that defied boundaries, but it wasn't enough to change our reality."
    pt "As I reflect on our journey, I understand that defiance is a double-edged sword. We were willing to face the consequences, and now, I must live with the choice we made."
    pt "Our love, though unfulfilled, taught me the power and the limits of defiance."
    
    window hide
    pause 3
    return

label corrupted_hero:
    if got_corrupted_hero:
        jump repeat_ending

    $ got_corrupted_hero = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "I watched him change, slowly, painfully, until the person I knew was gone. The magic that was meant to protect us became a curse, twisting him into something unrecognizable." 
    pt "His strength turned to darkness, and it broke my heart to see him struggle against it."
    pt "In the end, he made the hardest choice-to end his own life to protect me from the corruption that had taken hold. His final act was one of love, but it's a love that cost us everything."
    pt "I've learned that power can be a dangerous thing. The hero's corruption was a harsh reminder that not all strength is meant to be wielded, and not all magic can be controlled."
    pt "His sacrifice was not just a loss of life but a loss of hope. It was a reminder that even the best intentions can lead to unforeseen consequences."
    pt "Reflecting on this, I understand the importance of restraint, of knowing when to step back and let go of power. His tragedy has taught me the value of being resolved in the face of temptation, to protect not just myself but those around me." 
    pt "It's a painful lesson, but one that will guide me forward."

    window hide
    pause 3
    return

label inherited_throne:
    if got_inherited_throne:
        jump repeat_ending

    $ got_inherited_throne = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "I never thought I would find myself here, at the head of the kingdom, bearing the weight of the crown. The throne was never something I aspired to this soon, yet here I am, thrust into a role I never expected."
    pt "The loss of the queen was a tragedy, a shadow that looms over our kingdom. But in that moment of crisis, I realized that I couldn't just stand by and watch. The people needed a leader, someone to guide them through the darkness"
    pt "I've learned that being a leader is not just about power; it's about standing up for the people and guiding them with a steady hand, even when the path ahead is uncertain."
    pt "Taking the throne has shown me that I am capable of so much more than I ever imagined. It's not just about ruling; it's about protecting and serving the people."
    pt "As I reflect on this new chapter, I understand that leadership is a journey, one that I must undertake with care and dedication."
    pt "The crown is a heavy burden, but it is also a symbol of hope and resilience."

    window hide
    pause 3
    return

label forest_curse:
    if got_forest_curse:
        jump repeat_ending

    $ got_forest_curse = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "Bound to the forest... it's a fate I never foresaw. The magic we sought to control became our prison, chaining us for eternity. The forest, once a sanctuary, became a reminder of our choices and the consequences that follow."
    pt "We thought we could harness the magic, bend it to our will, but it had its own designs. It whispered promises of power, of freedom from the kingdom's constraints, but taking advantage of those promises came at a steep price." 
    pt "I've learned that magic is a double-edged sword. It can offer great power, but misusing it has drastic consequences. Our desire to defy the kingdom's rules led us down a dark path, one where we lost more than we gained."
    pt "That curse was not just a punishment but a lesson. It showed the dangers of unchecked ambition, the folly of thinking we could control forces beyond our understanding."
    pt "As I stand in this emptiness, I understand the gravity of our actions. That place, once filled with beauty, soon became an eternal reminder of our hubris."
    pt "It was a dark, corrupting force, a testament to the consequences of our sins."

    window hide
    pause 3
    return

label forest_protectors:
    if got_forest_protectors:
        jump repeat_ending

    $ got_forest_protectors = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "The forest is quiet now, a sanctuary of life and magic that we fought to preserve. Our journey wasn't just about overcoming the villain; it was about understanding what it means to protect and nurture something greater than ourselves."
    pt "I realized that stewardship is about being present, about being committed to caring for something. We became the forest's guardians, not because we had to, but because it was where our hearts led us."
    pt "It was about more than wielding power or overcoming obstacles; it was about the subtle strength that comes from caring deeply for something beyond oneself. We found a calling in the forest, a way to make a difference that goes beyond the stories I once knew."
    pt "Our actions have shown me that stewardship is a long commitment, a dedication to seeing what you care for grow and flourish."
    pt "As I reflect on this journey, I know that the decision to protect the forest was born from a place of love and understanding. It was a responsibility I never imagined, yet one I wouldn't have traded for anything."
    pt "The role of stewardship was a testament to the power of our choices, a reminder of the beauty we were committed to preserving."

    window hide
    pause 3
    return

label love_beyond_death:
    if got_love_beyond_death:
        jump repeat_ending

    $ got_love_beyond_death = True

    stop music
    scene bg actual_blackscreen
    pause 2.5

    pt "To love so deeply that death cannot separate us... it feels like a story from a legend, yet it became our reality. We chose to face the end together, to embrace a love that transcends life itself." 
    pt "Our choice was made out of a pure, unwavering devotion that is timeless."
    pt "They say that love conquers all, and perhaps it's true. We knew that our time in life together was coming to an end. So, we chose to defy even death, to hold onto each other beyond the fabrics of reality."
    pt "The memories we created -they live on, even as everything else fades away. It's a comforting thought, knowing that our love is timeless."
    pt "In death, we found a peace that life denied us. Knowing that we could be together, even in the afterlife, brings a sense of completion and fulfillment that we never found in life."
    pt "As I reflect on this choice, I understand the power of love, the strength it gives us to face the unknown. It's a love beyond life, beyond death, a love that is eternal." 
    pt "And that is a comfort, a final, lasting embrace that we carry with us into eternity."

    window hide
    pause 3
    return

label repeat_ending:
    stop music
    window hide
    scene bg actual_blackscreen
    pause 2.5
    window show Dissolve(1.5)

    pt "Haven't we been here before?"

    window hide
    pause 3
    return

label true_ending_monologue:
    window show Dissolve(1.5)

    pt "{plain}I once thought being a princess meant helplessness.{/plain}" 

    pt "{plain}Patiently awaiting a rescue.{/plain}"

    pt "{plain}A hero to change my life.{/plain}" 

    pt "{plain}That was not the case.{/plain}"

    pt "{plain}Discovering myself meant realizing that it wasn't the role that defined me, but how I chose to step beyond it.{/plain}" 

    pt "{plain}A happily ever after is not a hero we await, but rather something we forge ourselves.{/plain}"

    pt "{plain}Step beyond the story written for you.{/plain}"

    pt "{plain}Find your happily ever after.{/plain}"

    return


label reset_default_vars:
    # Reset all default variables to initial state

    # TODO: ADD MEADOW AND AWARE HERO VARS HERE WHEN DONE

    # script.rpy
    $ routes_completed = 0
    $ aware_hero_met = False
    $ romance = 50
    $ chose_magic = None
    $ game_done = False
    $ ending = None
    $ v_type = None
    $ hu_times_gotten = 0
    $ ff_times_gotten = 0
    $ vs_times_gotten = 0
    $ dml_times_gotten = 0
    $ fh_times_gotten = 0


    # tower.rpy
    $ tower_choices1_seen = set()
    $ tower_choices1_chosen = 0
    $ tower_room_inspected = False
    $ tower_table_inspected = False
    $ tower_chose_why_no_escape = False
    $ tower_attempted_open_door = False
    $ tower_chose_lesson_learned = False
    $ tower_chose_cant_believe = False
    $ tower_chose_who_is_he = False
    $ tower_chose_way_out = False

    # forest.rpy
    $ forest_choices1_seen = set()
    $ forest_choices1_chosen = 0
    $ forest_asked_who_are_you = False
    $ forest_asked_why_did_you_come = False
    $ forest_asked_is_it_safe = False
    $ forest_asked_have_we_done_this = False
    $ forest_asked_why_familiar = False


    # cryptic.rpy
    $ cryptic_choices1_seen = set()
    $ cryptic_choices1_chosen = 0
    $ dml_lore_shown = False
    $ fh_lore_shown = False
    $ ff_lore_shown = False
    $ hu_lore_shown = False
    $ vs_lore_shown = False
    $ what_truths_checked = False
    $ stone_gravings_examined = False
    $ can_decipher_runes = False


    # meadow.rpy
    $ meadow_choices1_seen = set()


    # hu.rpy
    $ hu_chose_who_are_you = False
    $ hu_chose_why_after_us = False
    $ hu_chose_kingdom_abolished_magic = False
    $ hu_chose_what_your_mission = False
    $ hu_chose_why_guard_forest = False
    $ hu_chose_how_become_hunter = False
    $ hu_chose_why_cant_let_us_pass = False
    $ hu_chose_have_you_always_been_alone = False
    $ hu_chose_how_long_been_here = False
    $ hu_chose_why_didnt_chase_us_before = False
    $ hu_chose_we_went_by_mistake = False


    # fh.rpy
    $ fh_chose_who_are_you = False
    $ fh_chose_why_hold_grudge = False
    $ fh_chose_things_have_changed = False
    $ fh_chose_what_happened = False
    $ fh_chose_why_kingdom_turn = False
    $ fh_chose_really_believe_revenge = False
    $ fh_chose_why_hunt_us = False
    $ fh_chose_killing_us_satisfy = False
    $ fh_chose_what_would_you_do = False
    $ fh_chose_why_cant_pass = False
    $ fh_chose_change_your_mind = False
    $ fh_chose_not_like_those = False


    # ff.rpy
    $ ff_chose_who_are_you = False
    $ ff_chose_why_doing_this = False
    $ ff_chose_what_you_gain = False
    $ ff_chose_why_enjoy_manipulating = False
    $ ff_chose_isnt_there_more = False
    $ ff_chose_do_you_not = False
    $ ff_chose_how_did_you = False
    $ ff_chose_was_there_ever = False
    $ ff_chose_do_you_think = False
    $ ff_chose_what_do_you = False
    $ ff_chose_is_this_just = False
    $ ff_chose_when_will_it = False


    # dml.rpy
    $ dml_chose_who_are_you = False
    $ dml_chose_why_do_you = False
    $ dml_chose_what_do_you = False
    $ dml_chose_how_did_you = False
    $ dml_chose_what_drives_your = False
    $ dml_chose_do_you_not = False
    $ dml_chose_what_is_your = False
    $ dml_chose_do_you_really = False
    $ dml_chose_how_do_you = False
    $ dml_chose_why_cant_you = False
    $ dml_chose_is_there_nothing = False
    $ dml_chose_what_would_happen = False


    # vs.rpy
    $ vs_chose_who_are_you = False
    $ vs_chose_why_do_you_seek = False
    $ vs_chose_can_you_ever = False
    $ vs_chose_what_do_you = False
    $ vs_chose_why_do_you_blame = False
    $ vs_chose_isnt_there_a = False
    $ vs_chose_why_cant_you = False
    $ vs_chose_do_you_not = False
    $ vs_chose_cant_you_find = False
    $ vs_chose_what_will_you = False
    $ vs_chose_will_your_vengeance = False
    $ vs_chose_what_then = False


    # princess_monologues.rpy
    $ got_happily_ever_after = False
    $ got_saved_hero = False
    $ got_sacrificed_hero = False
    $ got_sacrificed_princess = False
    $ got_unfulfilled_love = False
    $ got_corrupted_hero = False
    $ got_inherited_throne = False
    $ got_forest_curse = False
    $ got_forest_protectors = False
    $ got_love_beyond_death = False


    # aware_hero.rpy
    $ aware_hero_number = 0
    $ aware_hero_second_chosen = 0

    return

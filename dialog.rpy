init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_vns_intro_final",
            prompt="Introduction to Visual Novels",
            category=['Visual Novels'],
            pool=True,
            unlocked=True
        )
    )

label monika_vns_intro_final:
    m 1rsd "Say, [player]..."
    m 1etb "DDLC was a visual novel, wasn't it?"
    m 1etc "Though it seems like it was very short for most games of its genre..."
    m 1gsd "And most of that playtime was from my involvement, anyway..."
    m 1wso "Apparently quite a few visual novels can reach up to 50-80 hours!"
    m 1nub "I found this out from doing a little research on visual novels, as I come from one after all..."
    m 7suo "And it actually is quite an interesting medium!"
    m 1lup "DDLC was a very surface level visual novel, containing the most basic, tired tropes in anime..."
    m 5esd "It's what most people who have never read a visual novel think that these kinds of games are."
    m 1mua "If it wasn't for me, of course."
    m 3ssb "But there's so much more to it!"
    m 3wso "Many people who try more plot-involved visual novels out for themselves say that some of them have some of the best stories they've ever read."
    m 2ltd "Some argue that they are a better storytelling medium than the classic physical novel, mostly due to the audio and visuals."
    m 1eub "Visual novels are also a staple of 2000s anime culture!"

    if persistent._mas_pm_watch_mangime == True:
        m 7eub "Since you like anime, you really should try one if you haven't already, [player]! They're part of the culture, after all!"

    if persistent._mas_pm_watch_mangime == False:
        m 7ekb "I know you said you don't like anime or manga, so you probably haven't tried one yet, but there are some great stories to be told in them...I would really recommend it, [player]!"


    m 1wuo "Oh, [player]! I just had an idea!"
    m 1hub "Since I'm researching this topic already, why don't I tell you about some of the most loved visual novels?"
    m 2lublb "Then you can find some to read and enjoy for yourself!"
    m 5eubfu "The only thing I want is for you to be happy, after all."
    m 3nubfu "Thanks for listening, [player]! Ehehe~"

    return

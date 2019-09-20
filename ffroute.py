import json
import sys

def dungeonItems(l, c):
    d = {
        'Links Pocket': {
            'ADungeon': 'Free'
        },
        'Queen Gohma': {
            'ADungeon': 'Deku Tree',
            'Deku Stick Upgrade': c['Deku Stick Capacity'],
            'Deku Shield': c['Deku Shield'],
            'Deku Stick Shop': c['Buy Deku Stick (1)'],
            'Deku Shield Shop': c['Buy Deku Shield'],
            'Boomerang': c['Boomerang']
        },
        'King Dodongo': {
            'ADungeon': "Dodongo's Cavern",
            'Bombs': c['Bomb Bag'],
            'Bombchus': c['Bombchus'],
            'Strength': c['Progressive Strength Upgrade'],
            'Slingshot': c['Slingshot']
        },
        'Barinade': {
            'ADungeon': "Jabu Jabu's Belly",
            'Bombs': c['Bomb Bag'],
            'Scale': c['Progressive Scale'],
            'Slingshot': c['Slingshot'],
            'Boomerang': c['Boomerang'],
            'Letter': c['Bottle with Letter'],
            'Deku Stick Upgrade': c['Deku Stick Capacity'],
            'Deku Stick Shop': c['Buy Deku Stick (1)']
        },
        'Phantom Ganon': {
            'ADungeon': "Forest Temple",
            'Boss Key': c['Boss Key (Forest Temple)'],
            'All Small Keys': c['Small Key (Forest Temple)'],
            "Hookshot": c['Progressive Hookshot'],
            "Strength": c['Progressive Strength Upgrade'],
            "Bow": c['Bow'],
            "Ocarina": c['Ocarina'],
            "Song of Time": c['Song of Time'],
            "Hover Boots": c['Hover Boots']
        },
        'Volvagia': {
            'ADungeon': "Fire Temple",
            'Boss Key': c['Boss Key (Fire Temple)'],
            'All Small Keys': c['Small Key (Fire Temple)'],
            "Hookshot": c['Progressive Hookshot'],
            "Strength": c['Progressive Strength Upgrade'],
            "Bow": c['Bow'],
            "Megaton Hammer": c['Hammer'],
            'Bombs': c['Bomb Bag'],
            'Goron Tunic': c['Goron Tunic']
        },
        'Morpha': {
            'ADungeon': "Water Temple",
            'Boss Key': c['Boss Key (Water Temple)'],
            'All Small Keys': c['Small Key (Water Temple)'],
            'Scale': c['Progressive Scale'],
            'Iron Boots': c['Iron Boots'],
            "Longshot": c['Progressive Hookshot'],
            "Bow": c['Bow'],
            "Song of Time": c['Song of Time'],
            'Zora Tunic': c['Zora Tunic'],
            "Ocarina": c['Ocarina'],
            "Zelda's Lullaby": c['Zeldas Lullaby']
        },
        'Bongo Bongo': {
            'ADungeon': "Shadow Temple",
            'Boss Key': c['Boss Key (Shadow Temple)'],
            'All Small Keys': c['Small Key (Shadow Temple)'],
            "Nocturne of Shadow": c['Nocturne of Shadow'],
            "Din's Fire": c['Dins Fire'],
            "Fire Arrows": c['Fire Arrows'],
            "Magic": c['Magic Meter'],
            "Hover Boots": c['Hover Boots'],
            "Hookshot": c['Progressive Hookshot'],
            "Bow": c['Bow'],
            'Bombs': c['Bomb Bag'],
            'Bombchus': c['Bombchus'],
            "Ocarina": c['Ocarina'],
            "Zelda's Lullaby": c['Zeldas Lullaby']
        },
        'Twinrova': {
            'ADungeon': "Spirit Temple",
            'Boss Key': c['Boss Key (Spirit Temple)'],
            'All Small Keys': c['Small Key (Spirit Temple)'],
            "Hookshot": c['Progressive Hookshot'],
            "Strength": c['Progressive Strength Upgrade'],
            "Mirror Shield": c['Mirror Shield'],
            "Bow": c['Bow'],
            "Song of Time": c['Song of Time'],
            "Hover Boots": c['Hover Boots'],
            'Slingshot': c['Slingshot'],
            'Deku Stick Upgrade': c['Deku Stick Capacity'],
            'Deku Stick Shop': c['Buy Deku Stick (1)'],
            'Boomerang': c['Boomerang'],
            "Din's Fire": c['Dins Fire'],
            "Fire Arrows": c['Fire Arrows'],
            "Magic": c['Magic Meter'],
            'Bombs': c['Bomb Bag'],
            "Ocarina": c['Ocarina'],
            "Zelda's Lullaby": c['Zeldas Lullaby'],
            "Requiem of Spirit": c['Requiem of Spirit']
        }
    }
    return d[l[0]]

def invertSpoiler(f):
    with open(f) as spoiler_json:
        spoiler = json.load(spoiler_json)
        locs = spoiler['locations']
        c = {}
        for l, i in locs.items():
            if type(i) is dict:
                if i['item'] != 'Ice Trap':
                    if not (i['item'] in c):
                        c[i['item']] = []
                    c[i['item']].append(l + ', ' + str(i['price']) + ' Rupees')
                    if i['item'].split(" ")[0] == 'Bottle':
                        if not ('Bottle' in c):
                            c['Bottle'] = []
                        c['Bottle'].append(l + ', ' + str(i['price']) + ' Rupees')
                    if i['item'].split(" ")[0] == 'Bombchus':
                        if not ('Bombchus' in c):
                            c['Bombchus'] = []
                        c['Bombchus'].append(l + ', ' + str(i['price']) + ' Rupees')
            else:
                if not (i in c):
                    c[i] = []
                c[i].append(l)
                if i.split(" ")[0] == 'Bottle':
                    if not ('Bottle' in c):
                        c['Bottle'] = []
                    c['Bottle'].append(l)
                if i.split(" ")[0] == 'Bombchus':
                    if not ('Bombchus' in c):
                        c['Bombchus'] = []
                    c['Bombchus'].append(l)
    return c

def organizeChecks(c):
    return {
        'Medallions': {
            'Forest Medallion': dungeonItems(c['Forest Medallion'], c),
            'Fire Medallion': dungeonItems(c['Fire Medallion'], c),
            'Water Medallion': dungeonItems(c['Water Medallion'], c),
            'Shadow Medallion': dungeonItems(c['Shadow Medallion'], c),
            'Spirit Medallion': dungeonItems(c['Spirit Medallion'], c),
            'Light Medallion': dungeonItems(c['Light Medallion'], c)
        },
        'Trials': {
            "Longshot": c['Progressive Hookshot'],
            "Strength": c['Progressive Strength Upgrade'],
            "Bow": c['Bow'],
            "Bottle": c['Bottle'],
            "Megaton Hammer": c['Hammer'],
            "Magic": c['Magic Meter'],
            "Hover Boots": c['Hover Boots'],
            "Mirror Shield": c['Mirror Shield'],
            "Din's Fire": c['Dins Fire'],
            "Small Keys": c['Small Key (Ganons Castle)'],
            "Boss Key": c['Boss Key (Ganons Castle)'],
            "Fire Arrows": c['Fire Arrows'],
            "Light Arrows": c['Light Arrows']
        },
        'Stones': {
            "Kokiri Emerald": dungeonItems(c['Kokiri Emerald'], c),
            "Goron Ruby": dungeonItems(c['Goron Ruby'], c),
            "Zora Sapphire": dungeonItems(c['Zora Sapphire'], c)
        },
        'Songs': {
            "Zelda's Lullaby": c['Zeldas Lullaby'],
            "Epona's Song": c['Eponas Song'],
            "Saria's Song": c['Sarias Song'],
            "Suns Song": c['Suns Song'],
            "Song of Time": c['Song of Time'],
            "Song of Storms": c['Song of Storms'],
            "Minuet of Forest": c['Minuet of Forest'],
            "Bolero of Fire": c['Bolero of Fire'],
            "Serenade of Water": c['Serenade of Water'],
            "Requiem of Spirit": c['Requiem of Spirit'],
            "Nocturne of Shadow": c['Nocturne of Shadow'],
            "Prelude of Light": c['Prelude of Light']
        },
        'Equipment': {
            'Deku Stick Upgrade': c['Deku Stick Capacity'],
            'Deku Stick Shop': c['Buy Deku Stick (1)'],
            'Deku Nut Upgrade': c['Deku Nut Capacity'],
            'Bombs': c['Bomb Bag'],
            "Bow": c['Bow'],
            "Fire Arrows": c['Fire Arrows'],
            "Din's Fire": c['Dins Fire'],
            'Slingshot': c['Slingshot'],
            "Ocarina": c['Ocarina'],
            'Bombchus': c['Bombchus'],
            "Longshot": c['Progressive Hookshot'],
            'Ice Arrows': c['Ice Arrows'],
            "Farore's Wind": c['Farores Wind'],
            'Boomerang': c['Boomerang'],
            'Lens of Truth': c['Lens of Truth'],
            'Magic Beans': c['Magic Bean Pack'],
            "Megaton Hammer": c['Hammer'],
            "Light Arrows": c['Light Arrows'],
            "Bottle": c['Bottle'],
            'Weird Egg': c['Weird Egg'],
            "Strength": c['Progressive Strength Upgrade'],
            'Wallet': c['Progressive Wallet'],
            'Scale': c['Progressive Scale'],
            'Gerudo Card': c['Gerudo Membership Card'],
            'Kokiri Sword': c['Kokiri Sword'],
            'Biggoron Sword': c['Biggoron Sword'],
            'Deku Shield': c['Deku Shield'],
            'Deku Shield Shop': c['Buy Deku Shield'],
            'Hylian Shield': c['Hylian Shield'],
            'Hylian Shield Shop': c['Buy Hylian Shield'],
            'Mirror Shield': c['Mirror Shield'],
            'Goron Tunic': c['Goron Tunic'],
            'Zora Tunic': c['Zora Tunic'],
            'Double Defense': c['Double Defense'],
        },
        'GTG Access': {
            'Gerudo Card': c['Gerudo Membership Card'],
            "Small Keys": c['Small Key (Gerudo Training Grounds)'],
            'Bombs': c['Bomb Bag'],
            "Bow": c['Bow'],
            "Strength": c['Progressive Strength Upgrade'],
            "Hookshot": c['Progressive Hookshot']
        },
        'Well Access': {
            "Ocarina": c['Ocarina'],
            "Song of Storms": c['Song of Storms'],
            "Small Keys": c['Small Key (Bottom of the Well)'],
            'Bombs': c['Bomb Bag'],
            "Zelda's Lullaby": c['Zeldas Lullaby'],
        },
        'Heart Containers': c['Heart Container'],
        'Skulls': c['Gold Skulltula Token']
    }

if len(sys.argv) < 2:
    print('Enter your spoiler filename after the script and re-run')
else: 
    c = invertSpoiler(sys.argv[1])
    r = organizeChecks(c)
    with open('checks.json', 'w') as outfile:
        outfile.write(json.dumps(r, indent=4))
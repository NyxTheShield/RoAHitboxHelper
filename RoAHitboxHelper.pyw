import PySimpleGUI as sg
import pyperclip

effect_list = sorted([
"1 | no visual effect",
"301 | basic small (default)",
"302 | basic small with spin effect in center",
"303 | basic small directional",
"304 | basic large",
"305 | basic sweetspot",
"19 | sweetspot small",
"3 | fire small",
"4 | fire directional",
"148 | fire large",
"121 | plasma fspecial X",
"123 | plasma fspecial X hit",
"124 | plasma hit small",
"125 | tipper hit small X",
"126 | tipper hit small cross",
"127 | tipper hit large",
"128 | plasma hit small cross",
"129 | plasma hit small X",
"130 | plasma hit large X",
"256 | plasma orb break",
"194 | wind small",
"156 | wind large",
"196 | wind extra large",
"11 | feathers side small",
"12 | feathers up small",
"146 | feathers side large",
"147 | feathers up large",
"15 | seed break 1",
"16 | seed break 2",
"17 | leaf small",
"18 | leaf tiny",
"198 | leaf large",
"159 | leaf extra large",
"131 | flower large",
"132 | flower small",
"133 | flower sweetspot",
"134 | wood large",
"135 | wood small",
"162 | wood extra large",
"204 | fire whip large",
"136 | metal break",
"137 | molten metal break",
"20 | lightning small",
"21 | lightning medium",
"22 | lightning directional",
"197 | lightning large",
"157 | lightning extra large",
"192 | rock large",
"193 | rock small",
"155 | rock extra large",
"13 | smoke large",
"14 | smoke small",
"5 | dark water small",
"6 | light water small",
"7 | light + dark water small",
"8 | dark water directional",
"9 | light water directional",
"10 | light + dark water directional",
"149 | dark water medium",
"150 | light water medium",
"195 | water large",
"161 | water extra large",
"199 | ice large",
"158 | ice extra large",
"25 | ice shard long",
"26 | ice shard medium",
"27 | icy flash small",
"28 | old ice large",
"29 | old ice small",
"108 | spirit flame hit",
"109 | ori hit small",
"110 | ori hit large",
"111 | sein hit small",
"112 | sein hit large",
"113 | ori sweetspot",
"115 | light grenade explosion",
"116 | poison small",
"117 | poison large",
"118 | poison sweetspot",
"119 | poison large 2",
"160 | poison large 3",
"120 | poison extra large",
"138 | steam directional",
"139 | missile explode small",
"140 | rocket fist burst",
"141 | missile explode medium",
"142 | mine hit",
"143 | explosion large",
"144 | steam small",
"145 | mine combo explosion",
"306 | shovel effect",
"151 | buzzsaw destroy",
"152 | ghost glove disappear",
"153 | mobile gear destroy",
"154 | dirt block destroy",
"250 | coin capture",
"251 | flareo rod hit",
"252 | SK Dstrong hit small",
"253 | SK Dstrong hit large",
"254 | War Horn hit",
"66 | portal small",
"67 | abyss small"], key=lambda x: int(x.split('|')[0]))

const_list = ["HG_PARENT_HITBOX",
"HG_HITBOX_TYPE",
"HG_WINDOW",
"HG_WINDOW_CREATION_FRAME",
"HG_LIFETIME",
"HG_HITBOX_X",
"HG_HITBOX_Y",
"HG_WIDTH",
"HG_HEIGHT",
"HG_SHAPE",
"HG_PRIORITY",
"HG_DAMAGE",
"HG_ANGLE",
"HG_BASE_KNOCKBACK",
"HG_KNOCKBACK_SCALING",
"HG_EFFECT",
"HG_BASE_HITPAUSE",
"HG_HITPAUSE_SCALING",
"HG_VISUAL_EFFECT",
"HG_VISUAL_EFFECT_X_OFFSET",
"HG_VISUAL_EFFECT_Y_OFFSET",
"HG_HIT_SFX",
"HG_ANGLE_FLIPPER",
"HG_EXTRA_HITPAUSE",
"HG_GROUNDEDNESS",
"HG_EXTRA_CAMERA_SHAKE",
"HG_IGNORES_PROJECTILES",
"HG_HIT_LOCKOUT",
"HG_EXTENDED_PARRY_STUN",
"HG_HITBOX_GROUP",
"HG_HITSTUN_MULTIPLIER",
"HG_DRIFT_MULTIPLIER",
"HG_SDI_MULTIPLIER",
"HG_TECHABLE",
"HG_FORCE_FLINCH",
"HG_FINAL_BASE_KNOCKBACK",
"HG_THROWS_ROCK",
"HG_PROJECTILE_SPRITE",
"HG_PROJECTILE_MASK",
"HG_PROJECTILE_ANIM_SPEED",
"HG_PROJECTILE_HSPEED",
"HG_PROJECTILE_VSPEED",
"HG_PROJECTILE_GRAVITY",
"HG_PROJECTILE_GROUND_FRICTION",
"HG_PROJECTILE_AIR_FRICTION",
"HG_PROJECTILE_WALL_BEHAVIOR",
"HG_PROJECTILE_GROUND_BEHAVIOR",
"HG_PROJECTILE_ENEMY_BEHAVIOR",
"HG_PROJECTILE_UNBASHABLE",
"HG_PROJECTILE_PARRY_STUN",
"HG_PROJECTILE_DOES_NOT_REFLECT",
"HG_PROJECTILE_IS_TRANSCENDENT",
"HG_PROJECTILE_DESTROY_EFFECT"]

gui_list = ["Attack Name",
"Hitbox Number",
"Parent Hitbox Number",
"Hitbox Type",
"Window Number",
"Creation Frame",
"Lifetime",
"X Position",
"Y Position",
"Width",
"Height",
"Shape",
"Priority",
"Damage",
"Angle",
"Base KB",
"KB Scaling",
"Effect",
"Base Hitlag Frames",
"Hitlag Scaling",
"Hit Visual Effect",
"Hit Visual Effect X Offset",
"Hit Visual Effect Y Offset",
"Hit Visual Effect SFX",
"Angle Flipper",
"Extra Hitlag",
"Groundedness",
"Extra Camera Shake",
"Ignores Projectiles?",
"Hit Lockout",
"Extended Parry Stun",
"Hitbox Group",
"Hitstun Multiplier",
"Drift DI Multiplier",
"SDI Multiplier",
"Techable Type",
"Force Flinch",
"Final Base KB",
"Throws Rocks",
"Sprite Name",
"Mask Name",
"Animation Speed",
"Horizontal Speed",
"Vertical Speed",
"Gravity",
"Ground Friction",
"Air Friction",
"Wall Behaviour",
"Ground Behaviour",
"Enemy Behaviour",
"Unbashable?",
"Stunned When Parried?",
"Reflected When Parried?",
"Trascendent?",
"Destroy Effect Name"]

dict_gui = {}

for i in range(len(const_list)):
    dict_gui[gui_list[i+2]] = const_list[i]

clear = False;


required = [[sg.Text("Required Values",font = "Helvetica 16",size=(20, 1))],
[sg.Text("Attack Name",size=(20, 1)),sg.InputText("AT_YOURATTACK",key="Attack Name",size=(20, 1))],
[sg.Text("Hitbox Number",size=(20,1)),sg.InputText(1,key="Hitbox Number",do_not_clear=True,size=(20,1))],
[sg.Text("Parent Hitbox Number",size=(20,1)),sg.InputText(1,key="Parent Hitbox Number",do_not_clear=True,size=(20,1))],
[sg.Text("Hitbox Type",size=(20, 1)),sg.Combo(["1 | Physical","2 | Projectile"],key="Hitbox Type",size=(20,1))],
[sg.Text("Window Number",size=(20,1)),sg.InputText(1,key="Window Number",do_not_clear=True,size=(20,1))],
[sg.Text("Creation Frame",size=(20,1)),sg.InputText(1,key="Creation Frame",do_not_clear=True,size=(20,1))],
[sg.Text("Lifetime",size=(20,1)),sg.InputText(1,key="Lifetime",do_not_clear=True,size=(20,1))],        
[sg.Text("Width",size=(20,1)),sg.InputText(30, key="Width",do_not_clear=True,size=(20,1))],
[sg.Text("Height",size=(20,1)),sg.InputText(30, key="Height",do_not_clear=True,size=(20,1))]]

engine = [[sg.Text("Engine Values",font = "Helvetica 16",size=(20, 1))],
        
[sg.Text("X Position",size=(20,1)),sg.InputText(key="X Position",do_not_clear=clear,size=(20,1))],
[sg.Text("Y Position",size=(20,1)),sg.InputText(key="Y Position",do_not_clear=clear,size=(20,1))],
[sg.Text("Shape",size=(20, 1)),sg.Combo(["0 | Circle","1 | Rectangle","2 | Rounded Rectangle", "-1 | Projectile Precise Collision"],key="Shape",size=(20,1))],
[sg.Text("Priority",size=(20, 1)),sg.Combo(["","0 | No Priority","1",'2','3','4','5','6','7','8','9','10 | Maximum Priority'],key="Priority",size=(20, 1))],        
[sg.Text("Damage",size=(20,1)),sg.InputText(key="Damage",do_not_clear=clear,size=(20,1))],
[sg.Text("Angle",size=(20,1)),sg.InputText(key="Angle",do_not_clear=clear,size=(20,1))],
[sg.Text("Base KB",size=(20,1)),sg.InputText(key="Base KB",do_not_clear=clear,size=(20,1))],
[sg.Text("KB Scaling",size=(20,1)),sg.InputText(key="KB Scaling",do_not_clear=clear,size=(20,1))],
[sg.Text("Final Base KB",size=(20,1)),sg.InputText(key="Final Base KB",do_not_clear=clear,size=(20,1))],
[sg.Text("Base Hitlag Frames",size=(20,1)),sg.InputText(key="Base Hitlag Frames",do_not_clear=clear,size=(20,1))],
[sg.Text("Hitlag Scaling",size=(20,1)),sg.InputText(key="Hitlag Scaling",do_not_clear=clear,size=(20,1))],
[sg.Text("Extra Hitlag",size=(20,1)),sg.InputText(key="Extra Hitlag",do_not_clear=clear,size=(20,1))],
[sg.Text("Effect",size=(20, 1)),sg.Combo(["","1 | Burn",'2 | Consume Burn','3 | Burn Stun','4 | Wrap','5 | Freeze','6 | Mark','7 | Unused','8 | Auto Wrap','9 | Polite (Only Deals Hitstun if in Hitstun','10 | Poison','11 | Plasma Stun','12 | Crouch Armors Through It'],key="Effect",size=(20, 1))],
[sg.Text("Hitstun Multiplier",size=(20,1)),sg.InputText(key="Hitstun Multiplier",do_not_clear=clear,size=(20,1))],
[sg.Text("Drift DI Multiplier",size=(20,1)),sg.InputText(key="Drift DI Multiplier",do_not_clear=clear,size=(20,1))],
[sg.Text("SDI Multiplier",size=(20,1)),sg.InputText(key="SDI Multiplier",do_not_clear=clear,size=(20,1))],        
]


interactions = [[sg.Text("Interactions",font = "Helvetica 16",size=(20, 1))],

[sg.Text("Angle Flipper",size=(20, 1)),sg.Combo(["","0 | Set Angle",'1 | Away from Center of Enemy', '2 | Towards Center of Enemy','3 | Hor. Away from Hitbox ','4 | Hor. Towards Hitbox','5 | Hor. Reversed','6 | Hor. Away from Enemy','7 | Hor. Towards Enemy','8 | Towards Hitbox','9 | Away from Hitbox'],key="Angle Flipper",size=(20, 1))],
[sg.Text("Groundedness",size=(20, 1)),sg.Combo(["","0 | No Restriction",'1 | Only Hits Grounded Enemies', '2 | Only Hits Aerial Enemies'],key="Groundedness",size=(20, 1))],
[sg.Text("Ignores Projectiles?",size=(20, 1)),sg.Combo(["","0 | No ", '1 | Yes'],key="Ignores Projectiles?",size=(20, 1))],
[sg.Text("Hit Lockout",size=(20,1)),sg.InputText(key="Hit Lockout",do_not_clear=clear,size=(20,1))],
[sg.Text("Extended Parry Stun",size=(20,1)),sg.InputText(key="Extended Parry Stun",do_not_clear=clear,size=(20,1))],
[sg.Text("Techable Type",size=(20, 1)),sg.Combo(["","0 | Can Tech ", '1 | Cannot Tech', '2 | Ignores Platforms (Etalus uair)', '3 | Cannot Tech or Bounce'],key="Techable Type",size=(20, 1))],
[sg.Text("Force Flinch",size=(20, 1)),sg.Combo(["","0 | No ", '1 | Yes', '2 | Disable Flich', '3 | Only on Crouch'],key="Force Flinch",size=(20, 1))],
[sg.Text("Throws Rocks",size=(20, 1)),sg.Combo(["","0 | Breaks Rock ", '1 | Throws Rock', '2 | Ignores Rock'],key="Throws Rocks",size=(20, 1))],
[sg.Text("Hitbox Group",size=(20,1)),sg.InputText(key="Hitbox Group",do_not_clear=clear,size=(20,1))]]
        

visuals = [[sg.Text("Visuals and SFX",font = "Helvetica 16",size=(20, 1))],
        
[sg.Text("Hit Visual Effect",size=(20, 1)),sg.Combo([""]+effect_list,key="Hit Visual Effect",size=(20, 1))],        
[sg.Text("Hit Visual Effect X Offset",size=(20,1)),sg.InputText(key="Hit Visual Effect X Offset",do_not_clear=clear,size=(20,1))],
[sg.Text("Hit Visual Effect Y Offset",size=(20,1)),sg.InputText(key="Hit Visual Effect Y Offset",do_not_clear=clear,size=(20,1))],
[sg.Text("Hit Visual Effect SFX",size=(20,1)),sg.InputText(key="Hit Visual Effect SFX",do_not_clear=clear,size=(20,1))],
[sg.Text("Extra Camera Shake",size=(20, 1)),sg.Combo(["",'0 | Normal Shake', '1 | Force Shake',"-1 | No Shake"],key="Extra Camera Shake",size=(20, 1))]

]

projectiles = [[sg.Text("Projectile Specific",font = "Helvetica 16",size=(20, 1))],

[sg.Text("Sprite Name",size=(20,1)),sg.InputText(key="Sprite Name", do_not_clear=clear,size=(20,1))],
[sg.Text("Mask Name",size=(20,1)),sg.InputText(key="Mask Name", do_not_clear=clear,size=(20,1))],
[sg.Text("Animation Speed",size=(20,1)),sg.InputText(key="Animation Speed", do_not_clear=clear,size=(20,1))],
[sg.Text("Horizontal Speed",size=(20,1)),sg.InputText(key="Horizontal Speed", do_not_clear=clear,size=(20,1))],
[sg.Text("Vertical Speed",size=(20,1)),sg.InputText(key="Vertical Speed", do_not_clear=clear,size=(20,1))],
[sg.Text("Gravity",size=(20,1)),sg.InputText(key="Gravity", do_not_clear=clear,size=(20,1))],
[sg.Text("Ground Friction",size=(20,1)),sg.InputText(key="Ground Friction", do_not_clear=clear,size=(20,1))],
[sg.Text("Air Friction",size=(20,1)),sg.InputText(key="Air Friction", do_not_clear=clear,size=(20,1))],
[sg.Text("Wall Behaviour",size=(20,1)),sg.Combo(["","0 | Stops at Walls ", '1 | Goes Through Walls', '2 | Bounces off Walls'], key="Wall Behaviour",size=(20,1))],
[sg.Text("Ground Behaviour",size=(20,1)),sg.Combo(["","0 | Stops at Ground ", '1 | Goes Through Ground', '2 | Bounces off Ground'], key="Ground Behaviour", size=(20,1))],
[sg.Text("Enemy Behaviour",size=(20,1)),sg.Combo(["","0 | Stops at Enemies ", '1 | Goes Through Enemies'],key="Enemy Behaviour",size=(20,1))],
[sg.Text("Unbashable?",size=(20,1)),sg.Combo(["","0 | No ", '1 | Yes'],key="Unbashable?", size=(20,1))],
[sg.Text("Stunned When Parried?",size=(20,1)),sg.Combo(["","0 | No ", '1 | Yes'], key="Stunned When Parried?",size=(20,1))],
[sg.Text("Reflected When Parried?",size=(20,1)),sg.Combo(["","0 | Yes ", '1 | No'],key="Reflected When Parried?", size=(20,1))],
[sg.Text("Trascendent?",size=(20,1)),sg.Combo(["","0 | No ", '1 | Yes'],key="Trascendent?", size=(20,1))],
[sg.Text("Destroy Effect Name",size=(20,1)),sg.InputText(key="Destroy Effect Name", do_not_clear=clear,size=(20,1))]]



layout2= [ [ sg.Image("logo.png"), sg.Text('USAGE: Fill each field with the wanted values for your hitbox, when you are done just click the "Copy to Clipboard" button \nto get the GML Code corresponding to the values below.\n\nIf you set the Hitbox Type to projectile, don\'t forget to set the "Mask Name" property, or the Shape of the hitbox to -1.', font="Helvetica 12")],
          [sg.Column(required + [[sg.Text('',size=(10,5))]] + [[sg.Button('Copy to Clipboard',size=(40,3))]]),sg.Column(engine), sg.Column(interactions+visuals), sg.Column(projectiles)],
          [sg.Text('*Created by NyxTheShield', font = "Helvetica 8")]]

window = sg.Window('RoA Hitbox Helper', layout2)

while True:
    
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    hitbox_id = int(values["Hitbox Number"])
    attack_name = values["Attack Name"]
    full_string = "set_num_hitboxes({0}, 999);\n".format(attack_name)
    
    print(values)

    keys = list(values.keys())
    keys.remove("Attack Name")
    keys.remove("Hitbox Number")
    for i in keys:
        aux = 'set_hitbox_value({0}, {1}, {2}, {3});\n'
        final_value = values[i].split("|")[0]

        
        aux2 = aux.format(attack_name, hitbox_id, dict_gui[i.replace("*","")], final_value)
        if values[i] != '':
            full_string += aux2

    pyperclip.copy(str(full_string))
    

window.Close()





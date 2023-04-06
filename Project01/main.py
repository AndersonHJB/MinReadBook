from xiyouji import Character, Scene, Event, Item, Interaction


# 创建角色
print("Adding characters...")
sunwukong = Character(None, "孙悟空", "主角")
sunwukong.add()
print("孙悟空 added.")

zhuwuneng = Character(None, "猪悟能", "主角")
zhuwuneng.add()
print("猪悟能 added.")

# 创建场景
scene1 = Scene(None, "女儿村", "一座美丽的村庄，村中只有女子。")
scene1.add()

# 创建事件
event1 = Event(None, "邂逅", "孙悟空和猪悟能在女儿村邂逅了一个神秘的女子。")
event1.add()

# 创建道具
item1 = Item(None, "紧箍咒", "紧箍咒可以控制孙悟空的行为。")
item1.add()

# 添加互动记录
print("Adding interactions...")
interaction1 = Interaction(None, sunwukong.id, scene1.id, event1.id, None)
interaction1.add()
print("Interaction 1 added.")

interaction2 = Interaction(None, zhuwuneng.id, scene1.id, event1.id, None)
interaction2.add()
print("Interaction 2 added.")
print("Interactions added. Querying...")

# 查询互动记录
interactions = Interaction.find_by_scene_id(scene1.id)
for interaction in interactions:
    character = Character.find_by_id(interaction['character_id'])
    scene = Scene.find_by_id(interaction['scene_id'])
    event = Event.find_by_id(interaction['event_id'])
    item = Item.find_by_id(interaction['item_id']) if interaction['item_id'] else None
    print(f"{character['name']} 在 {scene['name']} {event['name']}。" + (f"使用了 {item['name']}。" if item else ""))
    print("Character:", character)
    print("Scene:", scene)
    print("Event:", event)
    print("Item:", item)


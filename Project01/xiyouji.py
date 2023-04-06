import sqlite3

# 创建一个数据库连接
conn = sqlite3.connect('xiyouji.db')
conn.row_factory = sqlite3.Row
# 创建一个游标对象
c = conn.cursor()

# 创建角色表
c.execute("""
CREATE TABLE IF NOT EXISTS characters (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

# 创建场景表
c.execute("""
CREATE TABLE IF NOT EXISTS scenes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
""")

# 创建事件表
c.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
""")

# 创建道具表
c.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
""")

# 创建互动记录表
c.execute("""
CREATE TABLE IF NOT EXISTS interactions (
    id INTEGER PRIMARY KEY,
    character_id INTEGER,
    scene_id INTEGER,
    event_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY (character_id) REFERENCES characters (id),
    FOREIGN KEY (scene_id) REFERENCES scenes (id),
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (item_id) REFERENCES items (id)
)
""")
conn.commit()


class Character:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role

    def add(self):
        c.execute("INSERT INTO characters (name, role) VALUES (?, ?)", (self.name, self.role))
        conn.commit()

    def delete(self):
        c.execute("DELETE FROM characters WHERE id = ?", (self.id,))
        conn.commit()

    @staticmethod
    def find_by_id(character_id):
        c.execute("SELECT * FROM characters WHERE id = ?", (character_id,))
        return c.fetchone()

    @staticmethod
    def find_by_name(character_name):
        c.execute("SELECT * FROM characters WHERE name = ?", (character_name,))
        return c.fetchone()


class Scene:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def add(self):
        c.execute("INSERT INTO scenes (name, description) VALUES (?, ?)", (self.name, self.description))
        conn.commit()

    def delete(self):
        c.execute("DELETE FROM scenes WHERE id = ?", (self.id,))
        conn.commit()

    @staticmethod
    def find_by_id(scene_id):
        c.execute("SELECT * FROM scenes WHERE id = ?", (scene_id,))
        return c.fetchone()

    @staticmethod
    def find_by_name(scene_name):
        c.execute("SELECT * FROM scenes WHERE name = ?", (scene_name,))
        return c.fetchone()


class Event:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def add(self):
        c.execute("INSERT INTO events (name, description) VALUES (?, ?)", (self.name, self.description))
        conn.commit()

    def delete(self):
        c.execute("DELETE FROM events WHERE id = ?", (self.id,))
        conn.commit()

    @staticmethod
    def find_by_id(event_id):
        c.execute("SELECT * FROM events WHERE id = ?", (event_id,))
        return c.fetchone()

    @staticmethod
    def find_by_name(event_name):
        c.execute("SELECT * FROM events WHERE name = ?", (event_name,))
        return c.fetchone()


class Item:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def add(self):
        c.execute("INSERT INTO items (name, description) VALUES (?, ?)", (self.name, self.description))
        conn.commit()

    def delete(self):
        c.execute("DELETE FROM items WHERE id = ?", (self.id,))
        conn.commit()

    @staticmethod
    def find_by_id(item_id):
        c.execute("SELECT * FROM items WHERE id = ?", (item_id,))
        return c.fetchone()

    @staticmethod
    def find_by_name(item_name):
        c.execute("SELECT * FROM items WHERE name = ?", (item_name,))
        return c.fetchone()


class Interaction:
    def __init__(self, id, character_id, scene_id, event_id, item_id):
        self.id = id
        self.character_id = character_id
        self.scene_id = scene_id
        self.event_id = event_id
        self.item_id = item_id

    def add(self):
        c.execute("INSERT INTO interactions (character_id, scene_id, event_id, item_id) VALUES (?, ?, ?, ?)",
                  (self.character_id, self.scene_id, self.event_id, self.item_id))
        conn.commit()

    def delete(self):
        c.execute("DELETE FROM interactions WHERE id = ?", (self.id,))
        conn.commit()

    @staticmethod
    def find_by_character_id(character_id):
        c.execute("SELECT * FROM interactions WHERE character_id = ?", (character_id,))
        return c.fetchall()

    @classmethod
    def find_by_scene_id(cls, scene_id):
        c.execute("SELECT * FROM interactions WHERE scene_id = ?", (scene_id,))
        return c.fetchall()

    @staticmethod
    def find_by_event_id(event_id):
        c.execute("SELECT * FROM interactions WHERE event_id = ?", (event_id,))
        return c.fetchall()

    @staticmethod
    def find_by_item_id(item_id):
        c.execute("SELECT * FROM interactions WHERE item_id = ?", (item_id,))
        return c.fetchall()

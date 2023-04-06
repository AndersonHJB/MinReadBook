import sqlite3


# 创建数据库连接
def create_connection():
    conn = sqlite3.connect("farm.db")
    return conn


# 数据库操作类
class DatabaseOperations:
    def __init__(self, conn):
        self.conn = conn

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


# 农民类
class Farmer:
    def __init__(self, farmer_id, name):
        self.farmer_id = farmer_id
        self.name = name

    # 注册农民
    def register(self, db_operations):
        query = f"""
            INSERT INTO farmers (name)
            VALUES ('{self.name}');
        """
        db_operations.execute_query(query)


# 农场类
class Farm:
    def __init__(self, farm_id, name, location):
        self.farm_id = farm_id
        self.name = name
        self.location = location

    # 添加农场
    def add_farm(self, db_operations):
        query = f"""
            INSERT INTO farms (name, location)
            VALUES ('{self.name}', '{self.location}');
        """
        db_operations.execute_query(query)


# 动物类
class Animal:
    def __init__(self, animal_id, species, farm_id):
        self.animal_id = animal_id
        self.species = species
        self.farm_id = farm_id

    # 添加动物到农场
    def add_animal(self, db_operations):
        query = f"""
            INSERT INTO animals (species, farm_id)
            VALUES ('{self.species}', {self.farm_id});
        """
        db_operations.execute_query(query)


# 初始化数据库表
def initialize_database(db_operations):
    create_farmers_table = """
        CREATE TABLE IF NOT EXISTS farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """

    create_farms_table = """
        CREATE TABLE IF NOT EXISTS farms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        );
    """

    create_animals_table = """
        CREATE TABLE IF NOT EXISTS animals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            species TEXT NOT NULL,
            farm_id INTEGER,
            FOREIGN KEY (farm_id) REFERENCES farms (id)
        );
    """

    db_operations.execute_query(create_farmers_table)
    db_operations.execute_query(create_farms_table)
    db_operations.execute_query(create_animals_table)


# 查询农民
def query_farmer(db_operations, farmer_id):
    query = f"""
        SELECT * FROM farmers WHERE id = {farmer_id};
    """
    return db_operations.fetch_data(query)


# 查询农场
def query_farm(db_operations, farm_id):
    query = f"""
        SELECT * FROM farms WHERE id = {farm_id};
    """
    return db_operations.fetch_data(query)


# 查询农场的动物
def query_animals_on_farm(db_operations, farm_id):
    query = f"""
        SELECT * FROM animals WHERE farm_id = {farm_id};
    """
    return db_operations.fetch_data(query)


# 计算农场上特定种类动物的数量
def count_animal_species_on_farm(db_operations, farm_id, species):
    query = f"""
        SELECT COUNT(*) FROM animals WHERE farm_id = {farm_id} AND species = '{species}';
    """
    result = db_operations.fetch_data(query)
    return result[0][0]


# 主函数
def main():
    conn = create_connection()
    db_operations = DatabaseOperations(conn)

    initialize_database(db_operations)

    farmer1 = Farmer(1, "王大伟")
    farmer2 = Farmer(2, "李梅")

    farm1 = Farm(1, "绿野农场", "北京")
    farm2 = Farm(2, "蓝天农场", "上海")

    animal1 = Animal(1, "牛", farm1.farm_id)
    animal2 = Animal(2, "羊", farm2.farm_id)

    farmer1.register(db_operations)
    farmer2.register(db_operations)

    farm1.add_farm(db_operations)
    farm2.add_farm(db_operations)

    for i in range(10):
        animal1.add_animal(db_operations)
        animal2.add_animal(db_operations)

    # 查询农民信息
    print("查询农民信息:")
    print(query_farmer(db_operations, 1))
    print(query_farmer(db_operations, 2))

    # 查询农场信息
    print("查询农场信息:")
    print(query_farm(db_operations, 1))
    print(query_farm(db_operations, 2))

    # 查询农场上的动物
    print("查询农场上的动物:")
    print(query_animals_on_farm(db_operations, 1))
    print(query_animals_on_farm(db_operations, 2))

    # 统计农场上牛的数量
    print("统计农场上牛的数量:")
    print(count_animal_species_on_farm(db_operations, 1, "牛"))
    print(count_animal_species_on_farm(db_operations, 2, "牛"))

    conn.close()


if __name__ == "__main__":
    main()

import sqlite3


def add(account, item, type, date, status, position):
    """Add all the information of the military equipments"""
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS militaryequipmentsFor_{account}(id INTEGER PRIMARY KEY,
                                    item TEXT,
                                    type TEXT,
                                    date TEXT,
                                    status TEXT,
                                    position TEXT)""")
    cur.execute(f"""
INSERT INTO militaryequipmentsFor_{account}(item, type, date, status, position)
VALUES (?, ?, ?, ?, ?);""", (str(item), str(type), str(date), str(status), str(position)))
    con.commit()
    con.close()


def display(account):
    """Display all the data of the user"""
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    cur.execute(f"""
SELECT * FROM militaryequipmentsFor_{account}""")
    data = cur.fetchall()
    con.commit()
    con.close()
    return data


def update(account, id, item, type, date, status, position):
    """To update information in database

    Args:
        account: account of the users
        id:
        item: 
        type:
        date:
        status:
        position:
    """
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    cur.execute(f"""
UPDATE militaryequipmentsFor_{account}
SET item = ?,
    type = ?,
    date = ?,
    status = ?,
    position = ?
WHERE id = {id};""", (item, type, date, status, position))
    con.commit()
    con.close()


def delete(account, id):
    """Delete one date based on the id of military equipments you chose"""
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    cur.execute(f"DELETE FROM militaryequipmentsFor_{account} WHERE id = {id}")
    con.commit()
    con.close()


def delete_all(account):
    """Delete all the data in the database"""
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    cur.execute(f"DROP TABLE IF EXISTS militaryequipmentsFor_{account}")
    cur.execute(f"""
CREATE TABLE IF NOT EXISTS militaryequipmentsFor_{account}(id INTEGER PRIMARY KEY,
                                    item TEXT,
                                    type TEXT,
                                    date TEXT,
                                    status TEXT,
                                    position TEXT)""")
    con.commit()
    con.close()


def search(account, type_of_search, search):
    """To search the content you want to find in the database

    Args:
        account (_type_): account of the user
        type_of_search (_type_): choose the attribute you want to search
        search (_type_): search the content of that attribute

    Returns:
        data: return the data you want to search
    """
    con = sqlite3.connect('militaryequipments_management.db')
    cur = con.cursor()
    search_command = f"SELECT * FROM militaryequipmentsFor_{account} WHERE {type_of_search} LIKE '%{search}%'"
    cur.execute(search_command)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data
